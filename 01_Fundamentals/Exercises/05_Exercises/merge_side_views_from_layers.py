# ---------------------------------------------------------
# BINARY TREE SIDE-VIEW PROBLEM
# ---------------------------------------------------------
# Elimizde gerçek bir ikili ağaç (TreeNode) yok.
# Bunun yerine ağacı "katman katman" tutan bir liste var: all_parts
#
# Amaç:
#   1) Soldan baktığımızda gördüğümüz düğümler (bottom-up)
#   2) Sağdan baktığımızda gördüğümüz düğümler (top-down)
#   3) Bu iki görünümü tek bir listede birleştirmek
#
# Sol görünüm:  Her seviyenin İLK elemanı
# Sağ görünüm:  Her seviyenin SON elemanı
#
# Sol görünüm bottom-up istendiği için:
#   -> önce top-down çıkaracağız
#   -> sonra tersine çevrilmiş halini kullanacağız
#
# Sonuç = left_bottom_up + (right_top_down'daki yeni düğümler)
# ---------------------------------------------------------


# INPUT → Binary Tree katmanları
all_parts = [
    [1],        # Katman 1 (root)
    [2, 3],     # Katman 2
    [4, 6],     # Katman 3
    [5, 9, 7]   # Katman 4 (en alt)
]

left_view = []   # Soldan görünüm (önce top-down toplanacak)
right_view = []  # Sağdan görünüm (top-down)


# LEFT + RIGHT VIEW TOP-DOWN
for part in all_parts:
    # Sol görünüm → Her seviyenin ilk elemanı
    left_view.append(part[0])

    # Sağ görünüm → Her seviyenin son elemanı
    right_view.append(part[-1])


# Left view bottom-up istendiği için ters liste üret
left_view = left_view[::-1]   # Artık left_view bottom-up

print("Left View (bottom-up):", left_view)
print("Right View (top-down):", right_view)

binary_tree = []   # Final sonuç listesi

# left_view + right_view
# → İki listeyi arka arkaya tek bir liste gibi dolaşmamızı sağlar.
for value in left_view + right_view:
    if value not in binary_tree:
        binary_tree.append(value)

# SONUÇ
print("Left (bottom-up):", left_view)
print("Right (top-down):", right_view)
print("Final:", binary_tree)