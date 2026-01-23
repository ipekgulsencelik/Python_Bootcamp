
#! Abstraction (Soyutlama)

# OOP prensipleri içerisinde en önemli olanıdır.
# Özellikle büyük boyutlu projelerde, çok karmaşık iş mantıklarında (business logic) üst seviyeli yazılım prensiplerine
# ve tasarım desenlerine (design patterns) uymak için uyulması gereken oop yapısıdır. 
# Yani yazılım prensipleri ve tasarım desenlerinin uygulanması için muhakkak soyutlama bilinmesi gerekir.
# Soyutlamada ki ana mantık ata sınıfların soyut hale getirilmesidir. 
# Böylelikle soyutlamanın bize sunduğu nimetlerden faydalanmaya başlarız. 
# Peki nedir nimetler? Öncelikle soyut ata sınıf kullandığımızda alt sınıfalr ile ata sınıf arasında sözleşme imzalanır. 
# Yani soyut sınıf içerisinde soyut olarak işaretlenmiş bir üye alt sınıfta uygulanmak zorundadır. 
# Bu bakımdan üst sınıf ile alt sınıf arasında bir sözleşme imzalanmış olunur. 
# Soyutlamanın bir deiğer nimeti ise sınıflar arasında ki bağımlıkları kırmak için atılan ilk adım olamsıdır. 
# Soyutlama ile bu bağımlıkları kırmak için uygulanılacak yazılım prensiplerine alt yapı hazırlanmış olunur.

# Abstraction (Soyutlama):
# ✅ Hedef:
# - Soyut sınıf (ABC) ile alt sınıflara ZORUNLU sözleşme imzalatmak
# - Ortak davranışları Base sınıfta toplamak
# - İş kurallarını (business logic) entity’den ayırmak

#    - Soyut sınıflar üzerinden "SÖZLEŞME (contract)" tanımlamak.
#    - Alt sınıfların zorunlu implement etmesi gereken metotları belirlemek.
#    - Büyük projelerde bağımlılıkları azaltmak ve tasarım desenlerine altyapı hazırlamak.

# Soyutlama geçmeden önce decorator konusunu bilmek gerekmektedir.

# Decorator
# Python'da kullanılan bir keyword'tür. 
# Bir fonksiyonun bir decorator ile onun var olan yeteneği üzerine bir yetenek daha eklenir. 
# - Bir fonksiyonun var olan davranışına “ek davranış” ekleyen yapıdır.
# - Python’da fonksiyonlar first-class olduğu için (değişkene atanabilir, parametre geçilebilir) decorator ile fonksiyon sarma (wrapping) çok yaygındır.
# Yani adı üzerinde ilgi methodu dekore etmiş oluruz. 
# Python'da @ ile kullanılır.
# Python içerisinde built-in olarak bulunan bir çok decorator bulunmaktadır. 
# Bunlar "@staticmethod", "@abstractmethod" vb. built-in decoratorler bulunmaktadır. 
# Bunun yanında custom decoratorler yazabiliriz.

# Önemli:
# Decorator bir fonksiyon döndürmelidir.
# Yani `return wrapper` olmalı.
# `return wrapper()` yazarsan fonksiyon değil, sonucu döndürürsün (yanlış kullanım).


# region Decorator - Upper Name

"""
Decorator mantığı:
- Decorator bir fonksiyon alır.
- Onu "wrapper" (sarmalayıcı) fonksiyon ile sarar.
- Davranış ekler (örn: log, ölçüm, yetki kontrol, formatlama).
- En sonunda wrapper fonksiyonunu geri döndürür.

Kritik nokta:
✅ return wrapper   (doğru)
❌ return wrapper() (yanlış, direkt çalıştırıp sonucu döndürür)
"""

# def uppercase_result(func):
#     """
#     Örnek decorator: Fonksiyonun dönüş değerini büyük harfe çevirir.

#     Parametre:
#         func: Dekore edilecek fonksiyon

