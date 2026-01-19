# ============================================================
# region Imports
# ============================================================
# Python 3.7+ -> type hint'leri "string" gibi geç yazmadan,
# direkt class adıyla yazabilmek için (forward reference)
from __future__ import annotations

# os:
# - klasör/dosya işlemleri (logs klasörü oluşturma)
# - terminal temizleme (cls/clear)
# - işletim sistemi kontrolü (Windows mu değil mi)
import os

# json:
# - log kayıtlarını JSON formatında dosyaya yazmak için
import json

# re:
# - username/email doğrulama gibi regex tabanlı validasyonlar için
import re

# secrets:
# - güvenli random üretimi (token, session_id, salt üretimi)
# - compare_digest ile timing attack riskini azaltmak
import secrets

# hashlib:
# - PBKDF2-HMAC ile şifre hash'leme (sha256)
import hashlib

# datetime / timedelta:
# - audit tarihleri (create/modified/deleted)
# - token süreleri (expire)
# - lockout/cooldown süreleri
# - session TTL
from datetime import datetime, timedelta

# Enum:
# - Status / Role / AccountStatus gibi sabit seçenekler
# - magic number yerine okunabilir isimler
from enum import Enum

# gethostname / gethostbyname:
# - bilgisayar adı ve IP adresi (audit için)
# - local kullanım (demo)
from socket import gethostname, gethostbyname

# typing:
# - Optional, List, Dict, Any gibi type hint'ler
# - kodu okunabilir + daha güvenli hale getirir
from typing import Optional, List, Dict, Any
# endregion
# ============================================================


# ============================================================
# region Constants
# ============================================================
# Bu sabitler (constants), sistemde yapılan işlemlerin
# KİM tarafından tetiklendiğini audit / log kayıtlarında
# tutarlı ve okunabilir şekilde göstermek için kullanılır.
#
# Amaç:
# - Magic string kullanımını önlemek
# - Log kayıtlarında standartlaştırma sağlamak
# - İleride SIEM / log analiz sistemlerine kolay entegrasyon
# ============================================================

# Sistem tarafından otomatik yapılan işlemler
# (örn: seed admin oluşturma, background job)
ACTOR_SYSTEM = "SYSTEM"

# Kullanıcının kendi kendine yaptığı işlemler
# (register ekranı üzerinden)
ACTOR_SELF_REGISTER = "SELF_REGISTER"

# Email doğrulama linkine tıklanarak yapılan işlemler
ACTOR_EMAIL_VERIFY = "EMAIL_VERIFY"

# Başarısız login denemeleri
# (şifre hatası, brute-force denemesi vb.)
ACTOR_LOGIN_FAIL = "LOGIN_FAIL"

# Şifre sıfırlama akışı
# (forgot password + token ile reset)
ACTOR_PASSWORD_RESET = "PASSWORD_RESET"

# Token hash'lemek için "pepper" (server-side secret).
# Prod: ENV üzerinden ver.
TOKEN_PEPPER = os.getenv("AUTH_TOKEN_PEPPER", "dev-only-change-me")

# Not:
# - Bu sabitler doğrudan User.created_by / modified_by alanlarında kullanılabilir
# endregion
# ============================================================


# ============================================================
# region Custom Exceptions
# ============================================================
# Bu bölümde authentication / authorization akışında
# ortaya çıkabilecek HATA DURUMLARI için özel exception
# sınıfları tanımlanır.
#
# Neden custom exception?
# - Her hatayı Exception ile fırlatmak yerine
#   anlamlı ve ayrıştırılabilir hata türleri kullanmak
# - UI / CLI katmanında hataya göre farklı davranmak
#   (örneğin cooldown başlatmak, mesaj göstermek)
# - Loglama ve monitoring'i kolaylaştırmak
# ============================================================

class AuthError(Exception):
    """
    Authentication ile ilgili tüm hatalar için
    ortak base exception.

    Avantaj:
    - UI katmanında `except AuthError` ile
      tüm auth hatalarını tek noktada yakalayabilirsin.
    """
    pass


class InvalidCredentialsError(AuthError):
    """
    Kullanıcı adı veya şifre hatalı olduğunda fırlatılır.

    Kullanım senaryosu:
    - Yanlış şifre
    - Yanlış username
    - Güvenlik sebebiyle "hangisi yanlış" bilgisini
      AYIRT ETMEDEN tek tip hata döndürmek
    """
    pass


class AccountLockedError(AuthError):
    """
    Hesap geçici olarak kilitlendiğinde (cooldown / lock)
    fırlatılan özel exception.

    Bu exception NEDEN önemli?
    - Sadece hata mesajı değil,
      KALAN SÜRE ve LOCK SEVİYESİ gibi
      ek bilgileri de taşır.
    - UI tarafında countdown başlatmak için
      doğrudan kullanılabilir.
    """

    def __init__(self, remaining_seconds: int, lock_level: int):
        # Negatif süre gelmesini engeller
        self.remaining_seconds = max(0, int(remaining_seconds))

        # Lock seviyesi:
        # 1  -> kısa cooldown
        # 2+ -> gerçek lock (kademeli)
        self.lock_level = int(lock_level)

        # Exception mesajını __str__ üzerinden üretir
        super().__init__(self.__str__())

    def __str__(self) -> str:
        """
        Exception string temsili.
        UI/CLI çıktısında direkt gösterilir.
        """
        if self.lock_level <= 1:
            return f"Cooldown aktif ({self.remaining_seconds} sn)"

        return f"{self.lock_level}. LOCK aktif ({self.remaining_seconds} sn)"

# Not:
# - Bu yapı sayesinde UI tarafında şuna benzer net ayrım yapılır:
#
#   try:
#       auth.login(...)
#   except AccountLockedError as ex:
#       show_countdown(ex.remaining_seconds, ex.lock_level)
#   except InvalidCredentialsError:
#       print("Kullanıcı adı veya şifre hatalı")
# endregion
# ============================================================



# ============================================================
# region Enums
# ============================================================
# Bu Enum'lar sistemde kullanılan DURUM ve ROL bilgilerini
# magic number / string kullanmadan, okunabilir ve
# güvenli bir şekilde temsil etmek için tanımlanmıştır.
#
# Neden Enum?
# - Kod okunabilirliği artar
# - Yanlış değer atanması engellenir
# - Log ve audit kayıtları daha anlamlı olur
# - IDE autocomplete + type safety sağlar
# ============================================================

class Status(Enum):
    """
    Entity yaşam döngüsü (lifecycle) durumları.

    Bu enum, BaseEntity seviyesinde kullanılır ve
    kaydın sistem içindeki TEKNİK durumunu ifade eder.
    """

    Active = 1      # Aktif kayıt (normal kullanım)
    Modified = 2    # Güncellenmiş kayıt
    Passive = 3     # Pasif / devre dışı (soft disable)
    Deleted = 4     # Soft delete uygulanmış kayıt


class Role(Enum):
    """
    Kullanıcı ROL bilgisi.

    Bu enum, kullanıcının sistem içindeki
    YETKİ seviyesini belirtir.
    """

    Admin = 1   # Tam yetkili kullanıcı (yönetici)
    Member = 2  # Standart kullanıcı
    Author = 3  # İçerik üretebilen kullanıcı


class AccountStatus(Enum):
    """
    Kullanıcı hesabının BUSINESS durumunu ifade eder.

    Bu enum, teknik Status'tan FARKLI olarak
    hesabın sisteme giriş yapıp yapamayacağını belirler.
    """

    Pending = 1     # Kayıt var ama admin onayı bekliyor
    Active = 2      # Giriş yapabilir
    Suspended = 3   # Admin tarafından askıya alındı

# Not:
# - Status (teknik) ve AccountStatus (business) BİLİNÇLİ olarak ayrılmıştır
# - Örnek:
#   Status = Active ama AccountStatus = Suspended olabilir
#   (kayıt var ama login yasak)
# endregion
# ============================================================



# ============================================================
# region Password Hashing (PBKDF2)
# ============================================================
# Bu bölüm şifrelerin GÜVENLİ şekilde saklanması ve doğrulanması için kullanılır.
#
# ❗ ÖNEMLİ:
# - Şifreler ASLA düz metin (plain text) olarak saklanmaz
# - Hash + salt + iteration birlikte tutulur
# - Password policy (uzunluk, büyük harf vb.) burada yapılmaz
#   → o iş AuthService / Service katmanının sorumluluğudur
#
# Kullanılan algoritma:
# - PBKDF2-HMAC-SHA256
# - Brute-force ve rainbow-table saldırılarına karşı dayanıklıdır
# ============================================================

def hash_password(password: str, iterations: int = 120_000) -> tuple[str, str, int]:
    """
    Verilen şifreyi PBKDF2-HMAC-SHA256 ile hash'ler.

    Parametreler:
        password (str):
            Kullanıcının düz metin şifresi.
            (Policy kontrolü burada yapılmaz.)
        iterations (int):
            Hash'in kaç turda üretileceği.
            - Ne kadar yüksek → o kadar güvenli
            - Ama CPU maliyeti de artar
            - 120_000 güncel projeler için makul bir değerdir

    Dönüş:
        tuple[str, str, int]:
            (
                password_hash_hex,  # hash (hex string)
                salt_hex,           # salt (hex string)
                iterations          # kullanılan iteration sayısı
            )

    Notlar:
    - Her kullanıcı için AYRI salt üretilir
    - Aynı şifre → farklı hash üretir
    """

    # Boş şifre hash'lenmesin (ek güvenlik)
    if not password:
        raise ValueError("Password cannot be empty.")

    # Kriptografik olarak güvenli rastgele salt
    salt = secrets.token_bytes(16)  # 128-bit salt

    # PBKDF2-HMAC ile hash üretimi
    dk = hashlib.pbkdf2_hmac(
        "sha256",                   # hash algoritması
        password.encode("utf-8"),   # password bytes
        salt,                       # salt
        iterations                  # iteration count
    )

    # Hash ve salt hex string olarak saklanır (DB / JSON uyumlu)
    return dk.hex(), salt.hex(), iterations


def verify_password(password: str, password_hash_hex: str, salt_hex: str, iterations: int) -> bool:
    """
    Girilen şifrenin doğru olup olmadığını kontrol eder.

    Nasıl çalışır?
    1) DB'de kayıtlı salt + iteration alınır
    2) Kullanıcının girdiği şifre tekrar hash'lenir
    3) Oluşan hash ile kayıtlı hash karşılaştırılır

    Parametreler:
        password (str):
            Kullanıcının login sırasında girdiği şifre
        password_hash_hex (str):
            DB'de kayıtlı hash (hex)
        salt_hex (str):
            DB'de kayıtlı salt (hex)
        iterations (int):
            Hash üretiminde kullanılan iteration sayısı

    Dönüş:
        bool:
            True  -> şifre doğru
            False -> şifre yanlış

    Güvenlik Notu:
    - secrets.compare_digest kullanılır
    - Bu sayede timing attack riski azaltılır
    """

    # Eksik veri varsa doğrulama başarısız
    if not password_hash_hex or not salt_hex or not iterations:
        return False

    # Hex salt → bytes
    salt = bytes.fromhex(salt_hex)

    # Aynı parametrelerle hash'i tekrar üret
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)

    # Timing-attack-safe karşılaştırma
    return secrets.compare_digest(dk.hex(), password_hash_hex)

