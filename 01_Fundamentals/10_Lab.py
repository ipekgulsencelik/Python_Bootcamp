
#! set() function 
# Set, Python’da tekrar eden elemanları otomatik temizleyen, 
# sırasız (unordered) ve değiştirilebilir (mutable) bir koleksiyondur.
# Kesişim, birleşim, fark gibi matematiksel işlemleri destekler.

# Özellikler:
#     ✔ Duplicate kabul etmez (her eleman bir kez bulunur)
#     ✔ Sırasızdır → index ile erişim YOK
#     ✔ Mutable → eleman eklenip silinebilir
#     ✔ Elemanları immutable / hashlenebilir tipte olmalıdır
#           (int, float, str, tuple gibi)

# ⭐ Neden Önemli?
# ✔ Performanslı arama:
#       - O(1) ortalama arama hızı
#       - Aynı işlem list'te O(n) zaman alır.
#       - Büyük veri kümelerinde performansı dramatik bir hız farkı oluşturur.
# ✔ Listeden çok daha hızlıdır  
# ✔ Duplicate (tekrarlı veriyi) temizlemek için en hızlı yöntem  
# ✔ Matematiksel işlemleri destekler →
#       - union (birleşim)
#       - intersection (kesişim)
#       - difference (fark)
#       - symmetric_difference (simetrik fark)


# region Sample — Basic set() usage
# numbers = [1, 2, 2, 3, 4, 4, 4, 5]

# unique_numbers = set(numbers)
# print(unique_numbers)   # {1, 2, 3, 4, 5}
# endregion

# Uyarılar
# ⚠️ Set sırasızdır → çıktı her çalıştırmada farklı sırada görünebilir.
# ⚠️ Elemanlar hashable olmak zorundadır.

# region Remove Duplicates - set()
# Bir listedeki tekrar eden tüm elemanları kaldırmak için set() kullanılabilir.

# numbers = [1, 1, 2, 2, 9, 9, 6]

# print(
#     set(numbers)
# )     # Örn: {1, 2, 6, 9}
# endregion

# Bir string'i set’e dönüştürmek, karakterlerin tekrarsız halini elde etmenin en hızlı yoludur.

# region String → Unique Characters - set()
# Bir string içindeki tekrar eden karakterleri kaldırmak ve 
# sadece benzersiz (unique) karakterleri elde etmek.

# full_name = 'buraburak'

# unique_ch = list(set(full_name))

# print(unique_ch)    # ['b', 'u', 'r', 'a', 'k'] - (sıra farklı olabilir)
# endregion


# region String → Unique Characters (set + sort)
# String içindeki tekrar eden karakterleri kaldırarak sadece benzersiz (unique) karakterleri elde edin ve 
# bu karakterleri alfabetik olarak sıralayıp ekrana yazdırın.

# full_name = 'buraburak'

# set(full_name)
#       - String içindeki karakterleri kümeye dönüştürür
#       - Tüm tekrarları (duplicate) otomatik olarak kaldırır
#       - Sırasız bir yapı üretir (unordered)

# list(set(...))
#       - Set'i listeye çevirir
#       - Artık üzerinde sort(), index, slice gibi işlemler yapılabilir

# unique_ch = list(set(full_name))  # -> örn: ['b', 'u', 'r', 'a', 'k']

# sort()
#       - Listeyi alfabetik olarak sıralar
#       - Bu aşamada artık sıralı, temiz bir unique karakter listesi elde edilir

# unique_ch.sort()                  # -> alfabetik sıralama

# print(unique_ch)                  # -> ['a', 'b', 'k', 'r', 'u']
# endregion


# region Set Operations — union / intersection / difference / symmetric_difference

# a = {1, 2, 3}
# b = {3, 4, 5}

#   SET OPERATIONS (Matematiksel Küme İşlemleri)

#   ✔ Birleşim (Union)                → a ∪ b
#       - Her iki kümedeki tüm elemanlar
#       - Tekilleştirilmiş şekilde döner
#       - Operatör:       |
#       - Metod:          a.union(b)

#   ✔ Kesişim (Intersection)          → a ∩ b
#       - Ortak elemanlar
#       - Operatör:       &
#       - Metod:          a.intersection(b)

#   ✔ Fark (Difference)               → a − b
#       - a’da olup b’de olmayan elemanlar
#       - Operatör:       -
#       - Metod:          a.difference(b)

#   ✔ Simetrik Fark (Symmetric Difference) → a △ b
#       - Her iki kümede olup ORTAK olmayan elemanlar
#       - Yani birleşimden kesişimi çıkarır
#       - Matematiksel: (a ∪ b) − (a ∩ b)
#       - Operatör:       ^
#       - Metod:          a.symmetric_difference(b)

# print(a | b)   # Birleşim           → {1, 2, 3, 4, 5}
# print(a & b)   # Kesişim            → {3}
# print(a - b)   # Fark               → {1, 2}
# print(a ^ b)   # Simetrik Fark      → {1, 2, 4, 5}
# endregion


# region Set — Intersection & Union

# x = {1, 2, 3, 4, 5}
# y = {4, 5, 6, 7, 8}

# print(x & y)   # Kesişim → {4, 5}
# print(x | y)   # Birleşim → {1, 2, 3, 4, 5, 6, 7, 8}
# endregion


# region Set — Adding Elements (add)

# boxers = {'muhammed ali', 'mike tyson'}

#  set.add():
#     ✔ Set içine yeni bir eleman ekler
#     ✔ Eğer eleman zaten varsa tekrar eklemez (duplicate engelli)
#     ✔ Set sırasız (unordered) olduğu için çıktıdaki sıra garanti değildir

# boxers.add('lenox lewis')
# boxers.add('evander holyfield')
# boxers.add('antony jasua')