#     Dönüş:
#         wrapper: aynı imzaya yakın çalışan yeni fonksiyon
#     """

#     def wrapper(*args, **kwargs) -> str:
#         # Orijinal fonksiyonu çalıştır
#         result = func(*args, **kwargs)

#         # Dönüş değerine ek davranış uygula
#         return str(result).upper()

#     return wrapper


# def get_fullname():
#     return 'mike tyson'

# print(uppercase_result(get_fullname))


# @uppercase_result
# def get_name() -> str:
#     """
#     Normalde 'burak yılmaz' döner.
#     Decorator sayesinde 'BURAK YILMAZ' dönecek.
#     """
#     return "burak yılmaz"

# print(get_name)

# endregion


# region Decorator - Calculate Time

# from math import pow, factorial
# from time import sleep, time


# def calculate_time(func):
#     """
#     Decorator fonksiyonudur.

#     Parametre:
#         func (callable):
#             Dekore edilecek fonksiyonun KENDİSİDİR.
#             (Henüz çalıştırılmamıştır!)

#     Görev:
#         - Fonksiyonun çalışmaya başladığı zamanı almak
#         - Fonksiyon çalıştıktan sonra bitiş zamanını almak
#         - Geçen süreyi raporlamak
#     """

#     def inner_func(*args, **kwargs):
#         """
#         Wrapper (sarmalayıcı) fonksiyon.

#         *args  : Pozisyonel parametreler
#         **kwargs : Keyword parametreler

#         Bu sayede decorator:
#         - 1 parametre alan
#         - 5 parametre alan
#         - Hiç parametre almayan
#         HER fonksiyonu sarabilir.
#         """

#         # Fonksiyon çalışmadan ÖNCE
#         start_process = time()

#         sleep(5)
        
#         # Asıl fonksiyonun çağrılması
#         func(*args, **kwargs)

#         # Fonksiyon çalıştıktan SONRA
#         finish_process = time()

#         print(
#             f"\n=====================\n"
#             f"Process Name : {func.__name__}\n"
#             f"Start Time   : {start_process}\n"
#             f"Finish Time : {finish_process}\n"
#             f"Total Time  : {finish_process - start_process:.4f} sec\n"
#             f"=====================\n"
#         )

#     # ❗ ÇOK ÖNEMLİ
#     # inner_func() DEĞİL
#     # inner_func döndürülür
    
#     # Çünkü decorator bir FONKSİYON döndürmelidir, sonucu değil!
#     return inner_func


# @calculate_time
# def calculate_pow(a: int, b: int) -> None:
#     """
#     Üs alma işlemi.

#     Bu fonksiyon çağrıldığında aslında:
#     us_alma = calculate_time(us_alma)
#     işlemi yapılmış olur.
#     """
#     print(f"Result (pow): {pow(a, b)}")


# @calculate_time
# def calculate_factorial(number: int) -> None:
#     """
#     Faktoriyel hesaplama fonksiyonu.
#     """
#     print(f'Result: {factorial(number)}')


# @calculate_time
# def calculate_sum(x: int, y: int, z: int) -> None:
#     """
#     Basit toplama işlemi.
#     """
#     print(f'Result: {x + y + z}')


# print(">>> ÜS ALMA")
# # calculate_pow(a=2, b=3)

# print(">>> FAKTORİYEL")
# # calculate_factorial(number=5)

# print(">>> TOPLAMA")
# # calculate_sum(x=4, y=6, z=5)

# endregion


# region Abstraction - Music Domain

"""
Bu bölümde 2 katman göreceksin:

ENTITY (Model / Varlık)
- Sadece veri taşır.
- İş kuralı barındırmaz.
- Basit class / dataclass olması normaldir.

SERVICE (İş Kuralları)
- Filtreleme, hesaplama, doğrulama, loglama gibi business işleri buraya konur.
- Bu katman soyut sınıf üzerinden “sözleşme” ile zorunlu hale getirilebilir.
"""

