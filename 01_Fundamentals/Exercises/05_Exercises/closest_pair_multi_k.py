# -------------------------------------------------------------
# PROBLEM:
#  - Sıralı (sorted) bir tam sayı listesinden
#  - Toplamı k değerine en yakın olan tüm çiftleri bul.
#  - Toplam k'dan küçük, büyük veya eşit olabilir.
#  - Liste elemanları pozitif tam sayılardır.
#  - Birden fazla k değeri için analiz yapılabilir.
# -------------------------------------------------------------

# -------------------------------------------------------------
# 1) KULLANICIDAN LİSTEYİ AL
# -------------------------------------------------------------
while True:
    raw_input_numbers = input("Lütfen POZİTİF tam sayı listesini boşluk bırakarak giriniz: ")
    # Örnek: 5 8 14 17 25

    raw_input_numbers = raw_input_numbers.strip()

    # Boş giriş kontrolü
    if not raw_input_numbers:
        print("⚠ En az 2 sayı girmelisiniz. Örnek: 5 8 14")
        continue

    tokens = raw_input_numbers.split()

    arr = []
    valid = True

    for token in tokens:
        try:
            num = int(token)
        except ValueError:
            print(f"⚠ Geçersiz değer: '{token}'. Lütfen sadece TAM SAYI giriniz.")
            valid = False
            break

        # Pozitif kontrolü
        if num <= 0:
            print(f"⚠ '{num}' pozitif bir tam sayı değil. Lütfen sadece pozitif tam sayılar giriniz.")
            valid = False
            break

        arr.append(num)

    # Eğer tip / pozitiflik açısından problem varsa başa dön
    if not valid:
        continue

    # En az 2 sayı olmalı
    if len(arr) < 2:
        print("⚠ En az 2 sayı girmeniz gerekiyor.")
        continue

    # Buraya geldiysek giriş geçerli
    break

# -------------------------------------------------------------
# 2) BİRDEN FAZLA k DEĞERİ AL
# -------------------------------------------------------------
while True:
    raw_k_values = input("Hedef k değerlerini boşluk bırakarak giriniz (ör: 10 20 35): ")

    raw_k_values = raw_k_values.strip()

    if not raw_k_values:
        print("⚠ En az bir tane k değeri girmelisiniz. Örnek: 10 20 35")
        continue

    tokens_k = raw_k_values.split()
    k_values = []
    valid_k = True

    for token in tokens_k:
        try:
            val = int(token)
        except ValueError:
            print(f"⚠ Geçersiz k değeri: '{token}'. Lütfen sadece TAM SAYI giriniz.")
            valid_k = False
            break

        if val <= 0:
            print(f"⚠ '{val}' pozitif bir tam sayı değil. Lütfen pozitif tam sayılar giriniz.")
            valid_k = False
            break

        k_values.append(val)

    if not valid_k:
        continue

    # Buraya geldiysek k değerleri geçerli
    break

# -------------------------------------------------------------
# 3) LİSTEYİ SIRALA (tek seferlik)
# -------------------------------------------------------------
# arr.sort()

n = len(arr)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            # Yer değiştirme
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sıralanmış liste:", arr)

print("\n📌 Kullanılan sıralanmış liste:", arr)
print("📌 Analiz edilecek k değerleri:", k_values)

