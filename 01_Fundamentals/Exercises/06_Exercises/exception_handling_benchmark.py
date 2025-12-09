# ===============================================================
# TRY / EXCEPT vs IF / ELSE vs RAISE - PERFORMANCE BENCHMARK
# ===============================================================
# Bu dosyada 3 farklı hata yönetim yaklaşımını kıyaslıyoruz:
#
#   ✔ Method 1 → Try / Except
#   ✔ Method 2 → If / Else (saf koşul kontrolü)
#   ✔ Method 3 → Raise + Except (manuel hata fırlatma)
#
# Her yöntemde:
#   → Çalışma süresi (runtime, s)
#   → Bellek kullanımı (peak memory, MB)
# ölçülür.
#
#   - Amaç: try/except, if/else ve raise maliyet farkını görmek ve anlamak.
# ===============================================================


# region Performance Benchmark
import time                  # Çalışma süresini ölçmek için
import tracemalloc           # Bellek kullanımını izlemek için


tracemalloc.start()                 # Bellek takibini başlatıyoruz
t1 = time.perf_counter()            # Yüksek çözünürlüklü zaman sayacı (başlangıç)

# region Try/Except
# try:
#     bolunen = int(input('Bolunen: '))
#     bolen = int(input('Bolen: '))
#     sonuc = bolunen / bolen
#     print(f'Sonuc: {sonuc}')
# except (ZeroDivisionError, ValueError) as err:
#     print('Bir tam sayı sıfıra bölünemez..!')
#     #! kendimize mail gönderiyoruz
#     #* log --> uygulamada ne oldu ne bitti bunların kayıtlarının tutulmasına "log" denir
#     print(f'{err}')
# finally:
#     print('Ne olursa olsun çalışırım')
# endregion


# region If/Else
# bolunen = input("Bolunen: ")
# bolen = input("Bolen: ")

# if not (bolunen.lstrip("-").isdigit() and bolen.lstrip("-").isdigit()):
#     print("Bir tam sayı girmelisiniz..!")   # ValueError alternatifi
#     print("ValueError")
#     print("Ne olursa olsun çalışırım")
# else:
#     bolunen = int(bolunen)
#     bolen = int(bolen)

#     if bolen == 0:
#         print("Bir tam sayı sıfıra bölünemez..!")   # ZeroDivisionError alternatifi
#         print("ZeroDivisionError")
#         print("Ne olursa olsun çalışırım")
#     else:
#         sonuc = bolunen / bolen
#         print(f"Sonuc: {sonuc}")
#         print("Ne olursa olsun çalışırım")
# endregion


# region Raise+Except

# try:
#     bolunen = int(input('Bolunen: '))
#     bolen = int(input('Bolen: '))

#     # Manuel koşul kontrolü → raise ile hata fırlatma
#     if bolen == 0:
#         raise ZeroDivisionError("Bölen 0 olamaz..!")

#     # Bölme işlemi
#     sonuc = bolunen / bolen
#     print(f"✔ Sonuç: {sonuc}")
    
# except ValueError:
#     print("❌ Lütfen sadece sayısal değer giriniz!")

# except ZeroDivisionError as err:
#     # raise ile fırlattığımız hatayı burada yakalıyoruz
#     print("❌", err)

# except Exception as ex:
#     # Beklenmeyen diğer hatalar
#     print("❌ Beklenmeyen hata:", ex)

# endregion


t2 = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()
# current → şu an izleme sırasında kullanılan bellek (byte)
# peak    → izleme süresince görülen en yüksek bellek kullanımı (byte)

tracemalloc.stop()

runtime_s = (t2 - t1)   # saniye cinsinden çalışma süresi
peak_memory = peak / 1024 / 1024    # byte → MB

print(
    '===============================\n'
    'Method --> Raise+Except\n'
    f'Runtime: {runtime_s:.6f} s\n'
    f'Peak Memory: {peak_memory:.8f} MB' 
)


# region SUMMARY (PERFORMANCE RESULT)
"""
==============================================================
                🧾 PERFORMANCE SUMMARY
==============================================================

Bu benchmark çalışmasında 3 yöntemi karşılaştırdık:

    ✔ Try / Except
    ✔ If / Else
    ✔ Raise + Except

Aşağıda genel ve tutarlı sonuçların özeti bulunmaktadır:

--------------------------------------------------------------
🥇 1) IF / ELSE → EN HIZLI (WINNER)
--------------------------------------------------------------
Neden?
- Exception mekanizması kurulmaz.
- Sadece basit bir koşul kontrolü yapılır.
- Raise yok → stack trace yok → interpreter overhead düşük.

Sonuç:
- Runtime: En düşük
- Memory: En stabil
- Büyük döngülerde, sık yapılan validation fonksiyonları için ideal.

--------------------------------------------------------------
🥈 2) TRY / EXCEPT → ORTA SEVİYE
--------------------------------------------------------------
Neden?
- Hata olsa da olmasa da exception frame oluşturulur.
- Bu yüzden her iterasyonda küçük bir ek maliyet vardır. 
- Bu küçük ek maliyet yüzünden If/Else’den daha yavaştır.

Sonuç:
- Runtime: Orta
- Memory: Stabil
- Hafif bir overhead vardır ama Raise kadar yüksek değildir.
- Kullanıcıdan input alma, IO işlemleri, kritik olmayan kodlarda, pratik durumlarda mantıklı.

--------------------------------------------------------------
🥉 3) RAISE + EXCEPT → EN YAVAŞ
--------------------------------------------------------------
Neden?
- Her invalid veri için raise → exception objesi oluşturulur.
- Stack trace hazırlanır.
- Control flow except bloğuna sıçrar.
- Ek olarak fonksiyon çağrısı maliyeti eklenir.

Yani: Fonksiyon maliyeti + raise maliyeti + exception handling maliyeti → en yüksek yük

Sonuç:
- Runtime: En yüksek
- Memory: Normal
- Memory genelde düşük görünür ama bu önemsenmez.
- Sık çağrılan döngülerde kaçınılması gerekir.
- Sadece gerçekten “hata fırlatılması gereken” özel durumlarda kullanılmalı.

--------------------------------------------------------------
📌 GENEL TABLO
--------------------------------------------------------------
Method         | Runtime       | Memory       | Uygun Senaryolar
-----------------------------------------------------------------
If/Else        | 🟢 En hızlı    | 🟢 En Stabil  | En sık tekrar eden validasyonlar, büyük döngüler
Try/Except     | 🟡 Orta        | 🟢 Stabil     | Normal input işlemleri, beklenen hatalar
Raise+Except   | 🔴 En yavaş    | 🟡 Normal     | Gerçek hata fırlatma, kritik olmayan döngüler

--------------------------------------------------------------
🧠 KISA ÖZET
--------------------------------------------------------------
Performans açısından: If/Else daima en iyi sonuç, çünkü en temel kontrol → en düşük maliyet.
Kod netliği açısından: Try/Except çoğu zaman en okunabilir ve en güvenli yaklaşım.
Gerçek hata yönetimi açısından: Raise, "iş mantığı bozuldu → akışı durdur" demek için şarttır ama pahalıdır.

- Performans istiyorsan → IF / ELSE
- Kod güvenliği + okunabilirlik istiyorsan → TRY / EXCEPT
- Gerçek bir hata durumunu durdurmak için → RAISE

==============================================================
"""
# endregion