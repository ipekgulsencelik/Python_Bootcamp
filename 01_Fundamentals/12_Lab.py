
#! Dictionary (Sözlük)
# Sözlük (dictionary), Python’da:
#   - list, tuple gibi verileri RAM’de geçici olarak tuttuğumuz
#     ancak bunun yanında "anahtar → değer" mantığıyla çalışan
#     çok güçlü bir veri yapısıdır.

# Sözlük objesi , list, tuple gibi geçici olarak verileri depoladığımız bir başka yapımızdır.
# Sözlükler anahtar (key) ve değer (value) ikili mekanizması ile çalışırlar.
# Anahtarlar herhangi bir değere erişmek için kullanılmaktadırlar.

# Sözlükler:
#   ✔ “Key → Value” (Anahtar → Değer) mantığıyla çalışır.
#   ✔ Her key benzersizdir (unique) — aynı key’i tekrar eklersen, eski değeri ezersin.
#   ✔ Key’ler immutable (değiştirilemez) tipte olmalıdır:
#           str, int, float, tuple, frozenset, vs.
#      (list, dict, set gibi mutable tipler key olamaz.)
#   ✔ Value tarafında HER TÜRLÜ tip kullanılabilir:
#           int, float, str, list, dict, tuple, vs.

# ✔ Erişim HIZLIDIR:
#       - Ortalama erişim maliyeti: O(1) (hash tablosu kullanır)
#       - Yani yüzlerce / binlerce eleman olsa bile key ile erişim genellikle sabit zamanda gerçekleşir.

# ✔ Ne zaman dictionary kullanmalıyım?
#       - Bir şeyi ID / isim / kod ile eşlemek istiyorsan:
#           öğrenci_no → öğrenci_bilgisi
#           ürün_kodu → ürün_detayları
#           film_adı  → çıkış_yılı
#           kullanıcı_adı → profil_bilgisi
#       - Veriye pozisyonla (index) değil, "anlamlı bir anahtar" üzerinden erişmek istiyorsan.

# ✔ Diğer yapılarla farkı:
#       list     → index bazlı, sıralı, tekrar eden eleman olabilir
#       tuple    → list gibi ama immutable (değiştirilemez), daha hızlı ve güvenlidir.
#       set      → sırasız, unique elemanlardan oluşur, matematiksel kümeler için idealdir.
#       dict     → key → value eşleşmesi, en hızlı lookup

# ✔ Dictionary MUTABLE bir yapıdır:
#       - Yeni key ekleyebilirsin
#       - Var olan key'in değerini güncelleyebilirsin
#       - Key silebilirsin

# ✔ Sıra davranışı:
#       - Python 3.7+ itibarıyla dict, EKLEME SIRASINI korur.
#       - Ancak teorik olarak "sıralı veri yapısı" değildir.
#         Sıralama garantisi için list/tuple kullanılmalıdır.

# ✔ Bellek & Hash Tablosu:
#       - Her key için bir "hash" değeri hesaplanır.
#       - Bu hash, key’in tabloda nereye yerleşeceğini belirler.
#       - Bu sayede: user["name"]  gibi erişimler çok hızlıdır.


# Mini Cheatsheet — Dictionary Ne Zaman Kullanılmaz?
""" 
-------------------------------------------------------------------------------------------------------
| Kullanım Durumu                              | Dict Kullanma!                   | Doğru Yapı        |
|----------------------------------------------|----------------------------------|-------------------|
| Sıra önemliyse (1., 2., 3. eleman)           | Dict sıralı mantık için değildir | List / Tuple      |
| Aynı eleman birden fazla olabilir            | Dict → key'ler unique            | List              |
| Değerler sabit kalmalı (immutable veri)      | Dict mutable                     | Tuple / Frozenset |
| İndeks ile erişim gerekiyorsa                | dict[key] index değildir         | List / Tuple      |
| Sadece değer koleksiyonu gerekiyorsa         | gereksiz key israfı              | List / Set        |
| Matematiksel set işlemleri (union/intersect) | dict uygun değil                 | Set               |
| Sadece anahtar listesi tutulacaksa           | dict fazla maliyetli             | Set               |
| ÇOK büyük veri (milyonlarca entry)           | yüksek RAM maliyeti              | List / Tuple (*)  |
-------------------------------------------------------------------------------------------------------
 """


