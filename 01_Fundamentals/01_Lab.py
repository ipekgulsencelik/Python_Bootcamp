
# ==============================================================
#  Konu: Değişkenler, Veri Tipleri ve Aritmetik İşlemler
# ==============================================================

# Hangi Python sürümünü kullanıyoruz?

# Günümüzde kullanılmakta olan Python programlama dilinin iki popüler sürümü vardır: Python 2 ve Python 3. 
# Python topluluğu Python 2'den Python 3'e geçmeye karar verdi ve 
# birçok popüler kütüphane Python 2'yi artık desteklemeyeceklerini açıkladı.

import sys
print(sys.version)

# Not: sys, kullanılan Python sürümü de dahil olmak üzere sisteme özgü birçok parametre ve işlevi içeren yerleşik bir modüldür. 

# Python'da "Merhaba Dünya" 
# Yeni bir programlama dili öğrenirken, "merhaba dünya" örneği ile başlamak gelenekseldir. 
# Bu kadar basit bir kod satırı, çıktıda bir dizenin nasıl yazdırılacağını ve çıktı alma fokssiyonunu size göstermektedir.

print('Hello, Python!')

# İki Satıra Merhaba Dünya Deyin
# Merhaba ve Dünya'yı iki ayrı satıra yazdıralım. 
# İpucu: Dizenin ortasındaki "\n", yeni bir satır karakteri gibi davranır. 
# Örneğin. yazdırma ("satır 1 \nsatır 2")

print('Hello Python World..!\nThis world is mine..!')

""""
Python'da yorum yazmak

Kod yazmanın yanı sıra, kodunuza yorum eklemenin her zaman iyi bir fikir olduğunu unutmayın. 
Başkalarının neyi başarmaya çalıştığınızı anlamalarına yardımcı olacaktır (verilen bir kod parçasını yazmanızın nedeni). 
Bu sadece diğer kişilerin kodunuzu anlamalarına yardımcı olmakla kalmaz, 
haftalar veya aylar sonra tekrar size geldiğinde size hatırlatma görevi de görür.

Python'da yorum yazmak için, yorumunuzu yazmadan önce "#" sayı sembolünü kullanın. 
Kodunuzu çalıştırdığınızda, Python verilen satırdaki "#" işaretinden sonraki her şeyi yok sayar.
"""

# Python nesne yönelimli bir dildir. 
# Python'da birçok farklı nesne türü vardır. 
# Strings, integers ve floats en yaygın nesne türleridir. 

# Değişken tiplerinin detayları için aşağıdaki documentation inceleyiniz
# https://docs.python.org/3/

# Integer​
11

# Float​
2.14

# String
"Hello, Python 101!"

# Python içerisinde gömülü olarak bulunan "type()" işlevini kullanarak,
# Python'un bir ifade türünü size bildirmesini sağlayabilirsiniz. 
# Python'un tamsayıları int olarak ifade ettiğini, ondalıklı sayıları float olarak 
# ve karakter yahut metin değerlerini str olarak gördüğünü fark edeceksiniz.

# Type of 12​
type(12)

# Type of 2.14​
type(2.14)

# Type of "Hello, Python 101!"​
type("Hello, Python 101!")

#! Bir nesne türünden farklı bir nesne türüne dönüştürme
# Nesnenin türünü Python'da değiştirebilirsiniz; buna typecasting denir. 
# Örneğin, bir tamsayıyı bir float'a dönüştürebilirsiniz (örneğin 2 ila 2.0).

type(2) # Bunun bir tam sayı olduğunu doğrulayın
float(2) # 2 bir float'a dönüştür
type(float(2)) # 2 tamsayısını bir float'a dönüştürün ve türünü kontrol ediniz

# Bir tamsayıyı bir float'a dönüştürdüğümüzde, sayının değerini (yani, anlamını) gerçekten değiştirmeyiz. 
# Fakat bazı bilgileri potansiyel olarak kaybedebiliriz. 
# Örneğin, float 1.1'i tamsayıya çevirirsek 1 alırız ve ondalık bilgiyi kaybederiz (ör. 0.1):

