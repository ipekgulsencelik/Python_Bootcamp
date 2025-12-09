
#! Zip Function
# Listeleri, tuple’ları, numpy array’lerini yani koleksiyonları 
# birbirleriyle indeks bazlı eşleyerek birleştiren fonksiyondur.

# Birden fazla listeyi eleman eleman birleştirir.
# Çoklu veriyi tek yapıda tutmak için mükemmeldir.

# zip() fonksiyonu:
#   → Birden fazla listeyi "yan yana" birleştirir.
#   → Aynı indekslerdeki elemanları eşleştirir.
#   → En kısa listenin uzunluğu kadar eşleştirme yapılır.

# zip() nasıl çalışır?
# Aynı indeksli elemanları tuple olarak bir araya getirir.
# Liste uzunlukları eşit değilse → en kısa liste kadar eşleştirir.
# Çıkan sonuçlar tuple olduğu için list(zip(...)) ile liste formatında bastırılır.
#   → Sonuç iterable’dır → list(zip(...)) ile görünür hâle gelir

# ⭐ Neden Önemli?
#   - İsim + yaş + şehir → gibi çoklu veri eşleşmelerini kolaylaştırır
#   - Çoklu datayı tek yapıda toplamak için mükemmeldir
#   - Birden fazla listeyi sütun gibi birleştirir  
#   - Excel tablosu gibi "sütun bazlı" çalışma sağlar
#   - Veri bilimi, raporlamada çok kullanılır
#   - Çok satırlı veriyle uğraşırken veri eşleştirme sağlar  

# region Zip Function — Sample
# names = ["burak", "hakan", "ipek"]
# age = [36, 39, 41]

# result = list(
#     zip(names, age)
# )
# print(result)     # ÇIKTI: [('burak', 36), ('hakan', 39), ('ipek', 41)]
# endregion


# region Zip Function — Matching Multiple Lists (names, age, job)
# names = ['burak', 'hakan', 'ipek']
# age = [36, 39, 41]
# occupation = ['developer', 'chemist - chemical engineer']

# result = list(
#     zip(names, age, occupation)
# )
# print(result)     # ÇIKTI: [('burak', 36, 'developer'), ('hakan', 39, 'chemist')]

# NOT:
# occupation listesi daha kısa olduğundan "ipek" eşleşemez.

# DİKKAT:
#   occupation listesi daha kısa olduğu için:
#       ["developer", "chemist"]
#   zip() yalnızca ilk 2 elemanı eşleştirebilir.
# endregion


# region Random List Generation & Zip → Pairwise Sum
# Rastgele 10 elemanlı iki liste üret
# Aynı indekslerdeki elemanları zip() ile eşleştir
# Eşleşen sayı çiftlerini toplayıp yeni bir liste üretmek

#   - zip(list1, list2):
#         aynı indekslerdeki değerleri tuple olarak eşleştirir.
#         ör: (number1[i], number2[i])

# from random import randint

# number1 = [randint(a= 0, b=100) for _ in range(10)]
# number2 = [randint(a= 0, b=100) for _ in range(10)]

# temp_lst = list(
#     zip(number1, number2)
# )
# print(temp_lst)

# result = [x + y for x,y in temp_lst]    # → her tuple içindeki iki sayıyı toplar.
# print(result)
# endregion


#! Unzip
# Bir listede birden fazla tuple (demet) varsa ve bu tuple'ların 
# içindeki değerleri "sütun sütun" ayırmak istiyorsak → zip(*) kullanırız.
# tuple'lar sökülüp kolonlara ayrılır.

# ZIP → Birleştirme
# UNZIP → Sökme (zip(*) ile kolon kolon ayırma)

# Zip, birden fazla iterable’ı sıralı olarak eşler.
# Zip(*) ise var olan eşlemeleri tekrar kolonlara böler (unzip).

# Önemli:
#   - zip bir generator döndürür → list(), tuple() ile açılır.
#   - Eşleme, EN KISA iterable uzunluğu kadar yapılır.


