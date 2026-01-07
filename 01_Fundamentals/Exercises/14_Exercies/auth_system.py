# region Auth System — Sign In / Sign Up (SRP + SoC)
# todo: Sign In ve Sign Up
# todo: tüm problem main() fonksiyonu içinde çalışacak

"""
BU DOSYA NE YAPIYOR?
------------------------------------------------------------
Bu dosya, terminal üzerinden çalışan basit ama güvenli bir Auth (Kimlik Doğrulama) sistemi kurar.

✅ Sign Up (Kayıt):
    - Kullanıcı email + şifre girer
    - Email formatı kontrol edilir
    - Şifre kurallara uygun mu kontrol edilir
    - Şifre düz metin saklanmaz -> PBKDF2 ile hash'lenir
    - Kullanıcı “ID” üretilerek saklanır

✅ Sign In (Giriş):
    - Kullanıcı email + şifre girer
    - Email'den kullanıcı bulunur (O(1))
    - Lockout kontrol edilir (MAX_ATTEMPTS + LOCKOUT_SECONDS)
    - Şifre doğrulanır (verify_password)
    - Başarılıysa giriş yapılır ve deneme hakkı sıfırlanır
    - Başarısızsa deneme hakkı düşer, biterse hesap kilitlenir

SRP (Single Responsibility Principle) NEDİR?
------------------------------------------------------------
- Her fonksiyon sadece 1 sorumluluk taşımalı
Örn:
    email_is_valid -> sadece email doğrular
    hash_password  -> sadece hash üretir
    sign_in        -> sadece giriş akışını yönetir

SoC (Separation of Concerns) NEDİR?
------------------------------------------------------------
- UI (print/input) ile iş mantığını ayırmak
- Veri erişimini (lookup) ayrı fonksiyonlarda tutmak
- Lockout state yönetimini ayrı fonksiyonlara bölmek

BÖLÜMLER:
------------------------------------------------------------
- Config / Constants (MAX_ATTEMPTS, LOCKOUT_SECONDS, ITERATIONS)
- Input Helpers (get_password)
- Validators (normalize_mail, email_is_valid, pwd_is_valid)
- Hashing (hash_password, verify_password)
- Data Access (find_user_by_mail)
- Lockout State (get_state, check_lock, fail_attempt, reset_state)
- Commands (create_user, sign_up, sign_in)
- Main Orchestration (main + menu)
"""


# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
import os           # salt üretmek (os.urandom)
import time         # lockout süre hesabı (time.time)
import uuid         # kullanıcıya benzersiz id vermek
import hmac         # compare_digest ile timing attack riskini azaltmak
import hashlib      # pbkdf2_hmac ile parola hashlemek
from typing import Any


MAX_ATTEMPTS = 3    # # Bir kullanıcı arka arkaya kaç kere yanlış şifre girebilir?
LOCKOUT_SECONDS = 5 * 60  # Deneme hakkı biterse kaç saniye kilit? -> 5 dakika
PBKDF2_ITERATIONS = 100_000     # PBKDF2 iterasyon: yüksek = daha güvenli ama daha yavaş


# ------------------------------------------------------------
# INPUT HELPERS
# ------------------------------------------------------------

def get_password(prompt: str = "Password: ") -> str:
    """
    Kullanıcıdan terminal üzerinden **yıldızlı (*) şekilde** parola girişi alır.

    Bu fonksiyon, girilen karakterleri ekranda gizler ve her karakter
    yerine `*` basarak klasik password deneyimi sağlar.

    Özellikler:
    - Enter'a basılana kadar karakterleri tek tek okur
    - Backspace ile silme desteği vardır
    - Ctrl + C ile güvenli şekilde çıkış yapılabilir
    - Girilen gerçek karakterler ekranda görünmez

    Amaç:
    - Şifre ekranda görünmesin
    - Windows'ta yıldızlı (*) password input deneyimi olsun
    - Windows değilse getpass ile güvenli şekilde gizli alınsın

    Windows (os.name == "nt"):
        - msvcrt.getwch() ile karakter karakter okur
        - her karakter için '*' basar
        - backspace desteği vardır
        - Ctrl+C ile iptal edilir

    Non-Windows:
        - getpass.getpass() ile input gizlenir

    Args:
        prompt (str): Kullanıcıya gösterilecek giriş mesajı

    Returns:
        str: Kullanıcının girdiği parola (string)

    Raises:
        KeyboardInterrupt: Kullanıcı Ctrl + C yaptığında
    """
    if os.name == "nt":
        import msvcrt

        while True:
            print(prompt, end="", flush=True)

            password_chars: list[str] = []

            while True:

                # Klavyeden tek karakter oku (echo yapmaz)
                ch = msvcrt.getwch()

                # Enter'a basıldıysa -> giriş tamam
                if ch in ("\r", "\n"):
                    print()  # yeni satıra geç
                    break

                # Backspace -> son karakteri sil
                if ch == "\b":
                    if password_chars:
                        password_chars.pop()
                        # terminalde yıldızı da sil
                        print("\b \b", end="", flush=True)
                    continue

                # Ctrl + C -> manuel kesme
                if ch == "\x03":
                    raise KeyboardInterrupt

                # Normal karakter
                password_chars.append(ch)
                print("*", end="", flush=True)
            
            # Karakter listesini string'e çevir
            password = "".join(password_chars)

            # BOŞ / SADECE BOŞLUK kontrolü
            if not password.strip():
                print("❌ Şifre boş veya sadece boşluklardan oluşamaz.\n")
                continue

            return password

    # Windows değilse fallback
    import getpass

    while True:
        password = getpass.getpass(prompt)
        if not password.strip():
            print("❌ Şifre boş veya sadece boşluklardan oluşamaz.\n")
            continue
        return password