"""
Bu senaryoda amaç:

- Entity sınıfları: sadece veri taşısın (brand, model vb.)
- Service sınıfları: iş kurallarını yönetsin (call_sound gibi)

Soyutlama burada devreye girer:

BaseInstrumentService soyut sınıfı şunu söyler:
"Benim çocuklarım (alt sınıflarım) call_sound metodunu yazmak zorunda."

Bu bir SÖZLEŞME'dir (contract).
"""

# from abc import ABC, abstractmethod


# ENTITY KATMANI (MODELS)

# class BaseMusicInstrument:
#     """
#     Tüm müzik aletleri için ortak olan temel sınıf.

#     Ortak özellikler:
#     - marka
#     - model
#     """

#     def __init__(self, model, brand):
#         self.brand = brand
#         self.model = model


# class Guitar(BaseMusicInstrument):
#     """
#     Gitar entity.

#     Ek alan:
#     - guitar_string: tel/kalite bilgisi vs.
#     """

#     def __init__(self, brand, model, guitar_string):
#         super().__init__(brand, model)
#         self.guitar_string = guitar_string


# class Drum(BaseMusicInstrument):
#     """
#     Davul entity.

#     Ek alan:
#     - shell_type: kasa/deri türü vb.
#     """
     
#     def __init__(self, brand, model, shell_type):
#         super().__init__(brand, model)
#         self.shell_type = shell_type


# class Musician:
#     """
#     Müzisyen entity.

#     played_instruments:
#     - BaseMusicInstrument türünden liste tutar
#     - Böylece gitar da davul da aynı listede yönetilebilir (polymorphism)
#     """

#     def __init__(self, first_name, last_name):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.played_instruments = []


# SERVICE KATMANI (BUSINESS)
# Service olarak nitelendirilen sınıflarda uygulam içerisinde ki varlıklarımız (entity) CRUD operasyonlarının çözümlendiği yerdir.
# Örneğin veri tabanından belirli marka, fiyat, beden, renk bilgilerine göre elbiseler çekilecek. 
# Bu iş mantığı service olarak nitelendirilen sınıfta handle edilir.

# class BaseService(ABC):  # BaseService sınıfımız "ABC" meta sınıfından kalıtım alara, soyut sınıf olma özelliklerini kazanmıştır.
#     """
#     BaseService soyut (abstract) sınıfıdır.

#     🎯 Amaç:
#     - Alt sınıfların implement etmesi gereken zorunlu metotları belirlemek
#     - Ortak davranışları tek yerde toplamak

#     Bu sınıftan:
#     - Doğrudan instance alınamaz.
#     - Sadece kalıtım verilir.

#     - Doğrudan örneklenemez
#     - Sadece kalıtım vermek için vardır
#     - Ortak davranışları tanımlar
#     """

#     # Soyut ata sınıflardan örneklem (instance) alınmaz. 
#     # Çünkü bu sınıfların amacı kalıtım vermektir.

#     # Aşağıda ki fonksiyonu "@abstractmethod" dekoratörü ile işaretledik. 
#     # Böylelikle bu methodun soyut bir üye olması temin edildi.
#     # Soyut bir sınıf içersinde tanımlanmış soyut üyelerin gövdeleri olmaz yani üzerlerine bir iş atanmaz. 
#     # Çünkü bu method alt sınıflarda override edilmeye zorunlu tutulmuştur. 
#     # Bunun anlamı bu method zaten override edilecek yani alt sınıfta bu methoda bir iş verilecek üst sınıfta yani burada bu fonksiyonu bir iş yüklemek saçmalıktır.
#     @abstractmethod
#     def call_sound(self) -> str: 
#         """
#         Soyut metot:

#         - Gövde yok.
#         - Alt sınıfta zorunlu override.

#         ZORUNLU sözleşme.

#         Alt sınıflar bu metodu implement etmezse:
#         TypeError: Can't instantiate abstract class ...

