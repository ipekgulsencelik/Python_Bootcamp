# ============================================================
# ATM UYGULAMASI
#
# - Kullanıcı adı / şifre ile giriş
# - 2 adımlı doğrulama (şifre + kod)
# - Standart / Altın hesap türü
# - Günlük para çekme ve yatırma limiti
# - Kredi çekme / kredi borcu ödeme
# - Döviz işlemleri (USD)
# - Fatura ödeme (elektrik, su, internet, doğalgaz)
# - Havale / EFT (diğer hesaba gönderim)
# - İşlem ücreti mantığı (para çekme, havale)
# - Kart numarası ve temassız/temaslı ödeme
# - QR ile para çekme
# - Şifre kurtarma (gizli soru)
# - Dil (TR/EN) ve tema (Aydınlık/Karanlık) değiştirme
# - Ay sonu faizi ve gün sonu raporu:
# ============================================================

import time
import random

kullanici_adi = "admin"
sifre = "1234"
hak = 3
bakiye = 0
login_successful = False
hesap_turu = "Standart"

gunluk_cekim_limiti = 2000
bugun_cekilen = 0

gunluk_yatirma_limiti = 10000
bugun_yatirilan = 0

kredi_limiti = 5000
kredi_borcu = 0

dolar_bakiye = 0.0
dolar_kuru = 35.0

elektrik_borc = 500
su_borc = 200
internet_borc = 300
dogalgaz_borc = 400

diger_hesap_adi = "Ahmet"
diger_hesap_bakiye = 1000

islem_gecmisi = ""

kart_numarasi = ""
temassiz_limit = 750

dogrulama_kodu = "9999"

gizli_soru = "İlk evcil hayvanınızın adı nedir?"
gizli_cevap = "boncuk"

dil = "TR"
tema = "Aydınlık"
bugun_gun = 30
asistan_adi = "Asistan"

# -------- LOGIN KISMI --------
while hak > 0 and not login_successful:
    print("\n===== GİRİŞ EKRANI =====")
    print("1- Giriş yap")
    print("2- Şifremi unuttum (gizli soru ile sıfırla)")
    print("3- Programdan çık")
    giris_secim = input("Seçiminiz (1/2/3): ")

    match giris_secim:
        case "2":
            # Şifre kurtarma
            print("\n--- Şifre Kurtarma ---")
            print("Gizli soru:")
            print(gizli_soru)
            cevap = input("Cevabınız: ")

            if cevap.lower() == gizli_cevap.lower():
                yeni_sifre = input("Yeni şifrenizi giriniz: ")
                if yeni_sifre == "":
                    print("Şifre boş olamaz.")
                else:
                    sifre = yeni_sifre
                    print("Şifreniz başarıyla güncellendi. Şimdi giriş yapabilirsiniz.")
            else:
                print("Gizli soru cevabı yanlış.")
            continue

        case "3":
            print("Program sonlandırılıyor...")
            raise SystemExit

        case "1":
            username = input("Kullanıcı adınız: ")
            password = input("Şifreniz: ")

            if username == kullanici_adi and password == sifre:
                print("Şifre doğru.")
                kod_giris = input("Telefonunuza gönderilen 4 haneli kodu giriniz: ")

                if kod_giris == dogrulama_kodu:
                    print(f"Giriş başarılı, hoşgeldin {username}")
                    login_successful = True
                else:
                    hak -= 1
                    if hak == 0:
                        print("Doğrulama kodu yanlış. Hesabınız bloke edilmiştir.")
                    else:
                        print(f"Doğrulama kodu yanlış. Kalan hakkınız = {hak}")
                        print("Güvenlik nedeniyle kısa süreli bloke uygulanıyor...")
                        time.sleep(5)
            else:
                hak -= 1
                print("Kullanıcı adı veya şifre yanlış.")
                if hak == 0:
                    print("Giriş bilgileriniz yanlış. Hesabınız bloke edilmiştir.")
                else:
                    print(f"Giriş yanlış, kalan hakkınız = {hak}")
                    print("Güvenlik nedeniyle kısa süreli bloke uygulanıyor...")
                    time.sleep(5)

        case _:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 giriniz.")

