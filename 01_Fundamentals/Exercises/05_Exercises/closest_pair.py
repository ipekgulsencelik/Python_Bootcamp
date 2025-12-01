# Find and return a pair of integers in a sorted list (all integers are positive)
# that when summed, give you the closest value to k.
# Example Input: [5, 8, 14, 17, 25]
# Expected Output: (8, 25) since 8 + 25 = 33 
# (which is closest to 35 sum could be equals to, smaller or larger than k)

lst = [5, 8, 14, 17, 25]
k = 35

# Listenin başını ve sonunu gösteren pointerlar
left = 0
right = len(lst) - 1

# Başlangıçta en iyi çift olarak ilk ve son elemanı alıyoruz
best_pair = (lst[left], lst[right])
best_diff = abs((lst[left] + lst[right]) - k)   # k'ya uzaklık

# İki pointer birbirine yaklaşana kadar devam et
while left < right:
    current_sum = lst[left] + lst[right]    # Şu anki iki sayının toplamı
    current_diff = abs(current_sum - k)     # k'ya olan farkı

    # En yakın toplamı bulduğumuzda güncelle
    if current_diff < best_diff:
        best_diff = current_diff
        best_pair = (lst[left], lst[right])

    # Toplam küçükse artır (daha büyük toplam bul)
    if current_sum < k: # Eğer toplam k'dan küçükse, toplamı artırmak için sol pointer ilerletilir
        left += 1
    else:   # Toplam k'dan büyükse, toplamı azaltmak için sağ pointer geri gider
        right -= 1

print("En yakın çift:", best_pair)