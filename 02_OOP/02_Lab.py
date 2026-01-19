
#! Kalıtım (Inheritance)

# Adından da anlaşılacağı üzere bir sınıfın bir ata sınıftan kalıtım yoluyla özellik kazanmasınmasıdır. 
# Bunu biyolojide ki kalıtıma benzetebiliriz.  
# Nasıl ki bizler ebevylerimizden kalıtım yoluyla belirli fiziksel ve karakteristiksel özellik kazandıysak bunu yazılamada uyarlayabilir. 
# O halde artık bizlerin ata sınıfları olacak ve bu ata sınıflar alt sınıflara özellik aktaracaklar.

# Kalıtım (Inheritance), bir sınıfın (Child/Subclass) başka bir sınıftan (Parent/Base class) özellik ve davranışları miras almasıdır.
# - Base / Parent Class (Ata sınıf): Ortak özellikleri toplar.
# - Child / Sub Class (Alt sınıf): Ata sınıftan gelenleri kullanır, isterse yeni özellik ekler.
# - Amaç: Kod tekrarını azaltmak, ortak yapıyı tek yerde tutmak.

# Kalıtımın sağladıkları
# - Ortak alanlar (ör: full_name, weight, height) tek yerde tanımlanır.
# - Alt sınıflar ekstra özellik ekleyebilir (ör: weapon, rank, department).
# - İleride değişiklik gerektiğinde sadece base class düzenlemek yeterli olur.


# region Inheritance - Human Classes
# Base Class - Human
# class Human:
#     """
#     Temel (Base) sınıf.
#     İnsanlara ait ortak özellikleri tanımlar.
#     Bu sınıftan türeyen tüm sınıflar bu özellikleri otomatik alır.
#     - Alt sınıfların (FootSoldier, Knight) tekrar tekrar aynı alanları yazmamasını sağlamak.
#     """

#     def __init__(self, full_name: str, weight: float, height: float):
#         """
#         Human nesnesi oluşturulurken çalışan kurucu metot.

#         Parametreler:
#             full_name (str): Kişinin adı ve soyadı
#             weight (float): Kilo bilgisi
#             height (float): Boy bilgisi
#         """
#         self.full_name = full_name
#         self.weight = float(weight)
#         self.height = float(height)

#     def show_info(self): -> dict:
#         """
#         Nesnenin sahip olduğu tüm attribute'ları dictionary olarak döner.

#         __dict__:
#             Nesnenin bellekte tuttuğu tüm instance attribute'larını içerir.
#         """
#         return self.__dict__


# # Child Class - FootSoldier
# class FootSoldier(Human):
#     """
#     Human sınıfından türetilmiş bir alt sınıf.

#     ✔ Human içindeki __init__ metodunu otomatik kullanır
#     ✔ Human içindeki show_info metodunu otomatik kullanır

#     Şu an ekstra bir alan/metot eklenmedi.
#     Bu yüzden sadece kalıtımı göstermek adına boş bırakıldı.
#     """
#     pass


# # Child Class - Knight
# class Knight(Human):
#     """
#     Human sınıfından türetilmiş başka bir alt sınıf.

#     Şu an için ekstra bir özellik eklenmediği için pass kullanıldı.
#     """
#     pass


# foot_soldier_1 = FootSoldier(full_name='burak', weight=100.03, height=1.83)
# print("FootSoldier:", foot_soldier_1.show_info())

# knight_1 = Knight(full_name='hakan', weight=165, height=2.01)
# print("Knight:", knight_1.show_info())
# endregion


# region Inheritance - Person Classes
# Base Class - Person
# class Person:
#     """
#     Person sınıfı: hem class attribute hem instance attribute öğretir.

#     - class attribute: age (sınıfa aittir, varsayılan ortak değer)
#     - instance attribute: first_name, last_name (her objeye özel)
#     """

