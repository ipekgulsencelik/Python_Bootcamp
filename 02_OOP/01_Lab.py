
#! Object Oriented Programming - Class

# Bizlere kendi nesnelerimizi yaratma imkanı sunar. 
# Bugüne kadar python içerisinde built-in olarak bulunan bir çok nesne kullanıdk. 
# int, list, dictionary, random, fileio vb. 

# Artık projenin kapsamına göre ihtiyaç duyduğumuz nesnelerimizi 
# oop'ûn bizelere sunduğu 'class' mekanizması ile yaratabileceğiz. 

# Örneğin bir e-ticaret sitesi yapıyoruz
# ihtiyaç duyacağımız nesneler, user, employee, product, category, order vb olacaktır. 
# BU nesneleri sınıflar (class) aracılığuyla yaratabilecceğiz.

# region Class - Vehicle 
# Gerçek hayatta bir araba, ev, telefon, termos artık ne üreteceksek ilk önce bu üretilecek nesnenin özelliklerini içeren bir prototip yaratılır. Yazılım dünyasında bu prototiplere sınıf (class) diyoruz. yani yaratacağımız nesnenin özelliklerini bu sınıflarda tanımlıyoruz.

# Şimdi bir araba nesnesi yaratamak için ilk önce ihtiyaç duyduğumuz bu araba nesnenin özelliklerini içeren bir sınıf tanımlıyoruz.
# class Vehicle:
#     # sınıfı özelliklerini (class attribute) tanımlayaccağız. 
#     # Vehicle isimli nesenemin sahip olacağı özellikleri değişken tanımlar gibi burada tanımlayarak bir prototip inşa ediyorum.
    
#     # Bunlar CLASS ATTRIBUTE’lardır
#     # Varsayılan (default) değerlerdir
#     door_number = 0
#     engine_size = 0
#     torque = 0
#     length = 3.1
#     width = 1.2
#     color = 'black'
#     model = ""
#     brand = ""
#     cylinder = 0


# Projemde ihtiyaç duyduğum Vehicle'ın özelliklerini içeren sınıfımı yukarıda tanımladım. 
# Yani prototipim hazır artık bu prototipten istediğim yerde istediğim kadar nesne üretebilirim.
# Vehicle sınıfından bir nesne (instance) oluşturuluyor
# car_1 = Vehicle()  # tam olarak burada Vehicle sınıfımdan bir örneklem (instance) alarak nesne ürettim.

# aşağıda car_1 nesnesi üzerinden "." notasyonu kullanılarak örneklemi (instance) çıkarılan sınıfın attributelerine erişerek onalara istediğimi bilgileri assigned ettik.
# "." notasyonu ile instance attribute atanıyor
# car_1.brand = 'Dodge'
# car_1.model = 'TRX1500'
# car_1.torque = 9000
# car_1.cylinder = 5.6
# car_1.engine_size = 9

# Yukarıda ki işlem sonucunda içerisinde bazı bilgilere sahip bir car_1 isimli nesnem var.
# print(f'Brand: {car_1.brand}\n'
#       f'Model: {car_1.model}\n'
#       f'Torque: {car_1.torque}\n'
#       f'Cylinder: {car_1.cylinder}\n'
#       f'Engine Size: {car_1.engine_size}')

# İkinci bir Vehicle nesnesi
# car_2 = Vehicle()

# car_2.engine_size = 7.8
# car_2.torque = 900
# car_2.cylinder = 8.9
# car_2.brand = 'Ford'
# car_2.model = 'F150'

# print(f'Brand: {car_2.brand}\n'
#       f'Model: {car_2.model}\n'
#       f'Torque: {car_2.torque}\n'
#       f'Cylinder: {car_2.cylinder}\n'
#       f'Engine Size: {car_2.engine_size}')

# car_1 ve car_2 aynı sınıftan, ama farklı nesnelerdir.
# endregion


# region Class - Boxer
# class Boxer:
#     alias = ""
#     height = 0.0
#     weight = 0
#     full_name = ""
#     win = 0
#     lost = 0

# boxer_1 = Boxer()

# boxer_1.alias = 'iron'
# boxer_1.height = 1.80
# boxer_1.weight = 100
# boxer_1.win = 66
# boxer_1.lost = 4