# endregion
# ============================================================



# ============================================================
# region Helpers (UI)
# ============================================================
# Bu yardımcı fonksiyonlar, UI / log / audit çıktılarında
# KİŞİSEL VERİLERİ (PII) maskelemek ve CLI input akışını
# standartlaştırmak için kullanılır.
#
# Amaç:
# - Loglarda email / IP gibi hassas bilgileri açık yazmamak
# - Güvenlik ve KVKK / GDPR uyumluluğu
# - Hata ayıklarken yeterli bağlamı korumak
# - CLI tarafında tekrar eden input kodlarını merkezileştirmek
# ============================================================

def mask_email(email: str, mask_domain: bool = False) -> str:
    """
    Email adresini maskeleyerek döndürür.

    Örnek:
        ipek@example.com        -> i***@example.com
        a@example.com           -> *@example.com
        geçersiz input          -> ***

    Opsiyonel domain maskeleme:
        ipek@example.com -> i***@e***.com  (mask_domain=True)

    Kurallar:
    - '@' yoksa tamamen maskeler
    - Local-part'ın sadece ilk harfi görünür
    - Domain kısmı normalde korunur (debug için faydalı)
    - İstersen mask_domain=True ile domain de kısmen maskelenir
    """

    email = (email or "").strip()

    # Email formatı değilse tamamen gizle
    if "@" not in email:
        return "***"

    name, domain = email.split("@", 1)

    # local part
    # İlk harf + mask
    local_masked = f"{name[0]}***" if len(name) > 1 else "*"

    if not mask_domain:
        return f"{local_masked}@{domain}"
    
    # domain part (basit maskeleme)
    # example.com -> e***.com
    if "." in domain:
        d_name, d_tld = domain.rsplit(".", 1)
        d_masked = f"{d_name[0]}***" if d_name else "***"
        return f"{local_masked}@{d_masked}.{d_tld}"

    return f"{local_masked}@***"


def mask_ip(ip: str) -> str:
    """
    IPv4 adresini maskeleyerek döndürür.

    Örnek:
        192.168.1.25 -> 192.168.***.***
        10.0.0.1     -> 10.0.***.***
        geçersiz     -> ***

    Not:
    - Sadece IPv4 için tasarlanmıştır (demo amaçlı)
    - IPv6 için ayrı bir maskeleme stratejisi gerekir
    """

    ip = (ip or "").strip()

    # IPv6 (basit guard)
    if ":" in ip:
        return "****"

    # IPv4 değilse gizle
    parts = ip.split(".")
    if len(parts) != 4:
        return "***"

    # İlk iki oktet görünür, son ikisi gizli
    return f"{parts[0]}.{parts[1]}.***.***"


def ask(prompt: str) -> str:
    """
    Kullanıcıdan standart metin girişi alır.

    Özellikler:
    - input() çıktısını otomatik olarak strip() eder
    - Başındaki ve sonundaki boşlukları temizler

    Kullanım:
        username = ask("Username: ")
        email = ask("Email: ")
    """
    return input(prompt).strip()


def press_enter() -> None:
    """
    Kullanıcının ekrana bakabilmesi için
    akışı durdurur.

    Kullanım senaryosu:
    - İşlem sonucu gösterildikten sonra
    - Menüye dönmeden önce
    """
    input("\nDevam etmek için ENTER...")


def ask_password(prompt: str = "Password: ", show_hint: bool = True) -> str:
    """
    Kullanıcıdan şifreyi görünmez şekilde alır.

    show_hint=True ise kullanıcıya "şifre görünmez" bilgisini yazar.
    (Login'de spam olmasın diye show_hint=False tercih edilebilir.)

    Nasıl çalışır?
    - Önce getpass modülü denenir
      (terminalde karakterler görünmez)
    - getpass çalışmazsa (bazı IDE/ortamlar)
      input() ile fallback yapılır

    Güvenlik:
    - Ekrana yazılan karakterler görünmez
    - Omuzdan bakma (shoulder surfing) riskini azaltır

    Kullanım:
        password = ask_password("Password: ")
    """
    try:
        if show_hint:
            print("(Şifre görünmez şekilde girilir)")
        import getpass
        return getpass.getpass(prompt).strip()
    except Exception:
        # IDE / ortam getpass desteklemiyorsa fallback
        return input(prompt).strip()


def ask_password_confirm(prompt1: str = "Password: ", prompt2: str = "Password (again): ") -> str:
    """
    Kullanıcıdan şifreyi iki kez alır ve eşleşmesini kontrol eder.

    Neden gerekli?
    - Register / reset password gibi işlemlerde
      yazım hatalarını önlemek için
    - Kullanıcı yanlışlıkla farklı şifre girmesin diye

    Akış:
    1) İlk şifre alınır
    2) Tekrar şifre alınır
    3) Eşleşmezse hata fırlatılır

    Return:
        str -> doğrulanmış şifre
    """

    pw1 = ask_password(prompt1, show_hint=True)
    pw2 = ask_password(prompt2, show_hint=False)  # ikinci kez aynı uyarıyı basma

    if pw1 != pw2:
        # UI katmanında yakalanır ve kullanıcıya mesaj gösterilir
        raise ValueError("Passwords do not match.")

    return pw1


def show_countdown(seconds: int, lock_level: int) -> bool:
    """
    Cooldown / Lock durumlarında geri sayım gösterir.

    Özellikler:
    - Süreyi mm:ss formatında gösterir
    - Kullanıcı 'Q' tuşuna basarsa iptal edilir
    - Süre biterse otomatik olarak devam eder

    Parametreler:
        seconds (int):
            Beklenecek toplam süre (saniye)
        lock_level (int):
            1  -> kısa cooldown
            2+ -> gerçek lock (kademeli)

    Return:
        bool
        - True  -> countdown tamamlandı
        - False -> kullanıcı Q ile iptal etti (menüye dön)
    """

    # Negatif süreleri engelle
    seconds = max(0, int(seconds))

    def fmt(sec: int) -> str:
        """
        Saniyeyi mm:ss formatına çevirir.
        """
        m, s = divmod(max(0, sec), 60)
        return f"{m:02d}:{s:02d}"

    # Kullanıcıya lock türünü açıkça göster
    if lock_level <= 1:
        print("⏸️  Cooldown aktif (kısa bekleme)")
    else:
        print(f"🔒 {lock_level}. LOCK aktif (süre artıyor)")

    # Süre yoksa beklemeden devam
    if seconds == 0:
        print("✅ Tekrar deneyebilirsin.")
        return True

    print("(İptal etmek için Q)\n")

    # ========================================================
    # Windows ortamı
    # ========================================================
    # msvcrt:
    # - Klavyeden basılan tuşu beklemeden yakalayabilir
    # - Windows CLI için en stabil yöntem
    if os.name == "nt":
        import msvcrt
        import time

        for remaining in range(seconds, 0, -1):
            # Kullanıcı tuşa bastı mı?
            if msvcrt.kbhit():
                ch = msvcrt.getwch()
                if ch.lower() == "q":
                    print("\n↩️  İptal edildi, menüye dönülüyor...")
                    return False

            # Geri sayımı ekranda güncelle
            print(f"\r⏳ Kalan süre: {fmt(remaining)}", end="", flush=True)
            time.sleep(1)

        print("\n✅ Tekrar deneyebilirsin.")
        return True

    # ========================================================
    # Linux / macOS ortamı
    # ========================================================
    # select:
    # - 1 saniye boyunca input var mı diye bekler
    # - Ekstra sleep yok → ritim düzgün
    import sys
    import select

    for remaining in range(seconds, 0, -1):
        print(f"\r⏳ Kalan süre: {fmt(remaining)}", end="", flush=True)

        # 1 saniye input bekle
        rlist, _, _ = select.select([sys.stdin], [], [], 1)
        if rlist:
            ch = sys.stdin.read(1)
            if ch.lower() == "q":
                print("\n↩️  İptal edildi, menüye dönülüyor...")
                return False

    print("\n✅ Tekrar deneyebilirsin.")
    return True

# Not:
# - Bu fonksiyonlar özellikle AuditLogger ve to_log_dict içinde kullanılır
# - Countdown kullanıcıyı "kilitlenmiş hissi"ne sokmaz
# - Q ile çıkış UX açısından çok önemlidir
# ============================================================



# ============================================================
# region Kernel + BaseEntity
# ============================================================
# Bu bölüm sistemdeki tüm entity'lerin (User, Product, Order vb.)
# ortak altyapısını sağlar.
#
# Neden Kernel + BaseEntity ayrımı?
# - Kernel: En temel kimlik (id) yönetimi
# - BaseEntity: Audit (create/modified/deleted) + environment (machine/ip) + status
#
# Böylece her entity tekrar tekrar:
# - id üretme
# - create/modified/deleted tarihleri
# - who-did-it bilgileri
# - makine adı / ip
# gibi alanları yazmak zorunda kalmaz.
# ============================================================

class Kernel:
    """
    Kernel sınıfı, tüm entity'lere kimlik (ID) özelliğini kazandırır.

    - __id alanı private tutulur (encapsulation)
    - sadece internal metotlarla set edilir
    - dışarıya read-only şekilde get_id_value() ile açılır

    Not:
    - Fail-fast yaklaşımı kullanılır: ID set edilmeden okunmak istenirse hata verir.
      Bu sayede "sessiz" bug'lar yakalanır.
    """

    def __init__(self):
        # Entity'nin benzersiz ID değeri
        # 처음 None, create audit sırasında üretilir
        self.__id: Optional[str] = None

    def _set_id(self) -> None:
        """
        Internal kullanım: yeni bir UUID üretip entity'ye atar.

        Neden UUID?
        - Çakışma ihtimali çok düşük
        - DB bağımsız çalışır (in-memory, json, sqlite vs.)
        - Distribüe sistemlerde bile rahat kullanılır
        """
        import uuid
        self.__id = str(uuid.uuid4())

    def get_id_value(self) -> str:
        """
        Entity ID değerini döndürür.

        Fail-fast:
        - Eğer ID henüz set edilmemişse RuntimeError fırlatır.
        - Bu genelde _set_create_audit() çağrılmadığını gösterir.
        """
        if not self.__id:
            raise RuntimeError("Entity has no id yet. Did you forget _set_create_audit()?")

        return self.__id


