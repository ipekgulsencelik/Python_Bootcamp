# ===============================================================
# 100.000 RASTGELE SAYI ÜRETME & 3 FARKLI YÖNTEMLE POZİTİF BULMA
# ===============================================================
# Bu dosyada pozitif sayıları 3 farklı yöntemle bulacağız:
#
#   ✔ Path I   → List Comprehension
#   ✔ Path II  → filter() fonksiyonu (lambda ile)
#   ✔ Path III → For Loop (klasik yöntem)
#
# Her yöntemde:
#   → Çalışma süresini (time cost)
#   → Bellek kullanımını (memory cost)
# ölçeceğiz ve rapor olarak ekrana yazacağız.
#
# ===============================================================
# NEDEN BÖYLE BİR KARŞILAŞTIRMA?
# ---------------------------------------------------------------
# Aynı veri üzerinde farklı tekniklerin performans karşılaştırması:
#   • Hangi yapının daha hızlı olduğunu
#   • Hangi yapının daha hafif olduğunu
#   • Python’ın C tabanlı optimizasyon farklarını
# anlamamızı sağlar.
#
# Aynı veri üzerinde farklı tekniklerin performansını karşılaştırmak
# hangi yaklaşımın daha hızlı ve daha az bellek tükettiğini görmemizi sağlar.
# Bu da gerçek projelerde doğru veri işleme tekniğini seçmek için çok kritiktir.
# ===============================================================


# region Importlar (Zorunlu Kütüphaneler)
import random       # rastgele sayı üretmek için
import time         # zaman ölçümü için
import tracemalloc  # bellek (RAM) kullanımı ölçümü için
# endregion


# region 100.000 Rastgele Sayı Üretme
# ---------------------------------------------------------------
# Aşağıdaki satır 100.000 adet rastgele sayı üretir.
# randint(-5000, 5000) → -5000 ile +5000 arası sayılar
# range(100_000) → 100.000 tekrar anlamına gelir
#
# NOT - MEMORY:
# Python listeleri RAM'de dinamik array olarak tutulur.
# Her eleman eklenirken kapasite genişleyebilir.
# ---------------------------------------------------------------

print("📌 100.000 rastgele sayı üretiliyor...\n")

NUMBERS = [random.randint(-5000, 5000) for _ in range(100_000)]
# endregion



# ===============================================================
#           Big-O ANALİZİ (ZAMAN & BELLEK KARMASIKLIĞI)
# ===============================================================
# Üç yöntemin teorik karmaşıklığı aynıdır:
#
#   ✔ List Comprehension → O(n)
#   ✔ filter()           → O(n)
#   ✔ For Loop           → O(n)
#
# Bellek karmaşıklığı (Space Complexity) da teorik olarak:
#
#   ✔ O(n) — Pozitif değerlerden yeni bir liste üretildiği için.
#
# Performans farkı "Big-O"dan DEĞİL,
# Python’ın iç optimizasyon katmanından gelir.
# ===============================================================



# ===============================================================
#                 YARDIMCI FONKSİYON: measure_performance
# ===============================================================
# Bu fonksiyon her yöntemin:
#   - Başlama zamanını
#   - Bitiş zamanını
#   - Bellek kullanımını
# ölçüp rapor olarak bastırır.
# 
# ------------------------------------------------------------
# Neden time.perf_counter()?
# --------------------------
# time.time() → sistem saatine bağlıdır, hassasiyeti düşüktür.
# time.perf_counter() → yüksek çözünürlüklü sayaçtır.
# Mikro benchmark'lar için perf_counter kullanmak daha doğrudur.
#
# ------------------------------------------------------------
# MEMORY COST AÇIKLAMASI
# ------------------------------------------------------------
# tracemalloc.get_traced_memory() fonksiyonu 2 değer döndürür:
#   1) current → ŞU ANKİ bellek kullanımı (byte cinsinden)
#   2) peak    → EN YÜKSEK bellek kullanımı (byte cinsinden)
#
# Biz bu değerleri daha okunabilir olması için KB (kilobyte)
# cinsine çeviriyoruz. 1 KB = 1024 byte'tır.
#
# Memory Current:
#   Fonksiyon çalıştıktan sonra RAM’de o an kapladığı alan.
#
# Memory Peak:
#   Fonksiyon çalışırken RAM kullanımının ulaştığı TEPE noktası.
#   Yani geçici olarak en yoğun bellek yükünü ölçer.
#
# ------------------------------------------------------------
# EK NOT — PYTHON BELLEK ALLOCATOR
# ------------------------------------------------------------
# Python list() yapısı dinamik array kullanır:
#   • append() işlemi gerektiğinde kapasiteyi genişletir
#   • Bu işlem çok ufak RAM sıçramaları oluşturur (peak'i artırır)
#
# LC ve filter() daha "toplu" çalıştığı için peak genelde daha düşüktür.
# ===============================================================