# __dict__ sadece instance’a ait alanları gösterir
# print(boxer_1.__dict__)
# endregion


# region Constructor (Yapıcı Method)
# Sınıflardan (class) örneklem (instance) çıkarıldığında ilk ve otomatik olarak tetitklenen methodtur. 
# Bu method üzerine yüklenilen iş bize sorulmadan otomatik olarak icra edilir. 
# Asıl amaçları sınıfları kullanıma hazrılamaktır.

# region Class - Student 
# class Student:
#     # ✔ class attribute
#     # Tüm Student nesneleri tarafından PAYLAŞILIR
#     taken_courses = ['History I', 'Algorithm']  # ❗ CLASS ATTRIBUTE (mutable)

#     def __init__(self, full_name: str, student_id: str):
#         """
#         Bu metot:
#         - Sınıftan bir nesne oluşturulduğunda otomatik olarak çalışır
#         - Nesneye ait özellikleri (instance attribute) tanımlar
#         """
#         # ✔ instance attribute
#         # Her nesneye ÖZEL
#         # Öğrencinin tam adını nesneye ait bir özellik olarak atar
#         self.tam_ad = full_name

#         # Öğrencinin id bilgisini nesneye ait bir özellik olarak atar
#         self.ogrenci_id = student_id

# Student sınıfından bir nesne (instance) oluşturuluyor
# student_1 = Student(full_name="burak yilmaz", student_id="123456789")

# __dict__:
# - Nesneye ait olan attribute'ları sözlük (dict) olarak gösterir
# - Sadece instance'a ait veriler burada yer alır
# print(student_1.__dict__)   # SADECE instance’a ait olanlar

# print(
#     f'Student Name: {student_1.tam_ad}\n'
#     f'Student Id: {student_1.ogrenci_id}\n'
#     f'Taken Courses: {student_1.taken_courses}\n'
# )

# print(dir(Student))     # Bir nesnenin ulaşabildiği TÜM attribute ve methodları listeler
# Buna şunlar dahildir: class attribute’lar, methodlar, magic methodlar (__init__, __dict__, __module__), inheritance ile gelenler
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', '__weakref__', 'taken_courses']
# taken_courses burada görünür çünkü: class attribute, Student sınıfına aittir
# tam_ad, ogrenci_id → YOK (çünkü instance attribute)

# print(dir(student_1))     # nesnesinin ULAŞABİLDİĞİ TÜM attribute ve methodları listeler.
# Buna şunlar dahildir: instance attribute’lar (tam_ad, ogrenci_id), class attribute’lar (varsa), magic methodlar (__init__, __dict__, __str__, vs.), inheritance ile gelenler
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', '__weakref__', 'ogrenci_id', 'taken_courses', 'tam_ad']
# tam_ad → instance attribute ✅
# ogrenci_id → instance attribute ✅
# taken_courses → class attribute ama erişilebilir ✅
# endregion


# boxers = list()
# print(dir(boxers))
# ['__add__', '__class__', '__class_getitem__', '__contains__', __delattr__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',  '__iadd__', '__imul__', 
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__','__setattr__', '__sizeof__', '__sizeof__', 
# '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 
# 'remove', 'reverse', 'sort']
# Bunların hepsi list sınıfının method ve magic methodlarıdır.

# dir() = Ulaşabildiğin her şey
# __dict__ = Gerçekte sahip oldukların


# region Class - Circle
# class Cirle:
#     """
#     Circle sınıfı bir daireyi temsil eder.
#     Yarıçap bilgisi alır ve alan / çevre hesaplaması yapar.
#     """

#     # class attribute
#     # Tüm Circle nesneleri için ortak olan sabit değer
#     pi = 3.14
#
#     def __init__(self, r=0.1):
#         """
#         Circle nesnesi oluşturulurken çalışan kurucu metot.

#         Args:
#             r (int): Dairenin yarıçapı
#         """
#         # Instance attribute
#         # Her nesneye özel yarıçap değeri
#         # radius => object attiribute
#         self.radius = r
#
#     def calculate_area(self):
#         """
#         Dairenin alanını hesaplar.

#         Formül:
#             Alan = π * r²

#         Returns:
#             float: Dairenin alanı
#         """
#         return self.pi * self.radius ** 2
#
#     def calculate_environment(self):
#         """
#         Dairenin çevresini hesaplar.

