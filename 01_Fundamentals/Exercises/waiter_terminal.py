# -----------------------------------------------------------------------------
# GARSON TERMINALI UYGULAMASI
# Özellikler:
# - Masa numarası alma
# - Ürün ismi ile sipariş alma (çorba / kebap / salata / içecek)
# - Her ürün için adet sorulması
# - Her ürünün toplam adedini ve tutarını ayrı ayrı takip etme
# - Hesap istendiğinde:
#       * Her ürün için satır satır döküm
#       * İndirimsiz toplam
#       * İndirim oranı (%10 veya %0)
#       * İndirim tutarı
#       * İndirimli ara toplam
#       * KDV (%10)
#       * Servis ücreti (%5)
#       * Ödeme tipi (nakit / kart)
#       * Kartta %2 komisyon
#       * En çok sipariş edilen ürünü gösterme
# - 300 TL ve üzeri alışverişte %10 indirim
# - Hiç sipariş yoksa hesap kesilmemesi
# - Fonksiyon ve list kullanılmadan yazılmıştır.
# -----------------------------------------------------------------------------

print("=== GARSON TERMINALINE HOS GELDINIZ ===")

# Ürün fiyatları
soup_price = 50
kebab_price = 150
salad_price = 40
drink_price = 20

# Adet sayaçları
soup_qty = 0
kebab_qty = 0
salad_qty = 0
drink_qty = 0

# Sepet toplamı
total = 0

# Masa numarası alma
table = input("Please enter table number: ")

print("\n--- MENU ---")
print(f"Çorba   : {soup_price} TL")
print(f"Kebap   : {kebab_price} TL")
print(f"Salata  : {salad_price} TL")
print(f"İçecek  : {drink_price} TL")
print("------------------------------\n")
print(f"Taking orders for table {table}...\n")

try:
    while True:
        order = input("Ürün giriniz (Çorba/Kebap/Salata/İçecek) → 'hesap' ile bitir: ").lower()

        if order == "hesap":
            break

        match order:
            case "çorba" | "corba":
                qty = int(input("Kaç adet çorba?: "))
                if qty <= 0:
                    print("Adet geçerli değil.\n")
                    continue
                soup_qty += qty
                total += qty * soup_price
                print(f"{qty} adet çorba eklendi. Ara toplam: {total} TL\n")
            case "kebap":
                qty = int(input("Kaç adet kebap?: "))
                if qty <= 0:
                    print("Adet geçerli değil.\n")
                    continue
                kebab_qty += qty
                total += qty * kebab_price
                print(f"{qty} adet kebap eklendi. Ara toplam: {total} TL\n")
            case "salata":
                qty = int(input("Kaç adet salata?: "))
                if qty <= 0:
                    print("Adet geçerli değil.\n")
                    continue
                salad_qty += qty
                total += qty * salad_price
                print(f"{qty} adet salata eklendi. Ara toplam: {total} TL\n")
            case "içecek" | "icecek":
                qty = int(input("Kaç adet içecek?: "))
                if qty <= 0:
                    print("Adet geçerli değil.\n")
                    continue
                drink_qty += qty
                total += qty * drink_price
                print(f"{qty} adet içecek eklendi. Ara toplam: {total} TL\n")
            case _:
                print("Menüde böyle bir ürün yok.\n")
except Exception as err:
    print(f"Hata oluştu: {err}\nLütfen girdi formatını kontrol edin.")

# ---------------- HESAP DÖKÜMÜ ----------------

print("\n===== HESAP DÖKÜMÜ =====")
print(f"Masa: {table}\n")

# Hiç sipariş alınmamışsa hesap kesilmez
if total == 0:
    print("Bu masadan hiç sipariş alınmamış. Hesap çıkarılamaz.")
    print("İyi günler dileriz.\n")
else:
    # Ürün bazlı döküm
    if soup_qty > 0:
        print(f"Çorba  ({soup_qty} adet) → {soup_qty * soup_price} TL")
    if kebab_qty > 0:
        print(f"Kebap  ({kebab_qty} adet) → {kebab_qty * kebab_price} TL")
    if salad_qty > 0:
        print(f"Salata ({salad_qty} adet) → {salad_qty * salad_price} TL")
    if drink_qty > 0:
        print(f"İçecek ({drink_qty} adet) → {drink_qty * drink_price} TL")

    print("\n------------------------")
    print(f"İndirimsiz toplam: {total:.2f} TL")

    # İndirim hesaplama
    if total >= 300:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    discount_amount = total * discount_rate
    net_amount = total - discount_amount  # indirim sonrası

    # KDV ve servis ücreti
    kdv_rate = 0.10
    service_rate = 0.05

    kdv_amount = net_amount * kdv_rate
    service_amount = net_amount * service_rate

    grand_total = net_amount + kdv_amount + service_amount

    print(f"İndirim oranı       : %{discount_rate * 100:.0f}")
    print(f"İndirim tutarı      : {discount_amount:.2f} TL")
    print(f"İndirimli ara toplam: {net_amount:.2f} TL")
    print(f"KDV (%10)           : {kdv_amount:.2f} TL")
    print(f"Servis ücreti (%5)  : {service_amount:.2f} TL")

    # Ödeme tipi
    payment_type = ""
    while payment_type not in ["nakit", "kart"]:
        payment_type = input("Ödeme türü (nakit/kart): ").lower()
        if payment_type not in ["nakit", "kart"]:
            print("Geçersiz ödeme türü. Lütfen 'nakit' veya 'kart' giriniz.")

    card_commission = 0.0
    if payment_type == "kart":
        card_commission_rate = 0.02
        card_commission = grand_total * card_commission_rate
        grand_total += card_commission
        print(f"Kart komisyonu (%2) : {card_commission:.2f} TL")

    print(f"Ödeme tipi          : {payment_type.capitalize()}")
    print(f"Ödenecek net tutar  : {grand_total:.2f} TL")
    print("------------------------")

    # En çok sipariş edilen ürünü bulma
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
        print(f"En çok sipariş edilen ürün: {most_name} ({most_qty} adet)")

    print("Hesap çıkarıldı, iyi günler!\n")