def measure_performance(func, description):
    """
    Verilen fonksiyonun çalışma süresini ve bellek kullanımını ölçer.
    """

    print(f"▶ {description}")

    # Bellek takibi başlat
    tracemalloc.start()

    # Zamanı kaydet (başlangıç)
    start = time.perf_counter()

    # Fonksiyonu çalıştır
    result = func()

    # Zamanı kaydet (bitiş)
    end = time.perf_counter()

    # Bellek bilgilerini al
    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    # Sonuçları ekrana yazdır
    print(f"   ⏱  Time Cost     : {end - start:.6f} saniye")    # bitiş zamanı – başlangıç zamanı = geçen süre (saniye)
    print(f"   🧠 Memory Current: {current / 1024:.2f} KB")     # O anki RAM kullanımı
    print(f"   📈 Memory Peak   : {peak / 1024:.2f} KB")        # En yüksek RAM kullanımı
    print(f"   📌 Sonuç uzunluğu: {len(result)}\n")

    return result



# ===============================================================
#                PATH I → List Comprehension
# ===============================================================
# Python’da en hızlı ve en "pythonic" yöntemdir.
# Tek satırda filtreleme yapılır.
#
# NEDEN HIZLI?
#   • Python'un C tabanlı iç motorunda optimize edilir.
#   • Döngü, append gibi adımlar yoktur.
#   • Tek seferde, vectorized gibi davranır.
# ===============================================================

# region PATH I → List Comprehension
def path_list_comprehension():
    # Pozitif olanları seç
    return [n for n in NUMBERS if n > 0]
# endregion



# ===============================================================
#                PATH II → filter() + lambda
# ===============================================================
# filter() fonksiyonu, True dönen değerleri listeye dahil eder.
# lambda, küçük anonim fonksiyon yazmamızı sağlar.
#
# filter() FARKI:
#   • Filtreleme C seviyesinde yapılır → hızlıdır
#   • Ancak lambda bir Python objesi olduğundan
#     biraz overhead ekler
# ===============================================================

# region PATH II → filter()
def path_filter():
    # filter True döndürürse elemanı seçer → lambda: x > 0
    return list(filter(lambda x: x > 0, NUMBERS))
# endregion



# ===============================================================
#                PATH III → For Loop (Klasik)
# ===============================================================
# En temel yöntemdir. Genellikle en yavaş olanıdır.
# Çünkü her adımda append yapılır.
#
# NEDEN YAVAŞ?
#   • Python seviyesinde döner (C değil)
#   • Her append() bir fonksiyon çağrısıdır
#   • Interpreter overhead yüksektir
# ===============================================================

# region PATH III → For Loop
def path_for_loop():
    positives = []  # boş liste başlat
    for n in NUMBERS:
        if n > 0:   # pozitif mi?
            positives.append(n)
    return positives
# endregion




# ===============================================================
#             CPU / CACHE / TURBO BOOST TEKNİK NOTU
# ===============================================================
# Benchmark sonuçları:
#   • CPU’nun o anki sıcaklığına
#   • Turbo Boost açık olup olmamasına
#   • Cache hit/miss durumuna
#   • Arka planda çalışan uygulamalara
# bağlı olarak %1–5 oynayabilir.
#
# Bu normaldir. Mikro-benchmark’ların doğası böyledir.
# ===============================================================



# ===============================================================
#                    BENCHMARK RAPOR BAŞLANGICI
# ===============================================================

print("============== PERFORMANCE REPORT ==============\n")

measure_performance(path_list_comprehension,
                    "Path I  → List Comprehension ile pozitiflerin bulunması")

measure_performance(path_filter,
                    "Path II → filter() fonksiyonu ile pozitiflerin bulunması")

measure_performance(path_for_loop,
                    "Path III → For Loop ile pozitiflerin bulunması")

print("================================================")
print("✔ Benchmark tamamlandı.")


# ===============================================================
#                     ÖZET
# ===============================================================
# ✔ En hızlı yöntem → List Comprehension
# ✔ Orta seviye → filter()
# ✔ En yavaş → Klasik For Loop
#
# ✔ Bellek kullanımı farkları küçük olsa da
#   zaman farkı belirgindir.
#
# ✔ Gerçek projelerde:
#     Performans + okunabilirlik için LC en iyi tercihtir.
# ===============================================================