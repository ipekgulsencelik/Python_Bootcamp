# ============================================================
#  KARGO FİYATLANDIRMA SİSTEMİ
#
# 1) Login mekanizması:
#    - Sisteme giriş için kullanıcı adı ve şifre sorulsun.
#    - Giriş bilgileri hatalı ise ekrana uyarı verilip program sonlandırılsın.
#    - Giriş bilgileri doğru ise kargo hesaplama adımına geçilsin.
#
# 2) Kargo bilgileri:
#    - Kullanıcıdan kargonun ağırlığı (kg cinsinden) istenecektir.
#    - Kullanıcıdan kargonun gideceği mesafe (km cinsinden) istenecektir.
#    - Kullanıcıdan kargo türü istenecektir:
#         * "dosya"
#         * "elektronik"
#         * "mobilya"
#
# 3) Kargo türüne göre katsayı:
#    - Eğer kargo türü "dosya" ise katsayı = 1.5
#    - Eğer kargo türü "elektronik" ise katsayı = 3
#    - Eğer kargo türü "mobilya" ise katsayı = 5
#    - Bunların dışında bir giriş yapılırsa "Tanımsız tür" uyarısı verilip
#      kullanıcıdan tekrar kargo türü istenmelidir.
#
# Özet:
#    - Doğru login olmadan kargo hesabı yapılmamalıdır.
#    - Kargo türüne göre katsayı doğru seçilmeli,
#      yanlış girişte kullanıcı uyarılmalı ve tekrar tür girmesi istenmelidir.
#    - Mesafe türü hesaplanmalıdır.
#    - Formüle göre fiyat hesaplanıp, düzenli bir fiş çıktısı verilmelidir.
# ============================================================

import random
import time
from datetime import datetime

print("=== AKILLI LOJİSTİK KARGO SİSTEMİ ===")

# ----------------- TEMA / DİL / DEMO / UYARI SEVİYESİ -----------------
tema = input("Tema seçin (Açık/Koyu): ").strip().lower()
if tema != "koyu":
    tema = "acik"

dil = input("Dil seçin (TR/EN): ").strip().upper()
if dil != "EN":
    dil = "TR"

demo_mod = input("Demo modu? (E/H): ").strip().upper()
demo_mod_aktif = False
if demo_mod == "E":
    demo_mod_aktif = True

uyari_seviyesi = input("İpuçları sık gelsin mi? (E/H): ").strip().upper()
if uyari_seviyesi != "E":
    uyari_seviyesi = "H"

# ----------------- SABİT KULLANICILAR -----------------
NORMAL_KULLANICI = "admin"
NORMAL_SIFRE = "1234"

ADMIN_KULLANICI = "admin"
ADMIN_SIFRE = "admin"

VIP_KULLANICI = "vip"
VIP_SIFRE = "vip123"

# ----------------- SİSTEM SAYACLARI -----------------
toplam_kargo_sayisi = 0
toplam_ciro_tl = 0.0
dosya_adet = 0
elektronik_adet = 0
mobilya_adet = 0

sadakat_puani = 0
sadakat_seviye = "Bronze"

toplam_memnuniyet_puani = 0
memnuniyet_sayisi = 0

hatali_tur_sayisi = 0
hatali_arac_sayisi = 0
hatali_teslim_sayisi = 0

bonus_indirim_oran = 0.0  # Şans kutusundan gelen bir sonraki kargo indirimi

# 🌱 Karbon ayak izi toplamı (kg CO2)
toplam_karbon_ayak_izi = 0.0

# Tek string log sistemi
log_text = ""

# ----------------- GÜNÜN KAMPANYASI -----------------
kampanya_turu = random.randint(1, 4)
kampanya_aciklama = ""
kampanya_indirim_oran = 0.0
kampanya_sigorta_ucretsiz = False
kampanya_ek_hizmet_ucretsiz = False

if kampanya_turu == 1:
    kampanya_aciklama = "%5 genel indirim"
    kampanya_indirim_oran = 0.05
elif kampanya_turu == 2:
    kampanya_aciklama = "%10 genel indirim"
    kampanya_indirim_oran = 0.10
elif kampanya_turu == 3:
    kampanya_aciklama = "Sigorta ücretsiz"
    kampanya_sigorta_ucretsiz = True
elif kampanya_turu == 4:
    kampanya_aciklama = "Ek hizmetler ücretsiz"
    kampanya_ek_hizmet_ucretsiz = True

# ----------------- KUR SERVİSİ (FAKE) -----------------
if dil == "TR":
    print("Kur bilgileri alınıyor...")
else:
    print("Fetching exchange rates...")

kur_hata = random.randint(1, 10)
if kur_hata == 1:
    if dil == "TR":
        print("Bağlantı hatası! Yedek kurlar kullanılacak.")
    else:
        print("Connection error! Fallback rates will be used.")
    kur_usd = 30.0
    kur_eur = 33.0
else:
    kur_usd = 33.0
    kur_eur = 36.0

print("USD:", kur_usd, "EUR:", kur_eur)

# ----------------- LOGIN -----------------
aktif_kullanici = None
aktif_admin_mi = False
aktif_vip_mi = False

login_hak = 3

while login_hak > 0:
    if dil == "TR":
        print("\n--- GİRİŞ ---")
        kul = input("Kullanıcı adı: ")
        sifre = input("Şifre: ")
    else:
        print("\n--- LOGIN ---")
        kul = input("Username: ")
        sifre = input("Password: ")

    # Captcha zorluğu
    if login_hak == 3:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        try:
            c_cevap = int(input(f"Güvenlik sorusu: {a} + {b} = "))
        except ValueError:
            c_cevap = -1
        if c_cevap != a + b:
            if dil == "TR":
                print("Güvenlik sorusu hatalı!")
            else:
                print("Security question failed!")
            login_hak = login_hak - 1
            continue
    elif login_hak == 2:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)
        try:
            c_cevap = int(input(f"Güvenlik sorusu: {a} + {b} + {c} = "))
        except ValueError:
            c_cevap = -1
        if c_cevap != a + b + c:
            if dil == "TR":
                print("Güvenlik sorusu hatalı! (Seviye arttı 😈)")
            else:
                print("Security question failed! (Harder mode 😈)")
            login_hak = login_hak - 1
            continue
    else:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        try:
            c_cevap = int(input(f"Güvenlik sorusu: {a} - {b} = "))
        except ValueError:
            c_cevap = -999
        if c_cevap != a - b:
            if dil == "TR":
                print("Güvenlik sorusu hatalı! Son hakkı da yaktın gibi...")
            else:
                print("Security question failed! Last chance maybe gone...")
            login_hak = login_hak - 1
            continue

    if kul == ADMIN_KULLANICI and sifre == ADMIN_SIFRE:
        aktif_kullanici = kul
        aktif_admin_mi = True
        aktif_vip_mi = False
        if dil == "TR":
            print("Admin olarak giriş yaptınız.")
        else:
            print("Logged in as admin.")
        break
    elif kul == NORMAL_KULLANICI and sifre == NORMAL_SIFRE:
        aktif_kullanici = kul
        aktif_admin_mi = False
        aktif_vip_mi = False
        if dil == "TR":
            print("Giriş başarılı, hoş geldin", aktif_kullanici)
        else:
            print("Login successful, welcome", aktif_kullanici)
        break
    elif kul == VIP_KULLANICI and sifre == VIP_SIFRE:
        aktif_kullanici = kul
        aktif_admin_mi = False
        aktif_vip_mi = True
        if dil == "TR":
            print("VIP kullanıcı olarak giriş yaptınız! 👑")
        else:
            print("Logged in as VIP user! 👑")
        break
    else:
        if dil == "TR":
            print("Kullanıcı adı veya şifre hatalı!")
        else:
            print("Invalid username or password!")
        login_hak = login_hak - 1
        if login_hak > 0:
            if dil == "TR":
                print("Kalan giriş hakkı:", login_hak)
            else:
                print("Remaining attempts:", login_hak)

