
#! Method Overriding

# Ata sınıflarımızda bulunan methoların alt sınıflarda var olan yeteneklerinin üzerine yeni yetenekler ve özellikler ekleme 
# yada var olan özelliğin tamammen ezilerek ona yeni yetenek kazandırılımasına method overriding diyoruz.

# Ata sınıfta (Parent) bulunan bir metodu, alt sınıfta (Child) aynı isimle yeniden yazarak:
# - Davranışı tamamen değiştirebiliriz (override = ezme)
# - Ya da parent davranışı koruyup genişletebiliriz (super() ile)

# ✅ Neden Overriding Kullanırız?
# - Ortak davranışı base sınıfta tutarız
# - Bazı alt sınıflar bu davranışı farklı uygulamak ister
# - Böylece: DRY + temiz mimari + genişletilebilir tasarım

# ✅ super() Ne İşe Yarar?
# Child sınıfta:
# - parent metodu çağırıp çıktıyı/işi korur (reuse)
# - sonra üstüne child'a özel eklemeler yapar

# Örnek:
#     def show_info(self):
#         super().show_info()
#         print("Child'a özel alan...")


# region Method Overriding (Metot Ezme) - E-Commerce
# Base Entity - Parent Class
# class BaseEntity:
#     """
#     Base (Parent) sınıf.

#     Ortak alanlar:
#         name (str)
#         description (str)

#     Ortak metot:
#         show_info(): temel bilgileri yazdırır

#     Not:
#     - Category gibi bazı child sınıflar ekstra alan eklemez -> override gerekmez
#     - Product gibi bazı child sınıflar ekstra alan ekler -> override mantıklı

#     """

#     def __init__(self, name: str, description: str):
#         self.name = name
#         self.description = description

#     def show_info(self):
#         """
#         Parent metot.
#         Türetilen sınıflar isterse bu metodu EZEBİLİR (override).
#         """
#         print(
#             f'Name: {self.name}\n'
#             f'Description: {self.description}'
#         )


# Child Class - Category
# class Category(BaseEntity):
#     """
#     Category, BaseEntity'den kalıtım alır.
#     - BaseEntity'den name ve description alır

#     Ek alan eklenmediği için şimdilik override gerekmez.
#     - Extra alan yok -> override şart değil
#     """
#     pass


# Child Class - Product (Override Example)
# class Product(BaseEntity):
#     """
#     Product:
#     - BaseEntity'den ortak olan name ve description alanlarını alır
#     - Kendine özel price ve stock alanlarını ekler
#     - show_info metodunu override eder (metodu ezer)

#     Overriding stratejisi:
#     - super().show_info() -> parent çıktısını koru
#     - sonra Product'a özel alanları ekle
#     """

#     def __init__(self, name: str, description: str, price: float, stock: int):
#         """
#         super().__init__():
#         Parent (BaseEntity) constructor'ını çağırır.
#         Böylece name ve description burada tekrar yazılmaz.
#         """
#         super().__init__(name, description)

#         self.price = price
#         self.stock = stock

#         if self.price < 0:
#             raise ValueError("price cannot be negative.")
#         if self.stock < 0:
#             raise ValueError("stock cannot be negative.")

#     def show_info(self):
#         """
#         OVERRIDE EDİLEN METOT:
#         Parent'taki show_info() ile aynı isimde yazıldı.

#         super().show_info():
#         Parent'ın show_info() çıktısını da KORU (reuse et),
#         sonra Product'a özel alanları yazdır.
#         """
#         super().show_info()
#         print(
#             f'Price: {self.price}\n'
#             f'Stock: {self.stock}'
#         )


# product_1 = Product(name='Boxing Gloves', description='Boxing Gloves', price=10.999, stock=100)
# product_1.show_info()

# print("-" * 30)

# category_1 = Categorye(name="Sports", description="Sports equipments")
# category_1.show_info()
# endregion


# region Method Overriding - Phone
# Base Class - BasePhone
# class BasePhone:
#     """
#     Tüm telefonlar için temel (base) sınıf.
#     Ortak özellikler ve davranışlar burada tanımlanır.