# 1.1'i tamsayıya float'a cast etmek bilgi kaybına neden olur
int(1.1)

# Metinsel ifadeleri tamsayılara veya float'a dönüştürme
# Bazen içinde bir sayı içeren bir dize olabilir. 
# Bu durumda, sayıyı temsil eden değeri "int()" kullanarak bir tamsayıya çevirebiliriz:

# Bir metinsel değeri bir tamsayıya dönüştürme
int('1')

# Sayıların metinsel ifadeye dönüştürülmesi
# Metinsel ifadeleri sayılara dönüştürebilirsek, sayıyıları metinsel ifadelere dönüştürebileceğimizi varsaymak doğaldır, değil mi?

# Bir tamsayıyı dönüştürme
str(1)

# Bir float'ı dönüştürme
str(1.2)

# Boole veri türü
# Boolean, Python'da bir başka önemli türdür. 
# Boolean tipi bir nesne iki değerden birini alabilir: Doğru veya Yanlış:

# Değer doğru
True
# True değerinin büyük bir "T" olduğuna dikkat edin. 
# Aynısı False için de geçerlidir (yani "F" büyük harfini kullanmanız gerekir).

# Değer yanlış
False

# Python'dan bir boolean nesnesinin türünü görüntülemesini istediğinizde, 
# boolean anlamına gelen bool gösterilecektir:

# Gerçek Türü
type(True)   # <class 'bool'>
bool

# Yanlış Tipi
type(False)  # <class 'bool'>

# Boole nesnelerini diğer veri türlerine yayınlayabiliriz. 
# Eğer bir integer or float True değeri olan bir boolean yaparsak bir tane alırız. 
# Eğer bir integer or float bir False değeri olan bir boolean yaparsak, sıfır alırız. 
# Benzer şekilde, eğer Boolean'a 1 atarsak, True olur. Ve eğer bir Boole'ye 0 atarsak, False oluruz.

# İnt'ı int'a çevir
int(True)
1
# 1'i boolean değerine dönüştür
bool(1)

# 0 değerini boolean değerine dönüştür
bool(0)

# Yüzdürmek için Gerçek Dönüştür
float(True)

#! İfade(Expressions)
#Python'daki ifadeler, uyumlu tipler arasındaki işlemleri içerebilir (örneğin, tam sayılar ve değişkenler). 
# Örneğin, birden fazla sayı eklemek gibi temel aritmetik işlemler:

# Toplama İşlemi
43+60+16+41

# Çıkarma İşlemi
50 - 60

# Çarpma
5 * 5

# Bölme
25 / 5
25 / 6


# Python, matematiksel ifadeleri değerlendirirken işlem önceliğini takip eder. 
# Aşağıdaki örnekte Python, çarpımın sonucuna 30 ekler.
30 + 2 * 60 # Output:150

(30 + 2) * 60 # Output:1920, işlem önceliği parantez içindeki işlemde olduğu için sonuç farklı çıktı

#! Değişken (Variable) Nedir?
# Çoğu programlama dilinde olduğu gibi, değerleri değişkenlerde saklayabiliriz, böylece daha sonra kullanabiliriz.

# Değişkenler bizim için geçici olarak üzerlerinde değer tutan yapılardır. 

# Değişkenleri günlük hayatımızda kullandığımız kutulara benzetebiliriz. 
# Nasıl ki kutularda bir şeyler saklıyorsak değişkenler içerisinde biz kullanıcıdan aldığımız yada varsayılan olarak atadığımız değerleri saklıyoruz. 
# Kutuların sahip oldukları şekillere göre içerisinde eşya saklarız, bu husus yazılımda da aynı şekildedir. 
# Yani değişkenlerin tipleri mevcuttur. Tam sayılar için int, sözel ifadeler için string, doğru yanlış (boolean) tip kullanabiliriz.

