
# Döngüler (Loop)
# Tekrarlı olarak işlem yapmızı temin eden bir yapıdır. Örneğin kullanıcıdan 10 tane değer almak istediğimizde bunu döngü ile yapabiliriz. Python'da 2 tip döngü bulunmaktadır. Bunlardan birinci while loop. Bir diğeri ise for loop.
# Döngü mekanizmasında belirli bir şart doğrultusunda sayaç mantığı ile sayıcı azaltmak yada arttırmak suretiyle şart sağandığı sürece çalışan mekanizya döngü diyoruz.

# While loop söz dizimi
# sayac tanımlanır
# while şart belirle
#   işlemler yaptırılır
#   sayac azaıltılır yada artırılır

# region Sample
# sayac = 0
# while sayac < 10:
#     print(sayac)
#     sayac += 1  # sayac = sayac + 1
# endregion


# region Example 1
# 0-100 arasında kaç tane çift ve tek sayı varsa ekrana yazdıralım
# sayac = 0
# tek_sayilar = 0
# cift_sayilar = 0
# while sayac <= 100:
#     if sayac % 2 == 0:
#         cift_sayilar += 1
#     else:
#         tek_sayilar += 1
#     sayac += 1
#
# print(f"Cift Sayı Miktarı: {cift_sayilar}\nTek Sayi Miktarı: {tek_sayilar}")
# endregion


# region Example 2
# 0-100 arasındaki çift ve tek sayıların toplamını ekrana yazdıralım
# sayac = 0
# ciftlerin_toplami = 0
# teklerin_toplami = 0
# while sayac <= 100:
#     if sayac % 2 == 0:
#         ciftlerin_toplami += sayac  # ciftlerin_toplami = ciftlerin_toplami + sayac
#     else:
#         teklerin_toplami += sayac
#     sayac += 1
#
# print(f"Çift sayıların toplamı: {ciftlerin_toplami}\nTek sayıların toplamı: {teklerin_toplami}")
# endregion


# region Example 3
# Kullanıcılar toplamak istediği sayı miktarını alalım ve bu sayıları toplayarak sonucunu ekrana yazdıralım
# sayilarin_toplami = 0
# sayi_adeti = int(input("Kaç tane sayı toplamak istiyorsunuz: "))
# sayac = 0
# while sayac < sayi_adeti:
#     sayi = int(input("Sayı: "))
#     sayilarin_toplami += sayi
#     sayac += 1
#
# print(f"Sayıların Toplamı: {sayilarin_toplami}")
# endregion


# region Continue - Break Keywords
# Break: Bu deyim döngümüzü sonlandırmaya yarar. Bu durumu bir şart doğrultusunda yapmaktadır. Çünkü break değimi çalıştığında döngüyü otomatik olarak sonlandırmaktadır.
# Continue: Bu deyim ise döngümüzü otomatik olarak bir sonra ki adıma geçirmektedir.
# Break ve Continue deyimleri altında kalan kodlar ide (Integrated Developmant Environment) tarafından derlenemezler.
# endregion


# region Example 4
# Kullancıdan bir yıl bigisi alalım. Şayet girilen yıl 1923 ile günümüz yılları arasında ise buldunuz. değilse aradığınız yıl bulunmamaktadır diye feedback veren uygulamayı yapalım.
# from datetime import datetime
# # burada datetime modülü içerisinde bulunan datetime sınıf import ettik.
# start_date = 2022
# search_date = int(input("Aradığınız yılı girin: "))
# condition = False
# while start_date <= datetime.now().year:
#     if search_date > 0:
#         if search_date == start_date:
#             print("Aradığız yıl bulunmaktadır..!")
#             condition = True
#             break
#     else:
#         print("Geçerli bir tarih giriniz..!")
#         condition = True
#         break
#
#     start_date += 1
#
# if not condition:  # condition == False
#     print("Aradığınız yıl bulunmamaktadır..!")
# endregion


# region Example 5
# 1950 ile 1960 yılları arasında ki 1955 ve 1957 yılları haricinde ki yılları ekrana yazdıralım.
# started_year = 1950
# while started_year <= 1960:
#     if started_year == 1955 or started_year == 1957:
#         started_year += 1
#         continue
#     else:
#         print(started_year)
#         started_year += 1
# endregion


# region Example 6
# Kullanıcıdan alınan 2 sayı alalım ve işlem türü alalım. Örneğin '+', '-' vb.
# KUllanıcı klavyeden 'e' tuşana basarsa uygulamayı kapatalım.
# kUllanıcı istediği kadar 4 işlem yapabilsin.
# Kullanıcı klavyeden 'e' tuşu göndermediği sürece yani sonsuza kadar işlem yapabilecek.
# while True:
#     process = input("Please type into a process: ")
#
#     if process == 'e':
#         print("Closing..!")
#         break
#     else:
#         number_1 = int(input("please type into numerical value: "))
#         number_2 = int(input("please type into numerical value: "))
#
#         if process == '+':
#             print(f"Result:  {number_1 + number_2}")
#         elif process == '-':
#             print(f"Result:  {number_1 - number_2}")
#         elif process == '*':
#             print(f"Result:  {number_1 * number_2}")
#         elif process == '/':
#             print(f"Result:  {number_1 / number_2}")
#         else:
#             print("Please choose a valid process upon menu..!")
# endregion


# region Example 7
# Kullanıcıdan alınan sayının faktöriyeli hesaplayan uygulamayı yazınız.
# Örneğin 5 faktöriyel 5*4*3*2*1
# İstisnai durumlar: 0 ve 1 faktöriyeli 1'dir. negatif tam sayıların faktöriyeli hesaplanmaz
# number = int(input("Sayı giriniz: "))
# if number < 0:
#     print("Negatif sayıların faktöriyeli hesaplanmaz..!")
# elif number == 0 or number == 1:
#     print(f"Sonuç: 1")
# else:
#     result = 1
#     while number > 1:
#         result *= number  # result = result * number
#         number -= 1
#     print(f"Sonuç: {result}")
# endregion