#     Ortak alanlar:
#         phone_id (str)
#         model (str)
#         brand (str)
#         price (float)

#     Ortak davranışlar:
#         show_info()
#         phone_ring_sound() -> default zil sesi
#     """

#     def __init__(self, phone_id: str, model: str, brand: str, price: float):
#         """
#         BasePhone constructor.

#         Parametreler:
#             phone_id (str): Telefonun benzersiz ID'si
#             model (str): Model adı
#             brand (str): Marka adı
#             price (float): Fiyat bilgisi
#         """
#         self.phone_id = phone_id
#         self.model = model
#         self.brand = brand
#         self.price = price

#         if self.price < 0:
#             raise ValueError("price cannot be negative.")

#     def show_info(self): -> None:
#         """
#         Telefonun temel bilgilerini ekrana yazdırır.
#         """
#         print(
#             f'Id: {self.phone_id}\n'
#             f'Model: {self.model}\n'
#             f'Brand: {self.brand}\n'
#             f'Price: {self.price}'
#         )

#     def phone_ring_sound(self) -> str:
#         """
#         Tüm telefonlar için varsayılan zil sesi.
#         Child sınıflar override edebilir.
#         """
#         return 'general phone ring sound'


# Child Class - Iphone (Inheritance + Override)
# class Iphone(BasePhone):
#     """
#     Iphone sınıfı:
#     - BasePhone'dan kalıtım alır
#     - airDrop gibi kendine özel özellikler ekler
#     - show_info ve phone_ring_sound metotlarını override eder
#     """

#     def __init__(self, phone_id: str, model: str, brand: str, price: float, airdrop: bool):
#         """
#         Iphone constructor.

#         super().__init__():
#         BasePhone constructor'ını çağırarak ortak alanları tekrar yazmaktan kurtarır. (phone_id, model, brand, price)
#         """
#         super().__init__(phone_id, model, brand, price)
#         self.airdrop = airdrop

#     def show_info(self): -> None:
#         """
#         OVERRIDE:
#         Parent show_info() + Iphone'a özel alan
#         """
#         super().show_info()
#         print(f'Airdrop: {self.airdrop}')

#     def phone_ring_sound(self) -> str:
#         """
#         OVERRIDDEN METHOD:
#         Iphone'a özel zil sesi.
#         """
#         return 'iPhone default ring sound'


# class Samsung(BasePhone):
#     """
#     Samsung sınıfı:
#     - BasePhone'dan kalıtım alır
#     - operating_system (işletim sistemi) alanı ekler
#     - show_info ve phone_ring_sound override edilir
#     """

#     def __init__(self, phone_id: str, model: str, brand: str, price: float, operating_system: str):
#         """
#         Samsung constructor.
#         """
#         super().__init__(phone_id, model, brand, price)
#         self.operating_system = operating_system

#     def show_info(self): -> None:
#         """
#         OVERRIDE:
#         Parent show_info() + Samsung'a özel alan
#         """
#         super().show_info()
#         print(f'Operating System: {self.operating_system}')

#     def phone_ring_sound(self):
#         """
#         OVERRIDE:
#         Samsung'a özel zil sesi
#         """
#         return 'Samsung default ring sound'


# Test - Object Creation & Usage
# samsung_1 = Samsung(phone_id=1, model='Galaxy 20', brand='Samsung', price=120000, operating_system='Android')
# samsung_1.show_info()
# print("Ring Sound:", samsung_1.phone_ring_sound())

# print("-" * 30)

# iphone_1 = Iphone(phone_id='IP-001', model='iPhone 15 Pro', brand='Apple', price=79999.99, airdrop=True)
# iphone_1.show_info()
# print(f'Ring Sound: {iphone_1.phone_ring_sound()}')
# endregion


# region  Method Overriding - Entity + Status + System Info
# from enum import Enum
# from socket import gethostname, gethostbyname
# from datetime import datetime
#
#
# class Status(Enum):
#     """
#     Status enum:
#     - Active
#     - Modified
#     - Passive

