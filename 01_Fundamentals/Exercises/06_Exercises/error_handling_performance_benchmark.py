"""
=====================================================================
        ERROR HANDLING PERFORMANCE BENCHMARK (try vs if vs raise)
=====================================================================

Amaç:
    Python'da 3 farklı hata yönetim yaklaşımının performansını 
    (runtime + peak memory) karşılaştırmak:

        1) try / except
        2) if / else (koşul kontrolü)
        3) raise + except (manuel hata fırlatma)

Neden?
    Exception fırlatmanın ne kadar pahalı olduğunu görmek için.
    Özellikle sık gerçekleşen hatalarda if/else'in neden tercih 
    edilmesi gerektiğini göstermek için.

Beklenen Sonuç:
    En hızlı → if/else
    Orta      → try/except (otomatik ZeroDivisionError)
    En yavaş  → raise (manuel exception)

Not:
    Bu test her yöntemi tam 1.000.000 kez çalıştırır.
    Hata sürekli oluştuğu için istisna mekanizmasının maliyeti
    maksimum seviyede görülür.

=====================================================================
"""

import time
import tracemalloc


# =====================================================================
# 1) TRY / EXCEPT APPROACH
#    - Python bölme işleminde otomatik ZeroDivisionError fırlatır.
#    - Exception yaratma + traceback toplama maliyetlidir.
# =====================================================================
def with_try():
    for _ in range(1000000):
        try:
            x = 4
            y = 0
            z = x / y
        except ZeroDivisionError:
            pass


# =====================================================================
# 2) IF / ELSE APPROACH
#    - Hata yok.
#    - Sadece koşul kontrolü yapıldığı için çok hızlıdır.
# =====================================================================
def with_if():
    for _ in range(1000000):
        x = 4
        y = 0
        if y != 0:
            z = x / y
        else:
            pass


# =====================================================================
# 3) RAISE APPROACH
#    - Hata otomatik oluşmaz, biz manuel raise ederiz.
#    - Yeni bir ZeroDivisionError objesi yaratılır → en maliyetli yöntem.
# =====================================================================
def with_raise():
    for _ in range(1000000):
        try:
            x = 4
            y = 0
            if y == 0:
                raise ZeroDivisionError("Manual")
            z = x / y
        except ZeroDivisionError:
            pass


# =====================================================================
# 4) BENCHMARK HELPER FUNCTION
#    - Memory: tracemalloc.get_traced_memory()
#    - Time: time.perf_counter()
# =====================================================================
def benchmark(func, label: str):
    tracemalloc.start()
    t0 = time.perf_counter()

    func()

    t1 = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    runtime_ms = (t1 - t0) * 1000
    peak_mb = peak / 1024 / 1024

    print(f"{label} -> Runtime: {runtime_ms:.2f} ms | Peak memory: {peak_mb:.4f} MB")


benchmark(with_try, "with_try")
benchmark(with_if, "with_if")
benchmark(with_raise, "with_raise")