#         Formül:
#             Çevre = 2 * π * r

#         Returns:
#             float: Dairenin çevresi
#         """
#         return 2 * self.pi * self.radius
#
#
# r = float(input("Please type into radius value: "))
# circle_1 = Cirle(r)
# print(f'Alan: {circle_1.calculate_area()}')
# print(f'Çevre: {circle_1.calculate_environment()}')

# print(dir(circle_1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'calculate_area', 'calculate_environment', 'pi', 'radius']

# print(dir(Cirle))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'calculate_area', 'calculate_environment', 'pi']
# endregion


# region Class - Soccer Player
# class Soccer_Player:
#     # __init__() methodu python içerisinde built-in olarak bulunmaktadır. 
#     # Yukarıda izah ettiğimiz gibi sınıfımızı örneklem alındığında 
#     # kendisine argüman olarak verilen özellikler ile sınıfın yaratılmasını temin eder. 
#     # Yazılımcı ağızı ile konuşmak gerekirse sınıfımızı initialize etmeye başlatamaya yarar.
#     def __init__(self, player_name: str, player_number: int):
#         # self anahtar sözcüğü ise ilgili sınıfı işaret eder. 
#         # Bir başka değiş ile sınıfın kendisini temsil eder. 
#         # Burada ki self ifadesi yerina mahmutta kullanabilirdir. 
#         # self ifadesi bir best practice'dir.
#         # self → o an oluşturulan nesnenin kendisi
#         self.name = player_name
#         self.number = player_number
#         # Yukarıda ki iki satırda dışarıdan gelen argümanları sınıfın örneklemi alınırken 
#         # o anda yaratılan 'name' ve 'number' object attibutelerine atar.


# player_1 = Soccer_Player("Messi", 10)  # burada 'Soccer_Player("Messi", 10)' ifadesi ile yapılan şey aslında __init__() methodu tetiklenmesidir.
# İlk yaptığımız örnekte burada instance name üzerinden 'class attribute' değer atamıştık. 
# Şimdi öyle bir şey yapmadan direk attribute'leri print ettik. 
# Bu demek oluyor ki sınıfımız "Messi" ve 10 bilgileri ile birlikte kullanıma hazırlandı.
# print(f'Name: {player_1.name}\n'
#       f'Number: {player_1.number}')
# endregion


# region Class - Department
# class Department:
#     """
#     Department sınıfı bir departmanda çalışan personelleri temsil eder.
#     Her nesne bir çalışanı ifade eder.
#     """

#     # region Class Attributes
#     # Tüm nesneler için ortak (class-level) değişkenler
#     department_name = ""
#     employee_count = 0

#     def __init__(self, name: str, age: int):
#         """
#         Department nesnesi oluşturulurken çalışan bilgileri atanır.

#         Args:
#             name (str): Çalışanın adı
#             age (int): Çalışanın yaşı
#         """

#         # Instance attributes (nesneye özel)
#         self.adi = name
#         self.yas = age

#         # Class attribute güncelleme
#         # DİKKAT: employee_count tüm nesneler için ortaktır
#         Department.employee_count += 1 

#     def show_info(self):
#         """
#         Çalışanın kişisel bilgilerini ve departman bilgisini ekrana yazdırır.
#         """
#         print(
#             f'Name: {self.adi}\n'
#             f'Age: {self.yas}\n'
#             f'Department Name: {self.department_name}'
#         )

#     def show_employee_count(self):
#         """
#         Toplam çalışan sayısını ekrana yazdırır.
#         """
#         print(f'Total Employee: {Department.employee_count}')

# 1. çalışan
# department_1 = Department(name="burak", age=36)

# ⚠️ DİKKAT: Bu satır class attribute'u DEĞİL,
# instance attribute oluşturur (shadowing)
# department_1.department_name = "ARGE"

# department_1.show_info()
# department_1.show_employee_count()

# print("----------------------")

# 2. çalışan
# department_2 = Department(name="hakan", age=39)

# Yine instance attribute oluşur
# department_2.department_name = "Amele"

# department_2.show_info()
# department_2.show_employee_count()

# print("----------------------")

# 3. çalışan
# department_3 = Department(name="ipek", age=42)

# Yine instance attribute oluşur
# department_3.department_name = "Historian Art"