class BaseEntity(Kernel):
    """
    Audit (entity lifecycle) + Environment bilgilerini tutan base sınıf.

    BaseEntity neleri sağlar?
    - create_date, modified_date, deleted_date
    - created_by, modified_by, deleted_by
    - computer_name, ip_address (ortam bilgisi)
    - status (Active / Modified / Deleted / Passive)

    Bu alanlar "cross-cutting concern" olduğundan
    (tüm entity'lerde ortak), tek yerde toplanır.
    """

    def __init__(self):
        super().__init__()

        # -------------------------
        # Audit timestamps
        # -------------------------
        self.__create_date: Optional[datetime] = None
        self.__modified_date: Optional[datetime] = None
        self.__deleted_date: Optional[datetime] = None

        # -------------------------
        # Audit actors (who did it?)
        # -------------------------
        self.__created_by: Optional[str] = None
        self.__modified_by: Optional[str] = None
        self.__deleted_by: Optional[str] = None

        # -------------------------
        # Environment info
        # -------------------------
        self.__computer_name: Optional[str] = None
        self.__ip_address: Optional[str] = None

        # -------------------------
        # Entity status (technical)
        # -------------------------
        # Default: Passive (henüz create audit yapılmadı)
        self.__status: Status = Status.Passive

    def _set_env(self) -> None:
        """
        Entity oluşturulurken çalıştığı ortam bilgisini yakalar.

        Neden?
        - Audit / debug amaçlı
        - Hangi makineden işlem yapıldı?
        - Hangi IP üzerinden çalıştı?

        Not:
        - gethostbyname(gethostname()) her zaman gerçek IP'yi dönmeyebilir.
          Bazı sistemlerde 127.0.0.1 dönebilir. (demo için yeterli)
        """
        self.__computer_name = gethostname()
        try:
            self.__ip_address = gethostbyname(gethostname())
        except Exception:
            # IP bulunamazsa safe fallback
            self.__ip_address = "127.0.0.1"

    def _set_create_audit(self, performed_by_user_id: Optional[str]) -> None:
        """
        Entity ilk kez oluşturulduğunda çağrılır.

        Yaptıkları:
        - ID üretir
        - environment bilgilerini set eder
        - create_date ve created_by set eder
        - status'u Active yapar
        """
        self._set_id()
        self._set_env()
        self.__create_date = datetime.now()
        self.__created_by = performed_by_user_id
        self.__status = Status.Active

    def _set_modified_audit(self, performed_by_user_id: Optional[str]) -> None:
        """
        Entity güncellendiğinde çağrılır.

        Yaptıkları:
        - modified_date ve modified_by set eder
        - status'u Modified yapar

        Not:
        - Bu metot entity'nin "iş kuralları" ile değil,
          sadece audit kaydıyla ilgilenir.
        """
        self.__modified_date = datetime.now()
        self.__modified_by = performed_by_user_id
        self.__status = Status.Modified

    def _set_deleted_audit(self, performed_by_user_id: Optional[str]) -> None:
        """
        Soft delete için çağrılır.

        Yaptıkları:
        - deleted_date ve deleted_by set eder
        - status'u Deleted yapar

        Not:
        - Hard delete değil → obje bellekte kalır, DB'de kalır,
          ama business katmanı "görmez".
        """
        self.__deleted_date = datetime.now()
        self.__deleted_by = performed_by_user_id
        self.__status = Status.Deleted

    # ---------------------------------------------------------
    # Read-only properties (Encapsulation)
    # ---------------------------------------------------------
    # Dışarıdan audit alanlarının direkt set edilmesini engeller.
    # Değişiklikler sadece _set_*_audit metotlarıyla yapılır.
    @property
    def create_date(self) -> Optional[datetime]:
        return self.__create_date

    @property
    def modified_date(self) -> Optional[datetime]:
        return self.__modified_date

    @property
    def deleted_date(self) -> Optional[datetime]:
        return self.__deleted_date

    @property
    def created_by(self) -> Optional[str]:
        return self.__created_by

    @property
    def modified_by(self) -> Optional[str]:
        return self.__modified_by

    @property
    def deleted_by(self) -> Optional[str]:
        return self.__deleted_by

    @property
    def computer_name(self) -> Optional[str]:
        return self.__computer_name

    @property
    def ip_address(self) -> Optional[str]:
        return self.__ip_address

    @property
    def status(self) -> Status:
        return self.__status

# endregion
# ============================================================



# ============================================================
# region User Entity
# ============================================================
# Bu sınıf sistemdeki "kullanıcı" modelini temsil eder.
#
# User neden BaseEntity'den türetiliyor?
# - ID, create/modified/deleted audit alanları otomatik gelir
# - status (Active/Deleted vb.) ve env (machine/ip) bilgileri hazır olur
#
# User içinde hangi ana başlıklar var?
# 1) Kimlik bilgileri: first_name, last_name, user_name, email
# 2) Yetki: role (Admin/Member/Author)
# 3) Business durum: account_status (Pending/Active/Suspended)
# 4) Email doğrulama: token + expires + verified flag
# 5) Şifre güvenliği: PBKDF2 hash + salt + iterations
# 6) Login güvenliği: failed counter + lockout (cooldown/lock) + last login
# 7) Password reset: token + expires + token ile şifre değiştirme
# 8) Mapping: snapshot/safe/log için farklı dictionary dönüşleri
# ============================================================