# -------------------------------------------------------------
# 4) HER k İÇİN AYRI AYRI ANALİZ YAP
# -------------------------------------------------------------
for k in k_values:
    print("\n" + "=" * 60)
    print(f"🔎 k = {k} için analiz başlıyor...")
    print("=" * 60)

    # İki uçtan başlayacak pointer'lar:
    left = 0
    right = len(arr) - 1

    # En iyi farkı başlangıçta sonsuz (çok büyük) kabul ediyoruz.
    best_diff = float("inf")

    # k'ya en yakın olan TÜM çiftleri burada saklayacağız.
    best_pairs = []

    # 1) Tam olarak k'ye eşit olan çiftler
    equal_pairs = []

    # 2) k'den küçük tarafta en yakın çiftler
    best_below_diff = float("inf")
    best_below_pairs = []

    # 3) k'den büyük tarafta en yakın çiftler
    best_above_diff = float("inf")
    best_above_pairs = []

    # ----------------- Two-pointer döngüsü -----------------
    while left < right:
        a = arr[left]
        b = arr[right]
        current_sum = a + b      # Şu anki iki sayının toplamı
        current_diff = abs(current_sum - k)   # k'ya olan mutlak fark
        pair = (a, b)

        # 0) Genel olarak k'ya en yakın çift(ler)
        if current_diff < best_diff:
            best_diff = current_diff
            best_pairs = [pair]
        elif current_diff == best_diff:
            if pair not in best_pairs:
                best_pairs.append(pair)

        # 1) Toplamı tam k'ye eşit olan çift(ler)
        if current_sum == k:
            if pair not in equal_pairs:
                equal_pairs.append(pair)

        # 2) k'den küçük tarafta en yakın çift(ler)
        if current_sum < k:
            below_diff = k - current_sum

            if below_diff < best_below_diff:
                best_below_diff = below_diff
                best_below_pairs = [pair]
            elif below_diff == best_below_diff:
                if pair not in best_below_pairs:
                    best_below_pairs.append(pair)

        # 3) k'den büyük tarafta en yakın çift(ler)
        if current_sum > k:
            above_diff = current_sum - k

            if above_diff < best_above_diff:
                best_above_diff = above_diff
                best_above_pairs = [pair]
            elif above_diff == best_above_diff:
                if pair not in best_above_pairs:
                    best_above_pairs.append(pair)

        # Pointer hareket mantığı
        if current_sum < k:
            left += 1
        else:
            right -= 1

    # ----------------- SONUÇLARI YAZDIR -----------------
    print(f"\n✅ k = {k} için işlem tamamlandı.")
    print("Genel olarak k'ya en yakın fark:", best_diff)
    print("Genel en yakın çift(ler):")
    for p in best_pairs:
        print(f"{p} -> toplam: {p[0] + p[1]} (fark: {abs(p[0] + p[1] - k)})")

    print("\n🎯 Toplamı tam olarak k'ye eşit olan çiftler:")
    if equal_pairs:
        for p in equal_pairs:
            print(f"{p} -> toplam: {p[0] + p[1]} (fark: 0)")
    else:
        print("Bu listede toplamı tam olarak k'ye eşit olan bir çift yok.")

    print("\n⬇ k'den KÜÇÜK tarafta en yakın çift(ler):")
    if best_below_pairs and best_below_diff != float("inf"):
        print("En küçük fark (k - sum):", best_below_diff)
        for p in best_below_pairs:
            print(f"{p} -> toplam: {p[0] + p[1]} (k - sum = {k - (p[0] + p[1])})")
    else:
        print("k'den küçük hiçbir toplam yok.")

    print("\n⬆ k'den BÜYÜK tarafta en yakın çift(ler):")
    if best_above_pairs and best_above_diff != float("inf"):
        print("En küçük fark (sum - k):", best_above_diff)
        for p in best_above_pairs:
            print(f"{p} -> toplam: {p[0] + p[1]} (sum - k = {(p[0] + p[1]) - k})")
    else:
        print("k'den büyük hiçbir toplam yok.")

    # ----------------- ÖZET TABLO HAZIRLAMA -----------------
    all_summary_rows = []

    # Tam eşit olanlar (fark = 0)
    for p in equal_pairs:
        s = p[0] + p[1]
        all_summary_rows.append((p, s, 0, "eşit"))

    # Küçük taraftaki en yakınlar
    for p in best_below_pairs:
        s = p[0] + p[1]
        diff = abs(s - k)
        all_summary_rows.append((p, s, diff, "k'den küçük"))

    # Büyük taraftaki en yakınlar
    for p in best_above_pairs:
        s = p[0] + p[1]
        diff = abs(s - k)
        all_summary_rows.append((p, s, diff, "k'den büyük"))

    # Aynı çifti iki kere eklememek için benzersiz hale getirelim
    unique_rows = []
    seen_pairs = set()
    for row in all_summary_rows:
        pair_key = row[0]
        if pair_key not in seen_pairs:
            seen_pairs.add(pair_key)
            unique_rows.append(row)

    # Farka göre (diff) küçükten büyüğe, sonra toplam'a göre sırala
    unique_rows.sort(key=lambda x: (x[2], x[1]))

    print("\n📊 ÖZET TABLO (farka göre küçükten büyüğe sıralı):")
    if unique_rows:
        print("Çift        Toplam    |sum - k|    Konum")
        for row in unique_rows:
            pair, s, diff, position = row
            print(f"{pair}   {s:7d}   {diff:9d}   {position}")
    else:
        print("Özet oluşturulacak uygun çift bulunamadı.")