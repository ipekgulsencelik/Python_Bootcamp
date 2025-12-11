
#! Map() Function
# Listedeki her elemana TEK TEK bir fonksiyon uygular.
# Veri dönüştürme, matematiksel işlem, temizleme, filtrasyon öncesi hazırlık gibi alanlarda çok güçlüdür.

# ⭐ Neden Önemli?
# ✔ Büyük veri listelerinde hızlı toplu işlem sağlar  
# ✔ API’den gelen "ham" veriyi temizlemek için idealdir  
# ✔ string → int → float gibi veri tipi dönüşümlerinde sık kullanılır  
# ✔ Matematiksel işlemleri tek satırda yapmayı sağlar  
# ✔ Fonksiyonel programlamanın temel taşlarından biridir  
# ✔ Veri dönüştürme (data transformation) için MÜTHİŞ bir araçtır  

# Formül:
#     map(fonksiyon, iterable)

# Not:
#   - map() bir map objesi döndürür → çoğunlukla list() ile listeye çevrilir.
#   - Fonksiyon olarak lambda, str, int, float veya herhangi bir fonksiyon verilebilir.

# map():
#   - Birden fazla listeyi paralel olarak iterate eder.
#   - zip ile aynı kurala sahiptir → EN KISA liste kadar çalışır.
#   - Uzun listedeki sondaki elemanlar YOK SAYILIR.

from random import randint

# region Square Each Element — map + lambda
# nums listesinde bulunan her sayının karesini almak.

# nums = [1, 2, 3, 4, 5]

# map() → listedeki her elemanı sırayla lambda fonksiyonuna gönderir.
# squares = list(map(lambda x: x ** 2, nums)) # lambda x: x**2 → alınan elemanın karesini üretir.
# print(squares)      # Örnek çıktı: [1, 4, 9, 16, 25]

# Alternatif Kısa Kullanım:
# print(
#     list(map(lambda x: x ** 2, nums))
# )

# print(
#     list(
#         map(lambda x: x ** 2, [i  for i in range(10)]))
# )
# endregion


# region Convert Numbers to String — map + str
# nums listesi içinde bulunan bütün sayıları "str" tipine dönüştürmek.

# nums = [1, 2, 3, 4, 5]

# Not:
#   lambda kullanmaya gerek yok; Python'un hazır str fonksiyonunu doğrudan verebiliriz.
#   str → kendisine verilen her elemanı otomatik olarak string formatına çeviren bir fonksiyondur.

# nums_str = list(map(str, nums))
# print(nums_str)     # ['1', '2', '3', '4', '5']

# Alternatif Kısa Kullanım:
# print(
#     list(map(str, nums))
# )

# print(
#     list(
#         map(str, [i  for i in range(10)]))
# )
# endregion


# region Check '@' in E-mail Addresses — map + lambda
#   Listedeki her mail adresi '@' içeriyor mu? → True / False listesi üretmek.

# mail_address = ["burak.yilmaz@outlook.com", "hakan.yilmaz", "ipek.yilmaz@outlook.com"]

# lambda x: '@' in x → eğer x içinde '@' varsa True, yoksa False döner.
# mail_valid_flags = list(map(lambda x: '@' in x, mail_address))
# print(mail_valid_flags)   # [True, False, True]

# Alternatif Kısa Kullanım:
# print(
#     list(
#         map(lambda x: '@' in x, mail_address)
#     )
# )
# endregion


# region Apply 10% Price Increase — map + lambda
# products listesindeki her ürünün fiyatına (%10) zam uygulamak.

# Yapı:
#   products = [isim, stok, fiyat]
#   x[2] → ürünün fiyatı
#   round(değer, 2) → virgülden sonra 2 basamak

# products = [
#     ["Boxing Gloves", 100, 59.99],
#     ["Pucnhing Bags", 150, 160.99],
#     ["Hand Wrap", 200, 11.99]
# ]

# print(
#     list(
#         map(lambda x: x[2] * 1.10, products)
#     )
# )

# lambda x: round(x[2] * 1.10, 2) → ürünün fiyatına %10 zam ekler ve iki basamaklı yuvarlar.
# products_price = list(
#     map(lambda x: round(x[2] * 1.10, 2), products)
# )