class User(BaseEntity):
    """
    Kullanıcı entity'si.

    Not:
    - Bu sınıfın bazı setter'ları "internal" olarak tasarlanmıştır.
      Örn: _set_role_internal(), _set_account_status_internal()
      Çünkü role/status gibi kritik alanların UI tarafından
      direkt değiştirilmesi istenmez (sadece service üzerinden).
    """

    def __init__(self, first_name: str, last_name: str, user_name: str, email: str, password: str):
        super().__init__()

        # -------------------------
        # Basic identity fields
        # -------------------------
        # Kullanıcıdan gelen değerleri normalize ediyoruz
        # (strip, lower, None guard)
        self.first_name = (first_name or "").strip()
        self.last_name = (last_name or "").strip()
        self.user_name = (user_name or "").strip()
        self.email = (email or "").strip().lower()

        # -------------------------
        # Authorization / Business status
        # -------------------------
        # role: sistemdeki yetki seviyesi
        # account_status: sisteme giriş yapabilir mi? (iş kuralı)
        self.__role: Role = Role.Member
        self.__account_status: AccountStatus = AccountStatus.Pending

        # -------------------------
        # Email verification
        # -------------------------
        # email_verified: kullanıcı emailini doğruladı mı?
        # token + expires: doğrulama akışı için
        self.__email_verified: bool = False
        self.__email_verification_token_hash: Optional[str] = None
        self.__email_verification_expires_at: Optional[datetime] = None

        # -------------------------
        # Password hashing (PBKDF2)
        # -------------------------
        self.__password_hash: str = ""
        self.__password_salt: str = ""
        self.__password_iterations: int = 0

        # -------------------------
        # Login security
        # -------------------------
        # failed_login_count: brute-force takibi
        # lockout_until: cooldown/lock bitiş zamanı
        self.__last_login_date: Optional[datetime] = None
        self.__failed_login_count: int = 0
        self.__lockout_until: Optional[datetime] = None

        # -------------------------
        # Password reset
        # -------------------------
        self.__password_reset_token_hash: Optional[str] = None
        self.__password_reset_expires_at: Optional[datetime] = None

        # İlk şifre set edilir (hash+salt+iter)
        self._set_password_internal(password)

    # ========================================================
    # region Role (Authorization)
    # ========================================================
    @property
    def role(self) -> Role:
        """
        Kullanıcının rolünü read-only döndürür.
        Role değişimi sadece service/admin tarafından yapılmalı.
        """
        return self.__role

    def _set_role_internal(self, new_role: Role) -> None:
        """
        Internal setter:
        - UI doğrudan çağırmamalı
        - Admin işlemleri (UserService) üzerinden kullanılmalı
        """
        self.__role = new_role
    # endregion
    # ========================================================

    # ========================================================
    # region Account Status (Business)
    # ========================================================
    @property
    def account_status(self) -> AccountStatus:
        """
        Kullanıcı hesabının business statüsü:
        Pending/Active/Suspended
        """
        return self.__account_status

    def _set_account_status_internal(self, new_status: AccountStatus) -> None:
        """
        Internal setter:
        - register sonrası Pending
        - admin approve sonrası Active
        - suspend/unsuspend gibi işlemler service üzerinden
        """
        self.__account_status = new_status
    # endregion
    # ========================================================

    # ========================================================
    # region Email Verification
    # ========================================================
    @property
    def email_verified(self) -> bool:
        """
        Kullanıcı emailini doğruladı mı?
        Login için genelde şart koşulur.
        """
        return self.__email_verified

    def _issue_email_verification_token(self, ttl_minutes: int = 30, token_hash_provider=None) -> str:
        """
        Email doğrulama token'ı üretir.
        DB'de raw token değil HASH saklanır.

        ttl_minutes:
        - token ne kadar süre geçerli?
        - süresi dolunca tekrar token üretmek gerekir

        token_hash_provider:
        - AuthService._hash_token gibi bir fonksiyon verilir.
        - Böylece User, AuthService'e bağımlı olmaz.
        """
        raw = secrets.token_urlsafe(24)

        if not token_hash_provider:
            raise RuntimeError("token_hash_provider is required for secure token storage.")
        
        self.__email_verification_token_hash = token_hash_provider(raw)
        self.__email_verification_expires_at = datetime.now() + timedelta(minutes=ttl_minutes)
        return raw

    def _force_verify_email_internal(self) -> None:
        """
        Internal kullanımlı 'force verify'.

        Senaryo:
        - seed edilen ilk admin gibi sistem tarafından güvenilir kabul edilen hesaplar
        - normal kullanıcılar için kullanılmamalı (akışı bypass eder)
        """
        self.__email_verified = True
        self.__email_verification_token_hash = None
        self.__email_verification_expires_at = None

    def _verify_email_with_token(self, token: str, , token_hash_provider=None) -> None:
        """
        Kullanıcının email doğrulamasını token ile gerçekleştirir.

        Kontroller:
        - aktif token var mı?
        - token süresi dolmuş mu?
        - token doğru mu? (compare_digest ile timing attack azaltılır)
        """
        if not self.__email_verification_token_hash or not self.__email_verification_expires_at:
            raise PermissionError("No active verification token.")

        if datetime.now() > self.__email_verification_expires_at:
            raise PermissionError("Verification token expired.")

        if not token_hash_provider:
            raise RuntimeError("token_hash_provider is required for secure token check.")

        incoming_hash = token_hash_provider(token)
        if not secrets.compare_digest(incoming_hash, self.__email_verification_token_hash):
            raise PermissionError("Invalid verification token.")

        # başarılı doğrulama
        self.__email_verified = True
        self.__email_verification_token_hash = None
        self.__email_verification_expires_at = None
    # endregion
    # ========================================================

    # ========================================================
    # region Password
    # ========================================================
    def _set_password_internal(self, password: str) -> None:
        """
        Şifreyi PBKDF2 ile hash'ler ve saklar.

        Not:
        - Burada password policy yapılmaz (AuthService yapar)
        - Şifre değişince reset token'ı iptal edilir
        """
        pw_hash, salt, iters = hash_password(password)
        self.__password_hash = pw_hash
        self.__password_salt = salt
        self.__password_iterations = iters

        # reset token iptal
        self.__password_reset_token_hash = None
        self.__password_reset_expires_at = None

    def check_password(self, password: str) -> bool:
        """
        Login sırasında girilen şifre doğru mu?
        """
        return verify_password(password, self.__password_hash, self.__password_salt, self.__password_iterations)
    # endregion
    # ========================================================

    # ========================================================
    # region Login Security (Lockout / Cooldown)
    # ========================================================
    @property
    def last_login_date(self) -> Optional[datetime]:
        """
        Son başarılı login zamanı.
        """
        return self.__last_login_date

    @property
    def failed_login_count(self) -> int:
        """
        Başarısız login deneme sayısı.
        """
        return self.__failed_login_count

    @property
    def lockout_until(self) -> Optional[datetime]:
        """
        Hesap kilidi ne zamana kadar sürer?
        None ise kilit yok.
        """
        return self.__lockout_until

    def is_locked(self) -> bool:
        """
        Şu anda kilitli mi?
        - lockout_until set edilmiş olmalı
        - current time < lockout_until
        """
        return self.__lockout_until is not None and datetime.now() < self.__lockout_until

    def get_lock_level(self, cooldown_after: int = 3, lock_after: int = 5) -> int:
        """
        Lock seviyesini hesaplar.

        0 = lock yok (0-2 fail)
        1 = cooldown (3-4 fail arası)
        2+ = gerçek lock (5+ fail)

        Not:
        - Bu seviye UI'da gösterilir ve loglara yazılabilir.
        """
        if self.__failed_login_count < cooldown_after:
            return 0
        if self.__failed_login_count < lock_after:
            return 1
        return 2 + (self.__failed_login_count - lock_after)

    def record_login_success(self, performed_by_user_id: str) -> None:
        """
        Başarılı login olduğunda çağrılır.

        Yaptıkları:
        - last_login_date set eder
        - failed counter sıfırlar
        - lock kaldırır
        - audit modified günceller
        """
        self.__last_login_date = datetime.now()
        self.__failed_login_count = 0
        self.__lockout_until = None
        self._set_modified_audit(performed_by_user_id=performed_by_user_id)

    def record_login_failure(
        self,
        performed_by_user_id: str,
        cooldown_after: int = 3,
        cooldown_seconds: int = 10,
        lock_after: int = 5,
        base_lock_minutes: int = 5
    ) -> None:
        """
        Başarısız login olduğunda çağrılır.

        Hedef:
        - Brute-force saldırılarını yavaşlatmak
        - Kullanıcıyı "deneme yanılma" yerine doğru bilgiyle girişe yönlendirmek

        Politika:
        - 1-2 fail: sadece sayar (kilit yok)
        - 3. fail : kısa cooldown (örn 10 sn)
        - 5+ fail : kademeli lock (5dk, 10dk, 20dk... max 60dk)

        Not:
        - cooldown ile lock aynı lockout_until alanı üzerinden yönetilir
        - UI tarafı lock_level ile bunu ayırt eder
        """
        self.__failed_login_count += 1
        self._set_modified_audit(performed_by_user_id=performed_by_user_id)

        now = datetime.now()

        # 3. denemede kısa cooldown
        if self.__failed_login_count == cooldown_after:
            self.__lockout_until = now + timedelta(seconds=cooldown_seconds)
            return

        # 5+ denemede kademeli lock
        if self.__failed_login_count >= lock_after:
            lock_index = self.__failed_login_count - lock_after  # 0,1,2...
            minutes = min(60, base_lock_minutes * (2 ** lock_index))
            self.__lockout_until = now + timedelta(minutes=minutes)
    # endregion
    # ========================================================

    # ========================================================
    # region Password Reset
    # ========================================================
    def _issue_password_reset_token(self, ttl_minutes: int = 15, token_hash_provider=None) -> str:
        """
        Şifre sıfırlama token'ı üretir.
        Token süresi ttl_minutes kadar geçerlidir.
        """
        raw = secrets.token_urlsafe(24)

        if not token_hash_provider:
            raise RuntimeError("token_hash_provider is required for secure token storage.")
        
        self.__password_reset_token_hash = token_hash_provider(raw)
        self.__password_reset_expires_at = datetime.now() + timedelta(minutes=ttl_minutes)
        return raw

    def _reset_password_with_token(self, token: str, new_password: str, token_hash_provider=None) -> None:
        """
        Token ile şifre sıfırlar.

        Kontroller:
        - aktif reset token var mı?
        - token süresi dolmuş mu?
        - token doğru mu?
        """
        if not self.__password_reset_token_hash or not self.__password_reset_expires_at:
            raise PermissionError("No active password reset token.")

        if datetime.now() > self.__password_reset_expires_at:
            raise PermissionError("Password reset token expired.")

        if not token_hash_provider:
            raise RuntimeError("token_hash_provider is required for secure token check.")
        
        incoming_hash = token_hash_provider(token)
        if not secrets.compare_digest(incoming_hash, self.__password_reset_token_hash):
            raise PermissionError("Invalid password reset token.")

        # başarılı -> yeni şifreyi set et (reset token otomatik iptal olur)
        self._set_password_internal(new_password)
    # endregion
    # ========================================================

    # ========================================================
    # region Mapping (Snapshot / Safe / Log)
    # ========================================================
    def to_snapshot_dict(self) -> Dict[str, Any]:
        """
        Repository snapshot için.
        - İçerikte PII ve teknik alanlar bulunabilir.
        - Prod’da bu data dışarıya verilmez.
        """
        return {
            "id": self.get_id_value(),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "user_name": self.user_name,
            "email": self.email,
            "role": self.role.name,
            "account_status": self.account_status.name,
            "email_verified": self.email_verified,
            "status": self.status.name,
            "create_date": self.create_date.isoformat() if self.create_date else None,
            "modified_date": self.modified_date.isoformat() if self.modified_date else None,
            "deleted_date": self.deleted_date.isoformat() if self.deleted_date else None,
            "created_by": self.created_by,
            "modified_by": self.modified_by,
            "deleted_by": self.deleted_by,
            "computer_name": self.computer_name,
            "ip_address": self.ip_address,
            "last_login_date": self.last_login_date.isoformat() if self.last_login_date else None,
            "failed_login_count": self.failed_login_count,
            "lockout_until": self.lockout_until.isoformat() if self.lockout_until else None,
            "lock_level": self.get_lock_level(),
        }

    def to_safe_dict(self) -> Dict[str, Any]:
        """
        UI/API output için güvenli sözlük.

        Not:
        - password hash/salt içermez
        - yine de email burada açık döner (UI için)
          log için to_log_dict kullanılmalı
        """
        return {
            "id": self.get_id_value(),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "user_name": self.user_name,
            "email": self.email,
            "role": self.role.name,
            "account_status": self.account_status.name,
            "email_verified": self.email_verified,
            "status": self.status.name,
            "create_date": self.create_date.isoformat() if self.create_date else None,
            "modified_date": self.modified_date.isoformat() if self.modified_date else None,
            "last_login_date": self.last_login_date.isoformat() if self.last_login_date else None,
            "failed_login_count": self.failed_login_count,
            "locked": self.is_locked(),
            "lock_level": self.get_lock_level(),
        }

    def to_log_dict(self, mask_pii: bool = True) -> Dict[str, Any]:
        """
        Log için optimize edilmiş sözlük.

        mask_pii=True:
        - email maskelenir
        - ip maskelenir

        mask_pii=False:
        - admin/ops debug için PII açık (dikkatli kullanılmalı)
        """
        d = self.to_safe_dict()
        if mask_pii:
            d["email"] = mask_email(d.get("email", ""))
            d["ip_address"] = mask_ip(self.ip_address or "")
        else:
            d["ip_address"] = self.ip_address
        return d
    # endregion
    # ========================================================

# endregion
# ============================================================



# ============================================================
# region Repository
# ============================================================
# Repository katmanı "Data Access Only" (sadece veri erişimi) yaklaşımıyla
# tasarlanmıştır.
#
# Bu sınıfın amacı:
# - User objelerini saklamak (şimdilik in-memory list)
# - Arama (get/find) ve ekleme (add) gibi temel veri operasyonlarını yapmak
# - Business kuralları (approve, suspend, login, policy) BURADA OLMAZ
#   → onlar Service (UserService / AuthService) katmanının işidir.
#
# Neden repository?
# - UI / Service katmanı doğrudan list/dict ile uğraşmaz
# - İleride liste yerine DB (SQLite/PostgreSQL/Mongo) bağlamak kolay olur
# - Test yazmak kolaylaşır (mock repo vs.)
# ============================================================

class UserRepository:
    """
    UserRepository: Kullanıcı verisini yöneten data access sınıfı.

    İç yapısı:
    - _items: gerçek User objeleri (in-memory)
    - snapshots: User'ın farklı zamanlardaki "snapshot" kayıtları
      (debug / audit amaçlı; prod’da bu yaklaşım farklı uygulanabilir)
    """

    def __init__(self):
        # Sistemdeki gerçek User objeleri
        self._items: List[User] = []

        # Snapshot arşivi:
        # - create/update gibi işlemlerden sonra user.to_snapshot_dict() eklenir
        # - geçmiş durumları incelemek için kullanılabilir
        self.snapshots: List[Dict[str, Any]] = []

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------
    def add(self, user: User) -> None:
        """
        Yeni kullanıcı ekler.

        Kontroller:
        - username unique olmalı
        - email unique olmalı

        Not:
        - Bu kontrol repo seviyesinde "data integrity" amaçlıdır.
          Business kuralları (pending/active gibi) service katmanındadır.
        """
        if self.find_by_username(user.user_name):
            raise ValueError("This username is already taken.")
        if self.find_by_email(user.email):
            raise ValueError("This email is already taken.")

        self._items.append(user)

    # ---------------------------------------------------------
    # Read
    # ---------------------------------------------------------
    def list_all(self) -> List[User]:
        """
        Tüm kullanıcıları listeler.

        Not:
        - list(self._items) döndürerek shallow copy yapıyoruz.
          Böylece dışarıdan _items listesi direkt manipüle edilmez.
        """
        return list(self._items)

    def get_by_id(self, user_id: str) -> Optional[User]:
        """
        ID ile kullanıcı bulur.

        Return:
        - User bulunursa User objesi
        - bulunamazsa None
        """
        for u in self._items:
            if u.get_id_value() == user_id:
                return u
        return None

    def find_by_username(self, user_name: str) -> Optional[User]:
        """
        Username ile kullanıcı bulur (case-insensitive).

        Neden lower + strip?
        - Kullanıcı inputu farklı yazabilir: " Ipek " / "ipek" / "IPEK"
        - Normalize ederek tek standarda indiriyoruz.
        """
        key = (user_name or "").strip().lower()
        for u in self._items:
            if u.user_name.lower() == key:
                return u
        return None

    def find_by_email(self, email: str) -> Optional[User]:
        """
        Email ile kullanıcı bulur (case-insensitive).

        Not:
        - Email normalize: lower + strip
        - Prod’da ayrıca email canonicalization (gmail '.' vb.) ayrı ele alınabilir.
        """
        key = (email or "").strip().lower()
        for u in self._items:
            if u.email.lower() == key:
                return u
        return None

    # ---------------------------------------------------------
    # Snapshot
    # ---------------------------------------------------------
    def save_snapshot(self, user: User) -> None:
        """
        Kullanıcının o anki durumunu snapshot listesine ekler.

        Ne işe yarar?
        - Demo / debug: kullanıcı lifecycle'ını görmek
        - Audit benzeri bir kayıt üretmek

        Dikkat:
        - Snapshot PII içerebilir (email/ip vb.)
        - Bu yüzden dışarıya API ile dönmek için uygun değildir.
        """
        self.snapshots.append(user.to_snapshot_dict())