# department_3.show_info()
# department_3.show_employee_count()
# endregion


# region Class - Person
# class Person:
    # class attribute
    # address = ""
    # user_name = ""

    # def __init__(self, first_name='', last_name='', birth_date=''):
        # ad ve soyad object attribute ilglili sınıftan kalıtım alındıktan sonra erişilir ve üzerlerine değer atılabilinir. 
        # Yani şuan Person. dediğimizde ad ve soyad attributelerine sınıf dışarısında ise erişemeyiz.
        # self.ad = first_name
        # self.soyad = last_name
        # self.dogum_tarihi = birth_date

# Person.address
# Person.user_name
# yukarı da gördüğünüz gibi Person. dediğimde class attribute'lerine erişebiliyorum. 
# Bu demek oluyor ki sınıfın bu üyelerine her zaman erişebiliyorum. 
# Lakin ad, soyad ve doğum_tarihi gibi object attribute'lerine erişemiyorum. 
# Bunun nedeni ise bu attribute'lerin daha yaratılmamasıdır. 
# Bunun nedeni ise __init__() doğasında gizlidir. 
# Yani init() sınıfımızı initilize ettiğinde dışarıdan gelen değerleri yani argümanalrı alır 
# ve self. aracılığıyla ilgili alanları yaratarak onlara bu değerleri assigned eder.
# person_1 = Person()
# endregion


# region Class - Software Developer
# class SoftwareDeveloper:
#     # class attribute
#     knowledge_languages = []

#     def __init__(self, first_name: str, last_name: str):
#         # object attributes
#         self.first_name = first_name
#         self.last_name = last_name

#     # todo: add_new_language()
#     def add_new_language(self, language: str) -> str:
#         """
#         Yeni programlama dili / dilleri ekler.

#         Parametre:
#             language (str):
#         """

#         # Virgüle göre ayırıyoruz
#         languages = language.split(',')

#         for lang in languages:
#             # Boşlukları temizle + küçük harfe çevir
#             lang = lang.strip().lower()

#             # Aynı dil tekrar eklenmesin
#             if lang not in self.knowledge_languages:
#                 self.knowledge_languages.append(lang)

#         return 'Language has been added.'

#     # todo: show_info()
#     def show_info(self) -> str:
#         """
#         Developer bilgilerini string olarak döndürür.
#         """
#         return (
#             "=== SOFTWARE DEVELOPER INFO ===\n"
#             f"First Name : {self.first_name}\n"
#             f"Last Name  : {self.last_name}\n"
#             f"Languages  : {self.knowledge_languages}"
#         )

# dev = SoftwareDeveloper(first_name='Burak', last_name='Yilmaz')

# sample input --> 'python, c#, go'
# print(dev.add_new_language("python, c#, go"))

# sample input --> 'python'
# print(dev.add_new_language("python"))

p# rint(dev.show_info())

# sample - knowledge_languages = ['python', 'c#', 'go']
# print(SoftwareDeveloper.knowledge_languages)

# print(dev.add_new_language(language='python, c++, asp.net'))

# print(dev.show_info())
# endregion


# region Class - Teacher
# Teacher adında bir sınıf oluşturalım.
# Objecct Attribute => id, first_name, last_name
# Class Attribute => given_courses
# show_information isimli bir method ile ilgili sınıfın attribute'leri ekrana yazılsın
# class Teacher:
#     given_courses = ['Introduction to Philosophy']

#     def __init__(self, id: int, first_name: str, last_name: str):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name

#     def add_course(self, new_course: str):
#         values = new_course.split(',')
#         for value in values:
#             self.given_courses.append(value.lstrip())

#     def show_information(self):
#         print(f"Id: {self.id}")
#         print(f"First Name: {self.first_name}")
#         print(f"Last Name: {self.last_name}")
#         print("Given Courses")
#         print("============")
#         for course in self.given_courses:
#             print(f"Course: {course}")


# first_name = input("Please type teacher first name: ")
# last_name = input("Please type teacher last name: ")
# teacher_1 = Teacher(1, first_name, last_name)

# new_course = input("Type a new course name: ")
# teacher_1.add_course(new_course)

# teacher_1.show_information()
# endregion


