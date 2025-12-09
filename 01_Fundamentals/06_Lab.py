# region Lambda Function — Introduction
# Lambda Nedir?
#   İsimsiz, tek satırlık fonksiyon yazma yöntemidir.
#   Fonksiyon tanımı (def) yazmadan hızlıca işlem yapmayı sağlar.
#
# Neden Önemlidir?
# ---------------------------------------------------------
# ✔ map(), filter(), sorted() gibi fonksiyonlarla sık kullanılır
# ✔ Gereksiz fonksiyon tanımlamayı ortadan kaldırır
# ✔ Kodun sade ve temiz görünmesini sağlar
# ✔ Inline (satır içi) kullanım için idealdir
# ✔ Matematiksel işlemlerde çok pratiktir

# Basit bir lambda fonksiyonu — kare alma
# square = lambda x: x * x
# print(square(5))   # 25

# Lambda ile iki sayıyı toplama
# sum_two = lambda a, b: a + b
# print(sum_two(3, 7))  # 10

# Metin dönüştürme — lambdada string işlemleri
# add_text = lambda t: t.upper() + "!"
# print(add_text("hello"))  # HELLO!
# endregion


#! Filter
# Belirli koşulu sağlayan elemanları döndürür.
# Arama, filtreleme, validasyon gibi işlemler için idealdir.

# ⭐ Neden Önemli?
# ✔ Veri filtreleme (ör: pozitif sayıları seçmek)
# ✔ Fiyat filtreleme (ör: 200 TL altındakileri listelemek)
# ✔ Kullanıcı doğrulama (ör: e-posta formatı doğru mu?)
# ✔ Temiz veri oluşturma
# ✔ Hatalı veriyi ayırma
# ✔ Büyük veri setlerinde performanslı filtreleme
# ✔ Koşula bağlı veri seçimi

# Temel Formül:
#     filter(kosul_fonksiyonu, liste)

# Açıklama:
#   - filter() → Koşulu sağlayan elemanları döndürür.
#   - Sonuç bir "iterator" olduğu için genelde list() ile çevrilir.

#* Listeler üzerinde filtrelemeye yarayan fonksiyondur.
#* Listedeki tüm öğeleri gezer ve koşulu True döndüren öğeleri seçerek yeni bir sonuç dizisi oluşturur.
#* Filtreleme kuralı basit olduğunda, genellikle yerleşik ve isimsiz Lambda fonksiyonları kullanılır, bu da kodu daha kısa yapar:

# region Filter Function — Basic Sample
# Verilen numbers listesinden 20'den küçük olan sayıları filtreleyiniz.

# filter() çıktısı bir iterator olduğundan list() ile listeye çevrilir.

# numbers = [10, 15, 20, 25, 30]

# filtered = list(filter(lambda x: x < 20, numbers))
# print(filtered)   # [10, 15]
# endregion


# region Random Number Generation — Fill List With Numbers
# 1000 adet rastgele sayı üretetiniz.
# a = -100  → minimum değer
# b =  100  → maksimum değer
# randint(a, b) → a ve b dahil olmak üzere rastgele tam sayı üretir.

# list comprehension ile hızlıca 1000 elemanlı liste üretiyoruz.

# from random import randint

# numbers = [randint(a=-100, b=100) for i in range(1000)]
# print("Tüm Sayılar:", numbers)

# Yukarıda oluşturulan liste içerisinden sadece POZİTİF (0'dan büyük) olanları listeleyelim.

# Path I → List Comprehension
# Şartlı list comprehension:

# positive_numbers = [number for number in numbers if number > 0]
# print("Pozitif Sayılar (List Comprehension):", positive_numbers)

# Path II → filter() fonksiyonu

# filter(function, iterable)
#    → function True döndürürse eleman listeye alınır.

# lambda x: x > 0  → pozitif sayıları seçer
# filter sonucu 'iterator' döner, listeye çevirmek gerekir.

# temp_lst = filter(lambda x: x > 0, numbers)
# positive_numbers = list(temp_lst)
# print("Pozitif Sayılar (filter):", positive_numbers)
# endregion


# region Filter Function — Extract Even Numbers
# filter() fonksiyonu ile çift sayıları filtreleyerek sonucu liste olarak ekrana yazdırınız.

#   - filter sonucu bir iterator olduğu için list() ile listeye çeviriyoruz