#     # class attribute
#     age = 0
#
#     def __init__(self, first_name: str, last_name: str):
#         # object attribute
#         self.last_name = last_name
#         self.first_name = first_name
#         print("A person has been created..!")
#
#     def get_full_name(self) -> str:
#         return self.first_name + " " + self.last_name
#
#     def get_meta_information(self) -> list:
#         """
#         Person sınıfı hakkında meta bilgi (dir) döndürür.
#         """
#         return dir(Person)
#
#
# person_1 = Person("Burak", "Yılmaz")
# print(person_1.get_full_name())
# print(person_1.get_meta_information())
#
#
# Child Class - Employee
# class Employee(Person):  # Employee sınıfı artık Person sınıfın bütün özelliklerine sahip olacak
#     """
#     Person'dan türeyen Employee örneği.
#     Şu an ekstra alan eklemeden sadece inheritance gösteriyoruz.
#     """
#     pass
#
#
# employee_1 = Employee("Hakan", "Yılmaz")
# employee_1.age = 37
# print(employee_1.get_full_name())
# print(employee_1.get_meta_information())
# print("Employee age:", employee_1.age)
# endregion


# region Multiple Inheritance (Çoklu Kalıtım) - Bird Classes
# Base Class - Swimming Bird
# class SwimmingBird:
#     """
#     Yüzebilme yeteneği olan kuşlar için davranış sınıfı.
#     """

#     def swim(self) -> None:
#         print('Birds that can swim')


# # Base Class - Flying Bird
# class FlyingBird:
#     """
#     Uçabilme yeteneği olan kuşlar için davranış sınıfı.
#     """

#     def fly(self) -> None:
#         print('Birds that can fly')


# Base Class - Walking Bird
# class WalkingBird:
#     """
#     Yürüyebilme yeteneği olan kuşlar için davranış sınıfı.
#     """

#     def walk(self) -> None:
#         print('Birds that can walk')


# # Child Class - Penguin 
# Çoklu kalıtım ile sadece gerekli yetenekler alınır.
# class Penguin(SwimmingBird, WalkingBird):
#     """
#     Penguen:
#     ✔ Yüzebilir
#     ✔ Yürüyebilir
#     ✖ Uçamaz

#     Birden fazla sınıftan kalıtım alarak
#     sadece ihtiyacı olan yetenekleri kazanır.
#     """
#     pass


# Child Class - Chicken
# class Chicken(WalkingBird):
#     """
#     Tavuk:
#     ✔ Yürüyebilir
#     ✖ Uçamaz (uzun süreli)
#     ✖ Yüzemez

#     Tekli kalıtım örneği.
#     """
#     pass


# # Child Class - Eagle 
# class Eagle(FlyingBird, SwimmingBird):
#     """
#     Kartal:
#     ✔ Uçabilir
#     ✔ Yüzebilir
#     ✖ Uzun süreli yürüme yeteneği yok

#     Çoklu kalıtım ile birden fazla davranış kazanır.
#     """
#     pass


# penguin = Penguin()
# penguin.swim()
# penguin.walk()

# print('----------------------')

# chicken = Chicken()
# chicken.walk()

# print('----------------------')

# eagle = Eagle()
# eagle.fly()
# eagle.swim()
# endregion


# region Multiple Inheritance - Car Classes
# Base Class - Car 
# class Car:
#     model: str = ""
#     brand: str = ""
#
#
# Child Class - Sedan
# class Sedan(Car):
#     """Sedan araç: Car'dan kalıtım alır, ekstra alanlar ekler."""
#     door_count: str = ""
#     engine_volume: str = ""
#
#
# Child Class - Astra
# class Astra(Sedan):
#     """Sedan -> Astra (çok katmanlı kalıtım)."""
#     pass
#
#
# Child Class - Megane
# class Megane(Sedan):
#     """Sedan -> Megane (çok katmanlı kalıtım)."""
#     pass
#
#
# astra_1 = Astra()
# astra_1.model = "Opel"
# astra_1.brand = "Astra 2022"
# astra_1.door_count = "4"
# astra_1.engine_volume = "4.5"

# print("Astra:", astra_1.__dict__)
# Not: class attribute kullandığımız için __dict__ boş olabilir,
# çünkü değerler class seviyesinde tutuluyor.
# Bu yüzden doğrudan attribute'ları da göstermek iyi olur:
# print("Astra Details:", astra_1.brand, astra_1.model, astra_1.door_count, astra_1.engine_volume)
# endregion


