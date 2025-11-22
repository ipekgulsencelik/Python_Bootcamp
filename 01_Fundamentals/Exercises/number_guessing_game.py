# -------------------------------------------------------------
# SAYI TAHMİN OYUNU
# 0–50 / 0–100 / 0–200 aralığında rastgele sayı tutan,
# zorluk seçimi, hak sistemi, sıcak-soğuk ipucu,
# aralık daraltma modu, zaman ölçme, özel ipucu,
# dinamik puanlama, zorluk çarpanı, şans bonusu,
# eğlenceli yorumlar, en yüksek skor tutma ve
# hatalı girişlerde programın çökmeden çalışmaya devam etmesi.
# -------------------------------------------------------------

from random import randint  # Rastgele sayı üretmek için kullanılır
import time                # Zaman ölçmek için kullanılır

# Oyun başlangıç mesajı
print("=== SAYI TAHMİN OYUNUNA HOŞ GELDİN ===")

# Oyuncunun adını alıyoruz (ekranda daha samimi hitap için)
player_name = input("Önce seni tanıyalım, ismin nedir? : ")

# Oyun boyunca tutulacak: en yüksek skor ve en iyi (en kısa) süre
highest_score = 0   # Başlangıçta hiç skor yok, o yüzden 0
best_time = None    # Hiç oyun kazanılmadığı için süre bilinmiyor (None)

