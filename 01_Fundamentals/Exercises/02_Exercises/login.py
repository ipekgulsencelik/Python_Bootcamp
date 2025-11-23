# -----------------------------
# LOGIN UYGULAMASI
# - Kullanıcı adı / şifre ile giriş
# - 2 adımlı doğrulama (şifre + kod)
# - Şifre kurtarma (gizli soru ile)
# -----------------------------

import time  # time.sleep için gerekli

# Başlangıç verileri / değişken tanımları
kullanici_adi = "admin"     # Varsayılan kullanıcı adı
sifre = "1234"              # Varsayılan şifre
hak = 3                     # Giriş için toplam deneme hakkı
login_successful = False    # Giriş başarılı mı kontrolü için bayrak

dogrulama_kodu = "9999"     # 2 adımlı doğrulama için sabit kod (gerçek hayatta random olurdu)

gizli_soru = "İlk evcil hayvanınızın adı nedir?"
gizli_cevap = "boncuk"

# -------- LOGIN KISMI --------
# Kullanıcı adı ve şifre ile giriş yapılır.
# Şifre doğru ise ek olarak 4 haneli doğrulama kodu sorulur.
# İstenirse gizli soru ile şifre sıfırlanabilir.

while hak > 0 and not login_successful:
    print("\n===== GİRİŞ EKRANI =====")
    print("1- Giriş yap")
    print("2- Şifremi unuttum (gizli soru ile sıfırla)")
    giris_secim = input("Seçiminiz (1/2): ")

    # Menü seçimini match ile kontrol et
    match giris_secim:
        case "2":
            # Şifre kurtarma
            print("\n--- Şifre Kurtarma ---")
            print("Gizli soru:")
            print(gizli_soru)
            cevap = input("Cevabınız: ")

            # Cevapları küçük harfe çevirerek karşılaştır (büyük/küçük harf duyarsız)
            if cevap.lower() == gizli_cevap.lower():
                yeni_sifre = input("Yeni şifrenizi giriniz: ")

                if yeni_sifre == "":
                    print("Şifre boş olamaz.")
                else:
                    sifre = yeni_sifre
                    print("Şifreniz başarıyla güncellendi. Şimdi giriş yapabilirsiniz.")
            else:
                print("Gizli soru cevabı yanlış.")
            # Şifre kurtarma bitti, tekrar giriş ekranına dön
            continue
        case "1":
            # Normal giriş
            username = input("İsminiz: ")
            password = input("Şifreniz: ")

            # İlk kontrol: kullanıcı adı + şifre
            if username == kullanici_adi and password == sifre:
                print("Şifre doğru.")
                # İkinci adım: doğrulama kodu
                kod_giris = input("Telefonunuza gönderilen 4 haneli kodu giriniz: ")

                if kod_giris == dogrulama_kodu:
                    # Hem şifre hem doğrulama kodu doğruysa giriş başarılı
                    print(f"Giriş başarılı, hoşgeldin {username}")
                    login_successful = True
                else:
                    # Kod yanlışsa hak 1 azalır
                    hak -= 1
                    if hak == 0:
                        print("Doğrulama kodu yanlış. Hesabınız bloke edilmiştir.")
                    else:
                        print(f"Doğrulama kodu yanlış. Kalan hakkınız = {hak}")
                        print("Güvenlik nedeniyle kısa süreli bloke uygulanıyor...")
                        time.sleep(5)
            else:
                # Kullanıcı adı veya şifre yanlışsa da hak 1 azalır
                hak -= 1
                print("Kullanıcı adı veya şifre yanlış.")
                if hak == 0:
                    print("Giriş bilgileriniz yanlış. Hesabınız bloke edilmiştir.")
                else:
                    print(f"Giriş yanlış, kalan hakkınız = {hak}")
                    print("Güvenlik nedeniyle kısa süreli bloke uygulanıyor...")
                    time.sleep(5)
        case _:  # 1 veya 2 dışında bir şey girilirse
            print("Geçersiz seçim yaptınız. Lütfen 1 veya 2 giriniz.")
            # hak azaltmıyoruz, sadece tekrar menüye dönüyor
            continue

# Eğer giriş başarısızsa program tamamen sonlandırılır
if not login_successful:
    exit()