# Mini Cheatsheet — dict vs list vs tuple vs set
"""
-----------------------------------------------------------------------------------------------------------------------------------------------------
| Özellik / Yapı        | Dictionary (dict)           | List                     | Tuple                     | Set                                  |
| ----------------------| ----------------------------| ------------------------ | ------------------------- | ------------------------------------ |
| Temel yapı            | Key → Value eşleşmesi       | Sıralı eleman listesi    | Sıralı, immutable         | Unique eleman kümesi                 |
| Değiştirilebilir mi?  | Evet (mutable)              | Evet                     | Hayır                     | Evet                                 |
| Eleman sırası         | Korur (Py 3.7+)             | Korur                    | Korur                     | Koruma yok (unordered)               |
| Eleman tekrarı        | Value serbest               | Serbest                  | Serbest                   | Tekrara izin yok                     |
| Erişim yöntemi        | key ile                     | index ile                | index ile                 | index yok → “in”                     |
| Erişim hızı           | O(1) en hızlı               | O(1) index / O(n) search | O(1) index                | O(1) average                         |
| Kullanım amacı        | Veri eşleme, mapping        | Dinamik sıralı veri      | Sabit veri                | Kümeler, matematik işlemleri         |
| Mutable/Immutable     | Mutable                     | Mutable                  | Immutable                 | Mutable (elemanlar immutable olmalı) |
| Hashlenebilir mi?     | Keyler hashlenebilir olmalı | X                        | (tüm tuple hashlenebilir) | Elemanlar hashlenebilir              |
| Bellek kullanımı      | Orta / yüksek               | Orta                     | Düşük                     | Orta                                 |
| En iyi kullanım       | ID → bilgi eşleme           | Sık değişen veri         | Sabit, güvenli veri       | Unique data, hızlı arama             |
| JSON uyumluluğu       | Çok yüksek                  | Liste olarak             | Tuple → list olur         | Set → list olur                      |
| Sıralama desteği      | Doğrudan yok                | var                      | var                       | yok (önce listeye dönüştür)          |
-----------------------------------------------------------------------------------------------------------------------------------------------------
"""


# region Nested Dictionary 
# my_dict = {
#     'Full Name': 'Burak Yılmaz',
#     'Age': 34,
#     'Lig': ['Eşrefpaşaspor', 'Beşiktaş', 'Galatasaray', 'Göztepe', 'Adanaspor'],
#     'Notebook': ('Lenovo x1 Carbon', 49.000),
#     'Display Card': {
#         'Name': 'TI4090',
#         'Memory': {
#             'Memory Type': 'DDR4',
#             'Memory Capacity': '64GB'
#         }
#     }
# }
# endregion


#   SÖZLÜK METODLARI
#   .keys()     → Tüm anahtarlar
#   .values()   → Tüm değerler
#   .items()    → (key, value) çiftleri
#   .get(k, d)  → Hatasız okuma (yoksa default)
#   .update({...}) → Güncelleme / toplu ekleme
#   .pop(key)   → Key'i sil ve değerini döndür
#   .popitem()  → Son eklenen çifti sil ve döndür (LIFO)
#   .clear()    → Tüm içeriği sil

""" 
| Yapı            | Ne Döner?       | Açıklama                       | Örnek                |
| --------------- | --------------- | ------------------------------ | -------------------- |
| **dict**        | key → value     | Anahtar–değer yapısı           | `{'name': 'Ali'}`    |
| **key**         | Anahtar         | Değere ulaşmak için kullanılır | `'name'`             |
| **value**       | Değer           | Asıl veri                      | `'Ali'`              |
| **keys()**      | Tüm key’ler     | Sadece anahtarlar              | `dict.keys()`        |
| **values()**    | Tüm value’lar   | Sadece değerler                | `dict.values()`      |
| **items()**     | (key, value)    | Anahtar + değer birlikte       | `dict.items()`       |
| **get(key)**    | value / None    | Güvenli erişim                 | `dict.get('name')`   |
| **get(key, d)** | value / default | Yoksa varsayılan döner         | `dict.get('age', 0)` |
| **dict[key]**   | value           | Direkt erişim                  | `dict['name']`       |
| **in dict**     | True / False    | Key var mı kontrolü            | `'name' in dict`     |

"""