# endregion
# ============================================================



# ============================================================
# region Logger
# ============================================================
# Bu bölüm sistemde gerçekleşen tüm önemli aksiyonların
# KALICI olarak kaydedilmesi için kullanılan audit logger’ı içerir.
#
# Audit logging neden önemli?
# - Kim, ne zaman, ne yaptı? sorularına cevap verir
# - Güvenlik olaylarını (brute-force, lock, suspend vb.) izlemek
# - Hata ayıklama (debug) ve sistem davranışlarını analiz etmek
# - Gerçek projelerde compliance (KVKK / GDPR / ISO) gereksinimleri
#
# Bu logger:
# - Basit dosya tabanlıdır (append)
# - JSON Lines formatı kullanır (her satır bir JSON obje)
# - CLI / demo için idealdir
# ============================================================

class AuditLogger:
    """
    AuditLogger, sistem aksiyonlarını dosyaya yazmakla sorumludur.

    Özellikler:
    - Log klasörü otomatik oluşturulur
    - Her log satırı bağımsız JSON objesidir
    - Encoding UTF-8 (Türkçe karakter sorunu yok)
    """

    def __init__(self, folder: str = "logs", file_name: str = "user_activity.log"):
        """
        Logger constructor.

        Parametreler:
            folder (str):
                Log dosyalarının tutulacağı klasör.
                Varsayılan: "logs"
            file_name (str):
                Log dosyasının adı.
                Varsayılan: "user_activity.log"
        """
        self.folder = folder
        self.file_path = os.path.join(folder, file_name)

    def _ensure(self) -> None:
        """
        Log klasörünün varlığını garanti eder.

        - Eğer klasör yoksa oluşturur
        - Var ise hiçbir şey yapmaz
        """
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def write(self, action: str, data: Dict[str, Any]) -> None:
        """
        Audit log kaydı yazar.

        Parametreler:
            action (str):
                Yapılan işlemin kısa ve sabit adı.
                Örnek:
                    - REGISTER
                    - LOGIN_SUCCESS
                    - LOGIN_FAIL
                    - ACCOUNT_APPROVE
                    - PASSWORD_RESET
            data (Dict[str, Any]):
                İşleme ait bağlamsal bilgiler.
                Genelde:
                    - user_id
                    - masked email
                    - lock_level
                    - account_status
                    - session_id (varsa)

        Log Formatı (JSON Lines):
        {
            "timestamp": "2026-01-16T00:12:45.123456",
            "action": "LOGIN_SUCCESS",
            "data": { ... }
        }

        Notlar:
        - ensure_ascii=False → Türkçe karakterler bozulmaz
        - append mode ("a") → mevcut loglar silinmez
        """
        # Log klasörü hazır mı?
        self._ensure()

        record = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "data": data
        }

        # Her kayıt ayrı bir satır olarak yazılır
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

# endregion
# ============================================================



# ============================================================
# region Services
# ============================================================
# Service katmanı "business rules" (iş kuralları) katmanıdır.
#
# Repository neydi?
# - Sadece data access (ekle, bul, listele)
#
# Service ne yapar?
# - Yetki kontrolü (admin mi?)
# - İş kuralları (email verified mi? deleted mi? suspended mi?)
# - Durum geçişleri (Pending -> Active, Active -> Suspended vb.)
# - Audit alanlarını set etmek (modified_by, deleted_by...)
# - Log yazmak (AuditLogger)
#
# Bu sayede UI katmanı sadece "kullanıcıdan veri alır ve sonucu gösterir"
# iş kurallarına bulaşmaz.
# ============================================================

class UserService:
    """
    Admin tarafındaki yönetim operasyonlarını içerir.

    Bu sınıf şunları yapar:
    - İlk admin'i seed etmek (sistemi ayağa kaldırmak)
    - Kullanıcı onaylamak (Pending -> Active)
    - Suspend/Unsuspend
    - Role değişimi
    - Admin tarafından password reset
    - Soft delete

    Not:
    - "Self register" ve "Login/Session" gibi akışlar AuthService'te olur.
    """

    def __init__(self, repo: UserRepository, logger: AuditLogger, auth: AuthService):
        # repo: veri erişimi
        # logger: audit log
        self.repo = repo
        self.logger = logger
        self.auth = auth

    # ---------------------------------------------------------
    # Authorization guard
    # ---------------------------------------------------------
    def _require_admin(self, performed_by: User) -> None:
        """
        Admin olmayan kullanıcıların bu servis metotlarını
        çalıştırmasını engeller.
        """
        if performed_by.role != Role.Admin:
            raise PermissionError("Only Admin users can perform this operation.")

    # ---------------------------------------------------------
    # Seed first admin
    # ---------------------------------------------------------
    def seed_first_admin(self, user_name: str, email: str, password: str) -> User:
        """
        Sistemde hiç kullanıcı yokken ilk admin'i oluşturur.

        Kurallar:
        - Sadece sistem boşken çalışır (ilk kurulum)
        - Admin hesabı:
          - role = Admin
          - account_status = Active
          - email_verified = True (force)
        """
        if self.repo.list_all():
            raise RuntimeError("Seed is allowed only when there are no users.")

        # Admin user oluştur
        admin = User("System", "Administrator", user_name, email, password)

        # Audit + rol + status
        admin._set_create_audit(performed_by_user_id=ACTOR_SYSTEM)
        admin._set_role_internal(Role.Admin)
        admin._set_account_status_internal(AccountStatus.Active)

        # Seed admin'i internal olarak verified kabul ediyoruz
        admin._force_verify_email_internal()

        # Repo'ya ekle
        self.repo.add(admin)
        self.repo.save_snapshot(admin)

        # Admin için PII maskesi kaldırılabilir (ops/debug)
        # Ancak prod’da yine de mask'li log tercih edilebilir.
        self.logger.write("SEED_ADMIN_CREATE", admin.to_log_dict(mask_pii=False))
        return admin

    # ---------------------------------------------------------
    # Approve user (Pending -> Active)
    # ---------------------------------------------------------
    def approve_user(self, target_user_id: str, performed_by: User) -> User:
        """
        Admin onayı:
        - user email_verified olmalı
        - user Deleted olmamalı
        - user Suspended ise önce unsuspend gerekir
        - account_status -> Active
        """
        self._require_admin(performed_by)

        target = self.repo.get_by_id(target_user_id)
        if not target:
            raise ValueError("User not found.")

        if target.status == Status.Deleted:
            raise PermissionError("Deleted users cannot be approved.")

        if not target.email_verified:
            raise PermissionError("User must verify email before approval.")

        if target.account_status == AccountStatus.Suspended:
            raise PermissionError("Suspended accounts cannot be approved without unsuspending.")

        # Pending -> Active
        target._set_account_status_internal(AccountStatus.Active)
        target._set_modified_audit(performed_by_user_id=performed_by.get_id_value())

        self.repo.save_snapshot(target)
        self.logger.write("ACCOUNT_APPROVE", target.to_log_dict())
        return target

    # ---------------------------------------------------------
    # Suspend user
    # ---------------------------------------------------------
    def suspend_user(self, target_user_id: str, performed_by: User) -> User:
        """
        Kullanıcıyı askıya alır:
        - account_status -> Suspended
        - login engellenir
        """
        self._require_admin(performed_by)

        target = self.repo.get_by_id(target_user_id)
        if not target:
            raise ValueError("User not found.")

        if target.status == Status.Deleted:
            raise PermissionError("Deleted users cannot be suspended.")

        target._set_account_status_internal(AccountStatus.Suspended)
        target._set_modified_audit(performed_by_user_id=performed_by.get_id_value())

        self.repo.save_snapshot(target)
        self.logger.write("ACCOUNT_SUSPEND", target.to_log_dict())
        return target

    # ---------------------------------------------------------
    # Unsuspend user
    # ---------------------------------------------------------
    def unsuspend_user(self, target_user_id: str, performed_by: User) -> User:
        """
        Askıya alınmış kullanıcıyı tekrar onay sürecine alır:
        - Suspended -> Pending
        - admin tekrar approve edebilir
        """
        self._require_admin(performed_by)

        target = self.repo.get_by_id(target_user_id)
        if not target:
            raise ValueError("User not found.")

        if target.status == Status.Deleted:
            raise PermissionError("Deleted users cannot be unsuspended.")

        # Suspended -> Pending (tekrar approve gereksin)
        target._set_account_status_internal(AccountStatus.Pending)
        target._set_modified_audit(performed_by_user_id=performed_by.get_id_value())

        self.repo.save_snapshot(target)
        self.logger.write("ACCOUNT_UNSUSPEND", target.to_log_dict())
        return target

    # ---------------------------------------------------------
    # Change role
    # ---------------------------------------------------------
    def change_role(self, target_user_id: str, new_role: Role, performed_by: User) -> User:
        """
        Kullanıcının rolünü değiştirir.

        Kurallar:
        - Deleted kullanıcı değişemez
        - Admin kendini Admin dışına düşüremez
        """
        self._require_admin(performed_by)

        target = self.repo.get_by_id(target_user_id)
        if not target:
            raise ValueError("User not found.")

        if target.status == Status.Deleted:
            raise PermissionError("Deleted users cannot change role.")

        # Admin kendini downgrade edemesin
        if target.get_id_value() == performed_by.get_id_value() and new_role != Role.Admin:
            raise PermissionError("Admin cannot downgrade itself.")

        target._set_role_internal(new_role)
        target._set_modified_audit(performed_by_user_id=performed_by.get_id_value())

        self.repo.save_snapshot(target)
        self.logger.write("ROLE_CHANGE", target.to_log_dict())
        return target

    # ---------------------------------------------------------
    # Admin password reset
    # ---------------------------------------------------------
    def reset_password_admin(self, target_user_id: str, new_password: str, performed_by: User, password_policy_validator) -> User:
        """
        Admin tarafından şifre sıfırlama.

        Neden password_policy_validator parametre?
        - Şifre kuralını AuthService gibi merkezi bir yerde tutup
          burada tekrar etmeyelim
        - Test edilebilirliği artırır (dependency injection gibi)

        Kurallar:
        - Admin olmalı
        - Deleted kullanıcı reset edilemez
        - Şifre policy'ye uymalı
        """
        self._require_admin(performed_by)

        # Policy validation service dışından verilir
        password_policy_validator(new_password)

        target = self.repo.get_by_id(target_user_id)
        if not target:
            raise ValueError("User not found.")

        if target.status == Status.Deleted:
            raise PermissionError("Deleted users cannot reset password.")

        target._set_password_internal(new_password)
        target._set_modified_audit(performed_by_user_id=performed_by.get_id_value())

        # ✅ Admin reset -> session iptali
        self.auth._invalidate_user_sessions(target.get_id_value(), reason="admin_password_reset")

        self.repo.save_snapshot(target)
        self.logger.write("PASSWORD_RESET_ADMIN", target.to_log_dict())
        return target

    # ---------------------------------------------------------
    # Soft delete
    # ---------------------------------------------------------
    def soft_delete_user(self, target_user_id: str, performed_by: User) -> User:
        """
        Soft delete uygular:
        - status -> Deleted
        - deleted_date / deleted_by set edilir

        Not:
        - Bu işlem hard delete değildir
        - İleride geri alma (restore) gibi senaryolar eklenebilir
        """
        self._require_admin(performed_by)

        target = self.repo.get_by_id(target_user_id)
        if not target:
            raise ValueError("User not found.")

        target._set_deleted_audit(performed_by_user_id=performed_by.get_id_value())

        self.repo.save_snapshot(target)
        self.logger.write("DELETE", target.to_log_dict())
        return target

