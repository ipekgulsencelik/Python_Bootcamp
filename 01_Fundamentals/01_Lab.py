# ==============================================================
#  Konu: Değişkenler, Veri Tipleri ve Aritmetik İşlemler
# ==============================================================

# Değişken (Variable) Nedir?
# Değişkenler bizim için geçici olarak üzerlerinde değer tutan yapılardır. Değişkenleri günlük hayatımızda kullandığımız kutulara benzetebiliriz. Nasıl ki kutularda bir şeyler saklıyorsak değişkenler içerisinde biz kullanıcıdan aldığımız yada varsayılan olarak atadığımız değerleri saklıyoruz. Kutuların sahip oldukları şekillere göre içerisinde eşya saklarız, bu husus yazılımda da aynı şekildedir. Yani değişkenlerin tipleri mevcuttur. Tam sayılar için int, sözel ifadeler için string, doğru yanlış (boolean) tip kullanabiliriz.
# Değişkenler RAM (Random Access Memory) üzerinde tutulurlar. Uygulama kapatıldığında bütün değişkenler sıfırlanır. RAM üzerinden silinirler.

#! Variable (Değişken)
#? Değişken tanımlarken dikkat edilecek hususlar
#* 1. Değişken isimleri rakam ile başlamaz
#* 2. Boşluk karakteri içermez, boşluk yerine "_" sembolü kullanılır
#* 3. Türkçe karakter kullanmayalım.

#todo: Not --> Yukarıdaki satırlar yorum satırıdır (Comment Line). Interpeter tarafından yorumlanmazlar yani çalıştırılmazlar.
#! Not: IDE'ler kodları yukardan aşağıya doğru satır satır çalıştırırlar.

# user_name = 'beast'
# print(user_name)
# print(type(user_name))

#! Not: Python’da değişkenler içerisine attığımız değerin tipine sahip olurlar.
#todo: Yukarıdaki user_name değişkeninin tipi string'tir.

# user_name = 100
# print(user_name)
# print(type(user_name))

x = 10        #* x değişkenin tipi integer'dır
y = 3.14      #? y değişkeninin tipi float'tır
is_active = True   #* True yada False değer alan değişkenler boolean yada bool olarak isimlendirilir.

# Değişken Tanımlama
# C ailesine ait programlama dilelrinde, java, php gibi programlama dillerinde değişken tanımlarken ilk önce değişkenin tip sonra değişken adı gelmektedir
# int number;
# Yukarıdaki değişken tanımlamasında bir değişken uygulama ilk çalıştığında bir tip ile RAM'de yaşamaya başlar. Buna tip bağımlılığı diye biliriz.
# Python programlama dilinde ise bir değişken içerisine değer atandığında atanılan değerin tipi, değişkenin tipi olarak atanır. Yani fen derslerinde öğrendiğimiz gibi sıvılar nasıl bulundukları kabın şeklini alırlarsa pythonda değişken içerisine gönderdiğimiz değerin tipini alırlar.
# number = 12
# print(number)  # print() python içerisinde hiyerarşik (built-in) olarak bulunan bir fonksiyondur. Görevi ise içerisine verilen değeri consol ekranına yazdırmaktır.
# number = "beast"
# print(number)
#
# variableType = type(number)  # burada type() fonksiyonu bize bir değişkenin ne tipte olduğunu gösterir. Type() fonksiyonun sonucunda bize gelen değeri "variableType" isimli değişkene assigned ettik.
# print(variableType)
#
#! ARİTMATİKSEL İŞLEMLER

number_1 = 2
number_2 = 4

result = number_1 + number_2

print(result)

number_1 = input("Type a number: ")
number_2 = input("Type a number: ")

result = number_1 + number_2

print(result)

full_name = 'burak' + ' yılmaz'
print(full_name)

# # Kullanıcıdan alınan 2 adet sayı üzerinden temel 4 işlem yapan uygulamayı yazınız.
# number_1 = int(input("Lütfen bir sayı giriniz: "))
# number_2 = int(input('Lütfen bir sayı giriniz: '))
# # Not: input() fonksiyonuyla kullanıcıdan değer aldığımızda aldığımız değeri tipi her zaman string'tir. Biz burada aritmatiksel bir işlem yapmak istediğimzden ötürü kullanıcıdan gelen değerleri sayısal bir tipe dönüştürmemiz gerekmektedir. Bu bağlamda python içerisinde built-in olarak bulunan int() fonksiyonunu kullanacağız. int() fonksiyonu içerisine verilen değeri int tipine dönüştürmektedir.
# toplam = number_1 + number_2

number_1 = int(input("Type a number: "))
number_2 = int(input("Type a number: "))

result = number_1 - number_2

print(result)

# Aşağıda ki 3 satır kod aynı çıktıyı verir.
# print("Toplam:", toplam)  # burada string ifade ile toplam değişkenimizi birbirine bağladık.
# print(f"Toplam: {toplam}")  # "f" özel bir karakterdir ve {} parantezleri ile birlikte kullanılır. Bu kullanım şekli string bir ifade içerisinde süslü parantez ile kendimize yaşam alanı açarak değişkenimizi string ifade içerisinde yazma olanağı tanır.
# print("Toplam: {}".format(toplam))  # burada kullanılan format() fonksiyonu ile süslü parantez içerisinde değişken göndererek sting ifade ile ilgili değişkenin birleştirilmesi temin edilir.

# Kullanıcıdan alınan kenar bilgisine göre karenin alanını ve çevresini hesaplayan uygulamayı yazınız
# edge = float(input("Please type edge information: "))
#
# area = edge * edge
# zone = 4 * edge
#
# print(f"Area: {area} - Zone: {zone}")

# Kullanıcıdan alınan kısa ve uzun kenar bilgisine göre dikdörtgenin alanını ve çevresini hesaplayınız.
# kisa_kaner = int(input("Kısa Kenar: "))
# uzun_kaner = int(input("Uzun Kenar: "))
#
# cevre = 2 * (kisa_kaner + uzun_kaner)
# alan = kisa_kaner * uzun_kaner
#
# print(f"Cevre: {cevre}\nAlan: {alan}")
# print(f'Alan: {kısa_kenar * uzun_kenar} - Çevre: {2 * (kısa_kenar + uzun_kenar)}')

# Taban ve yükseklik değeri kullanıcıdan alınan üçgenin alanını hespalayın
# taban = float(input("Taban: "))
# yukselik = float(input("Yukseklik: "))
#
# alan = taban * yukselik / 2
#
# print(f"Alan: {alan}")

# Dairenin alanını ve çevresini hesaplayan uygulamayı yazınız
# Dairenin alanı => pi * r ** 2
# Dairenin çevresi => 2 * pi * r
import math  # math python içerisinde bulunan bir kütüphanedir. bize hazır fonksiyonlar yani formüller vb matematiksel ifadeleri temin eder.
r = float(input("Yarı çap: "))

alan = math.pi * r ** 2
cevre = 2 * math.pi * r

print(f"Cevre: {cevre:.2f}\nAlan: {alan:.2f}")