""" 
| Kullanım           | Key varsa | Key yoksa |
| ------------------ | --------- | --------- |
| dict[key]          |  value    |  KeyError |
| dict.get(key)      |  value    |  None     |
| dict.get(key, '-') |  value    |  -        | 
"""


# Mini Cheatsheet — Dictionary Performance Notes
"""
------------------------------------------------------------
| İşlem      | Ortalama Zaman | Açıklama                   |
|------------|----------------|----------------------------|
| Access     | O(1)           | Hash tablosu               |
| Insert     | O(1)           | Amortize sabit zaman       |
| Update     | O(1)           | Key varsa override         |
| Delete     | O(1)           | Hash tablodan çıkarma      |
| Search k   | O(1)           | 'in' ile key kontrol       |
| Search v   | O(n)           | Value taraması             |
------------------------------------------------------------
"""


# region Movie Release Years Dictionary
# release_year_movies = {
#     'Fight Club': 1999,
#     'Matrix': 1999,
#     'Interstaller': 2014,
#     'Inception':2010,
#     'Fringe': 2008,
#     'Dune': 2021
# }
# endregion


# region Read
# 'Fight Club' anahtarında tutulan değeri ekrana yazdıralım.

# Path - I → Köşeli parantez (KeyError atabilir)
# ✔ Köşeli parantez ([]) ile erişim:
#       release_year_movies['Fight Club']  → Key yoksa KeyError fırlatır.

# print(
#     release_year_movies['Fight Club']
# )

# Path - II → get() (Key bulunamazsa None döner, hata atmaz)
# ✔ .get(key, default=None) ile erişim:
#       release_year_movies.get('Fight Club')          → Key yoksa None döner.
#       release_year_movies.get('Fight Club', '-')     → Key yoksa "-" döner (default).

# print(
#     release_year_movies.get('Fight Club')
# )

# f-string ile formatlı çıktı
# print(f'Fringe Relase Year: {release_year_movies.get("Fringe")}')


# Get All Values
# print("\nAll Values:")
# for value in release_year_movies.values():
#     print(value)

# print(f'Movie Release Year: {release_year_movies.values()}')


# Get All Keys
# print("\nAll Keys:")
# for key in release_year_movies.keys():
#     print(key)

# print(f'Movie List: {release_year_movies.keys()}')


# Get All Items
# print("\nAll Items:")
# for key, value in release_year_movies.items():
#     print(
#         f'Movie Name: {key}\n'
#         f'Release Year: {value}'
#     )
# endregion


# region Pretty Printing with Dictionary Comprehension

# sözlüğün her bir elemanını 'name' ve 'year' döngüye gönderin.
# for name, year in release_year_movies.items():
#     print(f'Movie Name: {name} -- Release Year: {year}')

# from pprint import pprint

# Sözlüğü comprehension ile tekrar oluşturalım (örnek amaçlı)
# pprint({name: year for name, year in release_year_movies.items()})
# endregion


# region Create Item
# release_year_movies['Dune II'] = 2023
# print("After Create:", release_year_movies)
# endregion


# region Update Item
# release_year_movies.update({
#     'Dune II': 2024
# })
# print("After Update:", release_year_movies)
# endregion


# region Delete
# del release_year_movies['Dune II']
# print("After Delete:", release_year_movies)
# endregion


# products = [
#     {'name': 'Everlast Pro Boxing Gloves', 'price': 245},  # Buradaki her bir eleman bir product sözlüğüdür
#     {'name': 'Everlast Training Boxing Gloves', 'price': 145},
#     {'name': 'Everlast Heavy Bag', 'price': 345},
#     {'name': 'Everlast Hand-Wrap', 'price': 56},
#     {'name': 'Iphone 14 Pro Max', 'price': 44000},
#     {'name': 'Samsung G20', 'price': 13000},
#     {'name': 'Lenovo x1 Carbon', 'price': 49000},
# ] 

