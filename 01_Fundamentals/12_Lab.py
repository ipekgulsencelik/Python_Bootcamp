
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

# region Sample - Dictionary Comprehension

# from pprint import pprint

# numbers = [1, 2, 3, 4, 5]

# squares = {x: x * x for x in numbers}
# pprint({number: square for number, square in squares.items()})
# Sonuç:
#   {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# endregion