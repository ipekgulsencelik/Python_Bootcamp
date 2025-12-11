
#! Generator vs List Comprehension — Performance & Memory Benchmark
# =============================================================================
# AMAÇ:
#   - Python'da veri üretmenin iki yaygın yöntemi olan:
#         ✔ Generator Expression
#         ✔ List Comprehension
#     yapılarını performans ve bellek kullanımı açısından karşılaştırmak.
#
# AÇIKLAMA:
#   - Generator → Lazy evaluation kullanır. Veriyi TEK TEK üretir.
#       → Bellek tüketimi çok düşüktür.
#       → Çok büyük veri setleri için idealdir.
#
#   - List Comprehension → Tüm listeyi RAM’e YÜKLER.
#       → Erişim hızlıdır fakat bellek maliyeti yüksektir.
#
# Bu dökümanda:
#   • 1 milyon eleman üretilecek
#   • Runtime (ms) ve Peak Memory (MB) ölçülecek
# =============================================================================


# =============================================================================
# IMPORTS
# =============================================================================
import time                # Çalışma süresi ölçümü
import tracemalloc         # Bellek kullanım takibi
from random import randint # Rastgele sayı üretimi


# =============================================================================
# FUNCTION: benchmark()
# =============================================================================
def benchmark(label, iterable):
    """
    Verilen iterable üzerinde zaman ve bellek ölçümü yapar.
    Generator ise iterate edilerek gerçek tüketim sağlanır.
    """
    # Bellek ve zaman takibini başlat
    tracemalloc.start()                  # Bellek takibini başlat
    t_start = time.perf_counter()         # Başlangıç zamanı

    # Iterable tüketiliyor (generator ise lazy üretimi tetikler)
    for _ in iterable:
        pass

    # Ölçümler
    t_end = time.perf_counter()           # Bitiş zamanı
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    runtime_ms = (t_end - t_start) * 1000
    peak_mb = peak / 1024 / 1024

    print(f"{label:<22} -> Runtime: {runtime_ms:.2f} ms | Peak memory: {peak_mb:.4f} MB")


# =============================================================================
# REGION — TEST 1: GENERATOR EXPRESSION
# =============================================================================
# Not: Generator sonuçları RAM’e yüklemez. 
# Bu nedenle bellekte neredeyse hiç yer kaplamaz.
generator_data = (randint(a=1, b=100) for _ in range(1_000_000))
benchmark("Generator Expression", generator_data)


# =============================================================================
# REGION — TEST 2: LIST COMPREHENSION
# =============================================================================
list_data = [randint(a=1, b=100) for _ in range(1_000_000)]
benchmark("List Comprehension", list_data)


# =============================================================================
# REGION — NOTES
# =============================================================================
# ✔ List Comprehension genelde daha hızlıdır, fakat RAM tüketimi yüksektir.
# ✔ Generator çok düşük bellek kullanır, fakat lazy evaluation nedeniyle
#   bazen biraz daha yavaş olabilir.
# ✔ “Peak memory” → test sırasında görülen en yüksek bellek tüketimidir.
#
# Ne zaman hangisi?
#   • Çok büyük veri setlerinde → GENERATOR
#   • Küçük/orta veri + hızlı erişim gerekiyorsa → LIST COMPREHENSION
# =============================================================================