# region Products — Total Price of All Products
# products listesinde ki bütün ürünlerin fiyatlarını toplayın
# total_price = 0
# for product in products:
#     # product.get('price') → safety (key yoksa None dönebilir)
#     total_price += product.get('price')  # product['price'] da kullanılabilir.

# print(f'Total Price of Collection is {total_price}')
# # endregion


# region Products — Filter by Price (>= 30.000)
# products listesindeki ürün fiyatı 30.000'den büyük veya eşit olan ürünlerin isimlerini listeleyiniz.

# print("\nProducts with price >= 30000:")
# for product in products:
#     if product['price'] >= 30000:
#         print(product['name'])
# endregion


# region Products — Filter by Name + Price Range
# ürün adı içerisinde 'Everlast' geçen ve fiyat aralığı 150 ile 300 arasında olan ürünleri listelyiniz

# Çözüm yolu __contains__ ile
# print("\nEverlast products with 150 <= price <= 300 (using __contains__):")
# for product in products:
#     if product['name'].__contains__('Everlast') and 150 <= product['price'] <= 300:
#         pprint(product)

# Yukarıda kullandığımız __contains__ fonksiyonu string ifadelere uygulanan built-in bir fonksiyondur. 
# Çalışma mantığı:
#   fonksiyon içerisine parametre olarak gönderilen değer, uygulanılan string ifade içerisinde geçiyor mu?
#   geçmiyor mu diye kontrol ederek bize bool bir değer return eder. 
#   İlgili değeri içeriyorsa True içermiyorsa False döner.

# in ile çözümü
# ✔ 'key' in dict       → key var mı?
# ✔ DİKKAT: 'value' in dict ifadesi VALUE’ları değil KEY’leri kontrol eder.

# print("\nEverlast products with 150 <= price <= 300 (using 'in'):")
# for product in products:
#     if 'Everlast' in product['name'] and 150 <= product['price'] <= 300:
#         pprint(product)

# Not:
#   - 'Everlast' in product['name'] ifadesi, __contains__ ile aynı işi yapar
#   - Pythonic olan ve tercih edilmesi gereken kullanım → 'in'
# endregion


#! Dictionary Comprehension
# List Comprehension gibi sözlükler için de aynı yapı kullanılabilir.

# Format:
#       {key_expr : value_expr  for item in iterable}

# Avantajları:
#   ✔ Tek satırda güçlü sözlük oluşturma
#   ✔ Çok hızlı
#   ✔ Okunabilir
#   ✔ Veri dönüştürme işlemleri için ideal

""" 
| Yapı               | Sembol                 | Dönen |
| ------------------ | ---------------------- | ----- |
| List comprehension | [x for x in ...]       | Liste |
| Dict comprehension | {k: v for k, v in ...} | Dict  |
| Set comprehension  | {x for x in ...}       | Set   |

 """


# region Sample - Dictionary Comprehension

# from pprint import pprint

# numbers = [1, 2, 3, 4, 5]

# squares = {x: x * x for x in numbers}
# pprint({number: square for number, square in squares.items()})
# Sonuç:
#   {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# endregion


# region Product List
# products = [
#     {'name': 'Lenovo X1 Carbon', 'price': 110.000},
#     {'name': 'Lenovo Thinkpad',  'price': 89.000},
#     {'name': 'Macbook Pro',      'price': 250.000},
#     {'name': 'Macbook Air',      'price': 125.000},
#     {'name': 'Asus Zenbook',     'price': 150.000},
#     {'name': 'Monster Huma',     'price': 55.000},
#     {'name': 'Monster Alba'},               # price yok
#     {'price': 100.000},                     # name yok
# ]
# endregion


# region Path I — Total Price Calculation (loop)
#todo: products listesindeki tüm ürünlerin fiyatlarını toplayarak toplam fiyatı hesaplayınız.

# total_price = 0