#         Not:
#         Python'da pass yazmak yeterli ama daha net olması için
#         NotImplementedError da kullanılabilir.
#         """
#         raise NotImplementedError("Alt sınıf bu metodu implement etmeli.")

#     # Abstract sınıf içerisinde abstaract olmayan üyelerde barındırılabilinir.
#     # Burada gövdeli somut bir method tanımlamamızda ki amaç alt sınıflarda bu methodu hali hazrıda var olan yeteneği ile kullanmaktır. Bazı yerlerde var olan yeteneğini ezerek kullanabiliriz.
#     def hello_everyone(self):
#         """
#         Soyut sınıf içerisinde tanımlanmış SOMUT metot.

#         Alt sınıflar isterse:
#         - Olduğu gibi kullanabilir
#         - Override edebilir
#         """
#         print('Hi..!')


# class GuitarService(BaseService):
#     """
#     Gitar ile ilgili iş kurallarını yöneten servis sınıfı.

#     BaseInstrumentService sözleşmesini imzaladığı için:
#     - call_sound() metodunu implement etmek zorunda.
#     """

#     def call_sound(self) -> str:
#         return "Guitar sound"

#     # Burada hello_everyone() metdounun var olan yeteneğini ezerek ona yeni yetenek kazandırdık.
#     def hello_everyone(self):
#         """
#         Ortak metodu override ettik.
#         """
#         print("Salve..! (GuitarService)")

#     @staticmethod
#     def harmonize():
#         """
#         @staticmethod örneği:

#         - Nesneye bağlı değil.
#         - self almaz.
#         - Utility (yardımcı) fonksiyon gibi çalışır.
#         """
#         print("Guitar has been tuned!")


# class DrumService(BaseService):
#     """
#     Davul ile ilgili iş kurallarını yöneten servis sınıfı.
#     """

#     def call_sound(self) -> str:
#         return 'Drum sound'


# def main():
#     """
#     Music domain demo akışı:
#     - Entity oluştur
#     - Servis oluştur
#     - Polymorphism ile listeye ekle
#     - Servis çağrılarıyla iş mantığını çalıştır
#     """

#     guitar_service = GuitarService()
#     drum_service = DrumService()

#     guitar = Guitar("Ibanez", "Classical Guitar", "High quality strings")
#     drum = Drum("Traditional Drum", "Ramadan Drum", "High quality leather")

#     musician = Musician("Burak", "Yilmaz")
#     musician.played_instruments.append(guitar)
#     musician.played_instruments.append(drum)

#     # Gitar bilgisi
#     print("---- MUSIC DEMO / GUITAR ----")
#     print(
#         f"Musician: {musician.first_name} {musician.last_name}\n"
#         f"Brand   : {musician.played_instruments[0].brand}\n"
#         f"Model   : {musician.played_instruments[0].model}\n"
#         f"Sound   : {guitar_service.call_sound()}"
#     )
#     guitar_service.hello_everyone()

#     # Davul bilgisi
#     print("\n---- MUSIC DEMO / DRUM ----")
#     print(
#         f"Musician: {musician.first_name} {musician.last_name}\n"
#         f"Brand   : {musician.played_instruments[1].brand}\n"
#         f"Model   : {musician.played_instruments[1].model}\n"
#         f"Sound   : {drum_service.call_sound()}"
#     )
#     drum_service.hello_everyone()

#     # Static örneği
#     print("\n---- GUITAR HARMONIZE ----")
#     GuitarService.harmonize()


# main()

# endregion


# region Abstraction - Bill Domain

"""
Bu senaryoda amaç:

- Fatura entity'leri sadece veri taşısın.
- Her fatura türünün hesaplama iş kuralı servislerde olsun.
"""

# class BaseBill:
#     """
#     Tüm faturalar için ortak temel sınıf.

