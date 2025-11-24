# ================================================================
# ŞANSLI KOLTUKLU SİNEMA OTOMASYONU
# 
# Bu projede kullanılan temel Python konuları:
# - Değişkenler, veri tipleri (int, float, str, bool)
# - Karar yapıları: if / elif / else
# - Döngüler: for, while
# - Hata yakalama: try / except
# - Sayaç mantığı, birikimli toplama
# - Basit algoritma: asal sayı kontrolü, indirim hesaplama
# - Menü ve çok adımlı iş akışı tasarımı
# ================================================================

import time

# Gün sonu / yönetici için sayaçlar
genel_toplam_bilet_sayisi = 0
genel_toplam_sansli_koltuk = 0
genel_toplam_bilet_brut = 0.0
genel_toplam_bilet_net = 0.0
genel_toplam_bufe = 0.0
genel_musteri_sayisi = 0
toplam_memnuniyet_skoru = 0.0

# Satış numarası (işlem numarası)
satis_numarasi = 0

# Son satış bilgileri (iptal için)
son_satis_var = False
son_satis_bilet_sayisi = 0
son_satis_sansli_koltuk = 0
son_satis_bilet_brut = 0.0
son_satis_bilet_net = 0.0
son_satis_bufe = 0.0
son_satis_numarasi = 0

tries = 3