# ------------------------------------------------------------
# VALIDATORS (SRP)
# ------------------------------------------------------------
def normalize_mail(mail: str) -> str:
    """
    Email normalize eder:
    - strip(): baş/son boşlukları temizler
    - lower(): küçük harfe çevirir

    Neden?
    - Kullanıcı "BEAST@gmail.com" yazsa da aynı hesap olmalı
    - Kayıt ve girişte tutarlılık sağlar
    """
    return mail.strip().lower()


def email_is_valid(email: str) -> bool:
    """
    Verilen email adresinin **temel format doğrulamasını** yapar.

    Bu fonksiyon:
    - Email'in string olup olmadığını kontrol eder
    - Baştaki ve sondaki boşlukları temizler
    - Maksimum uzunluk (254 karakter) sınırını uygular
    - Basit ve hızlı bir regex ile email formatını doğrular

    ⚠️ Not:
    - Bu kontrol **RFC 5322'nin tamamını kapsamaz**
    - Ama sign-up gibi kullanıcı girişleri için
      yeterince güvenli ve performanslıdır

    Args:
        email (str): Doğrulanacak email adresi

    Returns:
        bool:
            - True → Email format olarak geçerli
            - False → Geçersiz email
    """
    import re

    # Email için basit ve performanslı regex pattern
    # - boşluk içeremez
    # - '@' zorunlu
    # - domain kısmında en az 2 karakter olmalı
    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]{2,}$"
    
    # Email parametresi string değilse direkt geçersiz say
    if not isinstance(email, str):
        return False
    
    # Kullanıcı girişindeki baştaki ve sondaki boşlukları temizle
    email = email.strip()

    # Email boş olamaz ve RFC standardına göre 254 karakteri geçemez
    if not email or len(email) > 254:
        return False
    
    # Regex'in tüm string ile eşleşip eşleşmediğini kontrol et
    # fullmatch kullanımı, kısmi eşleşmeleri engeller
    return re.fullmatch(pattern, email) is not None


def pwd_is_valid(password: str) -> tuple[bool, list[str]]:
    """
    Şifre doğrulama fonksiyonu.

    Kurallar:
    - En az `min_length` karakter
    - En az 1 büyük harf
    - En az 1 küçük harf
    - En az 1 rakam
    - En az 1 özel karakter
    - Sadece boşluklardan oluşamaz

    Args:
        password (str): Kontrol edilecek şifre

    Returns:
        tuple[bool, list[str]]:
            - bool: Şifre geçerli mi?
            - list[str]: Hata mesajları
    """
    min_length = 6
    errors: list[str] = []

    if not isinstance(password, str):
        return False, ["Şifre string tipinde olmalıdır."]
    
    if not password.strip():
        return False, ["Şifre boş veya sadece boşluklardan oluşamaz."]
    
    if len(password) < min_length:
        errors.append(f"Şifre en az {min_length} karakter olmalı.")

    special_chars = set("!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~")

    has_upper = has_lower = has_digit = has_special = False

    for ch in password:
        # erken çıkış: hepsi bulunduysa
        if has_upper and has_lower and has_digit and has_special:
            break

        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    # Rule validations
    if not has_upper:
        errors.append("Şifre en az 1 büyük harf içermeli.")
    if not has_lower:
        errors.append("Şifre en az 1 küçük harf içermeli.")
    if not has_digit:
        errors.append("Şifre en az 1 rakam içermeli.")
    if not has_special:
        errors.append("Şifre en az 1 özel karakter içermeli.")

    return not errors, errors


# ------------------------------------------------------------
# HASHING (SRP)
# ------------------------------------------------------------