# endregion
# ============================================================



# ============================================================
# region Session
# ============================================================
# Session sınıfı, başarılı bir login sonrası kullanıcı için
# oluşturulan GEÇİCİ oturumu temsil eder.
#
# Bu yapı:
# - JWT veya Redis gibi sistemlerin BASİT bir alternatifi
# - CLI / demo / eğitim amaçlı senaryolar için idealdir
#
# Session ne tutar?
# - session_id  : Oturumu temsil eden benzersiz anahtar
# - user_id     : Oturumun hangi kullanıcıya ait olduğu
# - username    : UI / log için pratik bilgi
# - role        : Yetki kontrolü (Admin / Member vb.)
# - created_at  : Oturumun başladığı zaman
# - expires_at  : Oturumun geçerlilik süresi
#
# Önemli:
# - Session, User objesinin kendisini tutmaz
# - Sadece gerekli, güvenli ve hafif bilgileri saklar
# ============================================================

class Session:
    """
    Kullanıcı oturumunu (session) temsil eder.

    Not:
    - Stateless auth (JWT) yerine stateful bir yapı
    - active_sessions dict içinde saklanır (AuthService)
    """

    def __init__(self, user: User, ttl_minutes: int = 30):
        """
        Yeni bir session oluşturur.

        Parametreler:
            user (User):
                Login olmuş kullanıcı
            ttl_minutes (int):
                Oturumun kaç dakika geçerli olacağı
                Varsayılan: 30 dk
        """

        # -------------------------
        # Session identity
        # -------------------------
        # secrets.token_hex:
        # - cryptographically secure
        # - tahmin edilmesi zor
        self.session_id: str = secrets.token_hex(16)

        # -------------------------
        # User reference (lightweight)
        # -------------------------
        self.user_id: str = user.get_id_value()
        self.username: str = user.user_name
        self.role: str = user.role.name

        # -------------------------
        # Lifetime
        # -------------------------
        self.created_at: datetime = datetime.now()
        self.expires_at: datetime = self.created_at + timedelta(minutes=ttl_minutes)

    def is_expired(self) -> bool:
        """
        Session süresi dolmuş mu?

        Return:
            True  -> session geçersiz (expired)
            False -> session hala aktif

        Kullanım:
            if session.is_expired():
                logout / session drop
        """
        return datetime.now() >= self.expires_at

# Notlar:
# - Süresi dolan session mutlaka active_sessions'tan silinmelidir
# - Uzun yaşayan session'lar güvenlik riskidir
# endregion
# ============================================================



# ============================================================
# region AuthService
# ============================================================
# AuthService, sistemin "kimlik doğrulama" (authentication) ve
# "oturum yönetimi" (session management) süreçlerini yönetir.
#
# Bu servis neleri kapsar?
# 1) Validasyonlar (username/email/password policy)
# 2) Register (self-register) + email verification token üretme
# 3) Email verify (token ile doğrulama)
# 4) Resend verification (enumeration-safe)
# 5) Forgot password (enumeration-safe) + reset token üretme
# 6) Reset password (token ile şifre değiştirme)
# 7) Login (credential doğrulama + lockout/cooldown + business checks)
# 8) Session oluşturma, session expire ve invalidation kontrolü
# 9) Logout
#
# Repository ile farkı:
# - Repo: data access only
# - AuthService: business + security rules
#
# Logger:
# - Tüm kritik aksiyonlar audit log’a yazılır.
# - PII (email/ip) log’da maskelenir (to_log_dict)
# ============================================================