# for product in products:    # Her product bir sözlüktür (dict)
#     total_price += product.get('price', 0)     # total_price = total_price + product.get('price', 0)
    
    # product.get('price', 0):
    #   - 'price' anahtarı varsa değerini alır
    #   - Yoksa 0 döner (KeyError oluşmasını engeller)

# print(f"Total Price: {total_price}")
# endregion


# region Path II — Total Price Calculation (sum + Generator Expression)
#todo: products listesindeki tüm ürünlerin fiyatlarını, sum() ve generator expression kullanarak hesaplayınız.

# NASIL ÇALIŞIR?
#   - (product.get('price', 0) for product in products)
#       → price değerlerini TEK TEK üreten bir generator oluşturur
#   - sum(...) bu değerleri toplayarak total_price değerini döndürür

# total_price = sum(product.get('price', 0) for product in products)

# print(f"Total Price: {total_price}")
# endregion


# region Filter Products — Price Greater Than Threshold
# TODO: products listesindeki ürünlerden, fiyatı 100.000'dan BÜYÜK olanları filtreleyiniz.

# Not:
#   - List comprehension kullanılır
#   - product.get('price', 0)
#       → 'price' anahtarı varsa değerini alır
#       → Yoksa 0 döner (KeyError oluşmasını engeller)

# price_threshold = 100.000   # → karşılaştırma değeri

# filtered_products = [product for product in products if product.get('price', 0) > price_threshold]

# for product in filtered_products:
#     print(
#         f"Product Name: {product.get('name', 'Unknown Product')}\n"
#         f"Price: {product.get('price', 'N/A')}\n"
#         "-----------------------------"
#     )
# endregion


# region Filter Products by Name & Price Range
# TODO: Ürün adı içerisinde "Lenovo" geçen VE fiyatı 100.000 ile 150.000 arasında olan ürünleri listeleyiniz.

# NOT:
#   - get() kullanımı KeyError riskini önler
#   - and operatörü ile tüm şartların aynı anda sağlanması beklenir

# name_kwd = 'Lenovo'
# min_price = 100.000
# max_price = 150.000

# filtered_products = [
#     product for product in products
#     if name_kwd in product.get('name', '') and
#     min_price < product.get('price', 0) < max_price
# ]

# for product in filtered_products:
#     print(
#         f"Product Name: {product.get('name', 'Unknown')}\n"
#         f"Price: {product.get('price', 'N/A')}\n"
#         "-----------------------------"
#     )
# endregion


# region uuid4
#   uuid4()  → rastgele UUID üretir (random).
#   - uuid.UUID tipinde bir nesne döndürür.
#   Her çağrıda farklı bir UUID üretir.
#   uuid4 → CRUD ve kullanıcı kayıtları için uygundur.

# GÜNLÜK HAYAT BENZETMESİ:
#   uuid4 = çekiliş numarası 🎟️
#   - Herkesin numarası farklıdır.
#   - Aynı numara tekrar üretilmez.

# from uuid import uuid4
# from pprint import pprint

# Her çağrıda farklı bir UUID üretir.
# uuid4_1 = uuid4()
# uuid4_2 = uuid4()

# print("uuid4 Demo")
# print("uuid4 1:", uuid4_1)
# print("uuid4 2:", uuid4_2)
# print("Same?:", uuid4_1 == uuid4_2)   # False → her zaman farklı
# print("Type :", type(uuid4_1))    # <class 'uuid.UUID'>

# uuid4() bir UUID objesi döndürür.
# CRUD uygulamalarında genelde string'e çevrilerek kullanılır.
# print("\nString Conversion")
# print("uuid4 as str:", str(uuid4_1), "| type:", type(str(uuid4_1)))

# categories = {}

# uuid4 → her kayıt benzersiz ID alır
# categories[str(uuid4())] = {
#     'name': 'Boxing Gloves',
#     'source': 'uuid4 (random)'
# }

# print("\nCATEGORIES:")
# pprint(categories)
# endregion


# region uuid5
#   uuid5() → aynı namespace + aynı input için her zaman aynı UUID üretir (deterministic).
#   - uuid.UUID tipinde bir nesne döndürür.
#   Rastgele değildir.
#   Sabit kimlik (stable identifier) gereken durumlar için uygundur.