# print(products_price)     # [65.99, 177.09, 13.19]
# endregion


# region Extract Product Names — map + lambda
# Her ürün listesinin ilk elemanı olan isimleri topluca çekmek.

# products = [
#     ["Boxing Gloves", 100, 59.99],
#     ["Pucnhing Bags", 150, 160.99],
#     ["Hand Wrap", 200, 11.99]
# ]

# print(
#     list(
#         map(lambda x: x[0], products)
#     )
# )

# products_name = list(map(lambda x: x[0], products))
# print(products_name)      # ['Boxing Gloves', 'Pucnhing Bags', 'Hand Wrap']
# endregion


# region Capitalize Each Name — map + str.title
# Her ismi "Title Case" formuna dönüştürmek.
# Örnek: "burak yılmaz" → "Burak Yılmaz"

# Not:
#   str.title bir string metodudur; lambda yazmaya gerek yoktur.
#   str.title() → bir string içindeki her kelimenin ilk harfini büyük, kalan tüm harflerini küçük yapar.

# names = ['burak yılmaz', 'hakan yilmaz', 'ipek yilmaz']

# print(
#     list(
#         map(str.title, names)
#     )
# )

# list_name = list(map(str.title, names))
# print(list_name)          # ['Burak Yılmaz', 'Hakan Yilmaz', 'Ipek Yilmaz']
# endregion


# region Generate outlook E-mail from Names — map + lambda
# "ad soyad" → "ad.soyad@outlook.com" formunda mail üretmek.

# domain_name = '@outlook.com'

# names = ['burak yılmaz', 'hakan yilmaz', 'ipek yilmaz']

# print(
#     list(
#         map(lambda x: f"{x.lower().replace(' ', '.')}{domain_name}", names)
#     )
# )

# Adımlar:
#   - x.lower()         → tüm harfleri küçült
#   - replace(' ', '.') → boşlukları nokta yap
#   - sonuna '@outlook.com' ekle

# emails_list = list(
#     map(lambda x: x.lower().replace(' ', '.') + domain_name, names)
# )
# print(emails_list)
# Örnek:
# ['burak.yılmaz@outlook.com', 'hakan.yilmaz@outlook.com', 'ipek.yilmaz@outlook.com']
# endregion


# region Sum Two Lists — zip + list comprehension vs map
# Aşağıdaki iki listeyi eleman bazında toplayarak yeni bir listeye ekleyin.
# Not:
#   - Bir liste diğerinden kısa olabilir, bunu göz önünde bulundurarak çözün.

# lst_1 = [87, 67, 81, 69, 65, 99, 79, 57, 62, 65]
# lst_2 = [20, 39, 46, 100, 48, 34, 75, 59]

# Her iki yöntem de aynı sonucu üretir.

# zip():
#   - İki listeyi eleman bazında eşleştirir.
#   - Listeler farklı uzunlukta ise sadece EN KISA listenin uzunluğu kadar döner.
#   - Uzun listedeki fazla elemanlar YOK SAYILIR.

# Yöntem 1: List Comprehension + zip
#   zip(list1, list2) → iki listeyi eleman bazında eşleştirir.
# sum_list_lc = [x + y for x, y in zip(lst_1, lst_2)]
# print(sum_list_lc)

# print(
#     list(
#         map(lambda x: x[0] + x[1], zip(lst_1, lst_2))
#     )
# )

# map():
#   - Birden fazla listeyi paralel olarak iterate eder.
#   - zip ile aynı kurala sahiptir → EN KISA liste kadar çalışır.
#   - Uzun listedeki sondaki elemanlar YOK SAYILIR.

# Yöntem 2: map + lambda (iki listeyi aynı anda gezer)
# sum_list_map = list(map(lambda x, y: x + y, lst_1, lst_2))
# print(sum_list_map)

# print(
#     list(
#         map(lambda x, y: x + y, lst_1, lst_2)
#     )
# )

# Not — Performance:
#   ✔ List Comprehension genelde daha hızlıdır çünkü CPython tarafından C seviyesinde optimize edilmiştir.
#   ✔ map + lambda daha yavaştır; lambda her elemanda ekstra function call maliyeti yaratır.
#   ✔ map + builtin (str, int, float) → en hızlı senaryodur (lambda kullanılmadığında).