#  region Multiple Inheritance - Employee / HumanResource
# BaseEntity adında bir ata sınıf oluşturunuz.
# Id, first_name, last_name, salary, departmant, create_date, status gibi özelikleri olsun.
# Employee adında bir sınıf oluşturunuz. BaseEntity'den kalıtım alsın.
# Human_Resource sınıfı yaratınız. Bu sınıf Employee Create, Read, Update ve Delete edebilsin. Bu işlemlere kısaca CRUD denir.

# from enum import Enum
# from datetime import datetime
# from typing import Optional
#
# Employee yaratma, okuma, güncelleme ve silme işlemleri için bu listeyi kullanacağız. 
# Yani bir Employee yaratıldığında bu listeye atılacak. 
# Bu listede ki bir Employee çağrılarak güncellenip yine buraya eklenecek vb.
# employees = []
#
#
# Enum uygulamalarda ki sabitlerimizi tanımladığımı ve yönettiğimiz bir sistemdir. 
# Listeye benzetebiliriz. Anahtar değer mantığıyla çalışırlar. 
# Şayet bir anahtara bir değer atamazsak listede ki gibi kendisi indexleme yaparak değerleri oluşturur. 
# Yani aşağıda ben 1001, 1002, 1003 diyerek ilerledim. 
# Bunu yapmasaydım kendisi indexleyeceğinden sıfırdan başlayarak değer verecekti.
# class Status(Enum):
#     """
#     Employee için durumlar.

#     Not:
#     - Magic number yerine Enum kullanmak daha güvenlidir.
#     """
#     ACTIVE = 1001
#     MODIFIED = 1002
#     PASSIVE = 1003
#
#
# class BaseEntity:
#     def __init__(self, Id: int, first_name: str, last_name: str, salary: int, departmant: str,
#                  create_date: Optional[datetime] = None, status: Status = Status.ACTIVE):
#         # validation
#         if int(salary) < 0:
#             raise ValueError("Salary cannot be negative!")

#         if create_date is None:
#             create_date = datetime.now()

#         self.Id = int(Id)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = int(salary)
#         self.departmant = departmant
#         self.create_date = create_date
#         self.status = status

#
#
# class Employee(BaseEntity):
#     """
#     Employee, BaseEntity’den kalıtım alır.
#     Şu an ekstra alan eklemedik.
#     """
#     pass
#
#
# class Human_Resource:
#     """
#     HumanResource: Employee CRUD yapar.

#     Not (önemli):
#     - HR bir "entity" değil, bir "service/manager" gibi davranır.
#     - Bu yüzden BaseEntity’den kalıtım aldırmak yerine bağımsız sınıf yapmak daha doğru.
#     """
#
#     # region Create New Employee
#     # Aşağıda ki methoda parametresinin tipi Employee'dir. 
#     # Bugüne kadar parametrelerin tipleri python içerisinde ki built-in olarak bulunan objelerdi. örneğin int, string, dict, list vb. 
#     # Burada kendi yarattığımızı nesneyi tip olarak kullanıyoruz.
#     def create_new_employee(self, new_employee: Employee) -> None:
#         """
#         Employee kaydeder (listeye ekler).

#         Not:
#         - Basit benzersiz id kontrolü ekledik.
#         """
#         if any(employee.Id == new_employee.Id for employee in employees):
#             print("⚠️ Employee already exists with same id!")
#             return

#         employees.append(new_employee)
#         print("Employee has been crated..!")
#
#     # İnsan kaynakları uzmanının yeni çalışanın bilgilerini girmesi lazım
#     def take_information_new_employee(self, Id: int, first_name: str, last_name: str, salary: int, departmant: str,
#                                       create_date: Optional[datetime] = None, status: Status = Status.ACTIVE) -> Employee:
#         """
#         Yeni bir Employee instance üretir (henüz listeye eklemez).

#         return: This function return the instance object of Employee class
#         """

#         if int(salary) < 0:
#             raise ValueError("Salary cannot be negative!")

#         if create_date is None:
#             create_date = datetime.now()

