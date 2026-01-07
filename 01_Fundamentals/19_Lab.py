
#! Decorator
#   - Var olan bir fonksiyonu DEĞİŞTİRMEDEN, ona ekstra davranış eklememizi sağlar.
# Fonksiyonları "sarar" (wrap eder)

# Nasıl çalışır?
#   - Bir fonksiyonu parametre olarak alır
#   - İçinde yeni bir fonksiyon (wrapper) tanımlar
#   - Orijinal fonksiyonu bu wrapper ile "sararak" geri döndürür

# Yani:
#   Fonksiyonun içine dokunmadan,
#   fonksiyon çalışmadan ÖNCE veya fonksiyon çalıştıktan SONRA ek kod çalıştırabiliriz.

# Temel Amaç:
# ✔ Var olan kodu bozmadan genişletmek
# ✔ Tekrar eden kodları merkezi bir yerde toplamak
# ✔ Daha temiz, okunabilir ve bakımı kolay kod yazmak

# En çok nerede kullanılır?
#   ✔ Loglama (request / response)
#   ✔ Yetkilendirme (role, JWT)
#   ✔ süre ölçme
#   ✔ login kontrolü
#   ✔ Performans ölçümü
#   ✔ Cache (memoization)
#   ✔ Retry (hata olunca tekrar dene)
#   ✔ Validation
#   ✔ Rate limiting
#   ✔ Transaction yönetimi

#   ✔ Bir fonksiyon birden fazla decorator alabilir
#   ✔ Sıra: yukarıdan aşağı TANIM, aşağıdan yukarı ÇALIŞMA
#   ✔ Decorator parametre alabilir (Decorator Factory)

# region Basic Decorator
# def my_decorator(func):
#     """
#     Parametre olarak bir fonksiyon alır.
#     Bu fonksiyon, decorator ile sarılacak olan asıl fonksiyondur.

#     Mantık:
#         - func: asıl fonksiyon (dekoratörün saracağı fonksiyon)
#         - wrapper: func çağrılmadan önce/sonra ekstra iş yapan katman
#     """

#     def wrapper():
#         """
#         Wrapper fonksiyon:
#         - Asıl fonksiyonu saran (wrap eden) fonksiyondur.
#         - Buraya yazılan kodlar:
#             * fonksiyon çalışmadan önce
#             * fonksiyon çalıştıktan sonra
#           otomatik olarak devreye girer.
#         """

#         # ⏱️ Fonksiyon çalışmadan ÖNCE
#         print('Bazı işler burada çalıaşcak..!')

#         # 🎯 Asıl fonksiyonun çağrılması
#         func()

#         # ⏱️ Fonksiyon çalıştıktan SONRA
#         print('belki bazı işlerde burada çalışacak..!')
    
#     return wrapper

# @my_decorator
# def hello():
#     """
#     Basit bir fonksiyon.
#     Decorator sayesinde bu fonksiyonun
#     öncesine ve sonrasına ekstra davranış eklenmiş olacak.
#     """
#     print('Merhaba')

# hello()   # hello = my_decorator(hello) 
# endregion


# region Performance Decorator
# from math import pow, factorial
# from time import time_ns

# def calculate_time_execution(func):
#     """
#     Bir fonksiyonun çalışma süresini ölçen decorator.

#     Amaç:
#         - Fonksiyonun ne kadar sürede çalıştığını ölçmek
#     Not:
#         *args ve **kwargs kullanmamızın sebebi:
#         - Decorator'ün HER TİP fonksiyonla çalışabilmesi
#         - Parametre sayısı ve tipi fark etmeksizin esnek olmak
#     """

#     def wrapper(*args, **kwargs):
#         """
#         Wrapper fonksiyon:
#         - Asıl fonksiyonu saran katmandır
#         - Zaman ölçümü burada yapılır
#         """

#         # ⏱️ Fonksiyon çalışmadan ÖNCE zaman alınır
#         start_time = time_ns()

#         # 🎯 Asıl fonksiyon çağrılır
#         func(*args, **kwargs)

#         # ⏱️ Fonksiyon çalıştıktan SONRA zaman alınır
#         end_time = time_ns()

#         print(f'Perfomace: {end_time - start_time} ns')
    
#     return wrapper
# endregion


# region Power Function 
# @calculate_time_execution
# def calculate_pow(x: int, y: int):
#     """
#     x üzeri y hesaplar.

#     Örnek:
#         2^3 = 8
#     """
#     print(f'Sonuç: {pow(x, y)}')
# endregion


# region Factorial Function 
# @calculate_time_execution
# def calculate_factorial(number: int):
#     """
#     Verilen sayının faktöriyelini hesaplar.

#     Örnek:
#         5! = 120
#     """
#     print(f'Sonuç: {factorial(number)}')
# endregion


# region Sum Function 
# @calculate_time_execution
# def sum_number(x: int, y: int, z: int):
#     """
#     Üç sayının toplamını hesaplar.
#     """
#     print(f'Sonuç: {x + y + z}')
# endregion