# Değişkenler RAM (Random Access Memory) üzerinde tutulurlar. 
# Uygulama kapatıldığında bütün değişkenler sıfırlanır. RAM üzerinden silinirler.

# Yazılımda da benzer bir durum vardır:
#   - Tam sayılar için: int
#   - Ondalıklı sayılar için: float
#   - Metinsel ifadeler için: str (string)
#   - Doğru / Yanlış için: bool (boolean)

# Program kapandığında RAM temizlenir ve değişkenler silinir.

#! Variable (Değişken)
#? Değişken tanımlarken dikkat edilecek hususlar
#* 1. Değişken isimleri rakam ile başlamaz
#* 2. Boşluk karakteri içermez, boşluk yerine "_" sembolü kullanılır
#* 3. Türkçe karakter kullanmamaya özen gösterelim.

#todo: Not --> Yukarıdaki satırlar yorum satırıdır (Comment Line). Interpeter tarafından yorumlanmazlar yani çalıştırılmazlar.
#! Not: IDE'ler kodları yukardan aşağıya doğru satır satır çalıştırırlar.

# user_name = 'beast'
# print(user_name)
# print(type(user_name))    # <class 'str'>

#! Not: Python’da değişkenler içerisine attığımız değerin tipine sahip olurlar.
#todo: Yukarıdaki user_name değişkeninin tipi string'tir.

# user_name = 100
# print(user_name)
# print(type(user_name))    # <class 'int'>

# x = 10        #* x değişkenin tipi integer'dır
# y = 3.14      #? y değişkeninin tipi float'tır
# is_active = True   #* True yada False değer alan değişkenler boolean yada bool olarak isimlendirilir.

# print(x, type(x))
# print(y, type(y))
# print(is_active, type(is_active))


#! Değişken Tanımlama
# C ailesine ait programlama dilelrinde, java, php gibi programlama dillerinde değişken tanımlarken 
# ilk önce değişkenin tip sonra değişken adı gelmektedir
# int number;
# Yukarıdaki değişken tanımlamasında bir değişken uygulama ilk çalıştığında bir tip ile RAM'de yaşamaya başlar. 
# Buna tip bağımlılığı diye biliriz.
# Python programlama dilinde ise bir değişken içerisine değer atandığında atanılan değerin tipi, değişkenin tipi olarak atanır. 
# Yani fen derslerinde öğrendiğimiz gibi sıvılar nasıl bulundukları kabın şeklini alırlarsa 
# pythonda değişken içerisine gönderdiğimiz değerin tipini alırlar.
# number = 12
# print(number)  # print() python içerisinde hiyerarşik (built-in) olarak bulunan bir fonksiyondur. Görevi ise içerisine verilen değeri consol ekranına yazdırmaktır.
# number = "beast"
# print(number)

# variableType = type(number)  # burada type() fonksiyonu bize bir değişkenin ne tipte olduğunu gösterir. 
# Type() fonksiyonun sonucunda bize gelen değeri "variableType" isimli değişkene assigned ettik.
# print(variableType)
# print("number değişkeninin tipi:", variableType)


#! ARİTMATİKSEL İŞLEMLER

x = 43 + 60 + 16 + 41 # Değeri değişkene sakla, toplama işleminin sonucunu "x" değişkenine atadık(assignment).
print(x) # toplama işleminin sonucunu ekrana bastık
y = x / 60 # toplama işleminin sonucunu 60 bölerek elde edilen sonucu "y" değişkenine atadık
print(y) 

# Python'da yeni değer önceden yaratılmış değişkenin üzerine yazılabilir
x = x / 60
print(x)

toplam = 43 + 42 + 57
print(toplam)
type(toplam) # yarattığımız "toplam"  değişkeninin tipine bakalım

toplam_saat = (43 + 42 + 57) / 60
print(toplam_saat)


""" 
number_1 = 2
number_2 = 4

result = number_1 + number_2

print(result)
"""


