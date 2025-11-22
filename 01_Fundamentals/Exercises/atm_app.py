# -----------------------------
#   ATM UYGULAMASI
#   - Kullanıcı adı / şifre ile giriş
#   - 2 adımlı doğrulama (şifre + kod)
#   - Standart / Altın hesap türü
#   - Günlük para çekme limiti
#   - Kredi çekme / kredi borcu ödeme
#   - İşlem geçmişi (string olarak)
#   - Kart numarası ekleme/değiştirme
#   - Gün sonu raporu
# -----------------------------

# Başlangıç verileri / değişken tanımları
kullanici_adi = "admin"     # Varsayılan kullanıcı adı
sifre = "1234"              # Varsayılan şifre
hak = 3                     # Giriş için toplam deneme hakkı
bakiye = 0                  # Hesaptaki başlangıç bakiyesi
login_successful = False    # Giriş başarılı mı kontrolü için bayrak
hesap_turu = "Standart"     # Hesap türü: "Standart" veya "Altın"

gunluk_cekim_limiti = 2000  # Günlük para çekme limiti (hesap türüne göre değişecek)
bugun_cekilen = 0           # Bugün çekilen toplam para miktarı

kredi_limiti = 5000         # Toplam kredi limiti (hesap türüne göre değişecek)
kredi_borcu = 0             # O anki kredi borcu

islem_gecmisi = ""          # İşlem geçmişini tutan metin (liste yok, her satır ekleniyor)
kart_numarasi = ""          # Kart numarası (son 4 hanesini göstereceğiz)

dogrulama_kodu = "9999"     # 2 adımlı doğrulama için sabit kod (gerçek hayatta random olurdu)

# -------- LOGIN KISMI --------
# Kullanıcı adı ve şifre ile giriş yapılır.
# Şifre doğru ise ek olarak 4 haneli doğrulama kodu sorulur.

while hak > 0 and not login_successful:
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
    else:
        # Kullanıcı adı veya şifre yanlışsa da hak 1 azalır
        hak -= 1
        if hak == 0:
            print("Giriş bilgileriniz yanlış. Hesabınız bloke edilmiştir.")
        else:
            print(f"Giriş yanlış, kalan hakkınız = {hak}")

# Eğer giriş başarısızsa program tamamen sonlandırılır
if not login_successful:
    exit()

# -------- ANA MENÜ / İŞLEM KISMI --------
# Bu kısım, kullanıcı başarılı şekilde giriş yaptıktan sonra çalışır.
# Sürekli dönen bir while döngüsü ile menü gösterilir.
# Kullanıcı 4 (güvenli çıkış) seçeneğini seçene kadar menü dönmeye devam eder.