#     Ortak Alanlar:
#     - bill_name        : Fatura adı (Su, Elektrik, Doğalgaz vb.)
#     - value_add_task   : Vergi / ek bedel oranı
#     - amount           : Ödenecek tutar
#     """

#     def __init__(self, bill_name: str, value_add_task: float, amount: float):
#         self.bill_name = bill_name
#         self.value_add_task = value_add_task
#         self.amount = amount


# class WaterBill(BaseBill):
#     """
#     Su faturası.

#     Ek Alan:
#     - mill : Kullanılan su miktarı (m³ / sayaç değeri)
#     """

#     def __init__(self, bill_name: str, value_add_task: float, amount: float, mill: int):
#         super().__init__(bill_name, value_add_task, amount)
#         self.mill = mill


# class NaturalGasBill(BaseBill):
#     """
#     Doğalgaz faturası.

#     Ek Alan:
#     - m3 : Tüketilen doğalgaz miktarı
#     """

#     def __init__(self, bill_name: str, value_add_task: float, amount: float, m3: float):
#         super().__init__(bill_name, value_add_task, amount)
#         self.m3 = m3


# class ElectricityBill(BaseBill):
#     """
#     Elektrik faturası.

#     Ek Alan:
#     - kw : Tüketilen elektrik miktarı (kWh)
#     """

#     def __init__(self, bill_name: str, value_add_task: float, amount: float, kw: float):
#         super().__init__(bill_name, value_add_task, amount)
#         self.kw = kw


# SERVICE KATMANI (İş Kuralları)

# from abc import ABC, abstractmethod
# from datetime import datetime


# class BaseService(ABC):
#     """
#     BaseService soyut (abstract) servis sınıfıdır.

#     🎯 Amaç:
#     - Tüm servis sınıfları için ortak bir sözleşme (contract) tanımlamak
#     - Hangi metodların ZORUNLU olduğunu belirlemek
#     - Ortak yardımcı (helper) metotları tek yerde toplamak

#     📌 Bu sınıftan:
#     - Doğrudan nesne oluşturulamaz
#     - Sadece kalıtım alınır
#     """
    
#     @abstractmethod
#     def calculate_bill(self, bill: "BaseBill") -> float:
#         """
#         Soyut metot.

#         ✔ Alt sınıflar bu metodu MUTLAKA implement etmek zorundadır.
#         ✔ Her fatura türü kendi hesaplama mantığını burada yazar.

#         Parametre:
#             bill (BaseBill): Hesaplanacak fatura nesnesi

#         Dönüş:
#             float: Hesaplanan toplam tutar
#         """
#         pass

#     def create_log(self, bill: "BaseBill", calculate_bill_result: float) -> str:
#         """
#         Ortak loglama işlemi.

#         📌 Soyut DEĞİL, somut bir metottur.
#         📌 Tüm servisler tarafından olduğu gibi kullanılabilir.
#         📌 Gerekirse alt sınıflarda override edilebilir.

#         Yapılan İş:
#         - Fatura bilgilerini dosyaya yazar
#         - Ödeme tarihini kayıt altına alır
#         """

#         with open(file="bill_info.txt", mode="a", encoding="utf-8") as file:
#             file.write(
#                 f"Bill Name     : {bill.bill_name}\n"
#                 f"Total Amount  : {calculate_bill_result}\n"
#                 f"Payment Date  : {datetime.now()}\n"
#                 f"===============================\n"
#             )

#         return f"{bill.bill_name} payment logged successfully."


# class WaterBillService(BaseService):
#     """
#     Su faturası servis sınıfı.

#     Sorumluluk:
#     - Su faturası için toplam ödeme tutarını hesaplamak

#     Hesaplama Mantığı:
#     - Kullanılan su miktarı (mill)
#     - Birim tutar (amount)
#     - Vergi / ek bedel oranı (value_add_task)
#     """

#     def calculate_bill(self, bill: WaterBill) -> float:
#         """
#         Su faturası hesaplama işlemi.