# GÜNLÜK HAYAT BENZETMESİ:
#   uuid5 = TC kimlik mantığı 🆔
#   - Aynı kişi → aynı numara
#   - Numara değişmez


# from uuid import uuid5, NAMESPACE_DNS
# from pprint import pprint

# Aynı namespace + aynı string → her zaman aynı UUID üretir.
# uuid5_1 = uuid5(NAMESPACE_DNS, "Boxing Gloves")
# uuid5_2 = uuid5(NAMESPACE_DNS, "Boxing Gloves")

# print("\nuuid5 Demo")
# print("uuid5 1:", uuid5_1)
# print("uuid5 2:", uuid5_2)
# print("Same?:", uuid5_1 == uuid5_2)   # True → aynı input, aynı UUID
# print("Type :", type(uuid5_1))      # <class 'uuid.UUID'>

# uuid5() bir UUID objesi döndürür.
# CRUD uygulamalarında genelde string'e çevrilerek kullanılır.
# print("\nString Conversion")
# print("uuid5 as str:", str(uuid5_1), "| type:", type(str(uuid5_1)))

# categories = {}

# # uuid5 → aynı input → aynı ID
# categories[str(uuid5(NAMESPACE_DNS, "MMA Gloves"))] = {
#     'name': 'MMA Gloves',
#     'source': 'uuid5 (deterministic)'
# }

# print("\nCATEGORIES:")
# pprint(categories)

# uuid5 Overwrite
#   - uuid5 aynı girdiye her zaman aynı ID üretir.
#   - CRUD uygulamalarında overwrite riski vardır.
#   - Sabit kimlik gerektiren durumlar için uygundur.

# Aynı input ile üretilen uuid5'ler AYNI olduğu için dictionary içinde önceki kayıt overwrite edilir.
# key_a = str(uuid5(NAMESPACE_DNS, "Same Name"))
# key_b = str(uuid5(NAMESPACE_DNS, "Same Name"))

# categories[key_a] = {'name': 'Same Name - First'}
# categories[key_b] = {'name': 'Same Name - Second'}

# print("\nuuid5 Overwrite Demo (same key)")
# print("key_a == key_b ?", key_a == key_b)  # True
# pprint(categories)
# endregion


""" 
| Senaryo                | Kullanılacak Yapı |
| ---------------------- | ----------------- |
| ID ile kayıt bulma     | dict[key]         |
| Güvenli okuma          | get()             |
| Tüm kayıtları gezme    | items()           |
| Sadece kayıt bilgileri | values()          |
| Sadece ID’ler          | keys()            |
| Var mı kontrolü        | key in dict       |
 """


# region CRUD App (uuid4)
# uuid4() kullanarak ID üreten, dictionary tabanlı bir CRUD uygulaması geliştirmek.
#   1. CREATE (Yeni Kayıt Oluşturma)
#      - ID bilgisi uuid4() fonksiyonu kullanılarak üretilecek (örnek: 'd912b8cf-0b59-4efb-bfcf-17356dd59c9b').
#   2. UPDATE (Kayıt Güncelleme)
#      - Kullanıcıdan güncellenecek kaydın ID bilgisi alınacak ve ilgili kaydın name ve description alanları güncellenecek.
#   3. DELETE (Kayıt Silme)
#      - Kullanıcıdan silinecek kaydın ID bilgisi alınacak ve ilgili kayıt dictionary içinden silinecek.
#   4. READ (Kayıt Listeleme)
#      - Tüm kayıtlar listelenecek.
#      - Kullanıcıdan kategori adı alınacak ve bu ada göre eşleşen kayıtlar listelenecek.

from uuid import uuid4          # Benzersiz ID üretmek için
from pprint import pprint      # Daha okunabilir çıktı için


categories = {       # 1️⃣ DIŞ (outer) dict
    'd912b8cf-0b59-4efb-bfcf-17356dd59c9b': {
        'name': 'Boxing Gloves',
        'description': 'Best boxing gloves'
    },      # 2️⃣ İÇ (inner) dict
    '9ecfa748-ee8e-4ac3-a471-33e1fd9fe52c': {
        'name': 'MMA Gloves',
        'description': 'Best MMA gloves'
    }       # 3️⃣ İÇ (inner) dict
}