#     Not:
#     Enum -> sabit değerleri daha okunabilir ve güvenli hale getirir.
#     """
#     Active = 1
#     Modified = 2
#     Passive = 3
#
#
# # Ata sınıflar kalıtım vericekleri alt sınıfların ortak özelliklerini barındırırlar.
# class BaseEntity:
#     """
#     BaseEntity (Parent) - Geniş kapsamlı örnek

#     Amaç:
#     - Category ve Product gibi entity'lerin ortak alanlarını tek yerde toplamak

#     Ortak alanlar:
#         ID, create_date, update_date, delete_date
#         status
#         ip_address, machine_name
#         name, description

#     Ortak davranış:
#         show_info(): temel bilgileri yazdır
#     """
#     def __init__(self, entity_id: int, create_date: datetime, update_date: datetime | None, delete_date: datetime | None,
#                 status: Status, ip_address: str, machine_name: str, name: str, description: str):
#         self.ID = int(entity_id)
#         self.description = description
#         self.name = name
#         self.machine_name = machine_name
#         self.ip_address = ip_address
#         self.status = status
#         self.create_date = create_date
#         self.update_date = update_date
#         self.delete_date = delete_date
#
#     def show_info(self): -> None:
#         """
#         Parent metot: ortak alanları basar.
#         Child sınıflar override edip ekstra alan yazdırabilir.
#         """
#         print(
#               f"Id: {self.ID}\n"
#               f"Name: {self.name}\n"
#               f"Description: {self.description}\n"
#               f"Crate Date: {self.create_date}\n"
#               f"Status: {self.status}\n"
#               f"Machine: {self.machine_name}\n"
#               f"IP: {self.ip_address}"
#         )
#
#
# Sub Classes
# class Category(BaseEntity):
#     """
#     Category:
#     - extra alan yok -> override şart değil
#     """
#     pass
#
#
# class Product(BaseEntity):
#     """
#     Product:
#     - price, stock alanlarını ekler
#     - show_info override ederek ekstra alanları yazdırır
#     """
#     def __init__(self, ID, create_date, update_date, delete_date, status, ip_address, machine_name, name, description, price, stock):
#         super().__init__(ID, create_date, update_date, delete_date, status, ip_address, machine_name, name, description)
#         self.stock = stock
#         self.price = price

#         if self.price < 0:
#             raise ValueError("price cannot be negative.")
#         if self.stock < 0:
#             raise ValueError("stock cannot be negative.")
#
#     def show_info(self):
#         super().show_info()
#         print(
#               f'Price: {self.price}\n'
#               f'Stock: {self.stock}'
#         )
#
#
# machine = gethostname()
# ip = gethostbyname(machine)
#
# category_1 = Category(1, datetime.now(), "", "", Status.Active, gethostname(), gethostbyname(gethostname()), "Boxing Gloves", "Best boxing gloves")
# category_1.show_info()
#
# product_1 = Product(1, datetime.now(), "", "", Status.Active, gethostname(), gethostbyname(gethostname()), "Everlast Pro Boxing Gloves", "Best ever", 13, 100)
# product_1.show_info()
# endregion


# region Method Overriding - Bill
# Çok minnak fatura ödeme uygulaması
# BaseBill sınıfı açalım. bill_name, value_add_task, amount attributeleri olsun. 
# calculate_bill fanksiyonu olsun
# Su, Elektrik, DogalGaz sınıfları olsun.
# Elektrik sınıfında ek özellik kw olsun. calculate_bill fonksiyonu kw dahil edilerek dizayn edilsin.
# su sınıfında ek mill olsun. calculate_bill fonksiyonu mill dahil edilerek dizayn edilsin.
# dogalgaz sınıfında m3 olsun. calculate_bill fonksiyonu m3 dahil edilerek dizayn edilsin.

# file = open(file='bill_info.txt', mode='w', encoding='utf8')
# file.write('Bill Information')
# file.close()

# from __future__ import annotations
# from datetime import datetime
# from pathlib import Path


# class BaseBill:
#     """
#     BaseBill (Parent)

#     Ortak alanlar:
#         bill_name (str)
#         unit_price (float)     -> birim fiyat (TL/kWh, TL/m3, TL/mill vb.)
#         amount (float)    -> tüketim

