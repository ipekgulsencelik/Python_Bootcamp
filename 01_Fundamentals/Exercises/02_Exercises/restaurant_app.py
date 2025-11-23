import datetime

# -----------------------------------------------------------------------------
# GELİŞMİŞ GARSON TERMINALI UYGULAMASI  (LIST ve FONKSIYON YOK)
# -----------------------------------------------------------------------------
# Özellikler:
# - Garson adı
# - Günlük satış hedefi
# - Gün başı kasa tutarı, gün sonu gerçek kasa ve kasa uyumsuzluğu
# - Rezervasyon sistemi: rezerve <masa>, reziptal <masa>, durum (rezerve masalar)
# - Masa seçme, rezerve masaya oturtmama
# - Masa taşıma: masa degis <yeni_masa>
# - Ürünler: çorba, kebap, salata, içecek
# - Adetli sipariş
# - Hazırlanma süresi (dakika): çorba=3, kebap=15, salata=5, içecek=0
# - Mutfak / bar toplamları (mutfak: çorba, kebap, salata / bar: içecek)
# - son iptal → son siparişi siler
# - fis → ara fiş
# - stok yok <ürün> → o ürünü siparişe kapatır
# - indirim ogrenci / indirim sadakat / indirim dogum
# - 300+ toplamda %10 temel indirim
# - Toplam indirim oranı max %50
# - KDV %10, servis %5
# - Ödeme tipi: nakit / kart (kartta %2 komisyon)
# - Yuvarlama: 0.25 altı .00, 0.25–0.75 .50, 0.75 üstü bir üst tam
# - Sipariş notu: not: ...
# - En çok sipariş edilen ürünü gösterir
# - Masa oturma süresi (dakika)
# - Masa için tahmini hazırlık süresi
# - Servis memnuniyeti (1–5) ve gün sonu ortalama
# - Gün sonu raporu + log gösterimi
# -----------------------------------------------------------------------------

print("=== GARSON TERMINALINE HOS GELDINIZ ===")

garson_name = input("Garson adınızı giriniz: ")

# Günlük satış hedefi
target_str = input("Günlük satış hedefi (TL) (istemiyorsanız 0): ")
try:
    daily_target = float(target_str)
except:
    daily_target = 0.0

# Gün başı kasa
opening_cash_str = input("Kasa başlangıç tutarı (TL): ")
try:
    opening_cash = float(opening_cash_str)
except:
    opening_cash = 0.0

# Gün sonu istatistikleri
day_total_revenue = 0.0
day_table_count = 0
day_soup_qty = 0
day_kebab_qty = 0
day_salad_qty = 0
day_drink_qty = 0

day_satisfaction_total = 0.0
day_satisfaction_count = 0

# Ürün stok durumları
soup_available = True
kebab_available = True
salad_available = True
drink_available = True

# Rezerve masalar: ",3,5,7," gibi tutulur
reserved_tables = ","

# Basit log metni
log_text = ""

print("\nRestoran sistemi hazır.")
print("Masa seçmeden önce kullanılabilecek komutlar:")
print("- rezerve <masa_no>   → Masa rezerve et")
print("- reziptal <masa_no>  → Rezervasyon iptal et")
print("- durum               → Rezerve masaları göster")
print("- q                   → Programı kapat\n")