# Kısaca:
#   Hız Sıralaması → map(builtin) > List Comprehension > map(lambda)
# endregion


# region Convert Positive Random Numbers to String — filter + map
# -100 ile +100 arasında 10 tane rastgele sayı üretin.
# Bu sayıların sadece pozitif olanlarını seçin.
# Pozitif sayıları string formatına çevirin.
# Sonucu bir liste içinde ekrana yazdırın.

# -100 ile +100 arasında 10 tane rastgele sayı üret
#       numbers = [randint(-100, 100) for _ in range(10)]
# Sonrasında yalnızca pozitif olanları seçip string'e dönüştürmek.
#       filter(lambda x: x > 0, numbers)    → sadece pozitif sayıları alır
#       map(str, ...)                       → süzülen pozitifleri string'e çevirir

# from random import randint

# numbers = (randint(a=-100, b=100) for _ in range(10))

# positive_str = list(
#     map(
#         str,
#         filter(lambda x: x > 0, numbers)
#     )
# )

# print(numbers)            # tüm sayılar (hem pozitif hem negatif)
# print(positive_str)       # sadece pozitiflerin string halleri, örn: ['55', '12', '90']

# Tek satırlık Demo:
# print(
#     list(
#         map(str, filter(lambda x: x > 0, [randint(-100, 100) for _ in range(10)]))
#     )
# )
# endregion


#! join() Function 
# join() → Bir ayraç (separator) kullanarak bir listedeki STRING elemanlarını tek bir string hâline getirir.
# join sadece STRING iterable üzerinde çalışır. Eğer elemanlar int ise hata verir.

# Genel söz dizimi:
#       SEPARATOR.join(ITERABLE)

# Örnek:
#       '-'.join(['12', '45', '88'])  → '12-45-88'

# Neden önemlidir?
#   ✔ Çok hızlıdır (C seviyesinde optimize edilmiştir)
#           → stringleri + operatöründen çok daha performanslı birleştirir
#   ✔ String birleştirmenin en doğru yöntemidir
#   ✔ CSV, log, telefon numarası, path, tarih formatı gibi birçok alanda kullanılır


# region Example 1 — Basic join usage
# Basit bir listeyi '-' ile birleştirelim:

# lst = ['12', '45', '88']

# result = '-'.join(lst)
# print("Example 1:", result)     # Çıktı → Example 1: 12-45-88
# print(type(result))     # <class 'str'>
# endregion


# region Generate Two Random Lists → Sum Elements → Convert Negatives to Positives
# List Comprehension kullanarak 2 tane rastgele sayı içeren liste oluşturun.
#   - Üretilecek sayı aralığı: -100 ile +100
# Her iki listedeki sayıları eleman bazında toplayın.
# Toplamı negatif olan değerleri pozitife dönüştürün.
# Sonucu bir liste içinde ekrana yazdırın.

# Not:
#   abs(x) → x negatifse pozitif yapar, pozitifse olduğu gibi bırakır.
#            Örnek: abs(-10) = 10, abs(7) = 7

# from random import randint

# -100 ile +100 arasında 10'ar adet rastgele sayıdan oluşan iki liste üretelim.
# a = [randint(a=-100, b=100) for _ in range(10)]
# b = [randint(a=-100, b=100) for _ in range(10)]

# Her iki listedeki sayıların toplamını alalım → zip + map + lambda
# result = [abs(x + y) for x, y in zip(a, b)]

# Eğer toplam negatifse → pozitife dönüştürelim (abs())
# lst_result = list(map(str, result))

# print(lst_result)

# listede bulunan string sayı değerlerini tek bir string içinde '-' karakteri ile birleştir
# hint: str.join()

# Not:
#   str.join(iterable)
#       → iterable içindeki string elemanları verilen ayraç ile birleştirir.

# output: ['132', '51', '66', '21', '54', '150', '66', '79', '6', '105']

# beklenen çıktı:
# 132-51-66-21....
# str_result = '-'.join(lst_result)
# str_result = '-'.join(map(str, result))

# print(str_result)
# endregion