while True:
    # Hesap türüne göre avantajları her turda güncelle
    if hesap_turu == "Altın":
        gunluk_cekim_limiti = 4000   # Altın hesapta günlük çekim limiti daha yüksek
        kredi_limiti = 10000         # Altın hesapta kredi limiti daha yüksek
        faiz_orani = 0.15            # Altın hesapta faiz oranı %15
    else:
        gunluk_cekim_limiti = 2000   # Standart hesap günlük çekim limiti
        kredi_limiti = 5000          # Standart hesap kredi limiti
        faiz_orani = 0.10            # Standart hesap faiz oranı %10

    try:
        # Kullanıcıya genel bilgiler ve menü seçenekleri gösterilir
        print("\n----- ATM MENÜ -----")
        print(f"Aktif kullanıcı: {kullanici_adi}")
        print(f"Hesap türü: {hesap_turu}")
        print(f"Günlük çekim limiti: {gunluk_cekim_limiti} TL")
        print(f"Kredi limiti: {kredi_limiti} TL")

        # Kart numarası varsa, güvenlik için sadece son 4 haneyi gösteriyoruz
        if kart_numarasi != "":
            print(f"Kart numarası: **** **** **** {kart_numarasi[-4:]}")
        else:
            print("Kart numarası: Tanımlı değil")

        # İşlem menüsü
        print("\n1- Bakiye Sorgula")
        print("2- Para Yatır")
        print("3- Para Çek")
        print("4- Güvenli Çıkış")
        print("5- Şifre Değiştir")
        print("6- Faiz Hesapla")
        print("7- Hesap Türü Değiştir (Standart/Altın)")
        print("8- İşlem Geçmişini Görüntüle")
        print("9- Kredi Çek")
        print("10- Kredi Borcu Öde")
        print("11- Kullanıcı Adı Değiştir")
        print("12- Kart Numarası Ekle/Değiştir")
        print("13- Gün Sonu Raporu")

        # Kullanıcıdan yapılacak işlemin numarası alınır
        islem = int(input("İşlem = "))

        # match-case ile seçim yapılır (Python 3.10+)
        match islem:
            # 1- BAKİYE SORGULAMA
            case 1:
                print(f"\nBakiyeniz = {bakiye} TL")
                print(f"Kredi borcunuz = {kredi_borcu} TL")

            # 2- PARA YATIRMA
            case 2:
                try:
                    yatir = int(input("Yatırılacak tutar: "))
                    if yatir > 0:
                        bakiye += yatir
                        print(f"{yatir} TL yatırıldı. Yeni bakiye = {bakiye} TL")
                        # İşlem geçmişine metin olarak eklenir
                        islem_gecmisi += f"Para yatırma: +{yatir} TL | Yeni bakiye: {bakiye} TL\n"
                    else:
                        print("Geçersiz tutar.")
                except:
                    print("Lütfen sayısal bir değer giriniz.")

            # 3- PARA ÇEKME (GÜNLÜK LİMİT VE BAKİYE KONTROLLÜ)
            case 3:
                try:
                    cek = int(input("Çekilecek tutar: "))
                    if cek <= 0:
                        print("Geçersiz tutar.")
                    elif cek > bakiye:
                        # Hesapta yeterli para yoksa
                        print("Yetersiz bakiye.")
                    elif bugun_cekilen + cek > gunluk_cekim_limiti:
                        # Günlük limit aşılırsa
                        kalan_limit = gunluk_cekim_limiti - bugun_cekilen
                        print(f"Günlük çekim limitini aşıyorsunuz. Kalan limit = {kalan_limit} TL")
                    else:
                        # Tüm kontroller geçerse para çekilir
                        bakiye -= cek
                        bugun_cekilen += cek
                        print(f"{cek} TL çekildi. Yeni bakiye = {bakiye} TL")
                        print(f"Bugün toplam çektiğiniz tutar = {bugun_cekilen} TL")
                        islem_gecmisi += f"Para çekme: -{cek} TL | Yeni bakiye: {bakiye} TL\n"
                except:
                    print("Lütfen sayısal bir değer giriniz.")

            # 4- GÜVENLİ ÇIKIŞ
            case 4:
                print("Güvenli çıkış yapılıyor... İyi günler!")
                break  # while True döngüsünden çıkar ve program biter

            # 5- ŞİFRE DEĞİŞTİRME
            case 5:
                eski = input("Eski şifre: ")
                if eski == sifre:
                    yeni = input("Yeni şifre: ")
                    if yeni == "":
                        print("Şifre boş olamaz.")
                    else:
                        sifre = yeni
                        print("Şifre başarıyla değiştirildi.")
                        islem_gecmisi += "Şifre değiştirildi.\n"
                else:
                    print("Eski şifre yanlış.")

            # 6- FAİZ HESAPLAMA (Hesap türüne göre faiz oranı değişir)
            case 6:
                # Faiz sadece hesaplama amaçlı, bakiyeye otomatik eklenmiyor
                faiz = bakiye * faiz_orani
                yeni_bakiye = bakiye + faiz
                print(f"Hesap türü: {hesap_turu}")
                print(f"Faiz oranı: %{faiz_orani * 100}")
                print(f"Faiz tutarı = {faiz} TL")
                print(f"Faiz sonrası bakiye (örnek) = {yeni_bakiye} TL")
                islem_gecmisi += f"Faiz hesaplandı: {faiz} TL (bakiye değişmedi, sadece hesaplama yapıldı)\n"

            # 7- HESAP TÜRÜ DEĞİŞTİRME (Standart <-> Altın)
            case 7:
                if hesap_turu == "Standart":
                    hesap_turu = "Altın"
                else:
                    hesap_turu = "Standart"
                print(f"Hesap türü değiştirildi → {hesap_turu}")
                islem_gecmisi += f"Hesap türü değişti: {hesap_turu}\n"

            # 8- İŞLEM GEÇMİŞİ GÖRÜNTÜLEME
            case 8:
                print("\n----- İŞLEM GEÇMİŞİ -----")
                if islem_gecmisi == "":
                    print("Henüz herhangi bir işlem yapılmamış.")
                else:
                    # Tüm geçmişi tek seferde yazdırıyoruz (her işlem satır satır)
                    print(islem_gecmisi)

            # 9- KREDİ ÇEKME (Hesap türüne göre kredi limiti kullanılır)
            case 9:
                print(f"Mevcut kredi borcunuz: {kredi_borcu} TL")
                print(f"Toplam kredi limiti: {kredi_limiti} TL")
                kalan_kredi_limiti = kredi_limiti - kredi_borcu
                print(f"Kullanılabilir kredi limiti: {kalan_kredi_limiti} TL")

                try:
                    kredi_tutar = int(input("Çekmek istediğiniz kredi tutarı: "))
                    if kredi_tutar <= 0:
                        print("Geçersiz tutar.")
                    elif kredi_tutar > kalan_kredi_limiti:
                        print("Bu tutarda kredi çekemezsiniz. Limiti aşıyor.")
                    else:
                        # Kredi çekilirse, borç artar ve para bakiyeye eklenir
                        kredi_borcu += kredi_tutar
                        bakiye += kredi_tutar
                        print(f"{kredi_tutar} TL kredi çekildi.")
                        print(f"Yeni bakiye = {bakiye} TL")
                        print(f"Yeni kredi borcunuz = {kredi_borcu} TL")
                        islem_gecmisi += f"Kredi çekildi: +{kredi_tutar} TL | Kredi borcu: {kredi_borcu} TL | Yeni bakiye: {bakiye} TL\n"
                except:
                    print("Lütfen sayısal bir değer giriniz.")

            # 10- KREDİ BORCU ÖDEME
            case 10:
                print(f"Mevcut kredi borcunuz: {kredi_borcu} TL")
                print(f"Mevcut bakiyeniz: {bakiye} TL")

                if kredi_borcu <= 0:
                    print("Ödenecek kredi borcu yok.")
                else:
                    try:
                        odeme = int(input("Ödemek istediğiniz tutar: "))
                        if odeme <= 0:
                            print("Geçersiz tutar.")
                        elif odeme > bakiye:
                            print("Bakiyeniz bu ödemeyi yapmaya yetmiyor.")
                        elif odeme > kredi_borcu:
                            print("Borçtan fazla ödeme yapamazsınız.")
                        else:
                            # Ödeme hem bakiyeden düşülür hem borçtan
                            bakiye -= odeme
                            kredi_borcu -= odeme
                            print(f"{odeme} TL kredi borcu ödendi.")
                            print(f"Kalan kredi borcu = {kredi_borcu} TL")
                            print(f"Yeni bakiye = {bakiye} TL")
                            islem_gecmisi += f"Kredi borcu ödemesi: -{odeme} TL | Kalan borç: {kredi_borcu} TL | Yeni bakiye: {bakiye} TL\n"
                    except:
                        print("Lütfen sayısal bir değer giriniz.")

            # 11- KULLANICI ADI DEĞİŞTİRME
            case 11:
                mevcut_sifre = input("Güvenlik için şifrenizi giriniz: ")
                if mevcut_sifre == sifre:
                    yeni_kullanici_adi = input("Yeni kullanıcı adını giriniz: ")
                    if yeni_kullanici_adi == "":
                        print("Kullanıcı adı boş olamaz.")
                    else:
                        kullanici_adi = yeni_kullanici_adi
                        print(f"Kullanıcı adınız '{kullanici_adi}' olarak değiştirildi.")
                        islem_gecmisi += f"Kullanıcı adı değişti: {kullanici_adi}\n"
                else:
                    print("Şifre yanlış, kullanıcı adı değiştirilemedi.")

            # 12- KART NUMARASI EKLE / DEĞİŞTİR
            case 12:
                yeni_kart = input("Kart numaranızı giriniz (sadece rakam, boşluk yok): ")
                if yeni_kart == "":
                    print("Kart numarası boş olamaz.")
                elif len(yeni_kart) < 8:
                    print("Kart numarası çok kısa.")
                else:
                    kart_numarasi = yeni_kart
                    print("Kart numarası başarıyla kaydedildi/değiştirildi.")
                    islem_gecmisi += "Kart numarası güncellendi.\n"

            # 13- GÜN SONU RAPORU
            case 13:
                print("\n===== GÜN SONU RAPORU =====")
                print(f"Hesap türü        : {hesap_turu}")
                print(f"Bakiyeniz         : {bakiye} TL")
                print(f"Kredi borcunuz    : {kredi_borcu} TL")
                print(f"Günlük limit      : {gunluk_cekim_limiti} TL")
                print(f"Bugün çekilen     : {bugun_cekilen} TL")
                print("\n--- İşlem Geçmişi ---")
                if islem_gecmisi == "":
                    print("Bugün için kayıtlı işlem yok.")
                else:
                    print(islem_gecmisi)
                print("===== RAPOR SONU =====\n")

            # GEÇERSİZ İŞLEM SEÇİMİ
            case _:
                print("Geçersiz işlem, 1-13 arası bir değer giriniz.")

    except:
        # Menü seçiminde sayı yerine harf vb. girilirse buraya düşer
        print("Lütfen yalnızca sayı giriniz.")