# region Class - Doctor (Shared Specialty Pool)
# # class Doctor:
#     # class attribute
#     # Hastanede bulunan tüm uzmanlık alanları (ortak)
#     hospital_specialties = []

#     # region Constructor
#     def __init__(self, name: str, branch: str):
#         # object attributes
#         self.name = name
#         self.branch = branch
#     # endregion

#     # region Add Specialty
#     def add_specialty(self, specialties: str) -> None:
#         """
#         Hastaneye yeni uzmanlık alanı ekler.

#         Parametre:
#             specialties (str):
#                 'cardiology'
#                 'cardiology, neurology, pediatrics'
#         """

#         specialty_list = specialties.split(',')

#         for specialty in specialty_list:
#             specialty = specialty.strip().lower()

#             if specialty not in Doctor.hospital_specialties:
#                 Doctor.hospital_specialties.append(specialty)
#     # endregion

#     # region Show Info
#     def show_info(self) -> str:
#         """
#         Doktor bilgilerini ve hastanenin uzmanlık havuzunu gösterir.
#         """
#         return (
#             "=== DOCTOR INFO ===\n"
#             f"Name        : {self.name}\n"
#             f"Department  : {self.branch}\n"
#             f"Specialties : {Doctor.hospital_specialties}"
#         )
#     # endregion

# # region Doctors
# doctor_1 = Doctor("Mehmet Arslan", "Internal Medicine")
# doctor_2 = Doctor("Zeynep Korkmaz", "Pediatrics")
# # endregion

# # region Add Specialties
# doctor_1.add_specialty("cardiology, neurology")
# doctor_2.add_specialty("pediatrics, endocrinology")
# # endregion

# # Output
# print(doctor_1.show_info())
# print()
# print(doctor_2.show_info())
# endregion


# region Class - Character
# Character isminde bir sınıf yaratalım
# Object Attribute => name, race, role, level, weapon, armour, hp
# attack, defend, escape => fonksiyonları olsun
# saldırırken level + weapon kadar vursun
# savunurken level + armour kadar savunsun
# escape olduğunda tapuk yapsın

# class Character:
#     def __init__(self, name: str, race: str, role: str, level: int, weapon: int, armour: int, hp: int):
#         self.name = name
#         self.race = race
#         self.role = role
#         self.level = level
#         self.weapon = weapon
#         self.armour = armour
#         self.hp = hp

#     def attack(self):
#         return self.level + self.weapon

#     def defend(self):
#         return self.level + self.armour

#     def escape(self):
#         print('Escape the fight. Cowered..!')


# def main():
#     kara_murat = Character('Kara Murat', 'Turk', 'Akıncı', 100, 100, 0, 100)
#     savege_viking = Character('Raider', 'Viking', 'Asker', 80, 80, 100, 100)

#     bot_actions = []
#     bot_actions.append(savege_viking.attack())
#     tur = 1
#     while True:
#         action = input("For Attack ==> 'a'\n"
#                        "For Defend ==> 'b'\n"
#                        "For Escape ==> 'e'\n"
#                        "Choose your move: ")

#         if action == 'e':
#             savege_viking.escape()
#             break
#         elif action == 'a':
#             kara_murat.hp -= savege_viking.attack() - kara_murat.defend()
#             savege_viking.hp -= kara_murat.attack() - savege_viking.defend()

#             print("=======================")
#             print(f"Tur: {tur}")
#             print(f"{savege_viking.name} verdiği hasar --> {savege_viking.attack() - kara_murat.defend()}")
#             print(f"{kara_murat.name} verdiği hasar --> {kara_murat.attack() - savege_viking.defend()}")
#             print("=======================")
#             print(f"{savege_viking.name} kalan can --> {savege_viking.hp}")
#             print(f"{kara_murat.name} kalan can --> {kara_murat.hp}")
#         else:
#             print('Please valid action order..!')

#         if kara_murat.hp <= 0 and savege_viking.hp > 0:
#             print(f'{savege_viking.name} has victor..!')
#             break
#         elif kara_murat.hp > 0 and savege_viking.hp <= 0:
#             print(f'{kara_murat.name} has victor..!')
#             break
#         elif kara_murat.hp <= 0 and savege_viking.hp <= 0:
#             print(f'Bu dünya hiç kimseye kalmaz..! Savaşma .....!')
#             break

#         tur += 1


# main()

# endregion