#         Formül:
#             toplam_tutar = value_add_task * amount * mill
#         """
#         return bill.value_add_task * bill.amount * bill.mill


# class NaturalGasService(BaseService):
#     """
#     Doğalgaz faturası servis sınıfı.

#     Sorumluluk:
#     - Doğalgaz faturası tutarını hesaplamak

#     Hesaplama Mantığı:
#     - Tüketilen doğalgaz miktarı (m3)
#     - Birim fiyat (amount)
#     - Vergi / ek bedel oranı (value_add_task)
#     """

#     def calculate_bill(self, bill: NaturalGasBill) -> float:
#         """
#         Doğalgaz faturası hesaplama işlemi.

#         Formül:
#             toplam_tutar = value_add_task * amount * m3
#         """
#         return bill.value_add_task * bill.amount * bill.m3


# class ElectricityService(BaseService):
#     """
#     Elektrik faturası servis sınıfı.

#     Sorumluluk:
#     - Elektrik faturası tutarını hesaplamak

#     Hesaplama Mantığı:
#     - Tüketilen elektrik (kWh)
#     - Birim fiyat (amount)
#     - Vergi / ek bedel oranı (value_add_task)
#     """

#     def calculate_bill(self, bill: ElectricityBill) -> float:
#         """
#         Elektrik faturası hesaplama işlemi.

#         Formül:
#             toplam_tutar = value_add_task * amount * kw
#         """
#         return bill.value_add_task * bill.amount * bill.kw


# def main():

#     # 1️⃣ Su faturası nesnesi oluşturulur (ENTITY)
#     # Sadece veri taşır, iş kuralı yoktur
#     water_bill = WaterBill(bill_name="İSKİ", value_add_task=25.5, amount=45.7, mill=100)

#     # 2️⃣ Su faturası servisi oluşturulur
#     # Hesaplama ve iş mantığı burada yer alır
#     water_bill_service = WaterBillService()

#     # 3️⃣ Fatura hesaplama işlemi
#     # calculate_bill() → BaseService üzerinden zorunlu kılınmıştır
#     bill_result = water_bill_service.calculate_bill(bill=water_bill)

#     # 4️⃣ Loglama işlemi
#     # create_log() → ortak davranış
#     # Metot geriye kullanıcıya gösterilecek bir mesaj döndürür
#     message = water_bill_service.create_log(bill=water_bill, calculate_bill_result=bill_result)

#     # 5️⃣ Kullanıcıya mesaj gösterilir
#     print(message)
#     print(
#         f"Bill: {water_bill.bill_name}\n"
#         f"Amount: {water_bill.amount}\n"
#         f"Bill Result (KDV): {bill_result}"
#     )


# main()

# endregion


# region Bills (Abstraction + Polymorphism + Dataclasses)
"""
Abstraction (Soyutlama)
   - BaseService(ABC) ile bir "sözleşme" tanımlarız.
   - Tüm servisler calculate_bill metodunu IMPLEMENT etmek zorundadır.

Polymorphism (Çok biçimlilik)
   - Aynı isimli metod (calculate_bill) farklı fatura türlerinde farklı şekilde çalışır.

SRP (Single Responsibility Principle)
   - Bill (entity) sadece veri taşır.
   - Service (business logic) sadece hesaplama yapar.
   - Loglama bu örnekte servis içinde ortak metotla gösterilir (eğitim amaçlı).

Not:
- Gerçek projelerde loglama genellikle ayrı bir Logger sınıfına taşınır (ILogger, FileLogger, DbLogger).
"""

# from dataclasses import dataclass
# from abc import ABC, abstractmethod
# from datetime import datetime

# @dataclass
# class BaseBill:
#     """
#     Tüm faturalar için ortak alanları içeren base entity.

#     Attributes:
#         bill_name (str): Fatura adı / kurum adı (örn: ISKI, IGDAS, BEDAS).