if aktif_kullanici is None:
    if dil == "TR":
        print("Çok fazla hatalı giriş, sistem kilitlendi.")
    else:
        print("Too many failed attempts, system locked.")
    exit()

if dil == "TR":
    print("\nGünün kampanyası:", kampanya_aciklama)
else:
    print("\nToday's campaign:", kampanya_aciklama)

# ----------------- ANA MENÜ -----------------
program_calisiyor = True

while program_calisiyor:
    print("\n===============================")
    if tema == "koyu":
        print("######## ANA MENÜ ########")
    else:
        print("----- ANA MENÜ -----")

    if dil == "TR":
        print("1 - Yeni kargo fiyatı hesapla")
        print("2 - Kargo takibi (simülasyon)")
        if aktif_admin_mi:
            print("3 - İstatistikleri göster (Admin)")
            print("4 - Kullanıcı değiştir")
            print("5 - Çıkış")
        else:
            print("3 - Kullanıcı değiştir")
            print("4 - Çıkış")
        print("6 - İade / iptal simülasyonu")
        print("9 - Yardım / Nasıl kullanılır?")
    else:
        print("1 - Calculate new cargo price")
        print("2 - Cargo tracking (simulation)")
        if aktif_admin_mi:
            print("3 - Show statistics (Admin)")
            print("4 - Change user")
            print("5 - Exit")
        else:
            print("3 - Change user")
            print("4 - Exit")
        print("6 - Refund / cancellation simulation")
        print("9 - Help / How to use?")

    secim = input("Seçiminiz / Your choice: ")

    # ==================== 1 - KARGO HESAPLAMA ====================
    if secim == "1":
        try:
            # ---------- Firma seçimi ----------
            if dil == "TR":
                print("\nKargo Firması Seçimi:")
                print("1 - HızlıKargo  (1.0x)")
                print("2 - UcuzKargo  (0.9x)")
                print("3 - GüvenKargo (1.1x)")
            else:
                print("\nCargo Company Selection:")
                print("1 - FastCargo   (1.0x)")
                print("2 - CheapCargo  (0.9x)")
                print("3 - SafeCargo   (1.1x)")

            firma_adi = "HızlıKargo"
            firma_carpan = 1.0

            while True:
                firma_secim = input("Firma / Company: ")
                if firma_secim == "1":
                    firma_adi = "HızlıKargo"
                    if dil == "EN":
                        firma_adi = "FastCargo"
                    firma_carpan = 1.0
                    break
                elif firma_secim == "2":
                    firma_adi = "UcuzKargo"
                    if dil == "EN":
                        firma_adi = "CheapCargo"
                    firma_carpan = 0.9
                    break
                elif firma_secim == "3":
                    firma_adi = "GüvenKargo"
                    if dil == "EN":
                        firma_adi = "SafeCargo"
                    firma_carpan = 1.1
                    break
                else:
                    if dil == "TR":
                        print("Geçersiz firma!")
                    else:
                        print("Invalid company!")

            # ---------- Mesafe belirleme ----------
            if dil == "TR":
                print("\nMesafe Belirleme:")
                print("1 - Mesafeyi manuel km olarak gireceğim")
                print("2 - Şehirden şehir hesabı (Ankara/İstanbul/İzmir)")
            else:
                print("\nDistance Mode:")
                print("1 - Enter distance in km manually")
                print("2 - City to city rough distance (Ankara/Istanbul/Izmir)")

            while True:
                mesafe_mod = input("Seçim / Choice: ")
                if mesafe_mod == "1":
                    while True:
                        try:
                            if dil == "TR":
                                mesafe = float(input("Mesafe (km): "))
                            else:
                                mesafe = float(input("Distance (km): "))
                            if mesafe <= 0:
                                if dil == "TR":
                                    print("Mesafe 0 veya negatif olamaz.")
                                else:
                                    print("Distance cannot be 0 or negative.")
                                continue
                            break
                        except ValueError:
                            if dil == "TR":
                                print("Sayısal bir değer giriniz.")
                            else:
                                print("Enter a numeric value.")
                    break
                elif mesafe_mod == "2":
                    gonderen = input("Gönderici şehir / From city: ").lower()
                    alici = input("Alıcı şehir / To city: ").lower()
                    if (gonderen == "ankara" and alici == "istanbul") or (gonderen == "istanbul" and alici == "ankara"):
                        mesafe = 450
                    elif (gonderen == "ankara" and alici == "izmir") or (gonderen == "izmir" and alici == "ankara"):
                        mesafe = 580
                    elif (gonderen == "istanbul" and alici == "izmir") or (gonderen == "izmir" and alici == "istanbul"):
                        mesafe = 480
                    else:
                        if dil == "TR":
                            print("Bu şehir kombinasyonu için hazır mesafe yok, manuel girmeniz gerekiyor.")
                        else:
                            print("No predefined distance for this combination, use manual mode.")
                        continue
                    if dil == "TR":
                        print("Tahmini mesafe:", mesafe, "km")
                    else:
                        print("Estimated distance:", mesafe, "km")
                    break
                else:
                    if dil == "TR":
                        print("Geçersiz seçim!")
                    else:
                        print("Invalid choice!")

            mesafe_turu = "Kısa Mesafe"
            if mesafe > 600:
                mesafe_turu = "Uzun Mesafe"

            # ---------- Bölge seçimi ----------
            if dil == "TR":
                print("\nBölge Seçimi:")
                print("1 - Bölge 1 (Yakın il) -> 1.0")
                print("2 - Bölge 2 (Komşu il) -> 1.2")
                print("3 - Bölge 3 (Uzak il)  -> 1.5")
                print("4 - Bölge 4 (Doğu/G.Doğu) -> 1.8")
                print("5 - Yurt Dışı -> 5.0 + gümrük")
            else:
                print("\nRegion Selection:")
                print("1 - Region 1 (Close) -> 1.0")
                print("2 - Region 2 (Neighbor) -> 1.2")
                print("3 - Region 3 (Far) -> 1.5")
                print("4 - Region 4 (East) -> 1.8")
                print("5 - International -> 5.0 + customs")

            yurt_disi = False
            while True:
                bolge_secim = input("Bölge / Region: ")
                if bolge_secim == "1":
                    bolge_carpan = 1.0
                    break
                elif bolge_secim == "2":
                    bolge_carpan = 1.2
                    break
                elif bolge_secim == "3":
                    bolge_carpan = 1.5
                    break
                elif bolge_secim == "4":
                    bolge_carpan = 1.8
                    break
                elif bolge_secim == "5":
                    bolge_carpan = 5.0
                    yurt_disi = True
                    break
                else:
                    if dil == "TR":
                        print("Geçersiz seçim!")
                    else:
                        print("Invalid choice!")

            # ---------- Mesai dışı çarpanı ----------
            if dil == "TR":
                mesai_cevap = input("\nMesai dışı gönderi mi? (E/H): ").upper()
            else:
                mesai_cevap = input("\nOut of working hours? (Y/N): ").upper()
            mesai_carpan = 1.0
            if mesai_cevap == "E" or mesai_cevap == "Y":
                mesai_carpan = 1.3

            # ---------- Ağırlık ve hacim ----------
            while True:
                try:
                    if dil == "TR":
                        agirlik = float(input("\nGerçek ağırlık (kg): "))
                    else:
                        agirlik = float(input("\nReal weight (kg): "))
                    if agirlik <= 0:
                        if dil == "TR":
                            print("Ağırlık 0 veya negatif olamaz.")
                        else:
                            print("Weight cannot be 0 or negative.")
                        continue
                    break
                except ValueError:
                    if dil == "TR":
                        print("Sayısal bir değer giriniz.")
                    else:
                        print("Enter a numeric value.")

            if dil == "TR":
                print("\nKutu ölçüleri (hacimsel ağırlık için):")
            else:
                print("\nBox dimensions (for volumetric weight):")

            try:
                en = float(input("En (cm): "))
                boy = float(input("Boy (cm): "))
                yukseklik = float(input("Yükseklik (cm): "))
            except ValueError:
                en = 0
                boy = 0
                yukseklik = 0

            hacim_agirlik = 0
            if en > 0 and boy > 0 and yukseklik > 0:
                hacim_agirlik = (en * boy * yukseklik) / 5000

            if agirlik >= hacim_agirlik:
                efektif_agirlik = agirlik
            else:
                efektif_agirlik = hacim_agirlik

            # Paket sınıfı
            if efektif_agirlik <= 5:
                paket_sinifi = "S"
                paket_carpan = 1.0
            elif efektif_agirlik <= 20:
                paket_sinifi = "M"
                paket_carpan = 1.1
            elif efektif_agirlik <= 50:
                paket_sinifi = "L"
                paket_carpan = 1.2
            else:
                paket_sinifi = "XL"
                paket_carpan = 1.3

            # ---------- Araç türü ----------
            if dil == "TR":
                print("\nAraç Türü:")
                print("1 - Motor (0.8)")
                print("2 - Hafif ticari (1.0)")
                print("3 - Kamyonet (1.3)")
                print("4 - Kamyon (1.8)")
            else:
                print("\nVehicle Type:")
                print("1 - Motorbike (0.8)")
                print("2 - Van (1.0)")
                print("3 - Pickup (1.3)")
                print("4 - Truck (1.8)")

            while True:
                arac_secim = input("Araç / Vehicle: ")
                if arac_secim == "1":
                    arac_carpan = 0.8
                    break
                elif arac_secim == "2":
                    arac_carpan = 1.0
                    break
                elif arac_secim == "3":
                    arac_carpan = 1.3
                    break
                elif arac_secim == "4":
                    arac_carpan = 1.8
                    break
                else:
                    hatali_arac_sayisi = hatali_arac_sayisi + 1
                    if hatali_arac_sayisi >= 3 and uyari_seviyesi == "E":
                        if dil == "TR":
                            print("İpucu: 1-4 arası bir sayı girmelisin.")
                        else:
                            print("Hint: Enter a number between 1 and 4.")
                    if dil == "TR":
                        print("Geçersiz seçim!")
                    else:
                        print("Invalid choice!")

            # ---------- Teslim süresi ----------
            if dil == "TR":
                print("\nTeslim Süresi:")
                print("1 - Normal (1.0)")
                print("2 - Aynı gün (1.4)")
                print("3 - Gece / 24 saat (1.7)")
                print("4 - Ekspres 4 saat (2.0)")
            else:
                print("\nDelivery Time:")
                print("1 - Normal (1.0)")
                print("2 - Same day (1.4)")
                print("3 - Night / 24h (1.7)")
                print("4 - Express 4h (2.0)")

            teslim_carpan = 1.0
            teslim_kodu = "1"

            while True:
                teslim_secim = input("Teslim / Delivery: ")
                if teslim_secim == "1":
                    teslim_carpan = 1.0
                    teslim_kodu = "1"
                    break
                elif teslim_secim == "2":
                    teslim_carpan = 1.4
                    teslim_kodu = "2"
                    break
                elif teslim_secim == "3":
                    teslim_carpan = 1.7
                    teslim_kodu = "3"
                    break
                elif teslim_secim == "4":
                    teslim_carpan = 2.0
                    teslim_kodu = "4"
                    break
                else:
                    hatali_teslim_sayisi = hatali_teslim_sayisi + 1
                    if hatali_teslim_sayisi >= 3 and uyari_seviyesi == "E":
                        if dil == "TR":
                            print("İpucu: 1-4 arası bir değer gir.")
                        else:
                            print("Hint: Enter a value between 1 and 4.")
                    if dil == "TR":
                        print("Geçersiz seçim!")
                    else:
                        print("Invalid choice!")

            # ---------- Kargo türü ----------
            while True:
                if dil == "TR":
                    tip = input("\nKargo türü (dosya/elektronik/mobilya): ").lower()
                else:
                    tip = input("\nCargo type (file/electronic/furniture): ").lower()

                if tip == "dosya" or tip == "file":
                    katsayi = 1.5
                    sigorta_oran = 0.02
                    dosya_adet = dosya_adet + 1
                    break
                elif tip == "elektronik" or tip == "electronic":
                    katsayi = 3.0
                    sigorta_oran = 0.05
                    elektronik_adet = elektronik_adet + 1
                    break
                elif tip == "mobilya" or tip == "furniture":
                    katsayi = 5.0
                    sigorta_oran = 0.03
                    mobilya_adet = mobilya_adet + 1
                    break
                else:
                    hatali_tur_sayisi = hatali_tur_sayisi + 1
                    if hatali_tur_sayisi >= 3 and uyari_seviyesi == "E":
                        if dil == "TR":
                            print("İpucu: Geçerli değerler: dosya / elektronik / mobilya")
                        else:
                            print("Hint: Valid values: file / electronic / furniture")
                    if dil == "TR":
                        print("Geçersiz tür!")
                    else:
                        print("Invalid type!")

            # ---------- Temel fiyat ----------
            temel_fiyat = (efektif_agirlik * mesafe * katsayi) / 100
            temel_fiyat = temel_fiyat * bolge_carpan
            temel_fiyat = temel_fiyat * arac_carpan
            temel_fiyat = temel_fiyat * teslim_carpan
            temel_fiyat = temel_fiyat * firma_carpan
            temel_fiyat = temel_fiyat * paket_carpan
            temel_fiyat = temel_fiyat * mesai_carpan

            yapay_zeka_katsayi = random.randint(95, 105) / 100
            ai_tahmini = temel_fiyat * yapay_zeka_katsayi

            # ---------- Yurt dışı ----------
            gumruk_vergisi = 0.0
            uluslararasi_tasimacilik_turu = ""
            if yurt_disi:
                if dil == "TR":
                    print("\nYurt dışı taşıma türü:")
                    print("1 - Hava (2.5x)")
                    print("2 - Deniz (0.7x)")
                    print("3 - Kara (1.2x)")
                else:
                    print("\nInternational mode:")
                    print("1 - Air (2.5x)")
                    print("2 - Sea (0.7x)")
                    print("3 - Land (1.2x)")

                while True:
                    ysec = input("Seçim / Choice: ")
                    if ysec == "1":
                        uluslararasi_tasimacilik_turu = "Hava"
                        temel_fiyat = temel_fiyat * 2.5
                        break
                    elif ysec == "2":
                        uluslararasi_tasimacilik_turu = "Deniz"
                        temel_fiyat = temel_fiyat * 0.7
                        break
                    elif ysec == "3":
                        uluslararasi_tasimacilik_turu = "Kara"
                        temel_fiyat = temel_fiyat * 1.2
                        break
                    else:
                        if dil == "TR":
                            print("Geçersiz seçim!")
                        else:
                            print("Invalid choice!")
                gumruk_oran = random.randint(12, 30) / 100
                gumruk_vergisi = temel_fiyat * gumruk_oran

            # ---------- ÖN ONAY EKRANI ----------
            if dil == "TR":
                print("\n--- ÖN FİYATLANDIRMA ÖZETİ ---")
                print("Firma:", firma_adi)
                print("Kargo türü:", tip)
                print("Mesafe:", mesafe, "km (", mesafe_turu, ")")
                print("Efektif ağırlık:", round(efektif_agirlik, 2), "kg")
                print("Paket sınıfı:", paket_sinifi)
                print("Mesai çarpanı:", mesai_carpan)
                print("Şu anki temel fiyat (gümrük hariç):", round(temel_fiyat, 2), "TL")
                onay = input("Bu bilgilerle devam edilsin mi? (E/H): ").upper()
            else:
                print("\n--- PRE-PRICE SUMMARY ---")
                print("Company:", firma_adi)
                print("Cargo type:", tip)
                print("Distance:", mesafe, "km (", mesafe_turu, ")")
                print("Effective weight:", round(efektif_agirlik, 2), "kg")
                print("Package class:", paket_sinifi)
                print("Overtime factor:", mesai_carpan)
                print("Current base price (excl. customs):", round(temel_fiyat, 2), "TL")
                onay = input("Continue with these values? (Y/N): ").upper()

            if not (onay == "E" or onay == "Y"):
                if dil == "TR":
                    print("İşlem iptal edildi, ana menüye dönülüyor.")
                else:
                    print("Operation cancelled, returning to main menu.")
                continue

            # ---------- Sigorta ----------
            sigorta_tutar = 0.0
            sigorta_paketi_adi = "Yok"
            sigorta_oran_kullanilan = 0.0

            if dil == "TR":
                sig_cevap = input("\nSigorta yapılsın mı? (E/H): ").upper()
            else:
                sig_cevap = input("\nAdd insurance? (Y/N): ").upper()

            if sig_cevap == "E" or sig_cevap == "Y":
                if kampanya_sigorta_ucretsiz:
                    if dil == "TR":
                        print("Kampanya nedeniyle sigorta ücretsiz!")
                    else:
                        print("Insurance is free due to campaign!")
                    sigorta_tutar = 0.0
                    sigorta_paketi_adi = "Kampanya-Ücretsiz"
                else:
                    # Sigorta paket seviyeleri
                    if dil == "TR":
                        print("\nSigorta Paketi Seçimi:")
                        print("1 - Temel (standart oran)")
                        print("2 - Plus  (oran x 1.5)")
                        print("3 - Full  (oran x 2.0)")
                    else:
                        print("\nInsurance Package Selection:")
                        print("1 - Basic   (standard rate)")
                        print("2 - Plus    (rate x 1.5)")
                        print("3 - Full    (rate x 2.0)")

                    paket_secim = input("Paket / Package: ")
                    sigorta_carpani = 1.0
                    if paket_secim == "1":
                        sigorta_paketi_adi = "Temel"
                        if dil == "EN":
                            sigorta_paketi_adi = "Basic"
                        sigorta_carpani = 1.0
                    elif paket_secim == "2":
                        sigorta_paketi_adi = "Plus"
                        sigorta_carpani = 1.5
                    elif paket_secim == "3":
                        sigorta_paketi_adi = "Full"
                        sigorta_carpani = 2.0
                    else:
                        sigorta_paketi_adi = "Temel"
                        sigorta_carpani = 1.0

                    sigorta_oran_kullanilan = sigorta_oran * sigorta_carpani
                    sigorta_tutar = temel_fiyat * sigorta_oran_kullanilan

                    if dil == "TR":
                        print("Sigorta paketi:", sigorta_paketi_adi, "- Oran:", round(sigorta_oran_kullanilan * 100, 2), "%")
                        print("Sigorta tutarı:", round(sigorta_tutar, 2), "TL")
                    else:
                        print("Insurance package:", sigorta_paketi_adi, "- Rate:", round(sigorta_oran_kullanilan * 100, 2), "%")
                        print("Insurance amount:", round(sigorta_tutar, 2), "TL")

            # ---------- Ek hizmetler ----------
            ek_hizmet_tutar = 0.0
            if dil == "TR":
                print("\nEk Hizmetler:")
                kap = input("Kapıya teslim (+50 TL)? (E/H): ").upper()
                kat_t = input("Kat teslim (+30 TL)? (E/H): ").upper()
                has = input("Hassas taşıma (+40 TL)? (E/H): ").upper()
            else:
                print("\nExtra Services:")
                kap = input("Door delivery (+50 TL)? (Y/N): ").upper()
                kat_t = input("Floor delivery (+30 TL)? (Y/N): ").upper()
                has = input("Fragile handling (+40 TL)? (Y/N): ").upper()

            if kap == "E" or kap == "Y":
                ek_hizmet_tutar = ek_hizmet_tutar + 50
            if kat_t == "E" or kat_t == "Y":
                ek_hizmet_tutar = ek_hizmet_tutar + 30
            if has == "E" or has == "Y":
                ek_hizmet_tutar = ek_hizmet_tutar + 40

            if kampanya_ek_hizmet_ucretsiz and ek_hizmet_tutar > 0:
                if dil == "TR":
                    print("Ek hizmetler kampanya nedeniyle ücretsiz!")
                else:
                    print("Extra services are free due to campaign!")
                ek_hizmet_tutar = 0.0

            # ---------- Müşteri tipi ----------
            if dil == "TR":
                print("\nMüşteri Tipi:")
                print("1 - Normal")
                print("2 - Engelli (%20)")
                print("3 - Öğrenci (%10)")
                print("4 - Kurumsal (%15)")
            else:
                print("\nCustomer Type:")
                print("1 - Regular")
                print("2 - Disabled (%20)")
                print("3 - Student (%10)")
                print("4 - Corporate (%15)")

            musteri_tipi = "Normal"
            if dil == "EN":
                musteri_tipi = "Regular"
            musteri_indirim_oran = 0.0

            while True:
                msec = input("Müşteri / Customer: ")
                if msec == "1":
                    musteri_indirim_oran = 0.0
                    musteri_tipi = "Normal"
                    if dil == "EN":
                        musteri_tipi = "Regular"
                    break
                elif msec == "2":
                    musteri_indirim_oran = 0.20
                    musteri_tipi = "Engelli"
                    if dil == "EN":
                        musteri_tipi = "Disabled"
                    break
                elif msec == "3":
                    musteri_indirim_oran = 0.10
                    musteri_tipi = "Öğrenci"
                    if dil == "EN":
                        musteri_tipi = "Student"
                    break
                elif msec == "4":
                    musteri_indirim_oran = 0.15
                    musteri_tipi = "Kurumsal"
                    if dil == "EN":
                        musteri_tipi = "Corporate"
                    break
                else:
                    if dil == "TR":
                        print("Geçersiz seçim!")
                    else:
                        print("Invalid choice!")

            # ---------- Sadakat seviye indirimi ----------
            sadakat_seviye_indirim_oran = 0.0
            if sadakat_puani >= 20 and sadakat_puani < 50:
                sadakat_seviye = "Silver"
                sadakat_seviye_indirim_oran = 0.03
            elif sadakat_puani >= 50 and sadakat_puani < 100:
                sadakat_seviye = "Gold"
                sadakat_seviye_indirim_oran = 0.05
            elif sadakat_puani >= 100:
                sadakat_seviye = "Platinum"
                sadakat_seviye_indirim_oran = 0.08
            else:
                sadakat_seviye = "Bronze"
                sadakat_seviye_indirim_oran = 0.0

            vip_ek_indirim_oran = 0.0
            if aktif_vip_mi:
                vip_ek_indirim_oran = 0.10

            # ---------- Ara toplam (indirim öncesi) ----------
            ara_toplam = temel_fiyat + sigorta_tutar + ek_hizmet_tutar + gumruk_vergisi

            # Bonus (şans kutusu) indirimi EN BAŞTA uygula
            bonus_indirim_tutar = ara_toplam * bonus_indirim_oran
            ara_toplam = ara_toplam - bonus_indirim_tutar
            bonus_indirim_oran = 0.0  # kullanıldı, sıfırla

            # Günün kampanyası indirimi
            kampanya_indirim_tutar = ara_toplam * kampanya_indirim_oran
            ara_toplam = ara_toplam - kampanya_indirim_tutar

            # Müşteri indirimi
            musteri_indirim_tutar = ara_toplam * musteri_indirim_oran
            ara_toplam = ara_toplam - musteri_indirim_tutar

            # Sadakat indirimi
            sadakat_indirim_tutar = ara_toplam * sadakat_seviye_indirim_oran
            ara_toplam = ara_toplam - sadakat_indirim_tutar

            # VIP indirimi
            vip_indirim_tutar = ara_toplam * vip_ek_indirim_oran
            ara_toplam = ara_toplam - vip_indirim_tutar

            # Kupon indirimi
            if dil == "TR":
                kupon = input("\nİndirim kuponu (yoksa Enter): ").upper().strip()
            else:
                kupon = input("\nDiscount coupon (press Enter for none): ").upper().strip()

            kupon_indirim_tutar = 0.0
            if kupon == "KARGO10":
                kupon_indirim_tutar = ara_toplam * 0.10
                ara_toplam = ara_toplam - kupon_indirim_tutar
                if dil == "TR":
                    print("Kupon ile %10 indirim uygulandı.")
                else:
                    print("10% coupon discount applied.")
            elif kupon != "":
                if dil == "TR":
                    print("Geçersiz kupon, indirim uygulanmadı.")
                else:
                    print("Invalid coupon, no discount.")

            # KDV
            kdv_oran = 0.18
            kdv_tutar = ara_toplam * kdv_oran
            kdv_dahil_tutar = ara_toplam + kdv_tutar

            # Ödeme tipi
            if dil == "TR":
                print("\nÖdeme Tipi:")
                print("1 - Nakit")
                print("2 - Kredi Kartı")
            else:
                print("\nPayment Type:")
                print("1 - Cash")
                print("2 - Credit Card")

            odeme_tipi = "Nakit"
            if dil == "EN":
                odeme_tipi = "Cash"

            taksit_sayisi = 1
            aylik_taksit = 0.0
            taksit_carpan = 1.0

            while True:
                odeme_secim = input("Seçim / Choice: ")
                if odeme_secim == "1":
                    break
                elif odeme_secim == "2":
                    if dil == "TR":
                        odeme_tipi = "Kredi Kartı"
                        print("Taksit seçenekleri: 1, 3, 6, 9 ay")
                    else:
                        odeme_tipi = "Credit Card"
                        print("Installments: 1, 3, 6, 9 months")
                    try:
                        taksit_sayisi = int(input("Taksit sayısı / Installments: "))
                    except ValueError:
                        taksit_sayisi = 1
                    if taksit_sayisi <= 1:
                        taksit_sayisi = 1
                        taksit_carpan = 1.0
                    elif taksit_sayisi == 3:
                        taksit_carpan = 1.03
                    elif taksit_sayisi == 6:
                        taksit_carpan = 1.06
                    elif taksit_sayisi == 9:
                        taksit_carpan = 1.09
                    else:
                        taksit_sayisi = 1
                        taksit_carpan = 1.0
                    break
                else:
                    if dil == "TR":
                        print("Geçersiz seçim!")
                    else:
                        print("Invalid choice!")

            kdv_dahil_tutar = kdv_dahil_tutar * taksit_carpan
            if taksit_sayisi > 1:
                aylik_taksit = kdv_dahil_tutar / taksit_sayisi

            # Döviz seçimi
            if dil == "TR":
                doviz = input("\nPara birimi (TL/USD/EUR): ").upper()
            else:
                doviz = input("\nCurrency (TL/USD/EUR): ").upper()

            if doviz == "TL":
                final_price = kdv_dahil_tutar
            elif doviz == "USD":
                final_price = kdv_dahil_tutar / kur_usd
            elif doviz == "EUR":
                final_price = kdv_dahil_tutar / kur_eur
            else:
                doviz = "TL"
                final_price = kdv_dahil_tutar

            # Tahmini teslim süresi
            tahmini_gun = 2
            if mesafe_turu == "Uzun Mesafe":
                tahmini_gun = tahmini_gun + 1
            if yurt_disi:
                tahmini_gun = tahmini_gun + 3
            if teslim_kodu == "2" or teslim_kodu == "3":
                tahmini_gun = 1
            if teslim_kodu == "4":
                tahmini_gun = 0

            # Risk skoru
            risk_skor = 0
            if efektif_agirlik < 1 and kdv_dahil_tutar > 1000:
                risk_skor = risk_skor + 50
            if tip == "elektronik" or tip == "electronic":
                risk_skor = risk_skor + 30
            if yurt_disi:
                risk_skor = risk_skor + 20
            if teslim_kodu == "4":
                risk_skor = risk_skor + 10

            risk_seviye = "Düşük"
            if risk_skor >= 30 and risk_skor <= 70:
                risk_seviye = "Orta"
            elif risk_skor > 70:
                risk_seviye = "Yüksek"
            if dil == "EN":
                if risk_seviye == "Düşük":
                    risk_seviye = "Low"
                elif risk_seviye == "Orta":
                    risk_seviye = "Medium"
                elif risk_seviye == "Yüksek":
                    risk_seviye = "High"

            riskli_mi = risk_skor > 0

            # Karbon ayak izi (tahmini) hesaplama
            # Basit model: mesafe * efektif_agirlik / 50
            co2_kg = (mesafe * efektif_agirlik) / 50

            # Yurt dışı ve hava taşımacılığında ek çarpan
            if yurt_disi:
                co2_kg = co2_kg * 1.5
            if uluslararasi_tasimacilik_turu == "Hava":
                co2_kg = co2_kg * 1.4

            # Demo modda değilsek toplam karbon ayak izine ekle
            if not demo_mod_aktif:
                toplam_karbon_ayak_izi = toplam_karbon_ayak_izi + co2_kg

            # Kargo takip numarası
            takip_no_rakam = random.randint(100000, 999999)
            takip_no = "KG-" + str(takip_no_rakam)

            # Demo değilse istatistik ve sadakat
            if not demo_mod_aktif:
                toplam_kargo_sayisi = toplam_kargo_sayisi + 1
                toplam_ciro_tl = toplam_ciro_tl + kdv_dahil_tutar
                ek_puan = int(kdv_dahil_tutar / 100)
                sadakat_puani = sadakat_puani + ek_puan

            # Log'a kaydet
            log_satir = str(datetime.now()) + " | KARGO | TAKIP:" + takip_no + " | TIP:" + str(tip) + " | TUTAR:" + str(round(kdv_dahil_tutar, 2)) + " TL\n"
            log_text = log_text + log_satir

            # Simülasyon mesajları
            if dil == "TR":
                print("\nRota planlaması yapılıyor...")
            else:
                print("\nPlanning route...")
            time.sleep(0.3)
            if dil == "TR":
                print("Depodaki uygun araç aranıyor...")
            else:
                print("Finding available vehicle in warehouse...")
            time.sleep(0.3)
            if dil == "TR":
                print("Teslimat zaman çizelgesi hazırlanıyor...")
            else:
                print("Preparing delivery schedule...")
            time.sleep(0.3)

            # ------------ HIZLI ÖZET / DETAYLI FİŞ SEÇİMİ ------------
            if dil == "TR":
                fis_modu = input("\nFiş tipi: Detaylı (D) / Özet (O): ").upper()
            else:
                fis_modu = input("\nReceipt type: Detailed (D) / Summary (S): ").upper()

            # ------------ FİŞ ÇIKTI ------------
            if fis_modu == "O" or fis_modu == "S":
                # ÖZET FİŞ
                if tema == "koyu":
                    print("\n######## ÖZET FİŞ ########")
                else:
                    print("\n===== ÖZET FİŞ =====")
                print("Tarih/Saat:", datetime.now())
                print("Takip No:", takip_no)
                print("Firma:", firma_adi)
                print("Kargo Türü:", tip)
                print("Toplam (KDV Dahil):", round(kdv_dahil_tutar, 2), "TL")
                print("Tahmini Teslim Süresi:", tahmini_gun, "gün")
                print("Tahmini Karbon Ayak İzi:", round(co2_kg, 2), "kg CO2")
                print("Risk Skoru:", risk_skor, "| Seviye:", risk_seviye)
                if tema == "koyu":
                    print("#########################")
                else:
                    print("=========================")
            else:
                # DETAYLI FİŞ
                if tema == "koyu":
                    print("\n################ KARGO FİŞİ ################")
                else:
                    print("\n========== KARGO FİŞİ ==========")

                print("Tarih/Saat:", datetime.now())
                print("Kullanıcı / User:", aktif_kullanici)
                print("Firma / Company:", firma_adi)
                print("Kargo Takip No:", takip_no)
                print("Müşteri Tipi:", musteri_tipi)
                print("Sadakat Seviyesi:", sadakat_seviye, " | Puan:", sadakat_puani)
                print("Kargo Türü:", tip)
                print("Gerçek Ağırlık:", round(agirlik, 2), "kg")
                if hacim_agirlik > 0:
                    print("Hacimsel Ağırlık:", round(hacim_agirlik, 2), "kg")
                print("Kullanılan Ağırlık:", round(efektif_agirlik, 2), "kg")
                print("Paket Sınıfı:", paket_sinifi)
                print("Mesafe:", mesafe, "km", "(", mesafe_turu, ")")
                print("Bölge Çarpanı:", bolge_carpan)
                print("Araç Çarpanı:", arac_carpan)
                print("Teslim Çarpanı:", teslim_carpan)
                print("Firma Çarpanı:", firma_carpan)
                print("Paket Çarpanı:", paket_carpan)
                print("Mesai Çarpanı:", mesai_carpan)
                if yurt_disi:
                    print("Yurt Dışı Taşıma:", uluslararasi_tasimacilik_turu)
                    print("Gümrük Vergisi:", round(gumruk_vergisi, 2), "TL")
                print("Temel Fiyat:", round(temel_fiyat, 2), "TL")
                print("Sigorta Paketi:", sigorta_paketi_adi)
                print("Sigorta Tutarı:", round(sigorta_tutar, 2), "TL")
                print("Ek Hizmet Tutarı:", round(ek_hizmet_tutar, 2), "TL")
                print("Bonus İndirimi:", round(bonus_indirim_tutar, 2), "TL")
                print("Kampanya İndirimi:", round(kampanya_indirim_tutar, 2), "TL")
                print("Müşteri İndirimi:", round(musteri_indirim_tutar, 2), "TL")
                print("Sadakat İndirimi:", round(sadakat_indirim_tutar, 2), "TL")
                print("VIP İndirimi:", round(vip_indirim_tutar, 2), "TL")
                print("Kupon İndirimi:", round(kupon_indirim_tutar, 2), "TL")
                print("Ara Toplam:", round(ara_toplam, 2), "TL")
                print("KDV (%18):", round(kdv_tutar, 2), "TL")
                print("Toplam (KDV Dahil):", round(kdv_dahil_tutar, 2), "TL")
                print("Ödeme Tipi:", odeme_tipi)
                if taksit_sayisi > 1:
                    print("Taksit Sayısı:", taksit_sayisi)
                    print("Aylık Taksit:", round(aylik_taksit, 2), "TL")
                print("Para Birimi:", doviz, "| Karşılık:", round(final_price, 2), doviz)
                print("Tahmini Teslim Süresi:", tahmini_gun, "gün")
                print("Tahmini Karbon Ayak İzi:", round(co2_kg, 2), "kg CO2")
                print("AI Ücret Tahmini:", round(ai_tahmini, 2), "TL")
                print("Risk Skoru:", risk_skor, "| Seviye:", risk_seviye)
                if riskli_mi:
                    if dil == "TR":
                        print("RİSK UYARISI: İşlem ek teyit gerektirebilir.")
                    else:
                        print("RISK WARNING: Operation may need extra confirmation.")
                if demo_mod_aktif:
                    if dil == "TR":
                        print("Not: DEMO mod aktif, istatistikler kaydedilmedi.")
                    else:
                        print("Note: DEMO mode is active, stats not updated.")
                if tema == "koyu":
                    print("###########################################")
                else:
                    print("===========================================")

            # ------------ KİŞİSELLEŞTİRİLMİŞ KAMPANYA MESAJI ------------
            if dil == "TR":
                if musteri_tipi == "Engelli":
                    print("Erişilebilirlik ve adalet odaklı indirimlerimiz sizin için var. 💛")
                elif musteri_tipi == "Öğrenci":
                    print("Öğrenci bütçesini biliyoruz, iyi dersler! 🎓")
                elif musteri_tipi == "Kurumsal":
                    print("Kurumsal gönderilerinizde süreklilik için yanınızdayız. 📦")
            else:
                if musteri_tipi == "Disabled":
                    print("Accessibility and fairness focused discounts are for you. 💛")
                elif musteri_tipi == "Student":
                    print("We know student budgets, good luck with your studies! 🎓")
                elif musteri_tipi == "Corporate":
                    print("We stand by your continuous corporate shipments. 📦")

            # ------------ OYUN / LEVEL MESAJLARI ------------
            if not demo_mod_aktif:
                oyun_mesaj = ""
                if toplam_kargo_sayisi == 10:
                    oyun_mesaj = "Lojistik startup'ınız büyümeye başladı! 🚀"
                elif toplam_kargo_sayisi == 50:
                    oyun_mesaj = "Bölgesel lojistik devi oldunuz! 💼"
                elif toplam_kargo_sayisi == 100:
                    oyun_mesaj = "Dünya çapında lojistik markası oldunuz! 🌍"
                if oyun_mesaj != "":
                    print("Oyun Modu:", oyun_mesaj)

            # ------------ MÜŞTERİ MEMNUNİYET PUANI ------------
            try:
                if dil == "TR":
                    mem_puan = int(input("Bu işlemi 1-5 arası puanlar mısınız?: "))
                else:
                    mem_puan = int(input("Rate this operation 1-5: "))
            except ValueError:
                mem_puan = 0
            if mem_puan >= 1 and mem_puan <= 5:
                toplam_memnuniyet_puani = toplam_memnuniyet_puani + mem_puan
                memnuniyet_sayisi = memnuniyet_sayisi + 1

            # ------------ MÜŞTERİ MEMNUNİYET MOTİVASYON MESAJI ------------
            if memnuniyet_sayisi > 0:
                ort_mem = toplam_memnuniyet_puani / memnuniyet_sayisi
                if ort_mem >= 4:
                    if dil == "TR":
                        print("Müşterileriniz oldukça memnun görünüyor, böyle devam! 🌟")
                    else:
                        print("Your customers seem very satisfied, keep it up! 🌟")
                elif ort_mem < 3:
                    if dil == "TR":
                        print("Memnuniyet ortalaması düşük, süreçleri gözden geçirmek iyi olabilir. 📉")
                    else:
                        print("Satisfaction is low, might be good to review your processes. 📉")

            # ------------ ŞANS KUTUSU (BONUS İNDİRİM) ------------
            sans = random.randint(1, 100)
            if sans <= 5:
                if dil == "TR":
                    print("🎁 Şans Kutusu: Bir sonraki kargonuzda ekstra %5 indirim kazandınız!")
                else:
                    print("🎁 Lucky Box: You won extra 5% discount for your next cargo!")
                bonus_indirim_oran = 0.05

        except Exception as ex:
            if dil == "TR":
                print("Kargo hesaplama sırasında beklenmeyen bir hata oluştu:", ex)
            else:
                print("Unexpected error during cargo calculation:", ex)

    # ==================== 2 - KARGO TAKİP ====================
    elif secim == "2":
        if dil == "TR":
            print("\n--- Kargo Takip Simülasyonu ---")
            tno = input("Takip numarası (örnek KG-123456): ")
            print(tno, "için örnek süreç:")
        else:
            print("\n--- Cargo Tracking Simulation ---")
            tno = input("Tracking number (e.g. KG-123456): ")
            print("Simulated process for", tno, ":")

        time.sleep(0.5)
        # Gecikme / kaybolma ihtimali
        olay = random.randint(1, 10)

        if dil == "TR":
            print("1) Kargo sisteme kaydedildi.")
            time.sleep(0.5)
            print("2) Kargo depoya ulaştı.")
            time.sleep(0.5)
            if olay == 1:
                print("⚠ Kargo aktarma merkezinde karışıklık yaşandı, süreç uzuyor...")
                time.sleep(0.8)
            print("3) Kargo aktarma merkezinde.")
            time.sleep(0.5)
            if olay == 2:
                print("⚠ Araç arızası nedeniyle sevkiyat gecikti.")
                time.sleep(0.8)
            print("4) Kargo dağıtım şubesine sevk edildi.")
            time.sleep(0.5)
            print("5) Kurye teslimata çıktı.")
            time.sleep(0.5)
            if olay == 3:
                print("⚠ Alıcı adreste bulunamadı, yeniden dağıtıma çıkacak.")
                time.sleep(0.8)
            print("6) Kargo alıcıya teslim edildi.\n")
        else:
            print("1) Cargo registered into the system.")
            time.sleep(0.5)
            print("2) Cargo arrived at warehouse.")
            time.sleep(0.5)
            if olay == 1:
                print("⚠ Confusion at transfer center, process delayed...")
                time.sleep(0.8)
            print("3) Cargo at transfer center.")
            time.sleep(0.5)
            if olay == 2:
                print("⚠ Vehicle failure, shipment delayed.")
                time.sleep(0.8)
            print("4) Cargo sent to delivery branch.")
            time.sleep(0.5)
            print("5) Courier is out for delivery.")
            time.sleep(0.5)
            if olay == 3:
                print("⚠ Receiver not found at address, will be re-delivered.")
                time.sleep(0.8)
            print("6) Cargo delivered to receiver.\n")

    # ==================== 3 - İSTATİSTİKLER veya KULLANICI DEĞİŞTİR ====================
    elif secim == "3" and aktif_admin_mi:
        if dil == "TR":
            print("\n--- SİSTEM İSTATİSTİKLERİ (ADMIN) ---")
        else:
            print("\n--- SYSTEM STATISTICS (ADMIN) ---")

        print("Toplam kargo sayısı:", toplam_kargo_sayisi)
        print("Toplam ciro (TL):", round(toplam_ciro_tl, 2))
        ortalama = 0
        if toplam_kargo_sayisi > 0:
            ortalama = toplam_ciro_tl / toplam_kargo_sayisi
        print("Ortalama kargo ücreti (TL):", round(ortalama, 2))
        print("Dosya kargo adedi:", dosya_adet)
        print("Elektronik kargo adedi:", elektronik_adet)
        print("Mobilya kargo adedi:", mobilya_adet)
        if memnuniyet_sayisi > 0:
            ort_mem = toplam_memnuniyet_puani / memnuniyet_sayisi
        else:
            ort_mem = 0
        print("Müşteri memnuniyet ortalaması:", round(ort_mem, 2), "/ 5")
        print("Sadakat Puanı:", sadakat_puani, "Seviye:", sadakat_seviye)
        print("Toplam tahmini karbon ayak izi:", round(toplam_karbon_ayak_izi, 2), "kg CO2")

        # Log göster
        if log_text != "":
            if dil == "TR":
                print("\n--- SİSTEM LOGU (OTURUM) ---")
            else:
                print("\n--- SYSTEM LOG (SESSION) ---")
            print(log_text)
        else:
            if dil == "TR":
                print("\nLog kaydı yok.")
            else:
                print("\nNo log records.")

    elif (secim == "3" and not aktif_admin_mi) or (secim == "4" and aktif_admin_mi):
        # Kullanıcı değiştir
        if dil == "TR":
            print("\n--- Kullanıcı Değiştir ---")
        else:
            print("\n--- Change User ---")

        login_hak = 3
        aktif_kullanici = None
        aktif_admin_mi = False
        aktif_vip_mi = False

        while login_hak > 0:
            if dil == "TR":
                kul = input("Yeni kullanıcı adı: ")
                sifre = input("Yeni şifre: ")
            else:
                kul = input("New username: ")
                sifre = input("New password: ")

            s1 = random.randint(1, 9)
            s2 = random.randint(1, 9)
            try:
                c_cevap = int(input(f"Güvenlik sorusu: {s1} + {s2} = "))
            except ValueError:
                c_cevap = -1

            if c_cevap != s1 + s2:
                if dil == "TR":
                    print("Güvenlik sorusu hatalı!")
                else:
                    print("Security question failed!")
                login_hak = login_hak - 1
                continue

            if kul == ADMIN_KULLANICI and sifre == ADMIN_SIFRE:
                aktif_kullanici = kul
                aktif_admin_mi = True
                aktif_vip_mi = False
                if dil == "TR":
                    print("Admin olarak giriş yapıldı.")
                else:
                    print("Logged in as admin.")
                break
            elif kul == NORMAL_KULLANICI and sifre == NORMAL_SIFRE:
                aktif_kullanici = kul
                aktif_admin_mi = False
                aktif_vip_mi = False
                if dil == "TR":
                    print("Giriş başarılı, hoş geldin", aktif_kullanici)
                else:
                    print("Login successful, welcome", aktif_kullanici)
                break
            elif kul == VIP_KULLANICI and sifre == VIP_SIFRE:
                aktif_kullanici = kul
                aktif_admin_mi = False
                aktif_vip_mi = True
                if dil == "TR":
                    print("VIP kullanıcı olarak giriş yapıldı.")
                else:
                    print("Logged in as VIP user.")
                break
            else:
                if dil == "TR":
                    print("Kullanıcı adı veya şifre hatalı!")
                else:
                    print("Invalid username or password!")
                login_hak = login_hak - 1

        if aktif_kullanici is None:
            if dil == "TR":
                print("Çok fazla hatalı giriş. Sistem sonlandırılıyor.")
            else:
                print("Too many wrong attempts. System exiting.")
            program_calisiyor = False

    # ==================== 6 - İADE / İPTAL SİMÜLASYONU ====================
    elif secim == "6":
        if dil == "TR":
            print("\n--- İade / İptal Simülasyonu ---")
            takip = input("İade talep edilen kargo takip no: ")
            sebep = input("İade / iptal nedeni (kısa açıklama): ")
            print("Talebiniz inceleniyor...")
        else:
            print("\n--- Refund / Cancellation Simulation ---")
            takip = input("Tracking number for refund: ")
            sebep = input("Reason for refund / cancellation (short): ")
            print("Your request is being reviewed...")

        time.sleep(0.7)
        # Basit karar: random ama birkaç kurala bağlı simülasyon
        sonuc_tipi = random.randint(1, 3)
        sonuc_text = ""

        if sonuc_tipi == 1:
            if dil == "TR":
                print("İşlem öncesi aşamada olduğundan, iptal talebiniz ONAYLANDI.")
                sonuc_text = "ONAYLANDI"
            else:
                print("Since shipment is in early stage, your cancellation is APPROVED.")
                sonuc_text = "APPROVED"
        elif sonuc_tipi == 2:
            if dil == "TR":
                print("Kargo dağıtım aşamasında olduğundan, iptal talebiniz kısmen REDDEDİLDİ.")
                print("Teslimden sonra iade süreci değerlendirilebilir.")
                sonuc_text = "KISMEN_RED"
            else:
                print("Cargo is in distribution stage, your cancellation is PARTIALLY REJECTED.")
                print("After delivery, a refund request may be evaluated.")
                sonuc_text = "PARTIAL_REJECT"
        else:
            if dil == "TR":
                print("Kargo teslim edildiği için iptal / iade talebiniz REDDEDİLDİ.")
                sonuc_text = "REDDEDİLDİ"
            else:
                print("Cargo has already been delivered; your refund/cancellation request is REJECTED.")
                sonuc_text = "REJECTED"

        # Log'a kayıt
        log_satir = str(datetime.now()) + " | IADE | TAKIP:" + takip + " | SONUC:" + sonuc_text + " | SEBEP:" + sebep + "\n"
        log_text = log_text + log_satir

    # ==================== ÇIKIŞ ====================
    elif (secim == "4" and not aktif_admin_mi) or (secim == "5" and aktif_admin_mi):
        # Çıkmadan önce OTURUM ÖZETİ
        if dil == "TR":
            print("\n--- OTURUM ÖZETİ ---")
        else:
            print("\n--- SESSION SUMMARY ---")
        print("Toplam kargo sayısı:", toplam_kargo_sayisi)
        print("Toplam ciro (TL):", round(toplam_ciro_tl, 2))
        if toplam_kargo_sayisi > 0:
            ortalama = toplam_ciro_tl / toplam_kargo_sayisi
        else:
            ortalama = 0
        print("Ortalama kargo ücreti (TL):", round(ortalama, 2))
        if memnuniyet_sayisi > 0:
            ort_mem = toplam_memnuniyet_puani / memnuniyet_sayisi
        else:
            ort_mem = 0
        print("Memnuniyet ortalaması:", round(ort_mem, 2), "/ 5")
        print("Sadakat Puanı:", sadakat_puani, "Seviye:", sadakat_seviye)
        if dil == "TR":
            print("Program sonlandırılıyor. Görüşmek üzere!")
        else:
            print("Exiting program. See you!")
        program_calisiyor = False

    # ==================== 9 - YARDIM ====================
    elif secim == "9":
        if dil == "TR":
            print("\n--- YARDIM / NASIL KULLANILIR? ---")
            print("1 - Yeni kargo oluşturur, fiyat hesaplar ve fiş verir.")
            print("2 - Örnek bir kargo takip süreci gösterir.")
            print("3 - Admin isen istatistikleri ve log kaydını gösterir; normal kullanıcıysan kullanıcı değiştirme menüsüdür.")
            print("4/5 - Çıkış veya kullanıcı değiştirme seçenekleri.")
            print("6 - İade / iptal sürecini senaryolaştıran simülasyon menüsüdür.")
            print("Sadakat puanı, bonus indirim ve memnuniyet puanları sadece bu oturumda geçerlidir.")
            print("Demo modda istatistikler ve puanlar güncellenmez.")
        else:
            print("\n--- HELP / HOW TO USE ---")
            print("1 - Creates a new cargo, calculates price and prints receipt.")
            print("2 - Shows a simulated cargo tracking process.")
            print("3 - If admin, shows statistics and log; if regular user, changes user.")
            print("4/5 - Exit or change user options.")
            print("6 - Simulates refund / cancellation scenarios.")
            print("Loyalty points, bonus discount and satisfaction stats are in-memory for this session only.")
            print("In demo mode, stats and points are not updated.")

    # ==================== GEÇERSİZ SEÇİM ====================
    else:
        if dil == "TR":
            print("Geçersiz seçim, lütfen menüdeki değerlerden birini giriniz.")
        else:
            print("Invalid choice, please select a valid menu option.")
