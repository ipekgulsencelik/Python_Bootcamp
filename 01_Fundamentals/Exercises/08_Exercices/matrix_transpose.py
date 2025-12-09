# ===============================================================
# File: matrix_transpose.py
# Purpose:
#   - 3x4 rastgele bir matrix üretmek
#   - Transpose işlemini 2 farklı yöntemle göstermek:
#       1) Manual For Loop (klasik yaklaşım)
#       2) zip(*matrix) (Pythonic yaklaşım)
# ===============================================================

from random import randint


# region Generate Random Matrix (3x4) + Transpose

# Rastgele 3x4 matrix üretelim
#    - Her satır 4 sayıdan oluşacak
#    - Toplam 3 satır olacak

matrix = [
    [randint(10, 99) for _ in range(4)]   # 4 kolon → 4 rastgele sayı
    for _ in range(3)                     # 3 satır
]

print("Original Matrix:")
for row in matrix:
    print(row)

# Matris boyutlarını belirleyelim
rows = len(matrix)       # satır sayısı
cols = len(matrix[0])    # kolon sayısı (ilk satırın uzunluğu)

# endregion


# region Transpose — Manual For Loop

# Bu yöntem, klasik “algoritmik” transpose yaklaşımıdır.
# Mantık:
#   - Yeni listede (transpose_manual) her kolon için bir liste oluşturuyoruz.
#   - new_col her seferinde matrix[r][c] değerlerini toplar.
#   - Böylece satırlar kolon, kolonlar satır olur.

transpose_manual = []

for col in range(cols):         # her kolon için
    new_col = []                # o kolona ait yeni liste
    for row in range(rows):     # ilgili kolonun tüm satırlarını gez
        new_col.append(matrix[row][col])
    transpose_manual.append(new_col)

print("\nTranspose (manual for-loop):")
for col in transpose_manual:
    print(col)

# endregion


# region Transpose — zip(*matrix)

# zip(*matrix) → satırları kolonlara çevirir.
# * operatörü iç listeleri zip'e ayrı argümanlar olarak yollar.
# zip() func tuple döndürdüğü için, list() ile listeye çeviriyoruz.
#
# Açıklama:
#   - * operatörü, matrix içindeki her satırı ayrı argüman olarak zip'e gönderir:
#         zip(row1, row2, row3, ...)
#   - zip, aynı index'e sahip elemanları bir araya toplar:
#         (row1[0], row2[0], row3[0])  → 1. kolon
#         (row1[1], row2[1], row3[1])  → 2. kolon
#   - Sonuç olarak satırlar kolonlara dönüşür → transpose elde edilir.
#   - zip tuple döndürdüğü için, list() ile listeye çeviriyoruz.

transpose_zip = list(zip(*matrix))

print("\nTranspose (zip method):")
for col in transpose_zip:
    print(col)

# endregion