# categories:
#   - key   → category id (string UUID)
#   - value → category bilgileri (dict)

# categories bir dict, içindeki her value da bir dict → nested dict

while True:
    process = input(
        "\nType a process name "
        "(create | get all | get by id | get by name | update | delete | exit): "
    ).lower()

    match process:
        case 'create':
            new_name = input('Please type a category name: ')
            new_descp = input('Please type a description: ')

            # uuid4() → rastgele ve benzersiz ID üretir
            categories[str(uuid4())] = {
                'name': new_name,
                'description': new_descp
            }

            print('\n✅ Category created successfully!')
            pprint(categories)
        case 'get all':
            print('\n📦 All Categories:')
            pprint(categories)
        case 'get by id':
            cat_id = input("Category id: ").strip().lower()

            filtered_categories = {id: info for id, info in categories.items() if cat_id in id.lower()}

            if filtered_categories:
                print('\n🔍 Matching Categories:')
                pprint(filtered_categories)
            else:
                print('\n❌ No category found.')
        case 'get by name':
            cat_name = input('Category name: ').lower()

            filtered_categories = [category for category in categories.values() if cat_name in category.get('name', '').lower()]

            if filtered_categories:
                print('\n🔍 Matching Categories:')
                pprint(filtered_categories)
            else:
                print('\n❌ No category found.')
        case 'update':
            cat_id = input('Category id: ').lower()

            if cat_id in categories:
                new_name = input('Please type a category name: ')
                new_descp = input('Please type a description: ')

                print("\nBefore:")
                pprint({cat_id: categories[cat_id]})

                categories[cat_id].update({
                    'name': new_name,
                    'description': new_descp
                })

                print('\n✏️ Category updated successfully!')
                pprint({cat_id: categories[cat_id]})

                print('\n📦 All Categories:')
                pprint(categories)
            else:
                print('\n❌ No category found.')
        case 'delete':
            cat_id = input('Category id: ').lower()

            if cat_id in categories:
                del categories[cat_id]
                print('\n🗑 Category deleted successfully!')

                print('\n📦 All Categories:')
                pprint(categories)
            else:
                print('\n❌ No category found.')
        case 'exit':
            print('\n👋 Exiting application...')
            break
        case _:
            print('\n❌ Invalid process type!')
# endregion


""" 
| Kafada Kalacak Cümle        |
| --------------------------- |
| **Key → erişim anahtarı**   |
| **Value → veri**            |
| **items() → key + value**   |
| **values() → sadece value** |
| **keys() → sadece key**     |
| **get() → güvenli erişim**  |
"""

# region DICTIONARY UPDATE — IMPORTANT NOTE
# NOT:
#   Dictionary (dict) üzerinde yapılan update / delete / create işlemleri
#   SADECE program çalıştığı sürece geçerlidir.
#
# NEDEN?
#   - Dictionary verileri RAM (hafıza) üzerinde tutulur.
#   - Program kapandığında RAM temizlenir.
#   - Program tekrar çalıştırıldığında kod en baştan okunur.
#
# SONUÇ:
#   - Program içinde update edilen bir dictionary,
#     program yeniden çalıştırıldığında
#     ilk tanımlandığı haline geri döner.
#
# ÖRNEK AKIŞ:
#   1) Program çalışır → categories oluşturulur
#   2) update / delete yapılır → RAM'de değişir
#   3) Program kapanır → RAM sıfırlanır
#   4) Program tekrar çalışır → eski hal geri gelir
#
# BENZETME:
#   - Dictionary = beyaz tahta 🧽
#   - Program kapanınca tahta silinir
#
# KALICI OLMASI İÇİN:
#   - Dosyaya yazılmalı (txt / json)
#   - veya veritabanı kullanılmalı
#
# ÖZET CÜMLE:
#   RAM’de yapılan update / delete / create kalıcı değildir.
#   Program tekrar çalışınca koddaki başlangıç sözlüğü yeniden oluşturulur.
# endregion
