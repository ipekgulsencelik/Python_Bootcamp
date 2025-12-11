#   Generate Two Random Lists → Sum Elements → Convert Negatives
# ===============================================================
# AMAÇ:
#   -100 ile +100 arasında rastgele 10 sayıdan oluşan İKİ farklı liste üretmek.
#   ✔ Elemanları index bazında toplamak (zip)
#   ✔ Toplamı NEGATİF olan değerleri pozitife çevirmek (abs)
#   ✔ Sonuçları liste olarak ekrana yazdırmak
# ===============================================================


# ---------------------------------------------------------------
# TEMEL BİLGİLER:
#   zip(lst1, lst2)
#       → İki listeyi eleman bazında eşler. (x, y) şeklinde ikililer üretir.
#
#   abs(x)
#       → x negatifse pozitif yapar; pozitifse aynen döndürür.
#
#   List Comprehension
#       → Hem hızlı, hem de Pythonic bir yazım sağlar.
# ---------------------------------------------------------------


# region Imports
from random import randint
# endregion

# region Step 1 — Generate Two Random Lists
# -100 ile +100 arasında 10'ar adet rastgele sayıdan oluşan iki liste üretelim.
lst_1 = [randint(-100, 100) for _ in range(10)]
lst_2 = [randint(-100, 100) for _ in range(10)]
# endregion


# region Step 2 — Sum Corresponding Elements
# Her iki listedeki sayıların toplamını alalım
# Eleman bazında toplama (3 farklı yöntem gösterildi)

# List Comprehension - En Pythonic Yöntem (önerilen)
summed = [x + y for x, y in zip(lst_1, lst_2)]

# map + lambda Yöntemi
# summed = list(map(lambda x, y: x + y, lst_1, lst_2))

# zip ile tuple alıp toplamı hesaplama Yöntemi
# summed = list(map(lambda pair: pair[0] + pair[1], zip(lst_1, lst_2)))
# endregion


# region Step 3 — Convert Negative Totals to Positive (abs)
# Eğer toplam negatifse → pozitife dönüştürelim (abs())

# Not:
#   abs(x) → x negatifse pozitif yapar, pozitifse olduğu gibi bırakır.
#            Örnek: abs(-10) = 10, abs(7) = 7

# En temiz kullanım: map(abs, iterable)
converted = list(map(abs, summed))

# Alternatif:
# converted = [abs(x) for x in summed]
# endregion


# region Output
print("List 1:", lst_1)
print("List 2:", lst_2)
print("Summed:", summed)
print("Converted (All Positive):", converted)
# endregion


# region One-Liner — Sum & Convert to Positive
# ✔ zip → iki listeyi eleman bazında eşler
# ✔ x + y → her bir çifti toplar
# ✔ abs(...) → toplam negatifse pozitife çevirir
# ✔ List Comprehension → tek satırda sonuç listesi oluşturur

# print([abs(x + y) for x, y in zip(lst_1, lst_2)])
# endregion