#         return Employee(Id=int(Id), first_name=first_name, last_name=last_name, salary=int(salary), 
#                         departmant=departmant, create_date=create_date, status=status)  # burada aslında instance alıyoruz.
#     # endregion
#
#     # region Read All Employees
#     def get_all_employee(self) -> None:
#         """
#         Tüm aktif employee kayıtlarını listeler.
#         """
#         print("\n[Employees List]")
#         found = False
#         for employee in employees:
#             if employee.status != Status.PASSIVE:
#                 found = True
#                 self._print_employee(employee)

#         if not found:
#             print("No active employee found.")#
#     # endregion
#
#     # region Read Employees by Id information
#     def get_by_id_employee(self, Id: int) -> None:
#         """
#         Id ile active employee getirir.
#         """
#         for employee in employees:
#             if int(Id) == employee.Id and employee.status != Status.PASSIVE:
#                 print("\n[Employee Detail]")
#                 self._print_employee(employee)
#                 return 

#         print("⚠️ Employee not found or passive.")#
#     # endregion
#
#     # Not: Update ve Delete işlemlerini yaparken dikkatli davranmamız gerekmektedir. 
#     # Bu yüzden güncelleyeceğimiz yada sileceğimiz kayıtları Id gibi biricik yani benzersiz bir alandan filtreleyerek Update yada Delete etmeliyiz. 
#     # Örneğin bir holdingte çalışan "Burak" isimli çalışanın maaşına zam yapılacak. 
#     # Şayet biz bu kullanıcıyı adından filtreler ve zam yaparsak holdingte çalışan bütün burak yılmazların maşına zam yapılımış olunur.
#     # region Update
#     def update_employee_department(self, Id: int, new_department: str) -> None:
#         """
#         Employee departmanını günceller.

#         Not:
#         - status MODIFIED yapılır.
#         """
#         for employee in employees:
#             if employee.Id == int(Id) and employee.status != Status.PASSIVE:
#                 employee.departmant = new_department
#                 employee.status = Status.MODIFIED
#                 print("✅ Employee department updated!")
#                 return

#         print("⚠️ Employee not found or passive.")

#     def update_employee_salary(self, Id: int, new_salary: int) -> None:
#         """
#         Maaş güncelleme
#         - salary güncellensin
#         - status MODIFIED olsun
#         - bulunamazsa mesaj basılsın
#         - validation: negatif olmasın
#         """
#         if int(new_salary) < 0:
#             print("⚠️ Invalid salary! Salary cannot be negative.")
#             return

#         for employee in employees:
#             if employee.Id == int(Id) and employee.status != Status.PASSIVE:
#                 employee.salary = int(new_salary)
#                 employee.status = Status.MODIFIED
#                 print("✅ Employee salary updated!")
#                 return

#         print("⚠️ Employee not found or passive.")
#     endregion
#
#
#     # region Delete (Soft Delete)
#     def delete_employee(self, Id: int) -> None:
#         """
#         Soft delete: status PASSIVE yapılır.
#         """
#         for employee in employees:
#             if employee.Id == int(Id) and employee.status != Status.PASSIVE:
#                 employee.status = Status.PASSIVE
#                 print("✅ Employee has been deleted (soft delete).")
#                 return

#         print("⚠️ Employee not found or already passive.")
#     # endregion

# # region Helpers
#     @staticmethod
#     def _print_employee(emp: Employee) -> None:
#         print(
#             f"Id: {emp.Id}\n"
#             f"First Name: {emp.first_name}\n"
#             f"Last Name: {emp.last_name}\n"
#             f"Department: {emp.departmant}\n"
#             f"Salary: {emp.salary}\n"
#             f"Create Date: {emp.create_date}\n"
#             f"Status: {emp.status.name}\n"
#             "--------------------------"
#         )
#     # endregion
#
#
# # region Main
# def main():
#     human_resource_1 = Human_Resource()

#     while True: 
#         process = input(
#                         "\nCreate New Employee ==> 1\n"
#                         "List of Emploees    ==> 2\n"
#                         "Get Employee By Id  ==> 3\n"
#                         "Update Employee     ==> 4\n"
#                         "Update Salary       ==> 5\n"
#                         "Delete Employee     ==> 6\n"
#                         "For Exit            ==> e\n"
#                         "Plase choose a process: "
#                     ).strip().lower()