if not login_successful:
    raise SystemExit

# -------- ANA MENÜ --------
while True:
    # Hesap türüne göre parametreler
    if hesap_turu == "Altın":
        gunluk_cekim_limiti = 4000
        kredi_limiti = 10000
        faiz_orani = 0.15
        para_cekme_ucreti = 0
        havale_ucreti = 2
    else:
        gunluk_cekim_limiti = 2000
        kredi_limiti = 5000
        faiz_orani = 0.10
        para_cekme_ucreti = 5
        havale_ucreti = 5

    baslik_cizgi = "#############################" if tema == "Karanlık" else "-----------------------------"

    print("\n" + baslik_cizgi)
    if dil == "EN":
        print(f"{asistan_adi}: Welcome to the ATM")
    else:
        print(f"{asistan_adi}: ATM sistemine hoş geldiniz")
    print(baslik_cizgi)

    print("\n----- ATM MENÜ -----")
    print(f"Aktif kullanıcı : {kullanici_adi}")
    print(f"Hesap türü      : {hesap_turu}")
    print(f"Günlük çekim limiti  : {gunluk_cekim_limiti} TL")
    print(f"Günlük yatırma limiti: {gunluk_yatirma_limiti} TL")
    print(f"Bugün çekilen        : {bugun_cekilen} TL")
    print(f"Bugün yatırılan      : {bugun_yatirilan} TL")
    print(f"Kredi limiti         : {kredi_limiti} TL")
    print(f"Kredi borcu          : {kredi_borcu} TL")
    print(f"Dolar bakiyesi       : {dolar_bakiye} USD (1 USD = {dolar_kuru} TL)")
    print(f"Bugün ayın {bugun_gun}. günü")

    if kart_numarasi != "":
        print(f"Kart numarası: **** **** **** {kart_numarasi[-4:]}")
    else:
        print("Kart numarası: Tanımlı değil")

    print("\n--- İŞLEM MENÜSÜ ---")
    print(" 1- Bakiye Sorgula")
    print(" 2- Para Yatır")
    print(" 3- Para Çek")
    print(" 4- Güvenli Çıkış")
    print(" 5- Şifre Değiştir")
    print(" 6- Faiz Hesapla")
    print(" 7- Hesap Türü Değiştir (Standart/Altın)")
    print(" 8- İşlem Geçmişini Görüntüle")
    print(" 9- Kredi Çek")
    print("10- Kredi Borcu Öde")
    print("11- Kullanıcı Adı Değiştir")
    print("12- Kart Numarası Ekle/Değiştir")
    print("13- Gün Sonu Raporu (Günü 1 artırır)")
    print("14- Fatura Öde")
    print("15- Döviz İşlemleri (USD)")
    print("16- Havale / EFT")
    print("17- Çek Kırma")
    print("18- Kartla Ödeme (Temaslı/Temassız)")
    print("19- QR ile Para Çek")
    print("20- Dil Değiştir (TR/EN)")
    print("21- Tema Değiştir (Aydınlık/Karanlık)")
    print("22- Ay Sonu Faizi Uygula (Manuel)")

    # Ana menü seçiminde try
    try:
        islem = int(input("İşlem = "))
    except ValueError:
        print("Lütfen menü için sadece sayı giriniz.")
        continue

    match islem:
        # 1- BAKİYE
        case 1:
            print(f"\nBakiyeniz = {bakiye} TL")
            print(f"Kredi borcunuz = {kredi_borcu} TL")
            print(f"Dolar bakiyeniz = {dolar_bakiye} USD")
            print(f"{asistan_adi}: Hesap özetiniz yukarıdadır.")

        # 2- PARA YATIR
        case 2:
            try:
                yatir = int(input("Yatırılacak tutar: "))
            except ValueError:
                print("Lütfen sayısal bir değer giriniz.")
                continue

            if yatir > 0:
                if bugun_yatirilan + yatir > gunluk_yatirma_limiti:
                    kalan_yatirma = gunluk_yatirma_limiti - bugun_yatirilan
                    print(f"Günlük yatırma limitini aşıyorsunuz. Kalan limit = {kalan_yatirma} TL")
                else:
                    bakiye += yatir
                    bugun_yatirilan += yatir
                    print(f"{yatir} TL yatırıldı. Yeni bakiye = {bakiye} TL")
                    print("📱 Bildirim: Hesabınıza para yatırıldı.")
                    islem_gecmisi += f"Para yatırma: +{yatir} TL | Yeni bakiye: {bakiye} TL\n"
            else:
                print("Geçersiz tutar.")

        # 3- PARA ÇEK
        case 3:
            try:
                cek = int(input("Çekilecek tutar: "))
            except ValueError:
                print("Lütfen sayısal bir değer giriniz.")
                continue

            if cek <= 0:
                print("Geçersiz tutar.")
            else:
                toplam_tutar = cek + para_cekme_ucreti
                if toplam_tutar > bakiye:
                    print("Yetersiz bakiye (işlem ücreti dahil).")
                elif bugun_cekilen + cek > gunluk_cekim_limiti:
                    kalan_limit = gunluk_cekim_limiti - bugun_cekilen
                    print(f"Günlük çekim limitini aşıyorsunuz. Kalan limit = {kalan_limit} TL")
                else:
                    bakiye -= toplam_tutar
                    bugun_cekilen += cek
                    print(f"{cek} TL çekildi. İşlem ücreti: {para_cekme_ucreti} TL")
                    print(f"Yeni bakiye = {bakiye} TL")
                    print(f"Bugün toplam çektiğiniz: {bugun_cekilen} TL")
                    print("📱 Bildirim: Hesabınızdan para çekildi.")
                    islem_gecmisi += f"Para çekme: -{cek} TL (Ücret: {para_cekme_ucreti} TL) | Yeni bakiye: {bakiye} TL\n"

        # 4- ÇIKIŞ
        case 4:
            print("Güvenli çıkış yapılıyor... İyi günler!")
            break

        # 5- ŞİFRE DEĞİŞTİR
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

        # 6- FAİZ HESAPLA
        case 6:
            faiz = bakiye * faiz_orani
            yeni_bakiye = bakiye + faiz
            print(f"Hesap türü: {hesap_turu}")
            print(f"Faiz oranı: %{faiz_orani * 100}")
            print(f"Faiz tutarı = {faiz} TL")
            print(f"Faiz sonrası bakiye (örnek) = {yeni_bakiye} TL")
            islem_gecmisi += f"Faiz hesaplandı: {faiz} TL (bakiye değişmedi, sadece hesaplama yapıldı)\n"

        # 7- HESAP TÜRÜ
        case 7:
            if hesap_turu == "Standart":
                hesap_turu = "Altın"
            else:
                hesap_turu = "Standart"
            print(f"Hesap türü değiştirildi → {hesap_turu}")
            islem_gecmisi += f"Hesap türü değişti: {hesap_turu}\n"

        # 8- İŞLEM GEÇMİŞİ
        case 8:
            print("\n----- İŞLEM GEÇMİŞİ -----")
            if islem_gecmisi == "":
                print("Henüz herhangi bir işlem yapılmamış.")
            else:
                print(islem_gecmisi)

        # 9- KREDİ ÇEK
        case 9:
            print(f"Mevcut kredi borcunuz: {kredi_borcu} TL")
            print(f"Toplam kredi limiti: {kredi_limiti} TL")
            kalan_kredi_limiti = kredi_limiti - kredi_borcu
            print(f"Kullanılabilir kredi limiti: {kalan_kredi_limiti} TL")

            try:
                kredi_tutar = int(input("Çekmek istediğiniz kredi tutarı: "))
            except ValueError:
                print("Lütfen sayısal bir değer giriniz.")
                continue

            if kredi_tutar <= 0:
                print("Geçersiz tutar.")
            elif kredi_tutar > kalan_kredi_limiti:
                print("Bu tutarda kredi çekemezsiniz. Limiti aşıyor.")
            else:
                kredi_borcu += kredi_tutar
                bakiye += kredi_tutar
                print(f"{kredi_tutar} TL kredi çekildi.")
                print(f"Yeni bakiye = {bakiye} TL")
                print(f"Yeni kredi borcunuz = {kredi_borcu} TL")
                print("📱 Bildirim: Kredi kullanımı gerçekleşti.")
                islem_gecmisi += f"Kredi çekildi: +{kredi_tutar} TL | Kredi borcu: {kredi_borcu} TL | Yeni bakiye: {bakiye} TL\n"

        # 10- KREDİ BORCU ÖDE
        case 10:
            print(f"Mevcut kredi borcunuz: {kredi_borcu} TL")
            print(f"Mevcut bakiyeniz: {bakiye} TL")

            if kredi_borcu <= 0:
                print("Ödenecek kredi borcu yok.")
            else:
                try:
                    odeme = int(input("Ödemek istediğiniz tutar: "))
                except ValueError:
                    print("Lütfen sayısal bir değer giriniz.")
                    continue

                if odeme <= 0:
                    print("Geçersiz tutar.")
                elif odeme > bakiye:
                    print("Bakiyeniz bu ödemeyi yapmaya yetmiyor.")
                elif odeme > kredi_borcu:
                    print("Borçtan fazla ödeme yapamazsınız.")
                else:
                    bakiye -= odeme
                    kredi_borcu -= odeme
                    print(f"{odeme} TL kredi borcu ödendi.")
                    print(f"Kalan kredi borcu = {kredi_borcu} TL")
                    print(f"Yeni bakiye = {bakiye} TL")
                    print("📱 Bildirim: Kredi borcu ödendi.")
                    islem_gecmisi += f"Kredi borcu ödemesi: -{odeme} TL | Kalan borç: {kredi_borcu} TL | Yeni bakiye: {bakiye} TL\n"

        # 11- KULLANICI ADI DEĞİŞTİR
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

        # 12- KART NUMARASI EKLE/DEĞİŞTİR
        case 12:
            yeni_kart = input("Kart numaranızı giriniz (sadece rakam, boşluk yok): ")
            if yeni_kart == "":
                print("Kart numarası boş olamaz.")
            elif len(yeni_kart) < 8:
                print("Kart numarası çok kısa.")
            elif not yeni_kart.isdigit():
                print("Kart numarası sadece rakamlardan oluşmalıdır.")
            else:
                kart_numarasi = yeni_kart
                print("Kart numarası başarıyla kaydedildi/değiştirildi.")
                islem_gecmisi += "Kart numarası güncellendi.\n"

        # 13- GÜN SONU RAPORU + GÜN ARTIR
        case 13:
            print("\n===== GÜN SONU RAPORU =====")
            print(f"Hesap türü        : {hesap_turu}")
            print(f"Bakiyeniz         : {bakiye} TL")
            print(f"Kredi borcunuz    : {kredi_borcu} TL")
            print(f"Günlük limit      : {gunluk_cekim_limiti} TL")
            print(f"Bugün çekilen     : {bugun_cekilen} TL")
            print(f"Bugün yatırılan   : {bugun_yatirilan} TL")
            print(f"Dolar bakiyesi    : {dolar_bakiye} USD")
            print("\n--- İşlem Geçmişi ---")
            if islem_gecmisi == "":
                print("Bugün için kayıtlı işlem yok.")
            else:
                print(islem_gecmisi)
            print("===== RAPOR SONU =====")

            bugun_gun += 1
            if bugun_gun > 30:
                bugun_gun = 1
            bugun_cekilen = 0
            bugun_yatirilan = 0
            print(f"Yeni gün başladı. Bugün ayın {bugun_gun}. günü.")
            print("(Bugün çekilen/yatırılan sayaçları sıfırlandı.)")

        # 14- FATURA ÖDE
        case 14:
            print("\n--- Fatura Ödeme ---")
            print(f"1- Elektrik (Borc: {elektrik_borc} TL)")
            print(f"2- Su       (Borc: {su_borc} TL)")
            print(f"3- İnternet (Borc: {internet_borc} TL)")
            print(f"4- Doğalgaz (Borc: {dogalgaz_borc} TL)")
            alt_islem = input("Ödemek istediğiniz faturayı seçiniz (1-4): ")

            if alt_islem == "1":
                if elektrik_borc <= 0:
                    print("Elektrik faturanız yok.")
                elif bakiye < elektrik_borc:
                    print("Bakiyeniz faturayı ödemeye yetmiyor.")
                else:
                    bakiye -= elektrik_borc
                    print(f"Elektrik faturası ödendi. Tutar: {elektrik_borc} TL")
                    print("📱 Bildirim: Elektrik faturası ödendi.")
                    islem_gecmisi += f"Elektrik faturası ödendi: -{elektrik_borc} TL | Yeni bakiye: {bakiye} TL\n"
                    elektrik_borc = 0

            elif alt_islem == "2":
                if su_borc <= 0:
                    print("Su faturanız yok.")
                elif bakiye < su_borc:
                    print("Bakiyeniz faturayı ödemeye yetmiyor.")
                else:
                    bakiye -= su_borc
                    print(f"Su faturası ödendi. Tutar: {su_borc} TL")
                    print("📱 Bildirim: Su faturası ödendi.")
                    islem_gecmisi += f"Su faturası ödendi: -{su_borc} TL | Yeni bakiye: {bakiye} TL\n"
                    su_borc = 0

            elif alt_islem == "3":
                if internet_borc <= 0:
                    print("İnternet faturanız yok.")
                elif bakiye < internet_borc:
                    print("Bakiyeniz faturayı ödemeye yetmiyor.")
                else:
                    bakiye -= internet_borc
                    print(f"İnternet faturası ödendi. Tutar: {internet_borc} TL")
                    print("📱 Bildirim: İnternet faturası ödendi.")
                    islem_gecmisi += f"İnternet faturası ödendi: -{internet_borc} TL | Yeni bakiye: {bakiye} TL\n"
                    internet_borc = 0

            elif alt_islem == "4":
                if dogalgaz_borc <= 0:
                    print("Doğalgaz faturanız yok.")
                elif bakiye < dogalgaz_borc:
                    print("Bakiyeniz faturayı ödemeye yetmiyor.")
                else:
                    bakiye -= dogalgaz_borc
                    print(f"Doğalgaz faturası ödendi. Tutar: {dogalgaz_borc} TL")
                    print("📱 Bildirim: Doğalgaz faturası ödendi.")
                    islem_gecmisi += f"Doğalgaz faturası ödendi: -{dogalgaz_borc} TL | Yeni bakiye: {bakiye} TL\n"
                    dogalgaz_borc = 0
            else:
                print("Geçersiz seçim.")

        # 15- DÖVİZ İŞLEMLERİ
        case 15:
            print("\n--- Döviz İşlemleri (USD) ---")
            print(f"Mevcut dolar bakiyeniz: {dolar_bakiye} USD")
            print(f"Güncel kur: 1 USD = {dolar_kuru} TL")
            print("1- Dolar Al")
            print("2- Dolar Bozdur")
            alt_islem = input("Seçiminiz (1/2): ")

            if alt_islem == "1":
                try:
                    tutar_usd = float(input("Alınacak dolar miktarı (USD): "))
                except ValueError:
                    print("Lütfen sayısal bir değer giriniz.")
                    continue

                if tutar_usd <= 0:
                    print("Geçersiz miktar.")
                else:
                    gereken_tl = tutar_usd * dolar_kuru
                    if gereken_tl > bakiye:
                        print("Yetersiz bakiye.")
                    else:
                        bakiye -= gereken_tl
                        dolar_bakiye += tutar_usd
                        print(f"{tutar_usd} USD satın alındı. Ödenen: {gereken_tl} TL")
                        print(f"Yeni TL bakiyesi: {bakiye} TL, yeni USD bakiyesi: {dolar_bakiye} USD")
                        print("📱 Bildirim: Döviz alım işlemi gerçekleşti.")
                        islem_gecmisi += f"Döviz alım: -{gereken_tl} TL, +{tutar_usd} USD | TL bakiyesi: {bakiye} TL\n"

            elif alt_islem == "2":
                try:
                    tutar_usd = float(input("Bozdurulacak dolar miktarı (USD): "))
                except ValueError:
                    print("Lütfen sayısal bir değer giriniz.")
                    continue

                if tutar_usd <= 0:
                    print("Geçersiz miktar.")
                elif tutar_usd > dolar_bakiye:
                    print("Yetersiz dolar bakiyesi.")
                else:
                    alinacak_tl = tutar_usd * dolar_kuru
                    dolar_bakiye -= tutar_usd
                    bakiye += alinacak_tl
                    print(f"{tutar_usd} USD bozduruldu. Alınan: {alinacak_tl} TL")
                    print(f"Yeni TL bakiyesi: {bakiye} TL, yeni USD bakiyesi: {dolar_bakiye} USD")
                    print("📱 Bildirim: Döviz bozdurma işlemi gerçekleşti.")
                    islem_gecmisi += f"Döviz bozdurma: +{alinacak_tl} TL, -{tutar_usd} USD | TL bakiyesi: {bakiye} TL\n"
            else:
                print("Geçersiz seçim.")

        # 16- HAVALE / EFT
        case 16:
            print("\n--- Havale / EFT ---")
            print(f"Alıcı: {diger_hesap_adi}")
            print(f"Alıcının mevcut bakiyesi (simülasyon): {diger_hesap_bakiye} TL")
            try:
                gonderilecek = int(input("Gönderilecek tutar: "))
            except ValueError:
                print("Lütfen sayısal bir değer giriniz.")
                continue

            if gonderilecek <= 0:
                print("Geçersiz tutar.")
            else:
                toplam_tutar = gonderilecek + havale_ucreti
                if toplam_tutar > bakiye:
                    print("Bakiyeniz, havale tutarı ve işlem ücretini karşılamıyor.")
                else:
                    bakiye -= toplam_tutar
                    diger_hesap_bakiye += gonderilecek
                    print(f"{diger_hesap_adi} hesabına {gonderilecek} TL gönderildi.")
                    print(f"İşlem ücreti: {havale_ucreti} TL, yeni bakiyeniz: {bakiye} TL")
                    print("📱 Bildirim: Havale/EFT işlemi gerçekleşti.")
                    islem_gecmisi += f"Havale/EFT: -{gonderilecek} TL (Ücret: {havale_ucreti} TL) | Yeni bakiye: {bakiye} TL\n"

        # 17- ÇEK KIRMA
        case 17:
            print("\n--- Çek Kırma ---")
            print("Banka komisyonu: %3")
            try:
                cek_tutari = int(input("Çek tutarını giriniz: "))
            except ValueError:
                print("Lütfen sayısal bir değer giriniz.")
                continue

            if cek_tutari <= 0:
                print("Geçersiz tutar.")
            else:
                komisyon = cek_tutari * 0.03
                net_tutar = cek_tutari - komisyon
                bakiye += net_tutar
                print(f"{cek_tutari} TL tutarındaki çek kırıldı.")
                print(f"Kesilen komisyon: {komisyon} TL, hesaba geçen: {net_tutar} TL")
                print(f"Yeni bakiyeniz: {bakiye} TL")
                print("📱 Bildirim: Çek kırma işlemi gerçekleşti.")
                islem_gecmisi += f"Çek kırma: +{net_tutar} TL (Komisyon: {komisyon} TL) | Yeni bakiye: {bakiye} TL\n"

        # 18- KARTLA ÖDEME
        case 18:
            if kart_numarasi == "":
                print("Kart numarası tanımlı değil, önce kart ekleyiniz.")
            else:
                print("\n--- Kartla Ödeme ---")
                try:
                    tutar = int(input("Ödeme tutarı: "))
                except ValueError:
                    print("Lütfen sayısal bir değer giriniz.")
                    continue

                if tutar <= 0:
                    print("Geçersiz tutar.")
                else:
                    secim = input("Temassız ödeme mi? (E/H): ")
                    if secim.upper() == "E":
                        if tutar > temassiz_limit:
                            print(f"Temassız limit aşıldı. Limit: {temassiz_limit} TL")
                        elif tutar > bakiye:
                            print("Yetersiz bakiye.")
                        else:
                            bakiye -= tutar
                            print(f"Temassız olarak {tutar} TL ödendi.")
                            print(f"Kalan bakiye: {bakiye} TL")
                            print("📱 Bildirim: Kartınızla temassız ödeme yapıldı.")
                            islem_gecmisi += f"Temassız kart ödemesi: -{tutar} TL | Yeni bakiye: {bakiye} TL\n"
                    else:
                        if tutar > bakiye:
                            print("Yetersiz bakiye.")
                        else:
                            bakiye -= tutar
                            print(f"Şifreli (temaslı) olarak {tutar} TL ödendi.")
                            print(f"Kalan bakiye: {bakiye} TL")
                            print("📱 Bildirim: Kartınızla şifreli ödeme yapıldı.")
                            islem_gecmisi += f"Temaslı kart ödemesi: -{tutar} TL | Yeni bakiye: {bakiye} TL\n"

        # 19- QR İLE PARA ÇEKME
        case 19:
            print("\n--- QR ile Para Çekme ---")
            try:
                cek_tutar = int(input("Çekmek istediğiniz tutar: "))
            except ValueError:
                print("Lütfen sayısal bir değer giriniz.")
                continue

            if cek_tutar <= 0:
                print("Geçersiz tutar.")
            elif cek_tutar > bakiye:
                print("Yetersiz bakiye.")
            elif bugun_cekilen + cek_tutar > gunluk_cekim_limiti:
                kalan_limit = gunluk_cekim_limiti - bugun_cekilen
                print(f"Günlük çekim limitini aşıyorsunuz. Kalan limit = {kalan_limit} TL")
            else:
                qr_kodu = random.randint(100000, 999999)
                print(f"Oluşturulan QR kodu (simülasyon): {qr_kodu}")
                print("Diğer cihazınızda bu kodu okuttuğunuzu varsayalım.")
                try:
                    girilen_kod = int(input("ATM ekranına kodu tekrar giriniz: "))
                except ValueError:
                    print("Kod sayı olmalıdır, işlem iptal edildi.")
                    continue

                if girilen_kod == qr_kodu:
                    bakiye -= cek_tutar
                    bugun_cekilen += cek_tutar
                    print(f"QR ile {cek_tutar} TL çekildi. Yeni bakiye: {bakiye} TL")
                    print(f"Bugün toplam çektiğiniz: {bugun_cekilen} TL")
                    print("📱 Bildirim: QR kod ile para çekme işlemi yapıldı.")
                    islem_gecmisi += f"QR ile para çekme: -{cek_tutar} TL | Yeni bakiye: {bakiye} TL\n"
                else:
                    print("Kod eşleşmedi, işlem iptal edildi.")

        # 20- DİL DEĞİŞTİR
        case 20:
            print("\n--- Dil Değiştirme ---")
            print("1- Türkçe (TR)")
            print("2- English (EN)")
            sec = input("Seçiminiz: ")
            if sec == "1":
                dil = "TR"
                print("Dil Türkçe olarak ayarlandı.")
            elif sec == "2":
                dil = "EN"
                print("Language set to English.")
            else:
                print("Geçersiz seçim.")

        # 21- TEMA DEĞİŞTİR
        case 21:
            print("\n--- Tema Değiştirme ---")
            print("1- Aydınlık")
            print("2- Karanlık")
            sec = input("Seçiminiz: ")
            if sec == "1":
                tema = "Aydınlık"
                print("Tema Aydınlık olarak ayarlandı.")
            elif sec == "2":
                tema = "Karanlık"
                print("Tema Karanlık olarak ayarlandı.")
            else:
                print("Geçersiz seçim.")

        # 22- AY SONU FAİZİ UYGULA
        case 22:
            print("\n--- Ay Sonu Faiz İşlemi ---")
            if bugun_gun == 30:
                faiz_tutari = bakiye * faiz_orani
                bakiye += faiz_tutari
                print(f"Ay sonu faizi uygulandı. Eklenen faiz: {faiz_tutari} TL")
                print(f"Yeni bakiye: {bakiye} TL")
                print("📱 Bildirim: Ay sonu faizi hesabınıza işlendi.")
                islem_gecmisi += f"Ay sonu faizi: +{faiz_tutari} TL | Yeni bakiye: {bakiye} TL\n"
            else:
                print("Bugün ayın son günü değil. (Simülasyon: sadece gün=30 iken faiz uygular.)")

        # GEÇERSİZ İŞLEM
        case _:
            print("Geçersiz işlem, 1-22 arası bir değer giriniz.")