#     Ortak metotlar:
#         calculate_bill(): total = unit_price * amount
#         create_log(): bill_info.txt dosyasına log yazar

#     Overriding:
#     - Child sınıflar hesaplamayı değiştirmek isterse calculate_bill override eder.
#     """
#     def __init__(self, bill_name: str, value_add_tax: float, amount: float):
#         # object attributes
#         self.bill_name = bill_name
#         self.value_add_tax = float(value_add_tax)
#         self.amount = float(amount)

#         # basit doğrulamalar
#         if self.value_add_tax < 0:
#             raise ValueError("value_add_tax cannot be negative.")
#         if self.amount < 0:
# #             raise ValueError("amount cannot be negative.")

#     def calculate_bill(self) -> float:
#         """
#         Toplam tutarı hesaplar.
#         value_add_tax * amount
#         """
#         return self.value_add_tax * self.amount
    
#     def create_log(self, payment_date: str | None = None, file_name: str = "bill_info.txt") -> None:
#         """
#         bill_info.txt dosyasına:
#         - bill name
#         - total amount
#         - payment date
#         yazar (append).

#         payment_date verilmezse: bugünün tarihi saat ile yazılır.

#         Format:
#             [YYYY-MM-DD HH:MM:SS] Bill: ... | Total: 123.45
#         """
#         total_amount = self.calculate_bill()

#         if payment_date is None:
#             payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         log_line = f"[{payment_date}] Bill: {self.bill_name} | Total: {total_amount:.2f}\n"

#         path = Path(file_name)
#         if not path.exists():
#             path.write_text(data="", encoding="utf-8")

#         with open(file=file_name, mode="a", encoding="utf-8") as file:
#             file.write(log_line)


# # Child Class - WaterBill
# class WaterBill(BaseBill):
#     """
#     WaterBill (Child)
#     - mll: instance attribute
#     amount = mll olarak BaseBill'e aktarılır
#     """

#     def __init__(self, bill_name: str, value_add_tax: float, mill: float):
#         self.mill = float(mill)  # child'a özel attribute
#         super().__init__(bill_name=bill_name, value_add_tax=value_add_tax, amount=self.mill)

#     def calculate_bill(self):
#         # return super().calculate_bill() * self.mill
#         return self.amount * self.value_add_tax * self.mill


# # Child Class - NaturalGasBill
# class NaturalGasBill(BaseBill):
#     """
#     NaturalGasBill (Child)
#     - m3: instance attribute
#     amount = m3 olarak BaseBill'e aktarılır
#     """

#     def __init__(self, bill_name: str, value_add_tax: float, m3: float):
#         self.m3 = float(m3)
#         super().__init__(bill_name=bill_name, value_add_tax=value_add_tax, amount=self.m3)

#     def calculate_bill(self):
#         # return super().calculate_bill() * self.m3
#         return self.amount * self.value_add_tax * self.m3


# # Child Class - ElectricityBill
# class ElectricityBill(BaseBill):
#     """
#     ElectricityBill (Child)
#     - kw: instance attribute
#     amount = kw olarak BaseBill'e aktarılır
#     """

#     def __init__(self, bill_name: str, value_add_tax: float, kw: float):
#         self.kw = float(kw)
#         super().__init__(bill_name=bill_name, value_add_tax=value_add_tax, amount=self.kw)

#     def calculate_bill(self):
#         # return super().calculate_bill() * self.kw
#         return self.amount * self.value_add_tax * self.kw


# TEST
# water = WaterBill(bill_name="Water Bill", value_add_tax=2.75, mll=120)
# print("Water total:", water.calculate_bill())
# water.create_log(payment_date="2026-01-14 20:30:00")

# gas = NaturalGasBill(bill_name="Natural Gas Bill", value_add_tax=6.40, m3=35)
# print("Gas total:", gas.calculate_bill())
# gas.create_log()  # otomatik tarih

# electric = ElectricityBill(bill_name="Electricity Bill", value_add_tax=3.10, kw=210)
# print("Electric total:", electric.calculate_bill())
# electric.create_log()

# endregion