#         if process == "1":
#             try:
#                 Id = int(input("Id: "))
#                 first_name = input("First Name: ")
#                 last_name = input("Last Name: ")
#                 departmant = input("Departmant: ")
#                 salary = int(input("Salary: "))

#                 new_employee = human_resource_1.take_information_new_employee(Id=Id, first_name=first_name,
#                     last_name=last_name, salary=salary, departmant=departmant, create_date=datetime.now(),
#                     status=Status.ACTIVE)
#                 human_resource_1.create_new_employee(new_employee)
#             except ValueError as e:
#                 print(f"⚠️ {e}")

#         elif process == "2":
#             human_resource_1.get_all_employee()
#         elif process == "3":
#             Id = int(input("Id: "))
#             human_resource_1.get_by_id_employee(Id)
#         elif process == "4":
#             Id = int(input("Id: "))
#             new_department = input("Department: ")
#             human_resource_1.update_employee_department(Id, new_department)
#             human_resource_1.get_by_id_employee(Id)
#         elif process == "5":
#             Id = int(input("Id: "))
#             new_salary = int(input("New Salary: "))
#             human_resource_1.update_employee_salary(Id, new_salary)
#         elif process == "6":
#             Id = int(input("Id: "))
#             human_resource_1.delete_employee(Id)
#         elif process == "e":
#             print("Applciation is closing..!")
#             break
#         else:
#             print("Please choose a valid process..!")


# if __name__ == "__main__":
#     main()
# # endregion


# region Multiple Inheritance - Product Classes
# Product nesnesi üzerinden CRUD operasyonları yürütelim
# BaseEntity mantığımız olucak.
# BaseEntity ID, name, description, unit_price, stock, create_date, update_date, delete_date, machine_name, ip_adress, status alanları bulunsun.

from socket import gethostname, gethostbyname
from enum import Enum
from datetime import datetime
from typing import Optional


products = []


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


def _next_product_id() -> int:
    """
    Auto-increment ID:
    - list boşsa 1
    - doluysa max(ID)+1
    """
    if not products:
        return 1
    
    return max(product.ID for product in products) + 1


class BaseEntity:
    def __init__(self, ID: int, name: str, description: str, unit_price: float, stock: int,
                create_date: Optional[datetime] = None, update_date: Optional[datetime] = None, delete_date: Optional[datetime] = None,
                machine_name: Optional[str] = None, ip_address: Optional[str] = None, status: Status = Status.Active):
        
        # validation
        if float(unit_price) < 0:
            raise ValueError("Unit price cannot be negative!")
        if int(stock) < 0:
            raise ValueError("Stock cannot be negative!")

        if create_date is None:
            create_date = datetime.now()

        if machine_name is None:
            machine_name = gethostname()

        if ip_address is None:
            # gethostbyname için hostname veriyoruz
            ip_address = gethostbyname(machine_name)

        self.ID = int(ID)
        self.name = name
        self.description = description
        self.unit_price = float(unit_price)
        self.stock = int(stock)

        self.create_date = create_date
        self.update_date = update_date
        self.delete_date = delete_date

        self.machine_name = machine_name
        self.ip_address = ip_address
        self.status = status


class Product(BaseEntity):
    """Product, ProductBaseEntity'den kalıtım alır."""
    pass