#         value_added_tax (float): KDV / vergi katsayısı.
#             Örnek:
#                 1.20 -> %20 KDV dahil katsayı gibi düşünülebilir.
#             Not:
#                 Gerçek hayatta KDV hesaplaması farklı olabilir (vergi oranı * ara toplam vb.)
#                 Bu örnekte "çarpan" gibi kullanıyoruz.

#         unit_price (float): Birim fiyat (örn: 1 m3 gazın fiyatı, 1 kw elektriğin fiyatı, 1 birim su fiyatı).
#     """
#     bill_name: str
#     value_added_tax: float
#     unit_price: float


# @dataclass
# class WaterBill(BaseBill):
#     """
#     Su faturası entity'si.

#     Su tüketimi örneği:
#         mill -> (örnekte "tüketim" gibi davranır)

#     Attributes:
#         mill (int):
#             Su faturası için tüketim değeri (örnek senaryoda çarpan).
#             Gerçek dünyada m3 / ton gibi ölçümler olabilir.
#     """
#     mill: int


# @dataclass
# class NaturalGasBill(BaseBill):
#     """
#     Doğalgaz faturası entity'si.

#     Attributes:
#         m3 (float): Doğalgaz tüketimi (m³).
#     """
#     m3: float


# @dataclass
# class ElectricityBill(BaseBill):
#     """
#     Elektrik faturası entity'si.

#     Attributes:
#         kw (float): Elektrik tüketimi (kWh).
#             (Değişken adı kw ama aslında kWh gibi düşünülebilir.)
#     """
#     kw: float


# class BaseService(ABC):
#     """
#     Tüm fatura servisleri için soyut servis sınıfı.

#     Bu sınıf iki şey sağlar:
#     1) calculate_bill() -> zorunlu implement edilecek soyut metot
#     2) create_log() -> tüm servislerin ortak kullanabileceği log metodu

#     Abstraction Mantığı:
#         - Bu sınıf bir "sözleşme" (contract) görevi görür.
#         - Alt sınıflar "hesaplama yapmak zorundadır".
#     """

#     @abstractmethod
#     def calculate_bill(self, bill: BaseBill) -> float:
#         """
#         Fatura hesaplama sözleşmesi.

#         Her alt servis bu metodu kendi fatura türüne göre uygular.

#         Args:
#             bill (BaseBill):
#                 Hesaplanacak fatura nesnesi (WaterBill / NaturalGasBill / ElectricityBill).

#         Returns:
#             float:
#                 Hesaplanan toplam tutar.

#         Raises:
#             NotImplementedError:
#                 ABC yapısı gereği alt sınıf implement etmezse hata oluşur.
#         """
#         raise NotImplementedError("Alt sınıf calculate_bill metodunu uygulamalıdır.")

#     def create_log(self, bill: BaseBill, calculate_bill_result: float) -> str:
#         """
#         Hesaplama sonrası log oluşturur.

#         Bu metot "ortak davranış" örneğidir:
#             Her faturanın log formatı aynı olduğu için tekrar yazmayız.

#         Args:
#             bill (BaseBill):
#                 Loglanacak fatura.

#             calculate_bill_result (float):
#                 Hesaplanan toplam tutar.

#         Returns:
#             str:
#                 Kullanıcıya gösterilecek mesaj.

#         Side Effects:
#             bill_info.txt dosyasına append (ekleme) yapar.

#         Notes:
#             - Gerçek projede bu iş ayrı bir Logger sınıfına taşınabilir.
#             - Burada BaseService içinde tutulmuştur.
#         """
#         with open(file='bill_info.txt', mode='a', encoding='utf-8') as file:
#             file.write(
#                 f'Bill Name: {bill.bill_name}\n'
#                 f'Total Amount: {calculate_bill_result}\n'
#                 f'Payment Date: {datetime.now()}\n'
#                 f'================================\n'
#             )
#         return f'{bill.bill_name} payment logged.'


# class WaterBillService(BaseService):
#     """
#     Su faturası hesaplama servisi.