def hash_password(password: str, iterations: int = PBKDF2_ITERATIONS) -> str:
    """
    Şifreyi güvenli şekilde hash'ler (PBKDF2 + SHA256 + salt).

    Neden PBKDF2?
        - Brute-force saldırılarına karşı yavaştır
        - Salt + iteration kullanır
        - Endüstri standardıdır

    Saklanan format:
        iterations$salt_hex$hash_hex
        Örn: 100000$ab12cd34...$9f8e7d...

    Format:
        iterations$salt_hex$hash_hex

   Args:
        password (str): Kullanıcının girdiği plain text şifre
        iterations (int): Hash'in kaç tur çalıştırılacağı
                          (yüksek değer = daha güvenli ama daha yavaş)

    Returns:
        str: Veritabanında güvenle saklanabilecek hash string
    """

    # Her kullanıcı için rastgele bir salt üret
    # Aynı şifreler bile farklı hash'ler üretir
    salt = os.urandom(16)  # 16 byte = 128-bit (önerilen minimum)

    # Şifreyi bytes'a çevir (hash fonksiyonları bytes ile çalışır)
    pwd_bytes = password.encode("utf-8")

    # PBKDF2 + HMAC + SHA256 ile şifreyi hash'le
    # iterations kadar tekrar edilerek brute-force zorlaştırılır
    hash_bytes = hashlib.pbkdf2_hmac(
        "sha256",     # Kullanılan hash algoritması
        pwd_bytes,    # Kullanıcının şifresi (bytes)
        salt,         # Rastgele üretilmiş salt
        iterations    # Kaç tur hash uygulanacağı
    )

    # Tek string halinde saklamak için:
    # iterations + salt + hash bilgilerini birleştiriyoruz
    # .hex() -> binary veriyi stringe çevirir (DB / JSON dostu)
    return f"{iterations}${salt.hex()}${hash_bytes.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Kullanıcının girdiği parolanın, sistemde kayıtlı hash ile eşleşip eşleşmediğini doğrular.

    Bu fonksiyon, veritabanında saklanan hash bilgisini (iterations$salt_hex$hash_hex)
    formatına göre parçalar ve kullanıcının girdiği parolayı aynı parametrelerle
    (PBKDF2 + SHA256 + aynı salt + aynı iterasyon) tekrar hash’ler.

    Ardından, elde edilen hash ile kayıtlı hash karşılaştırılır.
    Karşılaştırma işlemi timing-attack (zamanlama saldırısı) riskini azaltmak için
    `hmac.compare_digest` ile yapılır.

    Saklanan Hash Formatı:
        iterations$salt_hex$hash_hex

    Örnek:
        "100000$5f2c...a1$9c3e...ff"

    Güvenlik Notları:
        - PBKDF2, brute-force saldırılarını yavaşlatmak için iterasyon kullanır.
        - Salt, aynı parolanın her kullanıcıda farklı hash üretmesini sağlar.
        - compare_digest, erken çıkış yapan string karşılaştırmalarına göre daha güvenlidir.

    Args:
        password (str):
            Kullanıcının girişte yazdığı düz metin (plain text) parola.
        stored_hash (str):
            Veritabanında saklanan hash string’i.
            Format: iterations$salt_hex$hash_hex

    Returns:
        bool:
            - True: parola doğru (hash’ler eşleşiyor)
            - False: parola yanlış veya kayıt formatı geçersiz
    """

    # Hızlı tip/boş kontrol (defansif programlama)
    if not isinstance(password, str) or not isinstance(stored_hash, str):
        return False
    if not password or not stored_hash:
        return False

    # Kayıt formatını parçala: iterations$salt_hex$hash_hex
    try:
        iter_str, salt_hex, hash_hex = stored_hash.split("$", 2)
        iterations = int(iter_str)

        # Salt ve hash hex -> byte'a çevir
        salt = bytes.fromhex(salt_hex)
        expected_hash = bytes.fromhex(hash_hex)

        # Basit doğrulama: iterasyon mantıklı mı?
        # (0 veya negatif olamaz; aşırı küçük olmasın diye alt sınır da koyabilirsin)
        if iterations <= 0:
            return False
        if len(salt) < 16:  # sen 16 byte salt üretiyordun (os.urandom(16))
            return False
        if len(expected_hash) == 0:
            return False

    except (ValueError, TypeError):
        # split/int/hex parse patladıysa -> kayıt bozuk/uygunsuz
        return False

    # Kullanıcının girdiği parolayı aynı parametrelerle tekrar hash’le
    pwd_bytes = password.encode("utf-8")

    computed_hash = hashlib.pbkdf2_hmac(
        "sha256",        # hash algoritması
        pwd_bytes,       # parola bytes
        salt,            # kayıtlı salt
        iterations       # kayıtlı iterasyon
    )

    # Timing attack riskini azaltarak karşılaştır
    return hmac.compare_digest(computed_hash, expected_hash)


# ------------------------------------------------------------
# DATA ACCESS (SoC)
# ------------------------------------------------------------

def find_user_by_mail(users: dict[str, dict[str, str]], user_info: dict[str, str], mail: str) -> tuple[str | None, dict[str, str] | None]:
    """
    Mail adresi üzerinden kullanıcıyı **O(1)** zamanda bulur.

    Mantık:
        mail -> user_id -> user_data

    Parametreler:
        users (dict[str, dict[str, str]]):
            Kullanıcıların **ID bazlı** tutulduğu ana tablo.
            Örnek:
                {
                    "uuid-1": {"mail": "...", "password": "..."},
                    "uuid-2": {"mail": "...", "password": "..."}
                }

        user_info (dict[str, str]):
            Mail → UserId eşlemesi yapan index sözlüğü.
            Örnek:
                {
                    "beast@gmail.com": "uuid-1",
                    "lion@gmail.com": "uuid-2"
                }

        mail (str):
            Kullanıcıdan gelen e-mail adresi (ham input).

    Returns:
        tuple[str | None, dict[str, str] | None]:
            - user_id (str | None)
            - user_data (dict | None)

            Kullanıcı bulunamazsa:
                (None, None)
    """

    # ------------------------------------------------------------
    # 1️⃣ Mail normalize edilir
    # ------------------------------------------------------------
    # Neden?
    # - " BEAST@gmail.com "
    # - "beast@gmail.com"
    # - "BeAsT@Gmail.Com"
    #
    # Hepsi aynı kullanıcıyı temsil etmeli
    mail = mail.strip().lower()

    # ------------------------------------------------------------
    # 2️⃣ Mail üzerinden user_id bulunur (O(1))
    # ------------------------------------------------------------
    # user_info bir "index" gibi çalışır:
    # mail -> user_id
    user_id = user_info.get(mail)

    # ------------------------------------------------------------
    # 3️⃣ Kullanıcı yoksa güvenli çıkış
    # ------------------------------------------------------------
    # .get() None dönerse:
    # - kullanıcı yok
    # - ya da hiç kayıt edilmemiş
    if not user_id:
        return None, None

    # ------------------------------------------------------------
    # 4️⃣ user_id ile kullanıcı verisi alınır (O(1))
    # ------------------------------------------------------------
    # users sözlüğü ID bazlı olduğu için
    # doğrudan erişim yapılır
    return user_id, users.get(user_id)


# ------------------------------------------------------------
# LOCKOUT STATE (SRP)
# ------------------------------------------------------------

def get_state(attempts_left: dict[str, dict], mail: str) -> dict:
    """
    Belirli bir kullanıcıya ait giriş deneme ve kilit (lockout) durumunu döndürür.

    Bu fonksiyon, kullanıcıya ait giriş deneme bilgisini merkezi ve güvenli
    şekilde yönetmek için kullanılır. Amaç, `sign_in` gibi ana akış fonksiyonlarının
    içini karmaşık state kontrolleriyle doldurmadan, kullanıcıya ait mevcut
    durumu tek noktadan elde etmektir.

    Eğer kullanıcı daha önce hiç giriş denemesi yapmamışsa veya state bilgisi
    henüz oluşturulmamışsa, fonksiyon varsayılan bir state üretir.

    Dönen state sözlüğü şu alanları içerir:
        - left (int):
            Kullanıcının kalan hatalı giriş deneme hakkı.
            Varsayılan olarak MAX_ATTEMPTS ile başlar.

        - locked_until (float | None):
            Hesabın kilitli olduğu durumlarda, kilidin açılacağı zamanı
            UNIX timestamp (time.time()) formatında tutar.
            Eğer hesap kilitli değilse None olur.

    Bu yapı sayesinde:
        - Lockout kontrolü
        - Kalan deneme sayısı takibi
        - Zaman bazlı kilitleme
    gibi işlemler tutarlı ve tekrar kullanılabilir hale gelir.

    Args:
        attempts_left (dict[str, dict]):
            Kullanıcıların giriş deneme ve kilit bilgilerini tutan sözlük.
            Örnek yapı:
                {
                    "mail@example.com": {
                        "left": 2,
                        "locked_until": 1734950000.0
                    }
                }

        mail (str):
            Giriş yapmaya çalışan kullanıcının e-mail adresi.
            Bu değer sözlükte anahtar (key) olarak kullanılır.

    Returns:
        dict:
            Kullanıcıya ait state bilgisi.
            Eğer kullanıcı için kayıt yoksa, aşağıdaki varsayılan yapı döner:
                {
                    "left": MAX_ATTEMPTS,
                    "locked_until": None
                }
    """

    # Kullanıcıya ait daha önce oluşturulmuş bir state varsa onu döndür
    # Yoksa: yeni bir kullanıcı gibi varsayılan state üret
    return attempts_left.get(
        mail,
        {
            "left": MAX_ATTEMPTS,     # Başlangıç deneme hakkı
            "locked_until": None      # Hesap kilitli değil
        }
    )


def check_lock(state: dict) -> int:
    """
    Bir kullanıcının hesabının şu anda kilitli olup olmadığını kontrol eder
    ve kilitliyse kilidin açılmasına kalan süreyi saniye cinsinden döndürür.

    Bu fonksiyon, zaman bazlı kilitleme (time-based lockout) mekanizmasının
    merkezinde yer alır. Kullanıcının hesap durumu, daha önce oluşturulmuş
    bir `state` sözlüğü üzerinden değerlendirilir.

    Eğer hesap kilitli değilse veya kilit süresi sona ermişse,
    fonksiyon 0 döndürerek girişe izin verilebileceğini belirtir.

    Eğer hesap kilitliyse:
        - Kilidin açılacağı zaman (locked_until) ile
          mevcut zaman (time.time()) karşılaştırılır
        - Kalan süre hesaplanır ve saniye cinsinden döndürülür

    Bu yaklaşım sayesinde:
        - sign_in akışı gereksiz karmaşıklıktan kurtulur
        - Kilit kontrolü tek bir noktadan yapılır
        - Zaman bazlı güvenlik politikaları kolayca yönetilir

    Beklenen state yapısı:
        {
            "left": int,
            "locked_until": float | None
        }

    Args:
        state (dict):
            Kullanıcıya ait giriş deneme ve kilit bilgilerini içeren sözlük.
            'locked_until' anahtarı yoksa veya değeri None ise,
            hesap kilitli kabul edilmez.

    Returns:
        int:
            - 0  → hesap kilitli değil veya kilit süresi dolmuş
            - >0 → hesabın kilidinin açılmasına kalan saniye sayısı
    """

    # State içinden kilit bitiş zamanını al
    locked_until = state.get("locked_until")

    # Kilit bilgisi yoksa → hesap kilitli değil
    if locked_until is None:
        return 0

    # Mevcut zaman (UNIX timestamp)
    now = time.time()

    # Eğer şu anki zaman kilit bitiş zamanından küçükse,
    # hesap hâlâ kilitlidir → kalan süre hesaplanır
    if now < locked_until:
        return int(locked_until - now)

    # Kilit süresi dolmuşsa → kilit yok
    return 0


def reset_state(attempts_left: dict[str, dict], mail: str) -> None:
    """
    Bir kullanıcıya ait giriş deneme ve kilit (lockout) durumunu tamamen sıfırlar.

    Bu fonksiyon, kullanıcının giriş sürecinde bir “temiz başlangıç” yapılması
    gereken durumlarda kullanılır. Özellikle:
        - Kullanıcı başarılı şekilde giriş yaptığında
        - Zaman bazlı kilitleme süresi sona erdiğinde

    kullanıcıya ait tüm geçici güvenlik verilerinin temizlenmesini sağlar.

    State bilgisinin tamamen silinmesi, kullanıcının bir sonraki giriş
    denemesinde sistem tarafından yeni bir kullanıcı gibi
    varsayılan deneme haklarıyla değerlendirilmesine imkân tanır.

    Bu yaklaşımın avantajları:
        - Gereksiz state birikimi engellenir
        - Bellek kullanımı sade kalır
        - Deneme/kilit yönetimi merkezi ve tutarlı olur
        - sign_in gibi ana akış fonksiyonları sadeleşir

    Args:
        attempts_left (dict[str, dict]):
            Kullanıcıların giriş deneme ve kilit bilgilerini tutan sözlük.
            Bu sözlükte her kullanıcı e-mail adresi anahtar (key) olarak yer alır.

        mail (str):
            State’i sıfırlanacak kullanıcının e-mail adresi.
            Eğer bu e-mail için kayıt yoksa işlem güvenli şekilde yok sayılır.

    Returns:
        None
            Fonksiyon yalnızca state’i temizler, herhangi bir değer döndürmez.
    """

    # Kullanıcıya ait state bilgisini güvenli şekilde sil
    # pop(..., None) → key yoksa KeyError fırlatmaz
    attempts_left.pop(mail, None)


def fail_attempt(attempts_left: dict[str, dict], mail: str, state: dict) -> dict:
    """
    Bir kullanıcı için gerçekleşen hatalı giriş denemesini kaydeder
    ve ilgili deneme/kilit (lockout) state'ini günceller.

    Bu fonksiyon, başarısız giriş denemelerine ait tüm iş mantığını
    tek bir noktada toplamak amacıyla oluşturulmuştur.
    Böylece `sign_in` gibi ana akış fonksiyonları yalnızca
    “başarılı mı / başarısız mı?” kararına odaklanır.

    Fonksiyonun temel sorumlulukları:
        - Kullanıcının kalan giriş deneme hakkını 1 azaltmak
        - Deneme hakkı biterse zaman bazlı kilitlemeyi başlatmak
        - Güncellenmiş state bilgisini merkezi yapıda saklamak

    Güncellenen state sözlüğü şu alanları içerir:
        - left (int):
            Kullanıcının kalan hatalı giriş deneme hakkı.
            Her hatalı girişte 1 azaltılır.

        - locked_until (float | None):
            Deneme hakkı sıfırlandığında, hesabın kilitleneceği
            süreyi belirten UNIX timestamp değeridir.
            Hesap kilitlenmezse None olarak kalır.

    Bu yapı sayesinde:
        - Lockout kuralları tek yerden yönetilir
        - Hatalı deneme davranışı tutarlı hale gelir
        - Güvenlik politikaları kolayca değiştirilebilir

    Args:
        attempts_left (dict[str, dict]):
            Kullanıcıların giriş deneme ve kilit bilgilerini tutan sözlük.
            Güncellenen state bu sözlük içinde saklanır.

        mail (str):
            Hatalı giriş yapan kullanıcının e-mail adresi.
            State, bu anahtar (key) altında güncellenir.

        state (dict):
            Kullanıcıya ait mevcut giriş deneme durumu.
            Bu sözlük, fonksiyon tarafından güncellenir ve geri döndürülür.

    Returns:
        dict:
            Güncellenmiş kullanıcı state bilgisi.
            Bu değer, çağıran fonksiyon tarafından tekrar kullanılabilir.
    """

    # Kullanıcının kalan deneme hakkını 1 azalt
    # Eğer 'left' alanı yoksa varsayılan MAX_ATTEMPTS kabul edilir
    state["left"] = int(state.get("left", MAX_ATTEMPTS)) - 1

    # Deneme hakkı bittiyse zaman bazlı kilit başlat
    if state["left"] <= 0:
        state["locked_until"] = time.time() + LOCKOUT_SECONDS

    # Güncellenen state'i merkezi yapıya kaydet
    attempts_left[mail] = state

    # Güncel state'i çağıran fonksiyona geri döndür
    return state


# ------------------------------------------------------------
# COMMANDS (Sign Up / Sign In) - SRP
# ------------------------------------------------------------

def create_user(users: dict[str, dict[str, str]], user_info: dict[str, str], mail: str,
                password: str) -> str | None:    
    """
    Yeni bir kullanıcıyı sisteme güvenli şekilde kaydeder (Sign Up).

    Bu fonksiyon, verilen e-mail adresini kullanıcı için tek ve benzersiz
    kimlik (ID) olarak kabul eder. Kullanıcının parolası düz metin (plain text)
    olarak saklanmaz; güvenli bir şekilde hash'lenerek veritabanına kaydedilir.

    Fonksiyonun sorumlulukları:
        - E-mail adresini normalize etmek (strip + lower)
        - Aynı e-mail ile kayıtlı kullanıcı olup olmadığını kontrol etmek
        - Parolayı güvenli şekilde hash'lemek
        - Kullanıcıyı users_db yapısına eklemek

    Güvenlik Özellikleri:
        - Hash'lenmiş parola saklanır (PBKDF2 / SHA256 varsayılır)
        - E-mail bazlı mükerrer kayıt engellenir
        - Kullanıcı verisi minimal tutulur (gereksiz alan yok)

    Args:
        users_db (dict[str, dict[str, str]]):
            Kullanıcı veritabanını temsil eden sözlük.
            Anahtar (key) olarak e-mail adresi kullanılır.

        mail (str):
            Kullanıcının e-mail adresi.
            Bu değer kullanıcı için benzersiz kimliktir.

        password (str):
            Kullanıcının düz metin (plain text) parolası.
            Bu parola fonksiyon içinde hash'lenerek saklanır.

    Returns:
        None
            Kullanıcı başarıyla oluşturulur.
            Hata durumlarında kullanıcı oluşturulmaz.
    """

    # E-mail adresini normalize et
    # strip(): baştaki/sondaki boşlukları temizler
    # lower(): case-insensitive hale getirir
    mail = normalize_mail(mail)

    # Temel doğrulama: e-mail boş olamaz
    if not mail:
        print("❌ E-mail boş olamaz.")
        return

    if not email_is_valid(mail):
        print("❌ Geçersiz e-mail formatı.")
        return None

    # Temel doğrulama: parola boş olamaz
    if not password:
        print("❌ Parola boş olamaz.")
        return
    
    ok, errors = pwd_is_valid(password)
    if not ok:
        print("❌ Şifre geçersiz:")
        for e in errors:
            print(f"   - {e}")
        return None
    
    # Aynı e-mail ile kullanıcı var mı?
    # dict lookup -> O(1)
    if mail in user_info:
        print("❌ Bu e-mail ile kayıtlı kullanıcı zaten var.")
        return None

    user_id = str(uuid.uuid4())

    users[user_id] = {
        "id": user_id,
        "mail": mail,
        "password": hash_password(password),
    }

    user_info[mail] = user_id
    print("✅ Kullanıcı başarıyla oluşturuldu.")
    return user_id


# Register
def sign_up(users: dict[str, dict[str, str]], user_info: dict[str, str]) -> None:

    """
    Yeni kullanıcı kayıt (Sign Up) işlemini gerçekleştirir.

    Akış:
        - Kullanıcıdan e-mail ve password alınır
        - E-mail formatı doğrulanır
        - Şifre kurallara uygun mu kontrol edilir
        - E-mail daha önce kayıtlı mı kontrol edilir (O(1))
        - Tüm kontroller geçerse kullanıcı oluşturulur
    """
    print("\n--- SIGN UP ---")

    try:

        # Kullanıcıdan e-mail alınır
        mail = normalize_mail(input("E-mail: "))

        # Boş e-mail kontrolü
        if not mail:
            print("❌ E-mail boş olamaz.")
            return

        # E-mail format kontrolü
        if not email_is_valid(mail):
            print("❌ Geçersiz e-mail formatı.")
            return
        
        # E-mail daha önce kayıtlı mı?
        # dict lookup -> O(1)
        if mail in users:
            print("❌ Bu e-mail zaten kayıtlı.")
            return

        # Password yıldızlı şekilde alınır
        password = get_password("Password: ")

        # (Opsiyonel ama UX için önerilir)
        confirm = get_password("Confirm Password: ")

        # Şifreler uyuşuyor mu?
        if password != confirm:
            print("❌ Şifreler uyuşmuyor.")
            return

        # Şifre kurallara uygun mu?
        is_valid, errors = pwd_is_valid(password)
        if not is_valid:
            print("❌ Şifre geçersiz:")
            for err in errors:
                print(f"   - {err}")
            return

        hashed_password = hash_password(password)

        create_user(users, user_info, mail, hashed_password)

    except KeyboardInterrupt:
        # Ctrl+C ile kullanıcı iptal etti
        print("\n⚠️ İşlem iptal edildi (Ctrl+C).")
        return


# Login
def sign_in(users: dict[str, dict[str, str]], user_info: dict[str, str],
            attempts_by_id: dict[str, dict[str, Any]]) -> None:
    """
    Sisteme kayıtlı bir kullanıcının güvenli şekilde giriş (Sign In) yapmasını sağlar.

    Bu fonksiyon, kullanıcıdan alınan e-mail ve parola bilgileriyle
    kimlik doğrulama işlemini gerçekleştirir. Parola doğrulaması,
    düz metin karşılaştırması yerine hash doğrulaması ile yapılır.
    Güvenliği artırmak için hatalı giriş denemeleri sınırlandırılır
    ve belirlenen sayıda başarısız denemeden sonra hesap kilitlenir.

    İşleyiş:
        - Kullanıcıdan e-mail alınır ve format/boşluk kontrolü yapılır
        - Kullanıcının sistemde kayıtlı olup olmadığı kontrol edilir
        - Kullanıcının kalan giriş deneme hakkı kontrol edilir
        - Hesap kilitli değilse parola güvenli şekilde alınır
        - Girilen parola, kayıtlı hash ile doğrulanır
        - Doğruysa giriş başarılı olur ve deneme hakları sıfırlanır
        - Yanlışsa deneme hakkı düşürülür, hak biterse hesap kilitlenir

    Güvenlik Özellikleri:
        - Hash'lenmiş parola doğrulaması kullanır
        - Maksimum hatalı giriş denemesi (lockout) uygular
        - E-mail kontrolü case-insensitive yapılır
        - Ctrl + C ile güvenli şekilde iptal edilebilir

    Args:
        users_db (dict[str, dict[str, str]]):
            Kullanıcı bilgilerini tutan sözlük.
            Anahtar olarak e-mail adresi, değer olarak
            kullanıcının hash'lenmiş parola bilgisi bulunur.

        attempts_left (dict[str, int]):
            Her kullanıcı için kalan hatalı giriş deneme sayısını tutar.
            Kullanıcı ilk kez giriş yapıyorsa varsayılan deneme hakkı uygulanır.

    Returns:
        None
            Giriş işleminin sonucu terminal çıktıları ile kullanıcıya bildirilir.
    """

    print("\n--- SIGN IN ---")

    try:

        # Kullanıcıdan e-mail alınır
        # strip(): baştaki/sondaki boşlukları siler
        # lower(): e-mail'i case-insensitive yapar
        mail = normalize_mail(input("E-mail: "))

        # E-mail boşsa işlem iptal edilir
        if not mail:
            print("❌ E-mail boş olamaz.")
            return
        
        # Kullanıcı veritabanında var mı?
        user_id, user = find_user_by_mail(users, user_info, mail)
        if user_id is None or user is None:
            print("❌ Kullanıcı bulunamadı.")
            return
        
        # Kullanıcının kalan deneme hakkı
        # Daha önce giriş denemesi yoksa MAX_ATTEMPTS ile başlar
        state = get_state(attempts_by_id, user_id)

        # Lockout kontrolü
        # 🔒 Kilit kontrolü
        remaining = check_lock(state)
        if remaining > 0:
            print(f"⛔ Hesap kilitli. {remaining} saniye sonra tekrar deneyin.")
            return
        
        # Kilit süresi dolmuş olabilir -> temiz bir state ile devam et
        # (locked_until geçmişse check_lock zaten 0 döndürür)
        if state.get("locked_until") is not None:
            reset_state(attempts_by_id, user_id)
            state = get_state(attempts_by_id, user_id)

        # Kullanıcıdan şifre alınır
        # get_password -> yıldızlı ve güvenli input
        password = get_password("Password: ")

        # Girilen şifre, hash'lenmiş parola ile karşılaştırılır
        # verify_password -> PBKDF2 / SHA256 doğrulama yapar
        if verify_password(password, user["password"]):
            # Başarılı girişte: Kullanıcının deneme hakları sıfırlanır (kayıt silinir)
            reset_state(attempts_by_id, user_id)
            print("✅ Giriş başarılı!")
            return

        # ❌ Hatalı şifre -> hak düşür / kilitle
        state = fail_attempt(attempts_by_id, user_id, state)

        # Deneme hakkı bittiyse hesap kilitlenir
        remaining = check_lock(state)
        if remaining > 0:
            print("⛔ Çok fazla hatalı deneme. Hesap 5 dakika kilitlendi.")
        else:
            print(f"❌ Hatalı şifre. Kalan deneme hakkın: {state['left']}")

    except KeyboardInterrupt:
        print("\n⚠️ İşlem iptal edildi (Ctrl+C).")


# ------------------------------------------------------------
# SEED (DEV)
# ------------------------------------------------------------

def seed_sample_user(users: dict[str, dict[str, str]], user_info: dict[str, str]) -> None:

    """
    Uygulama başlangıcında geliştirme ve test (debug) amaçlı
    örnek bir kullanıcıyı otomatik olarak sisteme ekler.

    Bu fonksiyonun temel amacı, uygulama her çalıştırıldığında
    geliştiricinin manuel olarak kayıt (sign up) yapmasına gerek
    kalmadan, doğrudan giriş (sign in) akışını test edebilmesini
    sağlamaktır.

    Fonksiyon deterministik çalışır:
        - Eğer örnek kullanıcı sistemde zaten varsa hiçbir işlem yapmaz
        - Eğer kullanıcı yoksa, güvenli şekilde yeni kullanıcı oluşturur

    Bu yaklaşım sayesinde:
        - Aynı kullanıcı tekrar tekrar eklenmez
        - E-mail çakışması yaşanmaz
        - Test senaryoları her çalıştırmada tutarlı olur

    Oluşturulan örnek kullanıcı bilgileri:
        - E-mail   : beast@gmail.com
        - Password : 123Aa!

    Güvenlik Notu:
        - Bu fonksiyon yalnızca geliştirme / debug ortamlarında kullanılmalıdır
        - Gerçek (production) ortamlarda sabit parola ile kullanıcı oluşturmak
          ciddi bir güvenlik riski oluşturur
        - Parola, create_user fonksiyonu içinde hash'lenerek saklanır;
          düz metin (plain text) olarak tutulmaz

    Args:
        users_db (dict[str, dict[str, str]]):
            Kullanıcı veritabanını temsil eden sözlük.
            Anahtar (key) olarak e-mail adresi kullanılır,
            değer olarak kullanıcıya ait bilgiler saklanır.

    Returns:
        None
            Fonksiyon yalnızca gerekirse kullanıcı oluşturur;
            herhangi bir değer döndürmez.
    """

    # Örnek kullanıcıyı e-mail adresine göre veritabanında ara
    # dict.get kullanımı sayesinde arama işlemi O(1) karmaşıklığındadır
    if "beast@gmail.com" not in user_info:
        create_user(users, user_info, "beast@gmail.com", "123Aa!")


def get_user(users_db: dict[str, dict[str, str]], mail: str) -> dict | None:
    """
    Verilen e-mail adresine karşılık gelen kullanıcıyı kullanıcı veritabanından getirir.

    Bu fonksiyon, kullanıcı doğrulama sürecinde e-mail adresine göre
    kullanıcı arama işlemini merkezi ve performanslı şekilde yapmak için kullanılır.
    `dict.get` kullanımı sayesinde arama işlemi O(1) karmaşıklığındadır.

    Kullanıcı bulunamazsa None döndürerek,
    çağıran fonksiyonun (örneğin sign_in) nasıl bir aksiyon alacağına
    karar vermesine imkân tanır.

    Bu yaklaşımın avantajları:
        - sign_in fonksiyonu sadeleşir
        - Kullanıcı arama mantığı tek yerde toplanır
        - Test edilebilirlik artar
        - UI (print) ile iş mantığı ayrılmış olur

    Args:
        users_db (dict[str, dict[str, str]]):
            Kullanıcı veritabanı.
            Anahtar (key) olarak e-mail adresi,
            değer olarak kullanıcı bilgilerini içeren sözlük bulunur.

        mail (str):
            Aranacak kullanıcının e-mail adresi.
            E-mail adresinin normalize edilmiş (strip + lower) olması beklenir.

    Returns:
        dict | None:
            - dict → kullanıcı bulunduysa kullanıcı bilgileri
            - None → kullanıcı veritabanında yoksa
    """

    # dict.get kullanımı sayesinde O(1) zamanda kullanıcıyı getirir
    return users_db.get(mail)


# ------------------------------------------------------------
# MAIN (Orchestration)
# ------------------------------------------------------------

def main() -> None:
    """
    Uygulamanın ana giriş noktasıdır (entry point).

    Bu fonksiyon, terminal üzerinden çalışan uygulamanın tüm akışını yönetir:
        - Başlangıç verisini hazırlar (seed / örnek kullanıcı)
        - Kullanıcıdan menü seçimi alır
        - Seçime göre ilgili işlemleri (sign_up / sign_in) çağırır
        - Debug amaçlı kullanıcı listesini ekrana basabilir
        - Kullanıcı çıkış isteyene kadar döngüde kalır

    Akış:
        1) Örnek kullanıcı eklenir (seed_sample_user)
        2) attempts_left yapısı oluşturulur (giriş deneme hakları için)
        3) Sonsuz döngü içinde menü basılır
        4) Kullanıcıdan seçim alınır
        5) Seçime göre ilgili fonksiyon çağrılır
        6) "0" seçilirse döngü kırılır ve program biter

    Notlar:
        - Bu fonksiyon bilinçli olarak "orchestrator" görevi görür:
          İş mantığı burada yazılmaz; sadece diğer fonksiyonlar çağrılır.
        - Böyle tasarlamak, kodun okunabilirliğini ve bakımını kolaylaştırır.

    Returns:
        None
            Program akışı terminal çıktıları ile kullanıcıya bildirilir.
    """

    # Ana kullanıcı tablosu: user_id -> user
    users: dict[str, dict[str, str]] = {}

    # Index: mail -> user_id (O(1) mail lookup)
    user_info: dict[str, str] = {}

    # Başlangıçta örnek bir kullanıcı eklemek istersen:
    # Bu, uygulamayı test ederken "hemen sign in deneyeyim" kolaylığı sağlar.
    seed_sample_user(users, user_info)

    # Kullanıcının giriş denemelerini takip etmek için kullanılan yapı.
    # Mevcut senaryoda: dict[str, int]  -> mail -> kalan hak
    # Eğer time-based lockout'a geçtiysen bu dict[str, dict] olmalı.
    attempts_by_id: dict[str, dict[str, Any]] = {}

    # Menü sürekli gösterilsin, kullanıcı çıkış seçeneğini seçene kadar devam etsin
    while True:
        # Menü başlığı
        print("\n===== MENU =====")

        # Kullanıcının seçebileceği seçenekler
        print("1) Sign Up")       # yeni kullanıcı kaydı
        print("2) Sign In")       # mevcut kullanıcı girişi
        print("3) Users (debug)") # mevcut kullanıcıları listele (debug amaçlı)
        print("0) Exit")          # programdan çıkış

        # Kullanıcıdan seçim al
        # strip() -> baştaki/sondaki boşlukları temizler (daha sağlam input)
        choice = input("Seçim: ").strip()

        # 1) Sign Up: yeni kullanıcı kaydı
        if choice == "1":
            sign_up(users, user_info)

        # 2) Sign In: kullanıcı girişi
        # attempts_left burada sign_in fonksiyonuna aktarılır
        elif choice == "2":
            sign_in(users, user_info, attempts_by_id)

        # 3) Debug: kayıtlı kullanıcıları ekrana bas
        elif choice == "3":
            print("\n--- USERS (DEBUG) ---")
            if not users:
                print("(empty)")
                continue

            # users sözlüğü içinde dolaş
            # uid burada sözlüğün key'i (ör: mail veya id olabilir)
            # u ise kullanıcı bilgileri sözlüğü
            for uid, user in users.items():
                # Kullanıcı bilgilerini okunabilir şekilde yazdır
                # user['password'] ve user['mail'] alanlarının var olduğu varsayılır
                print(f"{uid} -> {user['mail']} | hash: {user['password'][:25]}...")

        # 0) Exit: programı sonlandır
        elif choice == "0":
            print("👋 Çıkış yapıldı.")
            break

        # Tanımsız bir seçim yapılırsa kullanıcıyı uyar
        else:
            print("❌ Geçersiz seçim.")


# Bu blok, dosya doğrudan çalıştırıldığında main() fonksiyonunu çağırır.
# Eğer bu dosya başka bir dosyadan import edilirse, main() otomatik çalışmaz.
if __name__ == "__main__":
    main()

# endregion