class ProductRepository:

    # region Create
    def create(self, new_product: Product) -> None:
        if any(product.ID == new_product.ID for product in products):
            print("⚠️ Product already exists with same id!")
            return

        products.append(new_product)
        print("✅ Product has been created!")

    def take_new_product_information(self, ID: Optional[int], name: str, description: str, unit_price: float, stock: int, 
                                    create_date: Optional[datetime] = None, update_date: Optional[datetime] = None, delete_date: Optional[datetime] = None, 
                                    status: Status = Status.Active) -> Product:
        """
        Product instance üretir.
        - ID verilmezse auto-increment
        - machine_name otomatik
        - ip_adress otomatik
        - create_date yoksa now
        """
        if ID is None:
            ID = _next_product_id()
        
        if float(unit_price) < 0:
            raise ValueError("Unit price cannot be negative!")
        if int(stock) < 0:
            raise ValueError("Stock cannot be negative!")
        
        if create_date is None:
            create_date = datetime.now()

        return Product(ID=int(ID), name=name, description=description, unit_price=float(unit_price), 
                       stock=int(stock), create_date=create_date, update_date=update_date, delete_date=delete_date, status=status)
    # endregion

    # region Read All Product
    def get_active_products(self) -> None:
        print("\n[Active Products]")
        found = False
        for product in products:
            if product.status != Status.Passive:
                found = True
                self._print_product(product)

        if not found:
            print("No active product found.")

    def get_trash_products(self) -> None:
        print("\n[Trash (Passive Products)]")
        found = False
        for product in products:
            if product.status == Status.Passive:
                found = True
                self._print_product(product)

        if not found:
            print("Trash is empty.")

    def get_all_product(self):
        print("\n[Products List]")
        found = False
        for product in products:
            if product.status != Status.Passive:
                found = True
                self._print_product(product)

        if not found:
            print("No active product found.")

    def get_by_id(self, ID: int, include_passive: bool = False) -> None:
        for product in products:
            if product.ID == int(ID) and (include_passive or p.status != Status.Passive):
                print("\n[Product Detail]")
                self._print_product(product)
                return
            
        print("⚠️ Product not found or passive.")

    def search_by_name(self, keyword: str, include_passive: bool = False) -> None:
        keyword = keyword.strip().lower()
        print(f"\n[Search Results: '{keyword}']")
        found = False

        for product in products:
            if not include_passive and product.status == Status.Passive:
                continue

            if keyword in product.name.lower():
                found = True
                self._print_product(product)

        if not found:
            print("No product matched your search.")

    def get_product_by_price(self, minimum_price: float, maximum_price: float) -> None:
        print(f"\n[Products Price Range: {minimum_price} - {maximum_price}]")
        found = False
        for product in products:
            if product.status != Status.Passive and (minimum_price <= product.unit_price <= maximum_price):
                found = True
                self._print_product(product)

        if not found:
            print("No product found in this range.")

    def get_by_min_stock(self, min_stock: int) -> None:
        print(f"\n[Products - Min Stock >= {min_stock}]")
        found = False
        for product in products:
            if product.status != Status.Passive and product.stock >= int(min_stock):
                found = True
                self._print_product(product)

        if not found:
            print("No product found for this stock criteria.")
    # endregion


    # region Update
    def update_price(self, ID: int, new_price: float) -> None:
        """
        update_price
        - unit_price güncelle
        - status MODIFIED
        - update_date now
        """
        if float(new_price) < 0:
            print("⚠️ Invalid price! Price cannot be negative.")
            return
        
        for product in products:
            if product.ID == int(ID) and product.status != Status.Passive:
                product.unit_price = float(new_price)
                product.update_date = datetime.now()
                product.status = Status.Modified
                print("✅ Product price updated!")
                return
            
        print("⚠️ Product not found or passive.")

    def update_stock(self, ID: int, new_stock: int) -> None:
        if int(new_stock) < 0:
            print("⚠️ Invalid stock! Stock cannot be negative.")
            return
        
        for product in products:
            if product.ID == int(ID) and product.status != Status.Passive:
                product.stock = int(new_stock)
                product.update_date = datetime.now()
                product.status = Status.Modified
                print("✅ Product stock updated!")
                return
            
        print("⚠️ Product not found or passive.")
    # endregion


    # region Delete (Soft Delete)
    def delete(self, ID: int) -> None:
        for product in products:
            if product.ID == int(ID) and product.status != Status.Passive:
                product.status = Status.Passive
                product.delete_date = datetime.now()
                print("✅ Product deleted (soft delete).")
                return            
        print("⚠️ Product not found or already passive.")

    def restore(self, ID: int) -> None:
        for product in products:
            if product.ID == int(ID) and product.status == Status.Passive:
                product.status = Status.Modified
                product.delete_date = None
                product.update_date = datetime.now()
                print("✅ Product restored from trash.")
                return            
        print("⚠️ Product not found in trash.")

    def hard_delete(self, ID: int) -> None:
        """
        Tam silme: listeden çıkarır (geri dönüş yok)
        """
        for index, product in enumerate(products):
            if product.ID == int(ID):
                products.pop(index)
                print("🗑️ Product hard deleted (permanent).")
                return
        print("⚠️ Product not found.")
    # endregion

    # region Helpers
    @staticmethod
    def _print_product(product: Product) -> None:
        print(
            f"Id: {product.ID}\n"
            f"Name: {product.name}\n"
            f"Description: {product.description}\n"
            f"Unit Price: {product.unit_price}\n"
            f"Stock: {product.stock}\n"
            f"Create Date: {product.create_date}\n"
            f"Update Date: {product.update_date}\n"
            f"Delete Date: {product.delete_date}\n"
            f"Machine: {product.machine_name}\n"
            f"IP: {product.ip_address}\n"
            f"Status: {product.status}\n"
            "--------------------------"
        )
    # endregion