# print(
#      list(
#       filter(lambda x: x % 2 == 0, numbers)
#      )
# )
# endregion


# region Filter Example - Fruits Containing 'a'
# fruits = [
#     "Apple", "Banana", "Orange", "Mango", "Pineapple",
#     "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
#     "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
#     "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
# ]

# 'a' harfi geçen meyveleri filtrele
# result = list(
#     filter(lambda fruit: 'a' in fruit.lower(), fruits)
# )

# print(result)
# endregion


# region Filter Example - Select Only Numbers (int & float)

# isinstance() → Bir nesnenin (x) belirli bir tipe (örneğin int, float, str…) ait olup olmadığını kontrol eder.
# Sonuç olarak True / False döner.

# Elimizde karışık tiplerde bir liste var:
# None, string, integer, float gibi farklı veri türleri içeriyor.
# lst = [None, 2, 'b', 3.19, 9, 'mike tyson']

# Amaç:
#   ✔ Sadece sayısal değerleri (int ve float) seçmek
#   ✔ Diğer tüm veri türlerini (None, string, vb.) elemek
#
# Burada filter() ve lambda kullanıyoruz:
#   - filter(func, iterable)
#       iterable içindeki elemanları func koşuluna göre süzer
#
#   - lambda x: isinstance(x, (int, float))
#       Sadece int veya float olan elemanlar geçecek
#       x hem int hem de float olabilir → (int, float) bir tuple’dır
#       isinstance() → x'in veri tipini kontrol eder 
#       isinstance(x, (int, float)) → x hem int olabilir hem float olabilir

# numbers = list(
#     filter(lambda x: isinstance(x, (int, float)), lst)
# )

# print(numbers)  #   [2, 3.19, 9]
# endregion


# region Filter Example - Valid .com Emails

# .endswith() → Bir string fonksiyonudur ve bir metnin belirli bir ifadeyle bitip bitmediğini kontrol eder.
# Sonuç olarak True / False döner.

# Elimizde karışık formatta e-mail adresleri var:
# mails = [
#     'burak.yilmaz@outlok.com',
#     'savage@mail.com',
#     'bear@',
#     'beast@com.xyz',
#     'burak@gmail.com'
# ]

# Amaç:
#   ✔ Gerçek anlamda ".com" ile biten mail adreslerini bulmak
#   ✔ Yanlış formatlı, eksik veya farklı uzantılı mailleri elemek
#
# Burada:
#   - filter() → listeyi süzer
#   - lambda x → her elemanı tek tek kontrol eder
#   - x.endswith('.com') → mail adresi gerçekten ".com" ile mi bitiyor?

# correct_mail = list(
#     filter(lambda x: x.endswith('.com'), mails)
# )

# print(correct_mail)
# endregion


# region Filter Example - Select Only Digit Strings

# Elimizde karışık tipte string değerlerden oluşan bir liste var.
# Bazıları tamamen rakamlardan oluşurken bazıları alfabetik.
# some_values = ['123', 'burak', 'zxc', '987', '345']

# Amaç:
#   ✔ Sadece tamamen rakamlardan oluşan string değerleri seçmek
#   ✔ Harf içerenleri veya karışık olanları elemek
#
# Burada str.isdigit fonksiyonunu kullanıyoruz:
#   - '123'.isdigit() → True
#   - 'burak'.isdigit() → False
#   - 'zxc'.isdigit() → False
#
# DİKKAT:
#   str.isdigit  -> fonksiyonun kendisini veriyoruz (çağırmıyoruz!)
#   filter(str.isdigit, some_values)
#      filter, listedeki her elemanı alır ve
#      eleman.str.isdigit() çağırarak True/False döner.
#
# Böylece sadece rakam içeren string'ler süzülmüş olur.

# str.isdigit() → fonksiyonu çağır, çalıştır, hemen sonuç (True/False) döndür → yanlış
# str.isdigit → fonksiyonun referansını filter’a veririz → doğru

# str.isdigit fonksiyonun kendisi,
# str.isdigit() fonksiyonun sonucudur.
# Filter fonksiyon ister, sonuç istemez.

# only_digit = list(
#     filter(str.isdigit, some_values)
# )

# print(only_digit)
# endregion