# Oyuncu çıkmak isteyene kadar oyun tekrar tekrar oynanabilir
while True:
    print("\n---------------------------------------")
    print(f"Hoş geldin {player_name}!")
    print(f"Şu anki en yüksek skorun: {highest_score}")

    # Eğer daha önce kazanılmış bir oyun varsa en iyi süreyi göster
    if best_time is not None:
        print(f"En hızlı bulduğun süre: {int(best_time)} saniye")

    print("---------------------------------------")

    # Kullanıcıdan zorluk seviyesi seçmesi istenir
    print("\nZorluk seçin:")
    print("1 - Kolay (0-50)  | Hak: 7 | Çarpan: 1.0")
    print("2 - Orta  (0-100) | Hak: 5 | Çarpan: 1.2")
    print("3 - Zor   (0-200) | Hak: 4 | Çarpan: 1.5")

    # Zorluk seçimi: burada hatalı girişler try-except ile yakalanır
    while True:
        difficulty_input = input("Seçiminiz: ").strip()  # Boşlukları temizle

        try:
            difficulty_choice = int(difficulty_input)    # Sayıya çevrilir

            # match-case ile seçilen zorluğa göre parametreler ayarlanır
            match difficulty_choice:
                case 1:
                    max_number = 50          # Rastgele sayının üst sınırı
                    lives = 7               # Tahmin hakkı
                    difficulty_name = "Kolay"
                    difficulty_multiplier = 1.0  # Skor çarpanı
                    break
                case 2:
                    max_number = 100
                    lives = 5
                    difficulty_name = "Orta"
                    difficulty_multiplier = 1.2
                    break
                case 3:
                    max_number = 200
                    lives = 4
                    difficulty_name = "Zor"
                    difficulty_multiplier = 1.5
                    break
                case _:
                    # 1, 2, 3 dışında bir değer girilirse uyar
                    print("Lütfen 1-2-3 girin.")
        except ValueError:
            # Sayıya çevrilemeyen girişler (harf vb.) buraya düşer
            print("Lütfen sadece sayı girin (1-2-3).")

    # Raporlamada kullanmak için başlangıç hak sayısını saklıyoruz
    starting_lives = lives

    # Aralık daraltma modu (sayı tahmini aralığını daraltan özellik)
    while True:
        range_mode_input = input("\nAralık daraltma modunu açmak ister misin? (e/h): ").lower().strip()

        # Kullanıcı aralık daraltma modunu açmak veya kapatmak ister
        match range_mode_input:
            case "e":
                range_shrink_enabled = True   # Aralık daraltma açık
                break
            case "h":
                range_shrink_enabled = False  # Aralık daraltma kapalı
                break
            case _:
                print("Lütfen sadece e veya h girin.")

    # Bilgisayarın tuttuğu rastgele sayı (0 ile max_number arasında)
    secret_number = randint(0, max_number)

    # Başlangıç puanı
    score = 100

    # Aralık daraltma modu için alt ve üst sınırlar
    lower_bound = 0
    upper_bound = max_number

    # Oyun içi durum değişkenleri
    won = False              # Oyuncu sayıyı buldu mu?
    special_hint_used = False  # Özel ipucu daha önce kullanıldı mı?
    special_hint_count = 0     # Kaç defa özel ipucu alındı
    bonus_life_given = False   # Şans bonusu daha önce verildi mi?

    print(f"\n➡ 0 ile {max_number} arasında bir sayı tuttum.")
    print(f"Zorluk: {difficulty_name}")
    print("Aralık daraltma modu:", "AÇIK" if range_shrink_enabled else "KAPALI")

    # Süre ölçümü için başlangıç zamanı
    start_time = time.time()

    # Tahmin döngüsü: haklar bitene kadar devam eder
    while lives > 0:
        try:
            guess = int(input(f"\nTahmininiz (Kalan hak: {lives}): "))
        except ValueError:
            # Sayıya çevrilemeyen girişlerde kullanıcı uyarılır, hak düşmez
            print("❗ Lütfen sadece tam sayı girin. Hak kaybı yok.")
            continue

        # Tahmin geçerli aralıkta mı kontrol edilir
        if guess < 0 or guess > max_number:
            print(f"Lütfen 0 ile {max_number} arasında bir değer girin. Hak kaybı yok.")
            continue

        # Tahmin ile tutulan sayı arasındaki fark
        difference = abs(secret_number - guess)

        # Fark sıfırsa doğru tahmin yapılmıştır
        if difference == 0:
            total_time = time.time() - start_time  # Geçen süre hesaplanır
            print("\n🎉 TAM İSABET! SAYIYI BULDUN!")
            print(f"Bulma süren: {int(total_time)} saniye")
            won = True
            break  # Tahmin döngüsünden çık

        # Yanlış tahminde hak bir azaltılır
        lives -= 1

        # Farka göre sıcaklık durumu ve puan cezası belirlenir
        match difference:
            case d if d <= 20:
                temp_status = "🔥 ÇOK SICAK"
                penalty = 5
                temp_comment = "Bir tık daha oynasan bulacaksın!"
            case d if d <= 40:
                temp_status = "🌡 SICAK"
                penalty = 10
                temp_comment = "Yaklaştın, devam!"
            case d if d <= 60:
                temp_status = "🙂 ORTALAMA"
                penalty = 15
                temp_comment = "Ne uzak ne yakın."
            case d if d <= 100:
                temp_status = "❄️ SOĞUK"
                penalty = 20
                temp_comment = "Biraz uzaklaştın."
            case _:
                temp_status = "🥶 ÇOK SOĞUK"
                penalty = 25
                temp_comment = "Bu tahminle kutuplara gittin. 😂"

        # Puan, ceza kadar düşürülür (minimum 0)
        score -= penalty
        if score < 0:
            score = 0

        # Tahmin tutulan sayıdan büyükse:
        if guess > secret_number:
            hint = "Daha küçük bir sayı dene."
            # Aralık daraltma açık ise üst sınır, tahmine çekilir
            if range_shrink_enabled and guess < upper_bound:
                upper_bound = guess
        else:
            # Tahmin tutulan sayıdan küçükse:
            hint = "Daha büyük bir sayı dene."
            # Aralık daraltma açık ise alt sınır, tahmine çekilir
            if range_shrink_enabled and guess > lower_bound:
                lower_bound = guess

        # Kullanıcıya genel geri bildirimler yazdırılır
        print(f"Yanlış tahmin! {temp_status}")
        print(f"Yorum: {temp_comment}")
        print(f"İpucu: {hint}")

        # Aralık daraltma aktifse güncel tahmin aralığı gösterilir
        if range_shrink_enabled:
            print(f"Sayı şu aralıkta olabilir: {lower_bound} - {upper_bound}")

        # Şans bonusu: henüz verilmediyse ve hak > 0 ise çalışabilir
        if not bonus_life_given and lives > 0:
            # %15 ihtimalle +1 ekstra hak verilir
            if randint(1, 100) <= 15:
                lives += 1
                bonus_life_given = True  # Bir daha bonus verilmemesi için
                print("🎁 Şans senden yana! +1 ekstra hak kazandın!")

        # Özel ipucu daha önce kullanılmadıysa ve hak varsa sorulur
        if not special_hint_used and lives > 0:
            while True:
                special_input = input("Özel ipucu ister misin? (e/h): ").lower().strip()

                # Özel ipucu için geçerli giriş kontrolü
                match special_input:
                    case "e":
                        break
                    case "h":
                        break
                    case _:
                        print("Lütfen sadece e veya h girin.")

            # Oyuncu özel ipucunu kullanmak isterse
            if special_input == "e":
                special_hint_used = True
                special_hint_count += 1  # Kaç defa özel ipucu kullanıldığını say
                hint_type = randint(1, 3)  # 1–3 arası rastgele ipucu tipi

                # Farklı özel ipucu türleri
                match hint_type:
                    case 1:
                        # Sayının tek mi çift mi olduğuna dair ipucu
                        print("Özel ipucu: Sayı TEK." if secret_number % 2 else "Özel ipucu: Sayı ÇİFT.")
                    case 2:
                        # Sayı aralığın alt yarısında mı üst yarısında mı?
                        print("Özel ipucu: Sayı ALT yarıda." if secret_number < max_number/2 else "Özel ipucu: Sayı ÜST yarıda.")
                    case 3:
                        # Sayının son rakamı hakkında ipucu
                        print("Özel ipucu: Son rakam 0–4." if secret_number % 10 < 5 else "Özel ipucu: Son rakam 5–9.")

    # Tahmin döngüsü bittikten sonra geçen toplam süre hesaplanır
    total_time = time.time() - start_time

    # Oyuncu sayıyı bulduysa skor çarpanla çarpılır, yoksa skor 0 yapılır
    if won:
        score = int(score * difficulty_multiplier)
    else:
        print("\n❌ Hakkınız bitti, kaybettiniz.")
        print(f"Tutulan sayı: {secret_number}")
        score = 0

    # Zaman bonusu: daha kısa sürede bulan daha fazla bonus alır
    if won:
        if total_time <= 15:
            score += 20
            time_comment = "+20 hızlı bonus ⚡"
        elif total_time <= 30:
            score += 10
            time_comment = "+10 iyi hız 🙌"
        elif total_time <= 60:
            score += 5
            time_comment = "+5 fena değil 🙂"
        else:
            time_comment = "Zaman bonusu yok 🐢"
    else:
        time_comment = "Bonus yok (bulamadın)"

    # En yüksek skor güncellenir
    if score > highest_score:
        highest_score = score
        score_comment = "🏆 Yeni en yüksek skor!"
    else:
        score_comment = "En yüksek skoru geçemedin."

    # En iyi (en kısa) süre güncellenir
    if won:
        if best_time is None or total_time < best_time:
            best_time = total_time
            time_record_comment = "⏱ Yeni hız rekoru!"
        else:
            time_record_comment = "Hız rekorunu geçemedin."
    else:
        time_record_comment = "Süre rekoru için sayıyı bulman gerek."

    # Kullanılan hak sayısı hesaplanır
    used_lives = starting_lives - lives

    # Oyun özeti ekrana yazdırılır
    print("\n=== OYUN ÖZETİ ===")
    print(f"Oyuncu            : {player_name}")
    print(f"Zorluk            : {difficulty_name}")
    print(f"Başlangıç hakkı   : {starting_lives}")
    print(f"Kullanılan hak    : {used_lives}")
    print(f"Özel ipucu        : {special_hint_count} kez")
    print(f"Şans bonusu       : {'Evet' if bonus_life_given else 'Hayır'}")
    print(f"Süre              : {int(total_time)} saniye")
    print(f"Skor              : {score}")
    print(score_comment)
    print(time_comment)
    print(time_record_comment)
    print(f"Genel en yüksek skor : {highest_score}")
    if best_time is not None:
        print(f"En iyi süre          : {int(best_time)} saniye")

    # Oyuncuya tekrar oynamak isteyip istemediği sorulur
    while True:
        play_again = input("\nTekrar oynamak ister misiniz? (e/h): ").lower().strip()

        match play_again:
            case "e":
                # Döngüden çık ve oyunu başa sardır
                break
            case "h":
                # Oyunu tamamen bitir
                print("\n🎮 Oyun kapatıldı. Teşekkürler!")
                exit()
            case _:
                print("Lütfen sadece e veya h girin.")