def product_menu(repo: ProductRepository) -> None:
    while True:
        print(
            "\n=== PRODUCT MENU (PRO) ===\n"
            "Create New Product            ==> 1\n"
            "List Active Products          ==> 2\n"
            "Get Product By ID             ==> 3\n"
            "Search By Name                ==> 4\n"
            "Update Price                  ==> 5\n"
            "Update Stock                  ==> 6\n"
            "Soft Delete (Move to Trash)   ==> 7\n"
            "Trash (List Passive)          ==> 8\n"
            "Restore From Trash            ==> 9\n"
            "Hard Delete (Permanent)       ==> 10\n"
            "Filter Price Range            ==> 11\n"
            "Filter By Min Stock           ==> 12\n"
            "Back                          ==> b\n"
        )
        choice = input("Choose: ").strip().lower()

        if choice == "1":
            try:
                raw_id = input("ID (boş bırak = otomatik): ").strip()
                ID = int(raw_id) if raw_id else None
                name = input("Name: ")
                desc = input("Description: ")
                price = float(input("Unit Price: "))
                stock = int(input("Stock: "))

                product = repo.take_new_product_information(ID=ID, name=name, description=desc, unit_price=price, stock=stock)
                repo.create(product)
            except ValueError as e:
                print(f"⚠️ {e}")

        elif choice == "2":
            repo.get_active_products()

        elif choice == "3":
            ID = int(input("ID: "))
            repo.get_by_id(ID, include_passive=True)

        elif choice == "4":
            word = input("Keyword: ")
            repo.search_by_name(word, include_passive=False)

        elif choice == "5":
            ID = int(input("ID: "))
            new_price = float(input("New Price: "))
            repo.update_price(ID, new_price)

        elif choice == "6":
            ID = int(input("ID: "))
            new_stock = int(input("New Stock: "))
            repo.update_stock(ID, new_stock)

        elif choice == "7":
            ID = int(input("ID: "))
            repo.delete(ID)

        elif choice == "8":
            repo.get_trash_products()

        elif choice == "9":
            ID = int(input("ID (trash): "))
            repo.restore(ID)

        elif choice == "10":
            ID = int(input("ID (permanent): "))
            repo.hard_delete(ID)

        elif choice == "11":
            min_price = float(input("Min Price: "))
            max_price = float(input("Max Price: "))
            repo.get_product_by_price(min_price, max_price)

        elif choice == "12":
            min_stock = int(input("Min Stock: "))
            repo.get_by_min_stock(min_stock)

        elif choice == "b":
            return

        else:
            print("⚠️ Invalid choice!")


def main() -> None:
    repo = ProductRepository()

    # demo data (istersen sil)
    repo.create(repo.take_new_product_information(101, "Laptop", "Gaming laptop", 49999.99, 5))
    repo.create(repo.take_new_product_information(102, "Mouse", "Wireless mouse", 799.50, 50))
    repo.create(repo.take_new_product_information(103, "Keyboard", "Mechanical keyboard", 2499.00, 20))

    while True:
        print(
            "\n====================\n"
            "   MAIN MENU\n"
            "====================\n"
            "Product Operations   ==> 1\n"
            "Exit                 ==> e\n"
        )
        choice = input("Choose: ").strip().lower()

        if choice == "1":
            product_menu(repo)
        elif choice == "e":
            print("Application is closing..!")
            return
        else:
            print("⚠️ Invalid choice!")


if __name__ == "__main__":
    main()

# endregion