while True:
    table_input = input("Masa numarası giriniz (veya komut: rezerve/reziptal/durum/q): ").lower().strip()

    # Çıkış
    if table_input == "q":
        break

    # Rezerve masaları göster
    if table_input == "durum":
        if reserved_tables == ",":
            print("Hiç rezerve masa yok.\n")
        else:
            reserved_view = reserved_tables[1:len(reserved_tables) - 1]
            print("Rezerve masalar: " + reserved_view + "\n")
        continue

    # Masa rezerve etme
    if table_input.startswith("rezerve"):
        space_index = table_input.find(" ")
        if space_index != -1:
            masa_no = table_input[space_index + 1:].strip()
            if masa_no != "":
                tag = "," + masa_no + ","
                if tag in reserved_tables:
                    print(masa_no + " numaralı masa zaten rezerve.\n")
                else:
                    reserved_tables = reserved_tables + masa_no + ","
                    print(masa_no + " numaralı masa rezerve edildi.\n")
                    log_text = log_text + "[LOG] Masa " + masa_no + " rezerve edildi.\n"
            else:
                print("Kullanım: rezerve <masa_no>\n")
        else:
            print("Kullanım: rezerve <masa_no>\n")
        continue

    # Rezervasyon iptal
    if table_input.startswith("reziptal"):
        space_index = table_input.find(" ")
        if space_index != -1:
            masa_no = table_input[space_index + 1:].strip()
            if masa_no != "":
                tag = "," + masa_no + ","
                if tag in reserved_tables:
                    reserved_tables = reserved_tables.replace(tag, ",")
                    print(masa_no + " numaralı masanın rezervasyonu iptal edildi.\n")
                    log_text = log_text + "[LOG] Masa " + masa_no + " rezervasyonu iptal edildi.\n"
                else:
                    print(masa_no + " numaralı masa rezerve değil.\n")
            else:
                print("Kullanım: reziptal <masa_no>\n")
        else:
            print("Kullanım: reziptal <masa_no>\n")
        continue

    # Buraya geldiysek girilen şey masa numarasıdır
    table = table_input

    # Rezerve masaya oturtma engeli
    if ("," + table + ",") in reserved_tables:
        print(table + " numaralı masa rezerve. Önce rezervasyonu iptal edin ya da başka masa seçin.\n")
        continue

    if table.strip() == "":
        print("Geçerli bir masa numarası giriniz.\n")
        continue

    print("\nMasa " + table + " için sipariş alınıyor...")
    day_table_count = day_table_count + 1
    log_text = log_text + "[LOG] Masa " + table + " açıldı.\n"

    # Fiyatlar
    soup_price = 50
    kebab_price = 150
    salad_price = 40
    drink_price = 20

    # Hazırlama süreleri (dakika)
    prep_soup = 3
    prep_kebab = 15
    prep_salad = 5
    prep_drink = 0

    # Bu masa için adetler
    soup_qty = 0
    kebab_qty = 0
    salad_qty = 0
    drink_qty = 0

    # Toplamlar
    total = 0.0          # indirimsiz toplam
    kitchen_total = 0.0  # çorba + kebap + salata
    bar_total = 0.0      # içecek
    prep_total_minutes = 0  # hazırlık süresi toplamı

    # Son sipariş bilgisi
    last_item_name = ""
    last_item_qty = 0
    last_item_total = 0.0

    # Ekstra indirim
    extra_discount_rate = 0.0
    extra_discount_name = "Yok"

    # Not
    order_note = ""

    # Masa açılış zamanı
    open_time = datetime.datetime.now()

    # Menü gösterimi
    print("\n--- MENU ---")
    if soup_available:
        print("Çorba   : " + str(soup_price) + " TL")
    else:
        print("Çorba   : STOK YOK")
    if kebab_available:
        print("Kebap   : " + str(kebab_price) + " TL")
    else:
        print("Kebap   : STOK YOK")
    if salad_available:
        print("Salata  : " + str(salad_price) + " TL")
    else:
        print("Salata  : STOK YOK")
    if drink_available:
        print("İçecek  : " + str(drink_price) + " TL")
    else:
        print("İçecek  : STOK YOK")
    print("------------------------------\n")

    print("Masa içi komutlar:")
    print("- Ürün: çorba, kebap, salata, içecek")
    print("- 'hesap'         → Hesap iste")
    print("- 'fis'           → Ara fiş")
    print("- 'son iptal'     → Son siparişi iptal et")
    print("- 'stok yok <ürün>' → Örn: stok yok kebap")
    print("- 'indirim ogrenci' / 'indirim sadakat' / 'indirim dogum'")
    print("- 'masa degis <yeni_masa>' → Masayı başka numaraya taşı")
    print("- 'not: ...'      → Sipariş notu ekle\n")

    try:
        while True:
            order = input("Sipariş / komut giriniz → ").lower().strip()

            # ---------------- MASA DEĞİŞTİR ----------------
            if order.startswith("masa degis"):
                prefix = "masa degis"
                new_table = order[len(prefix):].strip()
                if new_table != "":
                    print("Masa " + table + " → " + new_table + " olarak değiştirildi.\n")
                    log_text = log_text + "[LOG] Masa " + table + " yeni numara: " + new_table + "\n"
                    table = new_table
                else:
                    print("Kullanım: masa degis <yeni_masa>\n")
                continue

            # ---------------- HESAP ----------------
            if order == "hesap":
                log_text = log_text + "[LOG] Masa " + table + " için hesap istendi.\n"
                break

            # ---------------- ARA FİŞ ----------------
            if order == "fis" or order == "fiş":
                print("\n--- ARA FİŞ ---")
                print("Masa: " + table)
                if soup_qty > 0:
                    print("Çorba  (" + str(soup_qty) + " adet) → " + str(soup_qty * soup_price) + " TL")
                if kebab_qty > 0:
                    print("Kebap  (" + str(kebab_qty) + " adet) → " + str(kebab_qty * kebab_price) + " TL")
                if salad_qty > 0:
                    print("Salata (" + str(salad_qty) + " adet) → " + str(salad_qty * salad_price) + " TL")
                if drink_qty > 0:
                    print("İçecek (" + str(drink_qty) + " adet) → " + str(drink_qty * drink_price) + " TL")
                print("Mutfak toplam: " + format(kitchen_total, ".2f") + " TL")
                print("Bar toplam   : " + format(bar_total, ".2f") + " TL")
                print("İndirimsiz ara toplam: " + format(total, ".2f") + " TL")
                print("Tahmini hazırlık süresi: " + str(prep_total_minutes) + " dakika")
                print("--------------\n")
                continue

            # ---------------- SON İPTAL ----------------
            if order == "son iptal":
                if last_item_qty == 0 or last_item_total == 0.0:
                    print("İptal edilecek son bir sipariş yok.\n")
                else:
                    total = total - last_item_total
                    if last_item_name == "Çorba":
                        soup_qty = soup_qty - last_item_qty
                        kitchen_total = kitchen_total - last_item_total
                        prep_total_minutes = prep_total_minutes - last_item_qty * prep_soup
                    elif last_item_name == "Kebap":
                        kebab_qty = kebab_qty - last_item_qty
                        kitchen_total = kitchen_total - last_item_total
                        prep_total_minutes = prep_total_minutes - last_item_qty * prep_kebab
                    elif last_item_name == "Salata":
                        salad_qty = salad_qty - last_item_qty
                        kitchen_total = kitchen_total - last_item_total
                        prep_total_minutes = prep_total_minutes - last_item_qty * prep_salad
                    elif last_item_name == "İçecek":
                        drink_qty = drink_qty - last_item_qty
                        bar_total = bar_total - last_item_total
                        prep_total_minutes = prep_total_minutes - last_item_qty * prep_drink

                    print("Son sipariş (" + last_item_name + ", " + str(last_item_qty) + " adet) iptal edildi.")
                    print("Yeni ara toplam: " + format(total, ".2f") + " TL\n")

                    log_text = log_text + "[LOG] Masa " + table + " son sipariş iptal edildi.\n"

                    last_item_name = ""
                    last_item_qty = 0
                    last_item_total = 0.0
                continue

            # ---------------- STOK YOK <ÜRÜN> ----------------
            if order.startswith("stok yok"):
                product_name = order[len("stok yok"):].strip()
                if product_name == "çorba" or product_name == "corba":
                    soup_available = False
                    print("Çorba artık siparişe kapatıldı.\n")
                    log_text = log_text + "[LOG] Çorba stoktan çıkarıldı.\n"
                elif product_name == "kebap":
                    kebab_available = False
                    print("Kebap artık siparişe kapatıldı.\n")
                    log_text = log_text + "[LOG] Kebap stoktan çıkarıldı.\n"
                elif product_name == "salata":
                    salad_available = False
                    print("Salata artık siparişe kapatıldı.\n")
                    log_text = log_text + "[LOG] Salata stoktan çıkarıldı.\n"
                elif product_name == "içecek" or product_name == "icecek":
                    drink_available = False
                    print("İçecek artık siparişe kapatıldı.\n")
                    log_text = log_text + "[LOG] İçecek stoktan çıkarıldı.\n"
                else:
                    print("Stok kapatma için geçersiz ürün adı.\n")
                continue

            # ---------------- INDIRIM TURLERI ----------------
            if order.startswith("indirim"):
                disc_type = order[len("indirim"):].strip()
                if disc_type == "ogrenci" or disc_type == "öğrenci":
                    extra_discount_rate = 0.15
                    extra_discount_name = "Öğrenci indirimi (%15)"
                elif disc_type == "sadakat":
                    extra_discount_rate = 0.05
                    extra_discount_name = "Sadakat indirimi (%5)"
                elif disc_type == "dogum" or disc_type == "doğum":
                    extra_discount_rate = 0.20
                    extra_discount_name = "Doğum günü indirimi (%20)"
                else:
                    print("Bilinmeyen indirim türü. Geçerli türler: ogrenci, sadakat, dogum\n")
                    continue
                print("Uygulanacak ekstra indirim: " + extra_discount_name + "\n")
                log_text = log_text + "[LOG] Masa " + table + " için " + extra_discount_name + " ayarlandı.\n"
                continue

            # ---------------- NOT EKLEME ----------------
            if order.startswith("not"):
                colon_index = order.find(":")
                if colon_index != -1:
                    order_note = order[colon_index + 1:].strip()
                else:
                    order_note = order[3:].strip()
                print("Not kaydedildi: " + order_note + "\n")
                log_text = log_text + "[LOG] Masa " + table + " not: " + order_note + "\n"
                continue

            # ---------------- ÜRÜN SİPARİŞLERİ ----------------
            if order == "çorba" or order == "corba":
                if not soup_available:
                    print("Üzgünüz, çorba stokta yok.\n")
                    continue
                qty_str = input("Kaç adet çorba?: ")
                try:
                    qty = int(qty_str)
                except:
                    print("Adet geçerli değil.\n")
                    continue
                if qty <= 0:
                    print("Adet geçerli değil.\n")
                    continue
                soup_qty = soup_qty + qty
                line_total = qty * soup_price
                total = total + line_total
                kitchen_total = kitchen_total + line_total
                prep_total_minutes = prep_total_minutes + qty * prep_soup
                last_item_name = "Çorba"
                last_item_qty = qty
                last_item_total = line_total
                print(str(qty) + " adet çorba eklendi. Ara toplam: " + format(total, ".2f") + " TL\n")
                log_text = log_text + "[LOG] Masa " + table + " → " + str(qty) + " adet çorba eklendi.\n"

            elif order == "kebap":
                if not kebab_available:
                    print("Üzgünüz, kebap stokta yok.\n")
                    continue
                qty_str = input("Kaç adet kebap?: ")
                try:
                    qty = int(qty_str)
                except:
                    print("Adet geçerli değil.\n")
                    continue
                if qty <= 0:
                    print("Adet geçerli değil.\n")
                    continue
                kebab_qty = kebab_qty + qty
                line_total = qty * kebab_price
                total = total + line_total
                kitchen_total = kitchen_total + line_total
                prep_total_minutes = prep_total_minutes + qty * prep_kebab
                last_item_name = "Kebap"
                last_item_qty = qty
                last_item_total = line_total
                print(str(qty) + " adet kebap eklendi. Ara toplam: " + format(total, ".2f") + " TL\n")
                log_text = log_text + "[LOG] Masa " + table + " → " + str(qty) + " adet kebap eklendi.\n"

            elif order == "salata":
                if not salad_available:
                    print("Üzgünüz, salata stokta yok.\n")
                    continue
                qty_str = input("Kaç adet salata?: ")
                try:
                    qty = int(qty_str)
                except:
                    print("Adet geçerli değil.\n")
                    continue
                if qty <= 0:
                    print("Adet geçerli değil.\n")
                    continue
                salad_qty = salad_qty + qty
                line_total = qty * salad_price
                total = total + line_total
                kitchen_total = kitchen_total + line_total
                prep_total_minutes = prep_total_minutes + qty * prep_salad
                last_item_name = "Salata"
                last_item_qty = qty
                last_item_total = line_total
                print(str(qty) + " adet salata eklendi. Ara toplam: " + format(total, ".2f") + " TL\n")
                log_text = log_text + "[LOG] Masa " + table + " → " + str(qty) + " adet salata eklendi.\n"

            elif order == "içecek" or order == "icecek":
                if not drink_available:
                    print("Üzgünüz, içecek stokta yok.\n")
                    continue
                qty_str = input("Kaç adet içecek?: ")
                try:
                    qty = int(qty_str)
                except:
                    print("Adet geçerli değil.\n")
                    continue
                if qty <= 0:
                    print("Adet geçerli değil.\n")
                    continue
                drink_qty = drink_qty + qty
                line_total = qty * drink_price
                total = total + line_total
                bar_total = bar_total + line_total
                prep_total_minutes = prep_total_minutes + qty * prep_drink
                last_item_name = "İçecek"
                last_item_qty = qty
                last_item_total = line_total
                print(str(qty) + " adet içecek eklendi. Ara toplam: " + format(total, ".2f") + " TL\n")
                log_text = log_text + "[LOG] Masa " + table + " → " + str(qty) + " adet içecek eklendi.\n"

            else:
                print("Menüde böyle bir ürün veya komut yok.\n")

    except Exception as err:
        print("Hata oluştu: " + str(err) + "\nLütfen girdi formatını kontrol edin.")

    # ---------------- HESAP DÖKÜMÜ ----------------

    print("\n===== HESAP DÖKÜMÜ =====")
    print("Masa        : " + table)
    print("Garson      : " + garson_name)
    now_time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Hesap zamanı: " + now_time_str + "\n")

    if total == 0:
        print("Bu masadan hiç sipariş alınmamış. Hesap çıkarılamaz.")
        print("İyi günler dileriz.\n")
        continue

    if soup_qty > 0:
        print("Çorba  (" + str(soup_qty) + " adet) → " + str(soup_qty * soup_price) + " TL")
    if kebab_qty > 0:
        print("Kebap  (" + str(kebab_qty) + " adet) → " + str(kebab_qty * kebab_price) + " TL")
    if salad_qty > 0:
        print("Salata (" + str(salad_qty) + " adet) → " + str(salad_qty * salad_price) + " TL")
    if drink_qty > 0:
        print("İçecek (" + str(drink_qty) + " adet) → " + str(drink_qty * drink_price) + " TL")

    print("\nMutfak toplam: " + format(kitchen_total, ".2f") + " TL")
    print("Bar toplam   : " + format(bar_total, ".2f") + " TL")
    print("Tahmini hazırlık süresi: " + str(prep_total_minutes) + " dakika")

    # Masa oturma süresi
    close_time = datetime.datetime.now()
    duration_seconds = (close_time - open_time).total_seconds()
    duration_minutes = int(duration_seconds // 60)
    print("Masa oturma süresi: " + str(duration_minutes) + " dakika")

    if order_note != "":
        print("\nNot: " + order_note)

    print("\n------------------------")
    print("İndirimsiz toplam: " + format(total, ".2f") + " TL")

    # Ciroya bağlı temel indirim
    if total >= 300:
        base_discount_rate = 0.10
    else:
        base_discount_rate = 0.0

    total_discount_rate = base_discount_rate + extra_discount_rate
    if total_discount_rate > 0.5:
        total_discount_rate = 0.5  # max %50

    discount_amount = total * total_discount_rate
    net_amount = total - discount_amount

    print("Toplam indirim oranı : %" + str(int(total_discount_rate * 100)))
    print("Toplam indirim tutarı: " + format(discount_amount, ".2f") + " TL")
    print("İndirimli ara toplam : " + format(net_amount, ".2f") + " TL")

    # KDV + servis
    kdv_rate = 0.10
    service_rate = 0.05
    kdv_amount = net_amount * kdv_rate
    service_amount = net_amount * service_rate
    grand_total = net_amount + kdv_amount + service_amount

    print("KDV (%10)            : " + format(kdv_amount, ".2f") + " TL")
    print("Servis ücreti (%5)   : " + format(service_amount, ".2f") + " TL")

    # Ödeme tipi
    payment_type = ""
    while payment_type != "nakit" and payment_type != "kart":
        payment_type = input("Ödeme türü (nakit/kart): ").lower().strip()
        if payment_type != "nakit" and payment_type != "kart":
            print("Geçersiz ödeme türü. Lütfen 'nakit' veya 'kart' giriniz.")

    card_commission = 0.0
    if payment_type == "kart":
        card_commission_rate = 0.02
        card_commission = grand_total * card_commission_rate
        grand_total = grand_total + card_commission
        print("Kart komisyonu (%2)  : " + format(card_commission, ".2f") + " TL")

    # Yuvarlama
    lira = int(grand_total)
    kurus = grand_total - lira

    if kurus < 0.25:
        rounded_total = float(lira)
    elif kurus < 0.75:
        rounded_total = lira + 0.5
    else:
        rounded_total = float(lira + 1)

    print("\nHesap (yuvarlanmamış): " + format(grand_total, ".2f") + " TL")
    print("Yuvarlanmış ödeme    : " + format(rounded_total, ".2f") + " TL")
    print("Ödeme tipi           : " + payment_type.capitalize())
    print("------------------------")

    # Servis memnuniyeti
    satisfaction_str = input("Servis değerlendirmesi (1-5, boş geçerseniz sayılmaz): ").strip()
    if satisfaction_str != "":
        try:
            satisfaction = float(satisfaction_str)
            if satisfaction < 1:
                satisfaction = 1
            if satisfaction > 5:
                satisfaction = 5
            day_satisfaction_total = day_satisfaction_total + satisfaction
            day_satisfaction_count = day_satisfaction_count + 1
        except:
            pass

    # En çok sipariş edilen ürün
    most_name = "Yok"
    most_qty = 0

    if soup_qty > most_qty:
        most_qty = soup_qty
        most_name = "Çorba"
    if kebab_qty > most_qty:
        most_qty = kebab_qty
        most_name = "Kebap"
    if salad_qty > most_qty:
        most_qty = salad_qty
        most_name = "Salata"
    if drink_qty > most_qty:
        most_qty = drink_qty
        most_name = "İçecek"

    if most_qty > 0:
        print("En çok sipariş edilen ürün: " + most_name + " (" + str(most_qty) + " adet)")

    print("Hesap çıkarıldı, iyi günler!\n")

    # Gün sonu istatistiklerine ekle
    day_total_revenue = day_total_revenue + rounded_total
    day_soup_qty = day_soup_qty + soup_qty
    day_kebab_qty = day_kebab_qty + kebab_qty
    day_salad_qty = day_salad_qty + salad_qty
    day_drink_qty = day_drink_qty + drink_qty

    # Günlük hedefe göre durum
    if daily_target > 0:
        remaining = daily_target - day_total_revenue
        if remaining > 0:
            print("Günlük hedefe kalan: " + format(remaining, ".2f") + " TL\n")
        else:
            print("Günlük satış hedefi AŞILDI! (+"
                  + format(-remaining, ".2f") + " TL)\n")

# ---------------- GÜN SONU RAPORU ----------------

print("\n=== GÜN SONU RAPORU ===")
print("Garson       : " + garson_name)
print("Tarih        : " + datetime.datetime.now().strftime("%Y-%m-%d"))
print("Hizmet verilen masa sayısı: " + str(day_table_count))

if day_total_revenue == 0:
    print("Bugün hiç satış yapılmamış.")
else:
    print("Toplam ciro  : " + format(day_total_revenue, ".2f") + " TL")
    print("Toplam ürün adetleri:")
    print("- Çorba  : " + str(day_soup_qty) + " adet")
    print("- Kebap  : " + str(day_kebab_qty) + " adet")
    print("- Salata : " + str(day_salad_qty) + " adet")
    print("- İçecek : " + str(day_drink_qty) + " adet")

    if day_satisfaction_count > 0:
        avg_satisfaction = day_satisfaction_total / day_satisfaction_count
        print("Ortalama memnuniyet: " + format(avg_satisfaction, ".2f") + " / 5")

    if daily_target > 0:
        remaining_total = daily_target - day_total_revenue
        if remaining_total > 0:
            print("Günlük hedefe ulaşılamadı. Kalan: " + format(remaining_total, ".2f") + " TL")
        else:
            print("Günlük satış hedefi aşıldı! (+"
                  + format(-remaining_total, ".2f") + " TL)")

# Kasa kontrolü
print("\n--- KASA KONTROLÜ ---")
expected_cash = opening_cash + day_total_revenue
print("Beklenen kasa (başlangıç + ciro): " + format(expected_cash, ".2f") + " TL")
real_cash_str = input("Gün sonu gerçek kasa tutarını giriniz: ")
try:
    real_cash = float(real_cash_str)
except:
    real_cash = expected_cash

diff = real_cash - expected_cash
if diff == 0:
    print("Kasa tam, uyumsuzluk yok.")
elif diff > 0:
    print("Kasa FAZLASI: +" + format(diff, ".2f") + " TL")
else:
    print("Kasa EKSİĞİ: " + format(diff, ".2f") + " TL")

# Log gösterimi
print("\n--- GÜN İÇİ LOG KAYITLARI ---")
if log_text == "":
    print("Herhangi bir log kaydı yok.")
else:
    print(log_text)

print("Sistem kapatıldı. İyi çalışmalar!")