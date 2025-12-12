
#! Sum Two Lists — Handling Different Lengths
# =============================================================================
# AMAÇ:
#   - İki listeyi eleman bazında toplamak
#   - Listeler farklı uzunlukta olabilir
#   - Kısa listenin eksik elemanlarını 0 kabul ederek işlem yapmak
#
# NEDEN ÖNEMLİ?
#   - Gerçek hayatta API / DB / CSV verileri çoğu zaman eşit uzunlukta gelmez
#   - zip() ve map() varsayılan olarak kısa listeyi esas alır
#   - Veri kaybını önlemek için zip_longest kullanılır
# =============================================================================


# =============================================================================
# SAMPLE DATA
# =============================================================================
lst_1 = [87, 67, 81, 69, 65, 99, 79, 57, 62, 65]
lst_2 = [20, 39, 46, 100, 48, 34, 75, 59]


# =============================================================================
# region Method 1 — zip() + List Comprehension (KISA LİSTE ESAS ALINIR)
# =============================================================================
# zip():
#   - Elemanları index bazlı eşleştirir
#   - Farklı uzunlukta listelerde SADECE EN KISA liste kadar döner
#   - Uzun listedeki fazla elemanlar YOK SAYILIR

sum_list_zip = [x + y for x, y in zip(lst_1, lst_2)]
print("zip + list comprehension:", sum_list_zip)
# endregion


# =============================================================================
# region Method 2 — map() + lambda (KISA LİSTE ESAS ALINIR)
# =============================================================================
# map():
#   - Birden fazla iterable'ı paralel olarak iterate eder
#   - zip ile AYNI davranışı gösterir
#   - EN KISA liste kadar çalışır
#   - lambda kullanımı ekstra function-call maliyeti yaratır

sum_list_map = list(map(lambda x, y: x + y, lst_1, lst_2))
print("map + lambda:", sum_list_map)
# endregion


# =============================================================================
# region Method 3 — zip_longest() + List Comprehension (ÖNERİLEN YÖNTEM)
# =============================================================================
# zip_longest():
#   - En uzun liste bitene kadar devam eder
#   - Eksik elemanlara fillvalue atanır
#   - Veri kaybını ÖNLER
#   - Gerçek hayatta EN GÜVENLİ çözümdür

from itertools import zip_longest

sum_list_longest = [
    x + y
    for x, y in zip_longest(lst_1, lst_2, fillvalue=0)
]

print("zip_longest + list comprehension:", sum_list_longest)
# endregion


# =============================================================================
# region Method 4 — Manual Index Control (EĞİTİM AMAÇLI)
# =============================================================================
# Bu yöntem:
#   - Mantığı öğretmek için faydalıdır
#   - Ancak production kodlarda daha verbose kabul edilir

max_len = max(len(lst_1), len(lst_2))
sum_list_manual = []

for i in range(max_len):
    x = lst_1[i] if i < len(lst_1) else 0
    y = lst_2[i] if i < len(lst_2) else 0
    sum_list_manual.append(x + y)

print("manual index control:", sum_list_manual)
# endregion


# =============================================================================
# PERFORMANCE & BIG-O NOTES
# =============================================================================
# Zaman Karmaşıklığı (Time Complexity):
#   - Tüm yöntemler: O(n)
#
# Bellek Karmaşıklığı (Space Complexity):
#   - List Comprehension: O(n)
#   - map(): O(n)
#
# Performans Sıralaması (genel):
#   map(builtin) > list comprehension > map(lambda)
#
# Bu örnekte lambda kullanıldığı için:
#   zip_longest + list comprehension → en dengeli ve okunabilir çözüm
#
# =============================================================================


# =============================================================================
# SUMMARY
# =============================================================================
# ✔ zip() ve map() → EN KISA liste kadar çalışır
# ✔ Veri kaybı istemiyorsan zip_longest kullan
# ✔ fillvalue=0 → kısa listeyi güvenli şekilde tamamlar
# ✔ Gerçek projelerde önerilen yöntem:
#
#     zip_longest(list1, list2, fillvalue=0)
#
# =============================================================================