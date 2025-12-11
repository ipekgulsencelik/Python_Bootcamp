
#! Tuple (Demetler)
# Tuple, Python’da list'e benzeyen fakat **immutable** (değiştirilemez) yapıda olan bir veri koleksiyonudur.

# List objesi ile benzer bir mantığa sahiptir;
# ancak list'e özel bazı metotlar (append, extend, remove, sort, vs.)
# tuple üzerinde yoktur.

# Ortak noktalar:
#   ✔ Index mantıkları ortaktır
#   ✔ Hem list'ler hem de tuple'lar slicing (dilimleme) yapabilir

# Tuple'lar, list objesi gibi RAM'de tutulur. Yani uygulama run time'da
# iken oluşturulan tuple'lar da program sonlandığında RAM'den silinir.

# Listelere benzer ama değiştirilemez (immutable) yapılardır.

# Temel Özellikler:
# ✔ Ordered (sıralıdır)
# ✔ Immutable (değiştirilemez)
# ✔ Indexing ve slicing destekler
# ✔ Hızlıdır (özellikle sabit veri tutmak için)
# ✔ İç içe tuple oluşturulabilir (nested tuple)

# Kullanım Alanları:
# ✔ Koordinatlar (x, y)
# ✔ RGB renk kodları
# ✔ Sabit ayarlar
# ✔ Değişmemesi gereken bilgiler

# Bellek:
# Tuple RAM’de list gibi tutulur fakat değiştirilemez olduğundan Python optimizasyon yapar → daha hızlı & güvenli.

# ⭐ Neden Önemli?
#   ✔ Sabit veri tutmada
#   ✔ Koordinat, konum, renk gibi sabitlerde
#   ✔ Performans kritik, değişmeyecek verilerde
#   ✔ Güvenli veri temsilinde (yanlışlıkla değiştirilmesin diye)

# Why Tuple is Faster?
# Hızlı çalışır → immutable olduğu için Python daha az kontrol yapar
# Tuple immutable olduğu için Python bazı optimizasyonlar yapar:
#   - Hafızada daha kompakt saklanır
#   - Serialization / hashing işlemleri daha hızlıdır
#   - Değişmeyeceği garanti olduğu için CPU üzerinde ek kontrol maliyeti yoktur

# Bu nedenle:
#   ✔ Sabit veriler → tuple
#   ✔ Değişecek / dinamik veriler → list

# Not: Tuple'lar hash'lenebilir olduğu için dictionary veya set içinde key olarak kullanılabilir.

"""
Mini Cheatsheet — List vs Tuple
------------------------------------------------------
| Özellik              | List         | Tuple        |
| -------------------- | ------------ | ------------ |
| Değiştirilebilir mi? | ✔ Evet       | ❌ Hayır    |
| Hız                  | Orta         | Daha hızlı   |
| Kullanım Alanı       | Dinamik veri | Sabit veri   |
| Boyut (RAM)          | Daha büyük   | Daha küçük   |
| Güvenlik             | Düşük        | Daha güvenli |
"""

# region Tuple Extras & Pitfalls

# Tek elemanlı tuple tuzağı:
# Python'da ( ) tek başına tuple anlamına GELMEZ.
# t1, parantez içinde yazılsa da aslında bir int'tir: Çünkü tuple'ı asıl belirleyen şey virgüldür (,)

# t1 = (5)      # ❌ Bu bir int, tuple değil
# t2 = (5,)     # ✔ Bu bir tuple

# print(type(t1))  # <class 'int'>
# print(type(t2))  # <class 'tuple'>

# Immutable Example
# Tuple'lar immutable olduğu için, içindeki bir elemanı değiştirmeye çalışmak

# t = (1, 2, 3)
# t[0] = 99  # ❌ TypeError: 'tuple' object does not support item assignment

# Extended unpacking (yıldızlı unpacking)
# Yıldız (*) operatörü ile tuple'ın belli kısmını normal değişkenlere,
# kalanını ise liste olarak tek bir değişkende toplayabiliriz.

# numbers = (1, 2, 3, 4, 5, 6)
# first, second, *rest = numbers
# print(first)   # 1
# print(second)  # 2
# print(rest)    # [3, 4, 5, 6] - list olarak gelir

# Bu yapı, özellikle:
#   - İlk birkaç eleman önemliyse
#   - Geri kalan "tail" kısmını tek değişkende toplamak istediğimizde
#   - Data parsing / API response ayrıştırmada
# çok kullanışlıdır.

# endregion


# region Basic Tuple Usage

# tuple_1 = ('Galatasaray', 'Adana Demirspor', 'Beşiktaş', 'Trabzonspor', 'Fenerbahçe')
# tuple_2 = ('Red Skins', 'Seahawks', 'Vikings', 'Patriots')

# Tuple birleştirme
# tuple_3 = tuple_1 + tuple_2

#! Slicing
# print(tuple_3[2:5])         # ('Beşiktaş', 'Trabzonspor', 'Fenerbahçe')
# print(tuple_3[5::-2])       # 5. indexten geriye doğru, ikişer atlayarak
# print(tuple_3[2::3])        # 2. indexten sona kadar, üçer atlayarak
# endregion


# region Mixed Tuple Examples

# tuple_1 = ('Beşiktaş', 'Galatasaray', 'Adana Demir Spor', 'Trabzon Spor', 'Fenerbahçe')
# tuple_2 = (12, 34.5, 'b', 'Eagels', 'Red Skins', 'Patriot', 'Seahwak')

# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)

# Dilimleme
# print(tuple_3[0:3])  # output => ('Beşiktaş', 'Galatasaray', 'Adana Demir Spor')
# print(tuple_3[3:5])  # output => ('Trabzon Spor', 'Fenerbahçe')
# print(tuple_3[::2])  # output => ('Beşiktaş', 'Adana Demir Spor', 'Fenerbahçe', 34.5, 'Eagels', 'Patriot')
# print(tuple_3[-1])  # output => 'Seahwak'
# print(tuple_3[:5])  # ('Beşiktaş', 'Galatasaray', 'Adana Demir Spor', 'Trabzon Spor', 'Fenerbahçe')
# print(tuple_3[::-1])  # ('Seahwak', 'Patriot', 'Red Skins', 'Eagels', 'b', 34.5, 12, 'Fenerbahçe', 'Trabzon Spor', 'Adana Demir Spor', 'Galatasaray', 'Beşiktaş')
# print(tuple_3[::-2])  # ('Seahwak', 'Red Skins', 'b', 12, 'Trabzon Spor', 'Galatasaray')
# print(tuple_3[3::2])  # ('Trabzon Spor', 12, 'b', 'Red Skins', 'Seahwak')
# endregion


# region Nested Tuple Access

# tuple_4 = (
#     'Sariyer', 
#     ('Erenköy', 'Suadiye'), 
#     ('Yeniköy', 'Bebek', ('Ulus', 'Etiler'))
# )

# print(tuple_4[0])  # Sariyer
# print(tuple_4[1][1])  # Suadiye
# print(tuple_4[2][2][0])  # Ulus
# endregion


# region Tuple Unpacking

# my_family = [
#     ('Burak Yılmaz', 34, 'beast'),
#     ('Hakan Yılmaz', 37, 'bear'),
#     ('İpek Yılmaz', 39, 'keko')
# ]

# for x, y, z in my_family:
#     print(f'Full Name: {x}\nAge: {y}\nUser Name: {z}')
# endregion