# print(boxers)
# Örn çıktı: {'muhammed ali', 'mike tyson', 'lenox lewis', 'evander holyfield', 'antony jasua'}
# endregion


# region Set — Removing Elements (remove)

# boxers = {'muhammed ali', 'mike tyson', 'lenox lewis'}

#  set.remove(element):
#     ✔ Belirtilen elemanı set'ten siler
#     ✔ Eğer eleman YOKSA → KeyError fırlatır
#     ✔ Sırasız bir yapı olduğu için elemanların konumu önemli değildir

#  Not:
#     - remove() kesin silme methodudur
#     - Eğer hata istemiyorsan discard() tercih edilir

# boxers.remove('lenox lewis')

# print(boxers)
# Örn: {'muhammed ali', 'mike tyson'}
# endregion


# region Set — Removing Elements Safely (discard)

# boxers = {'muhammed ali', 'mike tyson', 'evander holyfield'}

#  set.discard(element):
#     ✔ Eleman set'te varsa siler
#     ✔ Eleman YOKSA bile HATA VERMEZ (remove() farklıdır!)
#     ✔ Bu yüzden güvenli silme yöntemi olarak kullanılır

#  remove() vs discard():
#     - remove('x')  → eleman yoksa KeyError fırlatır ❌
#     - discard('x') → eleman yoksa sessizce geçer ✔

# boxers.discard('evander holyfield')

# print(boxers)   # Örn: {'muhammed ali', 'mike tyson'}
# endregion


# region Set — add(), remove(), discard() Combined

# boxers = {'muhammed ali', 'mike tyson'}

# add()
#     ✔ Yeni eleman ekler
#     ✔ Duplicate engellidir → eleman zaten varsa eklemez

# boxers.add('lenox lewis')
# boxers.add('evander holyfield')
# boxers.add('antony jasua')

# print(boxers)
# Örn: {'muhammed ali', 'mike tyson', 'lenox lewis', 'evander holyfield', 'antony jasua'}


# remove()
#     ✔ Belirtilen elemanı siler
#     ✔ Eleman YOKSA → KeyError fırlatır ❌

# boxers.remove('lenox lewis')


# discard()
#     ✔ Eleman varsa siler
#     ✔ Eleman yoksa hata vermez (remove'dan farkı) ✔

# boxers.discard('evander holyfield')

# print(boxers)
# Kalan elemanlar: {'muhammed ali', 'mike tyson', 'antony jasua'}
# endregion


#! All Func
# all(iterable):
#   ✔ iterable içindeki *tüm* elemanlar True ise → True döner
#   ✔ Bir tane bile False varsa → False döner
#   ✔ Boş iterable → varsayılan olarak True döner (matematiksel tanım)

# Arka planda nasıl çalışır?
#   - Python, her elemanı sırayla kontrol eder.
#   - İlk False değerinde *hemen durur* (short-circuit behavior)
#   - Bu yüzden büyük listelerde çok hızlıdır.

# Neden Önemli?
#   ✔ Validasyon sistemlerinin temel taşıdır.
#   ✔ Çoklu koşulların kontrolünü tek satıra indirir.

# Kullanım Alanları:
#   - Form doğrulama
#   - Şifre kontrolü
#   - Veri uygunluk kontrolleri
#   - Filtre mekanizmaları


# region all - Sample

# ages = [18, 34, 13, 67, 23]

# all(age > 18 for age in ages)

# Mantık:
#   - Her yaş için "age > 18" ifadesi kontrol edilir.
#   - Koşul True → devam eder
#   - Koşul False → all() hemen durur ve False döner

# Bu listede:
#   18 > 18 → False  ❌  (eşitlik > değil)
#   Dolayısıyla all() daha 1. elemanda False döndürür.

# Eğer 18'i de kabul etseydi (>= 18), sonuç tamamen değişirdi.

# member = all(age > 18 for age in ages)

# print(member)   # False
# endregion


# region all() — Product Stock Validation
# Tüm ürünlerin stok miktarının 0'dan büyük olup olmadığını kontrol edin

# products = [
#     ['name', 'boxing gloves', 'price', 59.99, 'stock', 5],
#     ['name', 'punching bags', 'price', 159.99, 'stock', 15],
#     ['name', 'handwrap', 'price', 19.99, 'stock', 0]
# ]

# print(
#     all(
#         product[5] > 0 for product in products
#     )
# )
# ÇIKTI: False (çünkü 'handwrap' ürününün stoğu 0)
# endregion


# region Password Validation — any() + all()
# Şifrede aşağıdaki 4 kuralın sağlanıp sağlanmadığını kontrol etmek.
# Kurallar:
#   En az 1 büyük harf        → any(ch.isupper())
#   En az 1 küçük harf        → any(ch.islower())
#   En az 1 rakam             → any(ch.isdigit())
#   En az 1 özel karakter     → any(not ch.isalnum())

# password = 'Bu?ra4k_'

# is_password_valid = [
#     any(ch.isupper() for ch in password),       # Büyük harf var mı?
#     any(ch.islower() for ch in password),       # Küçük harf var mı?
#     any(ch.isdigit() for ch in password),       # Rakam var mı?
#     any(not ch.isalnum() for ch in password),   # Özel karakter var mı?
# ]

# is_password_valid listesi:
#   - Her kural için True / False değer üretir
#   - Örnek: [True, True, True, True]

# print(is_password_valid)    # Örn Çıktı: [True, True, True, True]

# all(is_password_valid):
#   ✔ Listedeki TÜM kurallar True ise → True döner
#   ✔ Bir kural bile False ise → False döner

# print(
#     all(is_password_valid)
# )   # True → tüm kurallar sağlandı
# endregion