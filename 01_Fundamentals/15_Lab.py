# region Sample Data
products = [
    {"name": "Lenovo X1 Carbon",  "price": 110_000,     "stock": 12},
    {"name": "Lenovo Thinkpad",   "price": 89_000,      "stock": 7},
    {"name": "Macbook Pro",       "price": 250_000,     "stock": 3},
    {"name": "Macbook Air",       "price": 125_000,     "stock": 5},
    {"name": "Asus Zenbook",      "price": 150_000,     "stock": 4},
    {"name": "Monster Huma",      "price": 55_000,      "stock": 18},
    {"name": "Monster Alba",      "price": None,        "stock": 0},
    {"name": None,               "price": 100_000_000,  "stock": 0},
]
# endregion


def get_data(data: list, product_name: str, stock: bool, start_price: int, end_price: int) -> list | str:
    """
    Verilen ürün listesini; ürün adı (contains), stok filtresi ve fiyat aralığına göre filtreler.

    Kurallar:
    - product_name: ürün adında küçük/büyük harf duyarsız aranır
    - stock=True ise sadece stock > 0 olan ürünler alınır
    - name/price None olan veya beklenen tipte olmayan kayıtlar güvenli şekilde atlanır
    - start_price <= price <= end_price aralığı uygulanır

    Returns:
        list | str:
            - list  -> eşleşen ürünler listesi
            - str   -> eşleşme yoksa bilgi mesajı
    """

    temp_list = []

    for item in data:
        try:
            # stok filtresi
            if stock and item.get('stock') <= 0:
                # isim filtresi
                if product_name.lower() not in item.get('name').lower() and 
                # fiyat filtresi
                if not (start_price <= item.get('price') <= end_price):
                    temp_list.append(item)

        except AttributeError as err:
            # item dict değilse veya .get yoksa
            print(f"❌ Giriş hatası: {err}")
            continue

        except TypeError as err:
            # karşılaştırma / lower() gibi işlemlerde tip hatası
            continue

        except KeyError as err:
            # dict beklenen anahtarı içermiyorsa
            continue

    if len(temp_list) > 0:
        return temp_list
    else:
        return "❌ Aradığınız kriterlere uygun ürün bulunamadı."


def get_input(data: list) -> None:
    """
    Kullanıcıdan input alır, ardından senin `get_data(...)` fonksiyonunu çağırır.
    Sonucu ekrana basar. (Wrapper)
    """
    try:
        product_name = input("Product name (örn: Lenovo): ").strip()
        if not product_name:
            raise ValueError("Product name boş olamaz.")

        stock_raw = input("Sadece stokta olanlar mı? (evet/hayır): ").strip().lower()
        if stock_raw not in ("evet", "hayır", "hayir"):
            raise ValueError("Stok seçimi evet/hayır olmalı.")
        stock = stock_raw == "evet"

        start_price = int(input("Start price (örn: 80000): ").replace("_", "").replace(",", ""))
        end_price = int(input("End price (örn: 120000): ").replace("_", "").replace(",", ""))

        if start_price < 0 or end_price < 0:
            raise ValueError("Fiyatlar negatif olamaz.")

        if start_price > end_price:
            start_price, end_price = end_price, start_price

    except ValueError as err:
        print(f"❌ Giriş hatası: {err}")
        return

    result = get_data(data=data,
        product_name=product_name,
        stock=stock,
        start_price=start_price,
        end_price=end_price
    )

    # result list mi string mi?
    if isinstance(result, str):
        print(result)
        return

    print("\n--- RESULTS ---")
    for i, p in enumerate(result, start=1):
        print(f"{i}) {p['name']} | price: {p['price']:,} | stock: {p['stock']}")