class AuthService:
    """
    Authentication & Session servisidir.

    Önemli kurallar:
    - Register -> user Pending olur
    - Email verify -> email_verified=True olur (hala Pending olabilir)
    - Admin approve -> account_status=Active olur
    - Login -> sadece email_verified=True AND account_status=Active ise başarılı
    - Brute-force -> failed count, cooldown ve lock ile engellenir
    """

    def __init__(self, repo: UserRepository, logger: AuditLogger, session_ttl_minutes: int = 30):
        """
        Parametreler:
            repo: User verisini bulmak/saklamak için repository
            logger: audit log yazmak için logger
            session_ttl_minutes: login sonrası session süresi (TTL)
        """
        self.repo = repo
        self.logger = logger
        self.session_ttl_minutes = session_ttl_minutes
        self.user_service = UserService(self.repo, self.logger, self.auth)

        # Active session store (stateful auth):
        # session_id -> Session
        self.active_sessions: Dict[str, Session] = {}

    # ========================================================
    # region Validations
    # ========================================================
    def _validate_username(self, username: str) -> str:
        """
        Username doğrulaması.
        - min 3 karakter
        - sadece harf, rakam, '_' ve '.' içerir

        Not:
        - Regex policy burada basit tutulmuştur (demo).
        - Prod'da reserved words, unicode, length upper bound vb. eklenebilir.
        """
        username = (username or "").strip()

        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters.")

        # allowed: letters, digits, underscore, dot
        if not re.fullmatch(r"[a-zA-Z0-9_.]+", username):
            raise ValueError("Username can contain only letters, digits, '_' or '.'.")

        return username

    def _validate_email(self, email: str) -> str:
        """
        Email format doğrulaması (basit regex).

        Not:
        - Email regex konusu çok geniştir.
        - Buradaki amaç: demo seviyesinde "bariz hatalı" input'u engellemek.
        """
        email = (email or "").strip().lower()

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            raise ValueError("Invalid email format.")

        return email

    def _validate_password_policy(self, password: str) -> None:
        """
        Password policy (iş kuralı).

        Kurallar:
        - En az 8 karakter
        - En az 1 büyük harf
        - En az 1 küçük harf
        - En az 1 rakam
        - En az 1 özel karakter (isalnum olmayan)

        Not:
        - Hash fonksiyonu policy yapmaz (separation of concerns)
        - Policy burada (service) uygulanır
        """
        if not password or len(password) < 8:
            raise ValueError("Password must be at least 8 characters.")

        if password.lower() == password:
            raise ValueError("Password must contain at least one uppercase letter.")

        if password.upper() == password:
            raise ValueError("Password must contain at least one lowercase letter.")

        if not any(ch.isdigit() for ch in password):
            raise ValueError("Password must contain at least one digit.")

        if not any(not ch.isalnum() for ch in password):
            raise ValueError("Password must contain at least one special character (e.g. !@#?).")
    # endregion
    # ========================================================

        # ========================================================
    # region Token Hashing Helpers
    # ========================================================
    def _hash_token(self, raw_token: str) -> str:
        """
        Raw token'ı DB'de/plain saklamamak için hash'ler.
        """
        raw_token = (raw_token or "").strip()
        if not raw_token:
            return ""

        # sha256(token + pepper)
        m = hashlib.sha256()
        m.update(raw_token.encode("utf-8"))
        m.update(TOKEN_PEPPER.encode("utf-8"))
        return m.hexdigest()

    def _invalidate_user_sessions(self, user_id: str, reason: str) -> None:
        """
        Bir kullanıcıya ait tüm aktif session'ları iptal eder.
        (Örn: password reset sonrası)
        """
        to_delete = [sid for sid, sess in self.active_sessions.items() if sess.user_id == user_id]
        for sid in to_delete:
            sess = self.active_sessions.pop(sid, None)
            if sess:
                self.logger.write("SESSION_INVALIDATED", {
                    "session_id": sess.session_id,
                    "user_id": sess.user_id,
                    "reason": reason
                })
    # endregion
    # ========================================================

    # ========================================================
    # region Register / Verify
    # ========================================================
    def register(self, first_name: str, last_name: str, username: str, email: str, password: str) -> str:
        """
        Self-register akışı.

        Yaptıkları:
        - username/email/password validate
        - user oluşturur (Pending)
        - email verification token üretir (gerçekte mail atılır)
        - repo'ya ekler
        - audit log yazar

        Return:
            verification token (demo)
        """
        username = self._validate_username(username)
        email = self._validate_email(email)
        self._validate_password_policy(password)

        # data integrity check (repo da ayrıca kontrol ediyor)
        if self.repo.find_by_username(username):
            raise ValueError("This username is already taken.")
        if self.repo.find_by_email(email):
            raise ValueError("This email is already taken.")

        user = User(first_name, last_name, username, email, password)

        # Audit: self register
        user._set_create_audit(performed_by_user_id=ACTOR_SELF_REGISTER)
        user._set_account_status_internal(AccountStatus.Pending)

        # Email verification token (demo: return)
        token = user._issue_email_verification_token(ttl_minutes=30, token_hash_provider=self._hash_token)

        # Save
        self.repo.add(user)
        self.repo.save_snapshot(user)

        # Log
        self.logger.write("REGISTER", user.to_log_dict())
        # token loglanmaz (güvenlik), sadece "sent" kaydı tutulur
        self.logger.write("EMAIL_VERIFICATION_SENT", {"user_id": user.get_id_value(), "email": mask_email(user.email)})

        return token

    def resend_verification(self, email: str) -> str:
        """
        Email doğrulama token'ını tekrar gönderme.

        Güvenlik (user enumeration önlemi):
        - Email kayıtlı OLSA DA OLMASA DA kullanıcıya aynı mesaj verilir.
        - Demo için token döndürüyoruz:
            - email yoksa dummy token döndürürüz.
        """
        email = self._validate_email(email)
        user = self.repo.find_by_email(email)

        # Email yoksa bile "başarılı" gibi davran (enumeration kapalı)
        if not user:
            self.logger.write("EMAIL_VERIFICATION_RESEND_IGNORED", {"email": mask_email(email), "reason": "not_found"})
            return secrets.token_urlsafe(24)  # dummy

        if user.status == Status.Deleted:
            self.logger.write("EMAIL_VERIFICATION_RESEND_IGNORED", {"user_id": user.get_id_value(), "reason": "deleted"})
            return secrets.token_urlsafe(24)

        if user.email_verified:
            self.logger.write("EMAIL_VERIFICATION_RESEND_IGNORED", {"user_id": user.get_id_value(), "reason": "already_verified"})
            return secrets.token_urlsafe(24)

        token = user._issue_email_verification_token(ttl_minutes=30, token_hash_provider=self._hash_token)
        user._set_modified_audit(performed_by_user_id="RESEND_VERIFY")

        self.repo.save_snapshot(user)
        self.logger.write("EMAIL_VERIFICATION_RESENT", {"user_id": user.get_id_value(), "email": mask_email(user.email)})

        return token

    def verify_email(self, email: str, token: str) -> User:
        """
        Email doğrulama.

        Kurallar:
        - user bulunmalı
        - user Deleted olmamalı
        - token doğru olmalı ve süresi dolmamalı
        """
        email = self._validate_email(email)
        user = self.repo.find_by_email(email)

        if not user:
            raise ValueError("User not found.")

        if user.status == Status.Deleted:
            raise PermissionError("Deleted users cannot verify email.")

        user._verify_email_with_token(token, token_hash_provider=self._hash_token)
        user._set_modified_audit(performed_by_user_id=ACTOR_EMAIL_VERIFY)

        self.repo.save_snapshot(user)
        self.logger.write("EMAIL_VERIFIED", user.to_log_dict())

        return user
    # endregion
    # ========================================================

    # ========================================================
    # region Forgot / Reset Password
    # ========================================================
    def forgot_password(self, email: str) -> str:
        """
        Şifre sıfırlama talebi (forgot password).

        Güvenlik (user enumeration önlemi):
        - Email kayıtlı olsa da olmasa da kullanıcıya aynı çıktı verilir.
        - Demo için token döndürüyoruz:
            - email yoksa dummy token döndürürüz.
        """
        email = self._validate_email(email)
        user = self.repo.find_by_email(email)

        if not user:
            self.logger.write("PASSWORD_RESET_REQUEST_IGNORED", {"email": mask_email(email), "reason": "not_found"})
            return secrets.token_urlsafe(24)  # dummy

        if user.status == Status.Deleted:
            self.logger.write("PASSWORD_RESET_REQUEST_IGNORED", {"user_id": user.get_id_value(), "reason": "deleted"})
            return secrets.token_urlsafe(24)

        token = user._issue_password_reset_token(ttl_minutes=15, token_hash_provider=self._hash_token)
        user._set_modified_audit(performed_by_user_id="FORGOT_PASSWORD")

        self.repo.save_snapshot(user)
        self.logger.write("PASSWORD_RESET_REQUESTED", {"user_id": user.get_id_value(), "email": mask_email(user.email)})

        return token

    def reset_password_with_token(self, email: str, token: str, new_password: str) -> User:
        """
        Token ile yeni şifre belirleme.

        Kurallar:
        - password policy geçerli olmalı
        - user bulunmalı ve deleted olmamalı
        - token doğru ve süresi dolmamış olmalı
        """
        email = self._validate_email(email)
        self._validate_password_policy(new_password)

        user = self.repo.find_by_email(email)
        if not user:
            raise ValueError("User not found.")

        if user.status == Status.Deleted:
            raise PermissionError("Deleted users cannot reset password.")

        user._reset_password_with_token(token, new_password, token_hash_provider=self._hash_token)
        user._set_modified_audit(performed_by_user_id=ACTOR_PASSWORD_RESET)

        # ✅ Şifre değişti -> tüm session'ları iptal et
        self._invalidate_user_sessions(user.get_id_value(), reason="password_reset")

        self.repo.save_snapshot(user)
        self.logger.write("PASSWORD_RESET_COMPLETED", user.to_log_dict())

        return user
    # endregion
    # ========================================================

    # ========================================================
    # region Session
    # ========================================================
    def get_session(self, session_id: str) -> Session:
        """
        Session doğrulama ve getirme.

        Kontroller:
        - session var mı?
        - süresi dolmuş mu? (expired)
        - session'a bağlı user hala var mı?
        - user deleted mi?
        - user account_status Active mi?

        Bu kontroller sayesinde:
        - admin bir kullanıcıyı suspend edince session anında invalid olur
        - deleted user session kullanamaz
        """
        sess = self.active_sessions.get(session_id)
        if not sess:
            raise PermissionError("Session not found.")

        if sess.is_expired():
            del self.active_sessions[session_id]
            self.logger.write("SESSION_EXPIRED", {"session_id": session_id, "user_id": sess.user_id})
            raise PermissionError("Session expired.")

        # Session içindeki user hala var mı?
        user = self.repo.get_by_id(sess.user_id)
        if not user:
            del self.active_sessions[session_id]
            self.logger.write("SESSION_INVALIDATED", {"session_id": session_id, "reason": "user_not_found"})
            raise PermissionError("Session invalidated.")

        # User aktif değilse session iptal
        if user.status == Status.Deleted or user.account_status != AccountStatus.Active:
            del self.active_sessions[session_id]
            self.logger.write("SESSION_INVALIDATED", {"session_id": session_id, "reason": "user_not_active_or_deleted"})
            raise PermissionError("Session invalidated.")

        return sess
    # endregion
    # ========================================================

    # ========================================================
    # region Login / Logout
    # ========================================================
    def login(self, username: str, password: str) -> Session:
        """
        Login akışı.

        Kontroller sırası (bilinçli):
        1) User var mı?
        2) Deleted/Passive mi?
        3) Suspended mı?
        4) Lock var mı?
        5) Şifre doğru mu? (yanlışsa failure kaydı + lock olabilir)
        6) Email verified mı?
        7) AccountStatus Active mi? (admin approval)
        8) Başarılı login -> session oluştur

        Bu sırayı korumak:
        - güvenlik
        - doğru log
        - doğru UX için önemlidir.
        """
        username = (username or "").strip()
        user = self.repo.find_by_username(username)

        # User yoksa: enumeration'a girmeden generic hata
        if not user:
            self.logger.write("LOGIN_FAIL", {"user_name": username, "reason": "invalid_credentials"})
            raise InvalidCredentialsError("Invalid username or password. (CapsLock açık olabilir)")

        # Status kontrolü (Deleted/Passive)
        if user.status in (Status.Deleted, Status.Passive):
            self.logger.write("LOGIN_FAIL", {**user.to_log_dict(), "reason": "status_not_allowed"})
            raise AuthError("Account is not available.")

        # Business: suspended
        if user.account_status == AccountStatus.Suspended:
            self.logger.write("LOGIN_FAIL", {**user.to_log_dict(), "reason": "suspended"})
            raise AuthError("Account is suspended.")

        # Lock kontrolü
        if user.is_locked():
            remaining = 0
            if user.lockout_until:
                remaining = int((user.lockout_until - datetime.now()).total_seconds())
            lock_level = user.get_lock_level()

            self.logger.write("LOGIN_FAIL", {**user.to_log_dict(), "reason": "locked"})
            raise AccountLockedError(remaining_seconds=remaining, lock_level=lock_level)

        # Şifre kontrolü
        if not user.check_password(password):
            # 실패 기록 + cooldown/lock
            user.record_login_failure(
                performed_by_user_id=ACTOR_LOGIN_FAIL,
                cooldown_after=3,
                cooldown_seconds=10,
                lock_after=5,
                base_lock_minutes=5
            )
            self.repo.save_snapshot(user)
            self.logger.write("LOGIN_FAIL", {**user.to_log_dict(), "reason": "invalid_credentials"})

            # Bu denemede lock devreye girdiyse locked exception dön
            if user.is_locked() and user.lockout_until:
                remaining = int((user.lockout_until - datetime.now()).total_seconds())
                raise AccountLockedError(remaining_seconds=remaining, lock_level=user.get_lock_level())

            raise InvalidCredentialsError("Invalid username or password. (CapsLock açık olabilir)")

        # Email verify şartı
        if not user.email_verified:
            self.logger.write("LOGIN_FAIL", {**user.to_log_dict(), "reason": "email_not_verified"})
            raise AuthError("Email is not verified.")

        # Admin approval şartı
        if user.account_status != AccountStatus.Active:
            self.logger.write("LOGIN_FAIL", {**user.to_log_dict(), "reason": "not_active"})
            raise AuthError("Account is pending approval or not active.")

        # Success
        user.record_login_success(performed_by_user_id=user.get_id_value())
        self.repo.save_snapshot(user)

        session = Session(user, ttl_minutes=self.session_ttl_minutes)
        self.active_sessions[session.session_id] = session

        self.logger.write("LOGIN_SUCCESS", user.to_log_dict())
        return session

    def logout(self, session_id: str) -> None:
        """
        Logout:
        - session store'dan siler
        - log yazar
        """
        sess = self.active_sessions.pop(session_id, None)
        if sess:
            self.logger.write("LOGOUT", {"session_id": sess.session_id, "user_id": sess.user_id, "user_name": sess.username})
    # endregion
    # ========================================================

# endregion
# ============================================================



# ============================================================
# region CLI App
# ============================================================
# App sınıfı, tüm sistemin CLI (terminal) üzerinden çalışan
# "presentation layer" (sunum katmanı) karşılığıdır.
#
# App ne yapar?
# - Repository + Service'leri oluşturur (composition)
# - Seed admin ile sistemi ayağa kaldırır
# - Menüleri gösterir (guest menu + admin panel)
# - Kullanıcıdan input alır (ask / ask_password / ask_password_confirm)
# - Service metotlarını çağırır
# - Hataları yakalar ve kullanıcıya düzgün mesaj verir
#
# Neden App ayrı bir sınıf?
# - main() çok kalabalık olmaz
# - UI akışları (ui_register, ui_login...) modüler olur
# - Test edilebilirlik ve okunabilirlik artar
# ============================================================