#     Bu sınıf BaseService sözleşmesini uygular:
#         - calculate_bill metodunu WaterBill'e göre hesaplar.

#     Polymorphism:
#         BaseService üzerinden çağrılan calculate_bill,
#         burada WaterBill'e özel farklı bir davranış gösterir.
#     """

#     def calculate_bill(self, bill: WaterBill) -> float:
#         """
#         Su faturası hesaplar.

#         Hesap formülü (örnek senaryo):
#             total = value_added_tax * unit_price * mill

#         Args:
#             bill (WaterBill):
#                 Su faturası.

#         Returns:
#             float:
#                 Toplam tutar.
#         """
#         return bill.value_added_tax * bill.unit_price * bill.mill


# class NaturalGasBillService(BaseService):
#     """
#     Doğalgaz faturası hesaplama servisi.
#     """

#     def calculate_bill(self, bill: NaturalGasBill) -> float:
#         """
#         Doğalgaz faturası hesaplar.

#         Örnek formül:
#             total = value_added_tax * unit_price * m3

#         Args:
#             bill (NaturalGasBill):
#                 Doğalgaz faturası.

#         Returns:
#             float:
#                 Toplam tutar.
#         """
#         return bill.value_added_tax * bill.unit_price * bill.m3


# class ElectricityBillService(BaseService):
#     """
#     Elektrik faturası hesaplama servisi.
#     """

#     def calculate_bill(self, bill: ElectricityBill) -> float:
#         """
#         Elektrik faturası hesaplar.

#         Örnek formül:
#             total = value_added_tax * unit_price * kw

#         Args:
#             bill (ElectricityBill):
#                 Elektrik faturası.

#         Returns:
#             float:
#                 Toplam tutar.
#         """
#         return bill.value_added_tax * bill.unit_price * bill.kw


# def pay_and_log_bill(service: BaseService, bill: BaseBill) -> str:
#     """
#     Polymorphism'i net göstermek için yardımcı fonksiyon.

#     Aynı fonksiyon:
#         - WaterBillService + WaterBill
#         - NaturalGasBillService + NaturalGasBill
#         - ElectricityBillService + ElectricityBill
#     ile çalışabilir.

#     Çünkü:
#         service.calculate_bill(...) her serviste farklı implement edilmiştir.

#     Args:
#         service (BaseService):
#             Hesaplama yapacak servis.

#         bill (BaseBill):
#             Hesaplanacak fatura.

#     Returns:
#         str:
#             Log mesajı.
#     """
#     total = service.calculate_bill(bill)          # polymorphic call
#     msg = service.create_log(bill, total)         # shared behavior
#     return msg


# def main() -> None:
#     """
#     Demo çalıştırma noktası.

#     Bu bölümde 3 farklı fatura oluşturup
#     ilgili servislerle hesaplayıp logluyoruz.
#     """

#     # 1) Water
#     water_bill = WaterBill(bill_name="ISKI", value_added_tax=1.25, unit_price=45.7, mill=100)
#     water_service = WaterBillService()
#     # bill_result = water_bill_service.calculate_bill(bill=water_bill)
#     # msg = water_bill_service.create_log(bill=water_bill, calculate_bill_result=bill_result)
#     # print(msg)
#     print(pay_and_log_bill(water_service, water_bill))

#     # 2) Natural Gas
#     gas_bill = NaturalGasBill(bill_name="IGDAS", value_added_tax=1.20, unit_price=12.5, m3=85.5)
#     gas_service = NaturalGasBillService()
#     print(pay_and_log_bill(gas_service, gas_bill))

#     # 3) Electricity
#     electric_bill = ElectricityBill(bill_name="BEDAS", value_added_tax=1.18, unit_price=3.25, kw=210.0)
#     electric_service = ElectricityBillService()
#     print(pay_and_log_bill(electric_service, electric_bill))


# if __name__ == "__main__":
#     main()   
# endregion