""" 
# Dikkat: input() fonksiyonuyla alınan her değer string (metin) tipindedir.
number_1 = input("Type a number: ")
number_2 = input("Type a number: ")

result = number_1 + number_2
# Burada toplama işlemi matematiksel değildir!
# İki string yan yana eklenir (concatenation). Örneğin:
# number_1 = "5"
# number_2 = "7"
# result = "57" olur, 12 olmaz.

print(result) 
"""


""" 
full_name = 'burak' + ' yılmaz'  # iki string yan yana eklenir
print(full_name) 
"""

# Kullanıcıdan alınan 2 adet sayı üzerinden temel 4 işlem yapan uygulamayı yazınız.
# number_1 = int(input("Lütfen bir sayı giriniz: ")) #* int() ile string → sayıya dönüştürülür
# number_2 = int(input('Lütfen bir sayı giriniz: '))
# Not: input() fonksiyonuyla kullanıcıdan değer aldığımızda aldığımız değeri tipi her zaman string'tir. 
# Biz burada aritmatiksel bir işlem yapmak istediğimzden ötürü kullanıcıdan gelen değerleri sayısal bir tipe dönüştürmemiz gerekmektedir. 
# Bu bağlamda python içerisinde built-in olarak bulunan int() fonksiyonunu kullanacağız. 
# int() fonksiyonu içerisine verilen değeri int tipine dönüştürmektedir.
# toplam = number_1 + number_2


""" 
number_1 = int(input("Type a number: "))
number_2 = int(input("Type a number: "))

result = number_1 - number_2

print(result)
 """

# Aşağıda ki 3 satır kod aynı çıktıyı verir.
# print("Toplam:", toplam)  # burada string ifade ile toplam değişkenimizi birbirine bağladık.
# print(f"Toplam: {toplam}")  # "f" özel bir karakterdir ve {} parantezleri ile birlikte kullanılır. 
# Bu kullanım şekli string bir ifade içerisinde süslü parantez ile kendimize yaşam alanı açarak değişkenimizi string ifade içerisinde yazma olanağı tanır.
# print("Toplam: {}".format(toplam))  # burada kullanılan format() fonksiyonu ile süslü parantez içerisinde değişken göndererek sting ifade ile ilgili değişkenin birleştirilmesi temin edilir.

# Kullanıcıdan alınan kenar bilgisine göre karenin alanını ve çevresini hesaplayan uygulamayı yazınız
# edge = float(input("Please type edge information: "))

# area = edge * edge
# zone = 4 * edge

# print(f"Area: {area} - Zone: {zone}")


# Kullanıcıdan alınan kısa ve uzun kenar bilgisine göre dikdörtgenin alanını ve çevresini hesaplayınız.
# kisa_kaner = int(input("Kısa Kenar: "))
# uzun_kaner = int(input("Uzun Kenar: "))

# cevre = 2 * (kisa_kaner + uzun_kaner)
# alan = kisa_kaner * uzun_kaner

# print(f"Cevre: {cevre}\nAlan: {alan}")
# print(f'Alan: {kisa_kenar * uzun_kenar} - Çevre: {2 * (kısa_kenar + uzun_kenar)}')

# Taban ve yükseklik değeri kullanıcıdan alınan üçgenin alanını hespalayın
# taban = float(input("Taban: "))
# yukselik = float(input("Yukseklik: "))

# alan = taban * yukselik / 2

# print(f"Alan: {alan}")

# Dairenin alanını ve çevresini hesaplayan uygulamayı yazınız
# Dairenin alanı => pi * r ** 2
# Dairenin çevresi => 2 * pi * r
import math  # math python içerisinde bulunan bir kütüphanedir. bize hazır fonksiyonlar yani formüller vb matematiksel ifadeleri temin eder.
r = float(input("Yarı çap: "))

alan = math.pi * r ** 2
cevre = 2 * math.pi * r

# :.2f → virgülden sonra 2 basamak göster
print(f"Cevre: {cevre:.2f}\nAlan: {alan:.2f}")