# region Performance Benchmark
# from random import randint   # Rastgele tam sayılar üretmek için
# import time                  # Çalışma süresini ölçmek için
# import tracemalloc           # Bellek kullanımını izlemek için


# tracemalloc.start()                 # Bellek takibini başlatıyoruz
# t1 = time.perf_counter()            # Yüksek çözünürlüklü zaman sayacı (başlangıç)

# Sayı yaratırken aşağıdaki list comprehension kullanmak yerine generator pattern kullansaydınız işin rengi baya değişirdi. 
# Sayı üretim hızı dramatik birşekilde artardı ve zaman maliyeti azalırdı.

# VERİ SETİNİ OLUŞTURMA (GENERATOR KULLANIMI)
# ===============================================================
# Burada "generator expression" kullanıyoruz:
#   numbers = (randint(a=-100, b=100) for _ in range(1000000))
#
# ✔ Bu yapı, 1.000.000 sayıyı RAM'e DİZİ (list) olarak yüklemez.
# ✔ İhtiyaç oldukça TEK TEK sayı üretir (lazy evaluation).
# ✔ Bellek maliyeti, listeye göre çok daha düşüktür.
#
# Eğer liste kullansaydık:
#   numbers = [randint(a=-100, b=100) for _ in range(1000000)]
# Bu durumda 1M elemanlık bir liste RAM'de tutulurdu. Bellek maliyeti çok artardı.
#
# Generator ise:
#   - Belleğe 1 milyon sayı koymaz
#   - Sayıları ihtiyaç oldukça üretir
# → Neredeyse hiç bellek kullanmaz.
# → Değerler tüketildikçe üretilir ve sonra silinir. 
#       İşlem bittikten sonra generator tüketilir (bir daha kullanılamaz)
#
# Generator şu an lazım olmayan sayıları üretmez.
# Listede ise tüm sayılar oluşturulur ve bellekte tutulur.
#
# ÖNEMLİ:
# - Generator bir kez tüketilir; yani bir kere döngüde kullanıldıktan sonra
#   tekrar kullanılamaz (ikincisinde boş döner).
#
# Basit benzetme:
#   Liste    → marketten 1 milyon ekmek alıp eve yığmak
#   Generator → ekmeği ihtiyaç olduğunda tek tek almak
# ===============================================================

# numbers = (randint(a=-100, b=100) for _ in range(1000000))

# List Comprehension
# ===============================================================
# Burada generator'dan gelen sayıları tek tek dolaşıp
# > 0 olanları yeni bir listede topluyoruz.
#
# Dikkat:
#   - numbers bir generator olduğu için,
#     bu satır çalıştıktan sonra "tükenir" (consume edilir).
#   - Yani aynı generator'ı tekrar kullanamazsın.
#
# Eğer filter() ya da for loop ile de benchmark yapmak istersen,
# her yöntem öncesi numbers'ı YENİDEN yaratman gerekir.

# positive_number = [number for number in numbers if number > 0]

# Filter Func
# positive_number = list(filter(lambda x: x > 0, numbers))

# With For Loop
# positive_number = []
# for number in numbers:
#     if number > 0:
#         positive_number.append(number)

# 1M elemanlı bir listeyi direkt print etmek aslında pahalıdır ve
# hem zamanı hem de bellek kullanımını gereksiz şişirir.
# Daha sağlıklı ölçüm için genelde sadece LEN yazdırmak tercih edilir:
#
#   print(len(positive_number))

# print(positive_number)

# t2 = time.perf_counter()

# current, peak = tracemalloc.get_traced_memory()
# current → şu an izleme sırasında kullanılan bellek (byte)
# peak    → izleme süresince görülen en yüksek bellek kullanımı (byte)

# tracemalloc.stop()

# runtime_ms = (t2 - t1) * 1000
# peak_memory = peak / 1024 / 1024

# print(
#     '===============================\n'
#     'Method --> List Comprehension\n'
#     f'Runtime: {runtime_ms}\n'
#     f'Peak Memory: {peak_memory}' 
# )

"""
===============================
Method --> List Comprehension
Runtime: 5728.366099996492
Peak Memory: 28.39721393585205
===============================
Method --> Filter Func
Runtime: 3872.5149999954738
Peak Memory: 28.40944004058838
===============================
Method --> With For Loop
Runtime: 4765.219499997329
Peak Memory: 28.41720485687256
"""
# endregion