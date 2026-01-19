
#! Encapsulation (Veri Gizleme)
# Bir sınıfın her hangi bir üyesini encapsulation ettiğimiz zaman, ilgili üyeye alt sınıflardan erişimi kapatmış oluyoruz. 
# Yani enkapsüle edilmiş üye alt sınıflarda değiştirilemeyecektir. 
# Buna bir nevi sınıf dışında erişime yani müdahele kapamamkta diyebiliriz. 
# Belirli şartlar doğruştusunda bu erişimi dolaylı yollar ile yapabiliyoruz.


from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self):
        # Enkapsüle edilecek attribute dışarıdan gelen değeri assigned etmiyoruz. 
        # Çünkü dış erşime kapalı olması için encapsule ediyoruz.
        self.__create_date = None
        self.__id = ""  # enkapsüle edilmiş üye başına double under score eklenir. Bunun anlamı bu üyenin encapsüle edildiği ve dışarıdan erişilemeyeceğidir.
        self.__created_computer_name = None
        self.__created_ip_address = None
        self.__status = None

    def set_value_private_attribute(self):
        """
        Bu methodun görevi enkapsüle ettiğimiz değerleri yani bizim private attribute'lerimize default değerler atamaktadır. Lakin bu method __init__() gibi çalışmamaktadır. Bir sınıftan örneklem aldığımızda init() tetikleniyordu. BU method tetiklenmez. Bu yüzden bu methodu instance objemiz üzerinden elle tetiklememiz gerekmektedir. Yada gidip init() içerisinde çağırmamız gerekir. Dış erişime kapadığımız bu attribute'leri incelerseniz aslında bunların loglama için kullanıldıklarını client ile her hangi bir bağlantısı olmadığını fark edeceksiniz. Yani client'ten değer alıp bazı işlemler yapıp onu veri tabanına kayıt edeceğim türden alanlar değiller.
        :return:
        """
        self.__id = uuid4()
        self.__create_date = datetime.now()
        self.__created_computer_name = gethostname()
        self.__created_ip_address = gethostbyname(gethostname())
        self.__status = Status.Active.name

    def show_infomation(self):
        print(f'Id: {self.__id}\n'
              f'Create Date: {self.__create_date}\n'
              f'Ip Address: {self.__created_ip_address}\n'
              f'Computer Name: {self.__created_computer_name}\n'
              f'Status: {self.__status}')


# BaseEntity sınıfından örneklem (instance) aldığımızda, "." notasyonu ile hiçbir attribute erişimedik. 
# Bunun nedeni BaseEntity sınıfının hiç bir üyesini sınıf dışından erişime açık olmamasıydı. 
# Bunu yerine kendilerine default değer atamak için "set_value_private_attribute()" methodunu kullandık.
c1 = BaseEntity()
# c1.__id erişemiyoruz.
c1.set_value_private_attribute()
c1.show_infomation()
print(dir(c1))
# ['_BaseEntity__create_date', '_BaseEntity__created_computer_name', '_BaseEntity__created_ip_address', '_BaseEntity__id', '_BaseEntity__status', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'set_value_private_attribute', 'show_infomation']
# Yukarıda "c1" isimli objenin dir() fonksiyonu ile özelliklerini döktüğümüzde bugüne kadar gördüğümüz yapıların dışında '_BaseEntity__create_date', '_BaseEntity__created_computer_name' ifadelerde geldi. Bunlar protected level'daki sınıfın kendisinin oluşturduğu alanlar. Yani esaden bunları kullanarakta değer atayabilirdi. Bunun yanında "__id" ifadeleri göremedik. Yani onlar private olarak hayatlarına devam ediyorlar.


class Product(BaseEntity):
    def __init__(self, name: str, description: str):
        super().__init__()
        # name ve desctiption object attribute'Leri kullanıcıdan alınacak bilgiler direk olarak içerisine assigned edilecek.
        self.description = description
        self.name = name
        # aşağıdaki __price ve __stock private object attribute'leri default değerler atadık 
        # ve sınıf ilk initialize edilirken gelicek değerleri yuakrıda ki 2 attribute olduğu gibi direk atamadık. 
        # Bu değerlere erişmi BaseEntity sınıfında olduğu gibi dolaylı ve artı olarak bir şart doğrultusunda değer atamsı yapıalcak.
        self.__price = 0
        self.__stock = 0

    # Method overriding öğrenmeye başladığımzıdan beri üst sınıflarda kil method isimleri ile alt sınıflarda ki method isimleri hep aynı idi. Burada ki methodun ismini incelerseniz istisnai bir durum olduğunu göreceksiniz. Diğer yaptığımız örneklerde ki overriding mantığında bizim methodlarımız hiç alt sınıflarda parametre almamaktaydı burada ilk kez alt sınıf içerisinde override edilen methoda paramtre yazdık ve hata aldık. Bu bağlamda methodun adını değiştirerek override olma durumunu ortadan kaldırdır. Method içerisinde üst sınıftan gelene method tetiklendi o kadar.
    # Peki parametre verince bize neden kızdı?
    # Bunu sebebi ata sınıftan gelen methodlar alt sınıflarda kullanılırken bu methodların yapısını değiştiremeyiz. Yani üst sınıftan bize gelen bir method alt sınıf tarafında override edilirken structure yani yapısı bozulamaz. Örneğin üst sınıftan alt sınıfa gelen bir methodun ata sınıfta tanımlanırken 2 parametre aldığını var sayalım alt sınıfta bu methoda iki parametre daha ekleyemeyiz. Yani yapısını bozamayız.
    # Peki aklımıza şu soru gelmiyor mu? Hocam method ve fonksiyonlara sınırsız paramtre gönderemiyor muyduk?
    def set_value_product_private_attribute(self, price: float, stock: int):
        # İlk encapsulation örneğimizde bodoslamadan default değerleri private attribute'lere atadık. Burada biraz daha değişik bir yol izledik. Ne yaptık? Kullanıcıdan gelen değerleri bir şartın sağlaması durumunda private alanlarımıza atamasını yaptık.
        if price >= 0 and stock >= 0:  # atama yapmak için geçilmesi gereken şart
            super(Product, self).set_value_private_attribute()
            self.__stock = stock  # private alanlara değerler şart sağlanırsa atandı.
            self.__price = price
            # Yukarı daki olay kullanıcı eksi bir fiyat yada stok bilgisi girerese işlem yaptırmamak yönündedir.
            self.show_infomation()
        else:
            print('Invalid input...!\nProduct stock and price information was wrong..!')

    def show_infomation(self):
        print(f'Product has been created..!\n'
              f'Details\n'
              f'==============='
              f'Product Name: {self.name}\n'
              f'Description: {self.description}\n'
              f'Price: {self.__price}\n'
              f'Stock: {self.__stock}')
        super().show_infomation()


name = input("Name: ")
description = input("Desctiption: ")
price = int(input("Price: "))
stock = int(input("Stock: "))

p1 = Product(name, description)
p1.set_value_product_private_attribute(price, stock)