# region Unzip Function — Sample
# Bir listede birden fazla tuple varsa ve bu tuple'lardaki verileri
# “sütun sütun” ayırmak istiyorsak → zip(*) kullanılır.

# lst = [('burak', 36, 'developer'), ('hakan', 39, 'chemist - chemical engineer')]

# names, ages, occupations = zip(*lst)

# print(names)      # → ('burak', 'hakan')
# print(ages)       # → (36, 39)
# print(occupations)        # → ('developer', 'chemist - chemical engineer')
# endregion


# region Zip Function Explanation — Sample
# lst = ['ayhan', 'elton', 'adal', 'merve']

#   range(len(lst)) → 0, 1, 2, 3
#   lst              → 'ayhan', 'elton', 'adal', 'merve'
#
# zip() sırayla elemanları eşler:
#   (0, 'ayhan')
#   (1, 'elton')
#   (2, 'adal')
#   (3, 'merve')
#
# zip → generator olduğu için list() ile açılır.
# list() → zip objesini listeye dönüştürür

# print(
#     list(zip(range(len(lst)), lst))
# )
# endregion


# region Zip Function — String
# Stringler iterable’dır → zip harf harf eşler.

# character_1 = 'xyz'
# character_2 = 'XYZ'

# Eşleşme şu şekilde olur:
#   ('x', 'X')
#   ('y', 'Y')
#   ('z', 'Z')

# print(
#     list(
#         zip(character_1, character_2)
#     )
# )
# endregion


# region Matrix Generation (List Comprehension + Random) & Zip
# 3 satırdan oluşan bir matrix oluşturmak
# Her satır 4 adet rastgele sayı içerecek (0–150 arası isteğe bağlı)
# Her iç liste list comprehension ile üretilecek
# Bu 3 satır zip() ile birleştirilip "kolon kolon" tuple listesi çıkarılacak
#
# zip(matrix[0], matrix[1], matrix[2]):
#     1. kolon → (row1[0], row2[0], row3[0])
#     2. kolon → (row1[1], row2[1], row3[1])
#     3. kolon → ...
#
# ÖRNEK ÇIKTI:
#     [(34, 23, 88), (56, 67, 12), (123, 12, 45), (56, 45, 77)]
#
# Bu çıktı her sütunu tuple olarak temsil eder.

# from random import randint

# Matrix — 3 Satır × 4 Sütun
# matrix = [
#     [randint(0, 150) for _ in range(4)],  # satır 1
#     [randint(0, 150) for _ in range(4)],  # satır 2
#     [randint(0, 150) for _ in range(4)]   # satır 3
# ]

# print("📌 Matrix:")
# for row in matrix:
#     print(row)

# result = list(zip(matrix[0], matrix[1], matrix[2]))

# print("\n📌 Zip Sonucu (Sütun Bazlı Tuple Listesi):")
# print(result)
# endregion


# region Generate Random Matrix (3x10)
# 3 satır ve her satırda 10 sayı bulunan bir matris oluşturmak.
# matrix içindeki 3 satırı zip() ile sütun bazında birleştirmek.

# from random import randint

# matrix = [
#     [randint(0, 100) for _ in range(10)] for _ in range(3)
# ]

# print("Matrix:")
# print(matrix)

# zip(matrix[0], matrix[1], matrix[2]) → aynı sütundaki elemanları eşler.
# zipped_list = list(
#     zip(matrix[0], matrix[1], matrix[2])
# )

# Sütun bazında birleştirme → row sayısını bilmeye gerek yok
# zipped_list = list(zip(*matrix))

# Not:
#   zip(*matrix) → satır sayısından bağımsız olarak tüm satırları otomatik açar.
#   zip(matrix[0], matrix[1], matrix[2]) gibi manuel kullanım sadece sabit satır sayısında çalışır.

# print("\nZipped List:")
# print(zipped_list)
# endregion