class App:
    """
    CLI uygulamasının ana sınıfı.

    Not:
    - Bu katman sadece UI akışını yönetir.
    - Business kuralları AuthService / UserService içinde kalır.
    """

    def __init__(self):
        # -------------------------
        # Infrastructure
        # -------------------------
        self.repo = UserRepository()
        self.logger = AuditLogger()

        # -------------------------
        # Services
        # -------------------------
        self.user_service = UserService(self.repo, self.logger)
        self.auth = AuthService(self.repo, self.logger, session_ttl_minutes=10)

        # -------------------------
        # UI State
        # -------------------------
        # current_session_id:
        # - login olunca set edilir
        # - logout veya session expire olunca sıfırlanır
        self.current_session_id: Optional[str] = None

        # -------------------------
        # Seed admin (first install)
        # -------------------------
        self.admin = self.user_service.seed_first_admin("admin", "admin@example.com", "Admin123A!")
        print("✅ Seed admin hazır -> username: admin / password: Admin123A!")

    # ========================================================
    # region Session/User helpers
    # ========================================================
    def _get_logged_user(self) -> Optional[User]:
        """
        UI tarafında "şu an login olan kullanıcı kim?" sorusunu çözer.

        Akış:
        - session_id yoksa None
        - session geçersiz/expired ise session temizlenir
        - session geçerliyse user repo'dan çekilir

        Not:
        - get_session() zaten user aktif mi/deleted mi kontrol eder.
        """
        if not self.current_session_id:
            return None

        try:
            sess = self.auth.get_session(self.current_session_id)
            return self.repo.get_by_id(sess.user_id)
        except Exception:
            # session invalid -> UI state temizle
            self.current_session_id = None
            return None

    def _require_login(self) -> User:
        """
        Login gerektiren işlemler için guard.
        """
        u = self._get_logged_user()
        if not u:
            raise PermissionError("Önce login olmalısın.")
        return u

    def _require_admin(self) -> User:
        """
        Admin gerektiren işlemler için guard.
        """
        u = self._require_login()
        if u.role != Role.Admin:
            raise PermissionError("Bu işlem için Admin olmalısın.")
        return u
    # endregion
    # ========================================================

    # ========================================================
    # region UI Actions (Guest/User)
    # ========================================================
    def ui_register(self) -> None:
        """
        Guest register ekranı.
        - Kullanıcı bilgileri alınır
        - AuthService.register çağrılır
        - Demo olarak token ekrana basılır
        """
        print("\n--- REGISTER ---")
        fn = ask("First name: ")
        ln = ask("Last name : ")
        un = ask("Username  : ")
        em = ask("Email     : ")

        print("Şifre kuralı: min 8 | 1 büyük | 1 küçük | 1 sayı | 1 özel karakter (!@#?)")
        pw = ask_password_confirm("Password  : ", "Password (again): ")

        token = self.auth.register(fn, ln, un, em, pw)
        print("\n✅ Register OK (Pending)")
        print("🔑 Verification Token (demo):", token)

        press_enter()

    def ui_verify_email(self) -> None:
        """
        Email verify ekranı.
        """
        print("\n--- VERIFY EMAIL ---")
        em = ask("Email: ")
        token = ask("Token: ")

        u = self.auth.verify_email(em, token)
        print("\n✅ Email verified:", u.to_safe_dict())

        press_enter()

    def ui_resend_verification(self) -> None:
        """
        Verify mail token yeniden gönderme.
        Enumeration-safe: email kayıtlı olmasa bile aynı mesaj.
        """
        print("\n--- RESEND VERIFICATION ---")
        em = ask("Email: ")

        token = self.auth.resend_verification(em)
        print("\n✅ Eğer email sistemde kayıtlıysa, doğrulama mesajı gönderildi. (demo token):", token)

        press_enter()

    def ui_forgot_password(self) -> None:
        """
        Şifremi unuttum ekranı.
        Enumeration-safe: email kayıtlı olmasa bile aynı mesaj.
        """
        print("\n--- FORGOT PASSWORD ---")
        em = ask("Email: ")

        token = self.auth.forgot_password(em)
        print("\n✅ Eğer email sistemde kayıtlıysa, şifre sıfırlama mesajı gönderildi. (demo token):", token)

        press_enter()

    def ui_reset_password(self) -> None:
        """
        Token ile şifre reset ekranı.
        """
        print("\n--- RESET PASSWORD (TOKEN) ---")
        em = ask("Email: ")
        token = ask("Token: ")

        print("Şifre kuralı: min 8 | 1 büyük | 1 küçük | 1 sayı | 1 özel karakter (!@#?)")
        new_pw = ask_password_confirm("New Password: ", "New Password (again): ")

        u = self.auth.reset_password_with_token(em, token, new_pw)
        print("\n✅ Password reset OK:", u.to_safe_dict())

        press_enter()

    def ui_login(self) -> None:
        """
        Login ekranı.

        Exception handling:
        - AccountLockedError -> countdown göster
        - InvalidCredentialsError -> kullanıcıya net mesaj
        - diğer -> generic hata
        """
        print("\n--- LOGIN ---")
        print("Şifre kuralı: min 8 | 1 büyük | 1 küçük | 1 sayı | 1 özel karakter (!@#?)")

        un = ask("Username: ")
        pw = ask_password("Password: ", show_hint=False)

        try:
            sess = self.auth.login(un, pw)
            self.current_session_id = sess.session_id

            print("\n✅ Login OK")
            print("Session:", sess.session_id)

            press_enter()

        except AccountLockedError as ex:
            print(f"\n🚫 {ex}")
            finished = show_countdown(ex.remaining_seconds, ex.lock_level)
            if finished:
                press_enter()

        except InvalidCredentialsError as ex:
            print(f"\n❌ {ex}")
            press_enter()

        except Exception as ex:
            print(f"\n❌ Hata: {ex}")
            press_enter()

    def ui_logout(self) -> None:
        """
        Logout ekranı.
        """
        if self.current_session_id:
            self.auth.logout(self.current_session_id)

        self.current_session_id = None
        print("\n✅ Logout OK")
        press_enter()

    def ui_list_users(self) -> None:
        """
        Kullanıcıları güvenli formatta listeler (hash yok).
        """
        print("\n--- USERS (SAFE) ---")
        for u in self.repo.list_all():
            print(u.to_safe_dict())
        press_enter()
    # endregion
    # ========================================================

    # ========================================================
    # region Admin Panel
    # ========================================================
    def ui_admin_panel(self) -> None:
        """
        Admin panel menüsü.

        Admin paneli içerisinde:
        - approve
        - suspend/unsuspend
        - role change
        - admin password reset
        - soft delete
        - list users
        """
        admin = self._require_admin()

        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("====================================")
            print("           ADMIN PANEL              ")
            print("====================================")
            print(f"Admin: {admin.user_name} ({admin.get_id_value()})")
            print("------------------------------------")
            print("1) Approve user (Pending -> Active)")
            print("2) Suspend user")
            print("3) Unsuspend user (Suspended -> Pending)")
            print("4) Change role")
            print("5) Reset password (Admin)")
            print("6) Soft delete user")
            print("7) List users (safe)")
            print("0) Back")

            c = ask("\nSeçim: ")

            try:
                if c == "1":
                    uid = ask("Target user id: ")
                    u = self.user_service.approve_user(uid, performed_by=admin)
                    print("✅ Approved:", u.to_safe_dict())
                    press_enter()

                elif c == "2":
                    uid = ask("Target user id: ")
                    u = self.user_service.suspend_user(uid, performed_by=admin)
                    print("✅ Suspended:", u.to_safe_dict())
                    press_enter()

                elif c == "3":
                    uid = ask("Target user id: ")
                    u = self.user_service.unsuspend_user(uid, performed_by=admin)
                    print("✅ Unsuspended:", u.to_safe_dict())
                    press_enter()

                elif c == "4":
                    uid = ask("Target user id: ")
                    print("Roles: Admin=1, Member=2, Author=3")
                    r = ask("New role (1/2/3): ")
                    new_role = Role(int(r))
                    u = self.user_service.change_role(uid, new_role, performed_by=admin)
                    print("✅ Role changed:", u.to_safe_dict())
                    press_enter()

                elif c == "5":
                    uid = ask("Target user id: ")
                    print("Şifre kuralı: min 8 | 1 büyük | 1 küçük | 1 sayı | 1 özel karakter (!@#?)")
                    pw = ask_password_confirm("New password: ", "New password (again): ")

                    # Policy validator'ı AuthService'ten alıyoruz (DRY)
                    u = self.user_service.reset_password_admin(
                        uid, pw, performed_by=admin, password_policy_validator=self.auth._validate_password_policy
                    )
                    print("✅ Password reset:", u.to_safe_dict())
                    press_enter()

                elif c == "6":
                    uid = ask("Target user id: ")
                    u = self.user_service.soft_delete_user(uid, performed_by=admin)
                    print("✅ Deleted:", u.to_safe_dict())
                    press_enter()

                elif c == "7":
                    self.ui_list_users()

                elif c == "0":
                    break

                else:
                    print("Geçersiz seçim.")
                    press_enter()

            except Exception as ex:
                print(f"\n❌ Hata: {ex}")
                press_enter()
    # endregion
    # ========================================================

    # ========================================================
    # region Main Loop
    # ========================================================
    def run(self) -> None:
        """
        Uygulamanın ana menü döngüsü.

        Kullanıcı durumuna göre:
        - guest menü (register/login/verify...)
        - logged user bilgisi (role/status/lock level)
        - admin panel erişimi
        """
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            user = self._get_logged_user()

            print("====================================")
            print("      USER AUTH CLI (10/10)         ")
            print("====================================")

            if user:
                print(
                    f"Login: ✅  {user.user_name} ({user.role.name}) | "
                    f"Account: {user.account_status.name} | Entity: {user.status.name} | "
                    f"LockLevel: {user.get_lock_level()}"
                )
            else:
                print("Login: ❌  (guest)")

            print("------------------------------------")
            print("1) Register")
            print("2) Verify Email")
            print("3) Resend Verification Email")
            print("4) Forgot Password")
            print("5) Reset Password (Token)")
            print("6) Login")
            print("7) Logout")
            print("8) List Users (safe)")
            print("9) Admin Panel")
            print("0) Exit")

            choice = ask("\nSeçim: ")

            try:
                if choice == "1":
                    self.ui_register()
                elif choice == "2":
                    self.ui_verify_email()
                elif choice == "3":
                    self.ui_resend_verification()
                elif choice == "4":
                    self.ui_forgot_password()
                elif choice == "5":
                    self.ui_reset_password()
                elif choice == "6":
                    self.ui_login()
                elif choice == "7":
                    self.ui_logout()
                elif choice == "8":
                    self.ui_list_users()
                elif choice == "9":
                    self.ui_admin_panel()
                elif choice == "0":
                    print("Çıkış...")
                    break
                else:
                    print("Geçersiz seçim.")
                    press_enter()

            except Exception as ex:
                print(f"\n❌ Hata: {ex}")
                press_enter()
    # endregion
    # ========================================================

# endregion
# ============================================================


# ============================================================
# region Main
# ============================================================
# main() fonksiyonu uygulamanın entry-point'idir.
# - App instance oluşturur
# - UI döngüsünü başlatır
# - Program bittiğinde log dosyası bilgisini gösterir
# ============================================================

def main():
    app = App()
    app.run()
    print("\nLogs written to: logs/user_activity.log")


if __name__ == "__main__":
    main()

# endregion
# ============================================================