for attempt in range(1, tries + 1):
    kullanici_adi = "adal"
    sifre = "1234"

    girilen_kullanici = input("Kullanıcı adı: ")
    girilen_sifre = input("Şifre: ")

    if girilen_kullanici == kullanici_adi and girilen_sifre == sifre:
        print("\nGiriş Başarılı!\n")

        while True:
            print("\n===== ANA MENÜ =====")
            print("1 - Bilet Satın Al")
            print("2 - Gün Sonu Özeti (Yönetici)")
            print("3 - Son Satışı İptal Et (Yönetici)")
            print("4 - Çıkış")
            secim = input("Seçiminiz: ")

            # ------------------------------------------------------------
            # 1) BİLET SATIN AL
            # ------------------------------------------------------------
            if secim == "1":
                # Müşteri adı ve yaş bilgisi
                musteri_adi = input("Müşteri adı (isteğe bağlı, boş bırakabilirsiniz): ")
                try:
                    musteri_yasi = int(input("Müşteri yaşı: "))
                except:
                    print("Geçersiz yaş girdiniz, işlem iptal edildi.")
                    continue

                # Film seçimi
                print("\nFilm Seçiniz:")
                print("1 - Animasyon (Genel İzleyici)")
                print("2 - Aksiyon (+13)")
                print("3 - Korku (+18)")
                film_secim = input("Seçiminiz (1-3): ")

                film_adi = ""
                film_turu = ""
                film_sure = 0
                minimum_yas = 0

                if film_secim == "1":
                    film_adi = "Sevimli Canavarlar"
                    film_turu = "Animasyon"
                    film_sure = 90
                    minimum_yas = 0
                elif film_secim == "2":
                    film_adi = "Hızlı ve Öfkeli X"
                    film_turu = "Aksiyon"
                    film_sure = 120
                    minimum_yas = 13
                elif film_secim == "3":
                    film_adi = "Gece Kabusu"
                    film_turu = "Korku"
                    film_sure = 110
                    minimum_yas = 18
                else:
                    print("Geçersiz film seçimi, işlem iptal edildi.")
                    continue

                # Yaş kontrolü
                if musteri_yasi < minimum_yas:
                    print(f"\nBu film için yaş sınırı: {minimum_yas}+")
                    print("Yaşınız uygun olmadığı için bu filme bilet satışı yapılamıyor.\n")
                    continue

                # Seans saati
                seans_saati = input("Seans saati (örn: 19:00 / 21:30): ")

                # Bilet sayısı
                try:
                    bilet_adedi = int(input("Kaç adet bilet satın almak istiyorsunuz?: "))
                except:
                    print("Geçersiz değer girdiniz. İşlem iptal edildi.")
                    continue

                if bilet_adedi <= 0:
                    print("Bilet adedi pozitif olmalıdır!")
                    continue

                # Bilet adedine göre baz fiyat
                if bilet_adedi < 10:
                    baz_fiyat = 250
                elif 10 <= bilet_adedi <= 20:
                    baz_fiyat = 200
                else:
                    baz_fiyat = 150

                print(f"\nBaz bilet fiyatı (tip/salon hariç): {baz_fiyat} TL")

                # Bilet tipi
                print("\nBilet Tipi Seçiniz:")
                print("1 - Tam")
                print("2 - Öğrenci (%20 indirim)")
                print("3 - Çocuk (%30 indirim)")
                print("4 - 65+ (%25 indirim)")
                print("5 - Engelli (%40 indirim)")
                bilet_tipi = input("Seçiminiz (1-5): ")

                bilet_tip_indirim_orani = 0.0

                if bilet_tipi == "2":
                    bilet_tip_indirim_orani = 0.20
                elif bilet_tipi == "3":
                    bilet_tip_indirim_orani = 0.30
                elif bilet_tipi == "4":
                    bilet_tip_indirim_orani = 0.25
                elif bilet_tipi == "5":
                    bilet_tip_indirim_orani = 0.40

                # Salon türü
                print("\nSalon Türü Seçiniz:")
                print("1 - 2D (x1.0)")
                print("2 - 3D (x1.2)")
                print("3 - VIP (x1.5)")
                salon_turu = input("Seçiminiz (1-3): ")

                salon_carpan = 1.0
                if salon_turu == "2":
                    salon_carpan = 1.2
                elif salon_turu == "3":
                    salon_carpan = 1.5

                # Etkin birim bilet fiyatı
                etkin_birim_fiyat = baz_fiyat * salon_carpan * (1 - bilet_tip_indirim_orani)

                print(f"\nEtkin birim bilet fiyatı: {etkin_birim_fiyat} TL\n")

                # Sayaçlar
                bilet_brut_toplam = 0.0
                bilet_net_toplam = 0.0
                sansli_koltuk_sayisi = 0
                bonus_indirim = 0.0
                seans_indirimi = 0.0
                indirim_gunu_indirimi = 0.0

                # >5 bilet bonus indirimi
                if bilet_adedi > 5:
                    bonus_indirim = 20.0
                    print("🎁 Kampanya: 5'ten fazla bilet aldığınız için 20 TL bonus indirim uygulanacaktır.")

                # Her bilet için koltuk numarası al
                bilet_numara = 1
                while bilet_numara <= bilet_adedi:
                    try:
                        koltuk_no = int(input(f"{bilet_numara}. bilet için koltuk numarasını giriniz: "))
                    except:
                        print("Geçersiz koltuk numarası, tekrar deneyin.")
                        continue

                    # Koltuk bölge bilgisi
                    if 1 <= koltuk_no <= 20:
                        print("➡ Ön sıra bölgesinde bir koltuk seçtiniz.")
                    elif 21 <= koltuk_no <= 40:
                        print("➡ Orta alan bölgesinde bir koltuk seçtiniz.")
                    elif 41 <= koltuk_no <= 60:
                        print("➡ Arka sıra bölgesinde bir koltuk seçtiniz.")

                    # Erişilebilir / çıkışa yakın koltuklar (örnek: 5–10 arası)
                    if 5 <= koltuk_no <= 10:
                        print("♿ Bu koltuk, erişilebilir / çıkışa yakın alandadır.")

                    # Brüt toplam
                    bilet_brut_toplam += etkin_birim_fiyat

                    # Başlangıç fiyatı
                    fiyat = etkin_birim_fiyat

                    # 13 numaralı koltuk
                    if koltuk_no == 13:
                        print("⚠️ 13 numaralı koltuk seçildi → Uğursuz koltuk! Ek indirim uygulanmadı.")
                    else:
                        # Asal kontrolü
                        asal = True
                        if koltuk_no < 2:
                            asal = False
                        else:
                            bolen = 2
                            while bolen < koltuk_no:
                                if koltuk_no % bolen == 0:
                                    asal = False
                                    break
                                bolen += 1

                        if asal:
                            print(f"🍀 Şanslı Asal Koltuk! ({koltuk_no}) → %50 indirim uygulandı.")
                            fiyat = fiyat * 0.5
                            sansli_koltuk_sayisi += 1

                    bilet_net_toplam += fiyat
                    print(f"{bilet_numara}. bilet fiyatı: {fiyat} TL\n")

                    bilet_numara += 1

                # Seans indirimi
                if seans_saati == "21:30":
                    seans_indirimi = bilet_net_toplam * 0.10
                    bilet_net_toplam -= seans_indirimi
                    print("🌙 Gece Seansı Kampanyası: 21:30 seansı için %10 indirim uygulandı (bilet toplamına).")

                # Bonus indirimi
                bilet_net_toplam -= bonus_indirim

                # İndirim günü indirimi
                indirim_gunu_cevap = input("Bugün sinema indirim günü mü? (E/H): ")
                if indirim_gunu_cevap.upper() == "E":
                    indirim_gunu_indirimi = bilet_net_toplam * 0.10
                    bilet_net_toplam -= indirim_gunu_indirimi
                    print("🎉 İndirim Günü: Bilet toplamına ekstra %10 indirim uygulandı.")

                if bilet_net_toplam < 0:
                    bilet_net_toplam = 0.0

                # Bilet bazlı indirim toplamı
                toplam_bilet_indirimi = bilet_brut_toplam - bilet_net_toplam

                # Büfe (Mısır + İçecek)
                bufeye_istek = input("\nBüfeden mısır veya içecek ister misiniz? (E/H): ")
                bufeden_toplam = 0.0

                if bufeye_istek.upper() == "E":
                    print("\n--- Mısır ---")
                    print("1 - Küçük (40 TL)")
                    print("2 - Orta  (60 TL)")
                    print("3 - Büyük (80 TL)")
                    misir_secim = input("Mısır seçimi (1-3 veya boş bırak): ")

                    misir_fiyati = 0.0
                    if misir_secim == "1":
                        misir_fiyati = 40.0
                    elif misir_secim == "2":
                        misir_fiyati = 60.0
                    elif misir_secim == "3":
                        misir_fiyati = 80.0

                    bufeden_toplam += misir_fiyati

                    print("\n--- İçecek ---")
                    print("1 - Küçük (20 TL)")
                    print("2 - Orta  (30 TL)")
                    print("3 - Büyük (40 TL)")
                    icecek_secim = input("İçecek seçimi (1-3 veya boş bırak): ")

                    icecek_fiyati = 0.0
                    if icecek_secim == "1":
                        icecek_fiyati = 20.0
                    elif icecek_secim == "2":
                        icecek_fiyati = 30.0
                    elif icecek_secim == "3":
                        icecek_fiyati = 40.0

                    bufeden_toplam += icecek_fiyati

                # Bilet net + büfe toplamı
                genel_toplam = bilet_net_toplam + bufeden_toplam

                # Kupon kodu
                kupon_kodu = input("Kupon kodunuz varsa giriniz (yoksa Enter): ")
                kupon_indirimi = 0.0

                if kupon_kodu == "CODE10":
                    kupon_indirimi = genel_toplam * 0.10
                    genel_toplam -= kupon_indirimi
                    print("✅ CODE10 kuponu uygulandı: %10 indirim!")

                if genel_toplam < 0:
                    genel_toplam = 0.0

                # KDV / Hizmet bedeli (%10)
                kdv_orani = 0.10
                kdv_tutari = genel_toplam * kdv_orani
                genel_toplam_kdv_dahil = genel_toplam + kdv_tutari

                # Ödeme yöntemi
                print("\nÖdeme Yöntemi Seçiniz:")
                print("1 - Nakit")
                print("2 - Kredi Kartı")
                odeme_yontemi = input("Seçiminiz: ")

                taksit_sayisi = 1
                taksit_tutari = genel_toplam_kdv_dahil

                if odeme_yontemi == "2":
                    print("\nTaksit Sayısı Seçiniz:")
                    print("1 - Tek çekim")
                    print("2 - 2 Taksit")
                    print("3 - 3 Taksit")
                    secilen_taksit = input("Seçiminiz: ")

                    if secilen_taksit == "2":
                        taksit_sayisi = 2
                    elif secilen_taksit == "3":
                        taksit_sayisi = 3

                taksit_tutari = genel_toplam_kdv_dahil / taksit_sayisi

                # Müşteri memnuniyet anketi
                try:
                    memnuniyet = int(input("Salon genel memnuniyet (1-5 arası, boş bırakmak için 0): "))
                except:
                    memnuniyet = 0

                if 1 <= memnuniyet <= 5:
                    genel_musteri_sayisi += 1
                    toplam_memnuniyet_skoru += memnuniyet

                # Gün sonu sayaçlarını güncelle
                genel_toplam_bilet_sayisi += bilet_adedi
                genel_toplam_sansli_koltuk += sansli_koltuk_sayisi
                genel_toplam_bilet_brut += bilet_brut_toplam
                genel_toplam_bilet_net += bilet_net_toplam
                genel_toplam_bufe += bufeden_toplam

                # Satış numarası güncelle
                satis_numarasi += 1
                son_satis_numarasi = satis_numarasi

                # Son satış bilgilerini kaydet (iptal için)
                son_satis_var = True
                son_satis_bilet_sayisi = bilet_adedi
                son_satis_sansli_koltuk = sansli_koltuk_sayisi
                son_satis_bilet_brut = bilet_brut_toplam
                son_satis_bilet_net = bilet_net_toplam
                son_satis_bufe = bufeden_toplam

                # Ödeme özeti
                print("\n==================== ÖDEME ÖZETİ ====================")
                print(f"Satış No               : {satis_numarasi}")
                if musteri_adi != "":
                    print(f"Müşteri Adı            : {musteri_adi}")
                print(f"Müşteri Yaşı           : {musteri_yasi}")
                print(f"Film Adı               : {film_adi}")
                print(f"Film Türü              : {film_turu}")
                print(f"Film Süresi            : {film_sure} dk")
                print(f"Seans Saati            : {seans_saati}")
                print(f"Alınan Bilet Adedi     : {bilet_adedi}")
                print(f"Şanslı Koltuk Sayısı   : {sansli_koltuk_sayisi}")
                print("-----------------------------------------------------")
                print(f"Bilet Brüt Toplam      : {bilet_brut_toplam} TL")
                print(f"Bilet İndirimi         : {toplam_bilet_indirimi} TL")
                print(f"  - Bonus İndirim      : {bonus_indirim} TL")
                print(f"  - Seans İndirimi     : {seans_indirimi} TL")
                print(f"  - İndirim Günü İnd.  : {indirim_gunu_indirimi} TL")
                print(f"Bilet NET              : {bilet_net_toplam} TL")
                print(f"Büfe (mısır+içecek)    : {bufeden_toplam} TL")
                print(f"Kupon İndirimi         : {kupon_indirimi} TL")
                print(f"KDV Tutarı (%10)       : {kdv_tutari} TL")
                print("=====================================================")
                print(f"KDV Hariç Genel Tutar  : {genel_toplam} TL")
                print(f"KDV Dahil Genel Tutar  : {genel_toplam_kdv_dahil} TL")
                if odeme_yontemi == "2":
                    print("Ödeme Yöntemi          : Kredi Kartı")
                else:
                    print("Ödeme Yöntemi          : Nakit")
                print(f"Taksit Sayısı          : {taksit_sayisi}")
                print(f"Her Taksit Tutarı      : {taksit_tutari} TL")
                print("=====================================================\n")

            # ------------------------------------------------------------
            # 2) GÜN SONU ÖZETİ / YÖNETİCİ
            # ------------------------------------------------------------
            elif secim == "2":
                rapor_sifre = input("Yönetici rapor şifresini giriniz: ")
                if rapor_sifre != "admin123":
                    print("Yetkisiz giriş! Rapor görüntülenemiyor.")
                else:
                    print("\n********** GÜN SONU ÖZETİ / YÖNETİCİ RAPORU **********")
                    print(f"Toplam Satılan Bilet        : {genel_toplam_bilet_sayisi} adet")
                    print(f"Toplam Şanslı Koltuk        : {genel_toplam_sansli_koltuk} adet")
                    print("------------------------------------------------------")
                    print(f"Toplam Bilet Brüt Ciro      : {genel_toplam_bilet_brut} TL")
                    print(f"Toplam Bilet Net Ciro       : {genel_toplam_bilet_net} TL")
                    print(f"Toplam Büfe Cirosu          : {genel_toplam_bufe} TL")
                    print("------------------------------------------------------")
                    toplam_genel_ciro = genel_toplam_bilet_net + genel_toplam_bufe
                    print(f"GENEL TOPLAM CİRO (KDV HARİÇ): {toplam_genel_ciro} TL")
                    if genel_musteri_sayisi > 0:
                        ortalama_memnuniyet = toplam_memnuniyet_skoru / genel_musteri_sayisi
                        print(f"Ortalama Memnuniyet Skoru   : {ortalama_memnuniyet:.2f} / 5")
                    else:
                        print("Henüz memnuniyet verisi yok.")
                    print("********************************************************\n")

            # ------------------------------------------------------------
            # 3) SON SATIŞI İPTAL ET / YÖNETİCİ
            # ------------------------------------------------------------
            elif secim == "3":
                if not son_satis_var:
                    print("İptal edilecek bir satış kaydı bulunmuyor.")
                else:
                    iptal_sifre = input("Son satışı iptal etmek için yönetici şifresini giriniz: ")
                    if iptal_sifre != "admin123":
                        print("Yetkisiz giriş! İptal işlemi yapılamaz.")
                    else:
                        print(f"Satış No {son_satis_numarasi} iptal ediliyor...")

                        # Gün sonu sayaçlarından son satışı geri al
                        genel_toplam_bilet_sayisi -= son_satis_bilet_sayisi
                        genel_toplam_sansli_koltuk -= son_satis_sansli_koltuk
                        genel_toplam_bilet_brut -= son_satis_bilet_brut
                        genel_toplam_bilet_net -= son_satis_bilet_net
                        genel_toplam_bufe -= son_satis_bufe

                        # Negatiflere karşı koruma
                        if genel_toplam_bilet_sayisi < 0:
                            genel_toplam_bilet_sayisi = 0
                        if genel_toplam_sansli_koltuk < 0:
                            genel_toplam_sansli_koltuk = 0
                        if genel_toplam_bilet_brut < 0:
                            genel_toplam_bilet_brut = 0.0
                        if genel_toplam_bilet_net < 0:
                            genel_toplam_bilet_net = 0.0
                        if genel_toplam_bufe < 0:
                            genel_toplam_bufe = 0.0

                        son_satis_var = False
                        print("Son satış başarıyla iptal edilip raporlardan düşüldü.")

            # ------------------------------------------------------------
            # 4) ÇIKIŞ
            # ------------------------------------------------------------
            elif secim == "4":
                print("Program sonlandırılıyor...")
                raise SystemExit

            else:
                print("Geçersiz menü seçeneği!")

    else:
        kalan = tries - attempt
        print(f"Hatalı giriş. Kalan deneme hakkınız: {kalan}")
        if kalan == 0:
            print("Deneme hakkınız bitti. Bir süre sonra tekrar deneyiniz.")
            time.sleep(3)
            raise SystemExit