# region Function Calls 
# Fonksiyonlar normal çağrılıyor gibi görünse de aslında decorator tarafından SARILMIŞ durumdalar.

# calculate_pow(x=2, y=3)
# calculate_factorial(number=5)
# sum_number(x=1, y=2, z=3)
# endregion


# region Log Decorator
# from datetime import datetime

# def log_info(func):
#     """
#     Loglama yapan decorator.

#     Amaç:
#         - Hangi fonksiyon çalıştı?
#         - Ne zaman çalıştı?
#         - Fonksiyonun kendi iş mantığına DOKUNMADAN bu bilgileri ekrana/loga yazdırmak

#     Önemli:
#         - return func(*args, **kwargs)
#           yazmamızın sebebi:
#             ➜ Asıl fonksiyonun return değerini KAYBETMEMEK
#     """

#     def wrapper(*args, **kwargs):
#         """
#         Wrapper fonksiyon:
#         - Asıl fonksiyon çağrılmadan önce log basar
#         - Sonra fonksiyonu çalıştırır
#         - Sonucu aynen geri döndürür
#         """

#         # 📝 Log bilgileri
#         print(
#             '===============================\n'
#             f'Yapılan İşlem: {func.__name__}\n'
#             f'İşlem Tarihi: {datetime.now()}\n'
#         )

#         # 🎯 Asıl fonksiyon çağrılır ve sonucu yakalanır
#         return func(*args, **kwargs)

#     return wrapper
# endregion


# region Pull Money Function
# @log_info
# def para_cekme(hesap_no: str, bakiye: int, cekilecek_tutar: int):
#     """
#     Hesaptan para çekme işlemi yapar.

#     Parametreler:
#         hesap_no (str)         : Hesap numarası
#         bakiye (int)           : Mevcut bakiye
#         cekilecek_tutar (int)  : Çekilecek para miktarı

#     Not:
#         - Bu örnek STATELESS'tir
#         - Gerçek projede bakiye DB üzerinden güncellenir
#     """

#     bakiye -= cekilecek_tutar

#     return (
#         f'Bu {hesap_no}, para çekildi..!\n'
#         f'Güncel Bakiye: {bakiye}'
#     )
# endregion


# region Deposit Money Function
# @log_info
# def para_yatırma(hesap_no: str, bakiye: int, yatırılacak_tutar: int):
#     """
#     Hesaba para yatırma işlemi yapar.
#     """

#     bakiye += yatırılacak_tutar

#     return (
#         f'Bu {hesap_no}, para yatırıldı..!\n'
#         f'Güncel Bakiye: {bakiye}'
#     )
# endregion
 
    
# region Function Calls 
# print(
#     para_cekme(
#         hesap_no='1234456',
#         bakiye=1000,
#         cekilecek_tutar=500
#     )
# )

# print(
#     para_yatırma(
#         hesap_no='1234456',
#         bakiye=1000,
#         yatırılacak_tutar=500
#     )
# )
# endregion


# region Role-Based Authorization Decorator
# def is_manager(func):
#     """
#     Yetki kontrolü yapan decorator.

#     Amaç:
#         - Sadece belirli rollere sahip kullanıcıların ilgili fonksiyonu çalıştırabilmesini sağlamak

#     İzin verilen roller:
#         - manager
#         - general manager

#     Not:
#         - Yetkisi olmayan kullanıcılar için fonksiyon ÇALIŞTIRILMAZ
#     """

#     def wrapper(user):
#         """
#         Wrapper fonksiyon:
#         - Kullanıcının rolünü kontrol eder
#         - Yetkisi varsa fonksiyonu çalıştırır
#         - Yetkisi yoksa bilgilendirici mesaj basar
#         """

#         # 🔐 Rol kontrolü
#         if user.get('role') in ['manager', 'general manager']:
#             return func(user)
        
#         # ❌ Yetkisiz erişim
#         print(f'{user.get("username")} - {user.get("role")}\n'
#               'Raporu görüntüleme yetkiniz bulunmamaktadır..!')
    
#     return wrapper
# endregion


# region Protected Function
# @is_manager
# def get_report(user):
#     """
#     Yetki gerektiren rapor görüntüleme fonksiyonu.
#     """
#     print(f'{user.get("username")} - {user.get("role")}\n'
#           'Report görüntülendi..!')
# endregion


# region User Data
# user_1 = {
#     'username': 'Hasan Cobanoğlu',
#     'role': 'manager'
# }

# user_2 = {
#     'username': 'Rana Nur Ceylan',
#     'role': 'general manager'
# }

# user_3 = {
#     'username': 'Burak Yılmaz',
#     'role': 'Irgat'
# }
# endregion


# region Function Calls 
# get_report(user_1)  # ✅ Yetkili
# get_report(user_3)  # ❌ Yetkisiz
# get_report(user_2)  # ✅ Yetkili
# endregion