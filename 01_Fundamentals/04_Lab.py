
#! For Loop
# Python içerisinde built-in olarak bulunan bir döngü türüdür. While loop yerine sıklıkla tercih ediliri. Bunun nedeni for loop ile birlikte kullanılan operatörlerdir. Bu operatörler "in" ve "range()" operatörleridir.

#! In - Not In
# In operatörü bir liste içerisinde bir eleman varsa "True" yoksa "False" döner.
# Not In ise "in" mantığın tam tersi çalışır. Yani bir liste içerisinde aradığımız eleman varsa "False" yoksa "True" döner.

#! in operatörü
# print('b' in 'burak')
# print('z' in 'burak')

# Python'da listeler "[]" parantez ile tanımlanırlar. Ayrıca "," sembolü listenin her bir elemanını bir birinden ayırır.
# number_list = [1, 2, 3, 4]

# print(3 in number_list)  # burada in bize True döner çünkü 3 sayısı number_list isimli listede bulunmaktadır.
# print(6 in number_list)  # False döner.

#! not in operatörü
# print('b' not in 'burak')
# print('z' not in 'burak')

# print(3 not in number_list)
# print(6 not in number_list)

# string ifadeler birer karakter listesidir. O zaman "Mike Tyson" ifadesine in ve not in operatörlerini uygulayabilir.
# user_name = "Mike Tyson"
# print('i' in user_name)
# print('a' in user_name)

#! range()
# Bu fonksiyon python içerisinde hiyerarşik olarak bulunmaktadır. Bu fonksiyon içerisine 3 tane değer almaktadır. Bu aldığı değerlere yazılımcılar "parametre" olarak isimlendirirler. Aldığı bu 3 parametre sırasıyla başlangıç, bitiş ve adım değerlerini temsil eder. Buradan şu sonuca varabiliriz. Range fonksiyonu bir başlangıç ve bitiş değeri arasındaki değerleri adım adım dolaşmamızı temin etmektedi. Örneğin başlangıç değerini 0, bitiş değerini 100 ve adım miktarınıda 1 verirsem. Sıfırdan başlayarak her bir tam sayıyı adım adım uğrayarak bana teslim eder ve 100 olduğunda durur. Bu durumda for loop ile rahat rahat bu sekans içerisinde dolaşabilirim.
# for i in range(0, 101, 10):
#     print(i)

# for i in range(10, 20, 2):
#     print(i)

# Fonksiyonlar aldıkları parametrelerle farklı şekiller de kullanılabilinirler. Örnğin range() fonksiyonu 2 paremetre alırsa, alınan birinci parametre başlangıç, ikinci parametre ise bitiş değerini temsil eder. Adım miktarıda default olarak 1 olur.
# for i in range(0, 11):
#     print(i)

# for i in range(5, 11):
#     print(i)

# range() tek parametre alırsa başlangıç değerini sıfır, bitiş değerini aldığı parametre, artış miktarını da varsayılan olarak 1 atar
# for i in range(11):
#     print(i)

# region Example 1
#! Kullanıcıdan başlangıç, bitiş ve artış miktarlarını alalım.
#? kullanıcı belirlediği bu şartlara göre oluşan sayıları ekrana yazdıralım
#
# baslangic = int(input('Başlangıç: '))
# bitis = int(input('Bitiş: '))
# adim = int(input('Adım: '))
#
# for i in range(baslangic, bitis, adim):
#     print(i, end='-')
# endregion


# region Example 2
# 0-101 arasındaki çif ve tek sayıları ayrı ayrı toplayalım
# ciftlerin_toplami = 0
# teklerin_toplami = 0
#
# for i in range(101):
#     if i % 2 == 0:
#         ciftlerin_toplami += i
#     else:
#         teklerin_toplami += i
#
# print(f"Çift Sayıların Toplamı: {ciftlerin_toplami}\nTek Sayıların Toplamı: {teklerin_toplami}")
# endregion


# region Exampe 3
# Kullanıcıdan başlangıç, bitiş ve adım miktarılarını alalım. Girdiği değerler aralığında kaç tane çift kaç tane tek sayı var bulalım.
# cift_sayi = 0
# tek_sayi = 0
# baslingic = int(input("Başlangıç değeri: "))
# bitis = int(input("Bitiş değeri: "))
# adim = int(input("Adım değeri: "))
#
# for i in range(baslingic, bitis + 1, adim):
#     if i % 2 == 0:
#         cift_sayi += 1
#     else:
#         tek_sayi += 1
#
# print(f'Girilen aralıkta ki çift sayı miktarı: {cift_sayi}')
# print(f'Girilen aralıkta ki tek sayı miktarı: {tek_sayi}')
# endregion


# region Example 4
# Kullanıcıdan alınan sayı asal mı değil mi?
# Yol - 1
# sayi = int(input("Sayı giriniz: "))
# if sayi <= 0:
#     print("Sıfır ve negatif sayılar asal değildir...!")
# else:
#     is_prime = True
#     if sayi == 1:
#         is_prime = False
#
#     for i in range(2, sayi):
#         if sayi % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print("Sayı asaldır.")
#     else:
#         print("Sayı asal değildir")
#
# Yol - 2
# sayi = int(input("Sayı girin: "))
# if sayi <= 1:
#     print("Bir, sıfır ve negatif sayılar asal değildir...!")
# else:
#     for i in range(2, sayi):
#         if sayi % i == 0:
#             print(f"{sayi}, {i} sayısına tam bölündü. Bu yüzden asal değil")
#             break
#     else:
#         print("asal")
# endregion


# region Example 5
# 0 - 100 arasında ki sayıları 10'nar 10'nar toplatalım.  her bir adımda ki toplamı kullanıcıya gösterelim.
# Örnek çıktı: 1. adımda toplam: 10
# sayac = 1
# toplam = 0
# for i in range(0, 101, 10):
#     toplam += i
#     print(f"{sayac}. adımda toplam ==> {toplam}")
#     sayac += 1
# endregion


# region Example 6
# Nested for kullanarak çarpım tablosu yapınız.
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
#     print("============")
# endregion


# region Example 7
# "*" sembollerini kullanara kare sembolü yapınız
# for i in range(0, 4):
#     for j in range(0, 4):
#         print("*", end="")
#     print(" ")
# endregion


# region Example 8
# "*" sembollerini kullanar dik üçgen yapalım
# for i in range(0, 6):
#     for j in range(0, 6):
#         if j <= i:
#             print("*", end="")
#     print("")
# endregion


# from random import randint

# region Example 9
#! 10 tane rastgele sayı üretip ekrana yazdırın
# for i in range(1, 11):
#     random_number = randint(a=0, b=100)
#     print(f'{i}. üretilen sayı --> {random_number}')
# endregion


# region Example 10
#! kullanıcı rastgele üretilen sayıyı tahmin etsin. 3 kez deneme şansı olsun.
# generated_number = randint(a=0, b=100)
# print(generated_number)
#
# hak = 2
# while hak >= 0:
#     x = int(input('Tahmin Gir: '))
#     if generated_number == x:
#         print('Tebrikler kazandınız..!')
#         break
#     else:
#         print(f'Bilemediniz..!\nKalan hakkınız: {hak}')
#     hak -= 1
# endregion