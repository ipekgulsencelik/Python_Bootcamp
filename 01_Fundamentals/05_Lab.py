# List
# Uygulama içerisinde anlık olarak bizim için değer tutan yapılarıdr. Birden fazla tipte değerleri içerisinde barındırabilirler. List'ler RAM üzerinde tutulduğu için uygulama çalıştığı sürece üzerine eklenilen yeni değerleri tutatlar. Uygulama kapatıldığında ise ilk yaratıldıkları hale dönerler. örneğin futbol takımlarının tuutlduğu bir listem olsun.
# futbol_takimlari = ['Galatasaray', 'Beşiktaş']
# Bu liste içerisine uygulama run time'da iken 2 yeni takım daha eklenilsin
# futbol_takimlari.append('Fenerbahçe')
# futbol_takimlari.append('Trabzonspor')
# Uygulama run time iken artık listemiz 4 elemanlıdır. Lakin uygulama kapatıldığında listemiz ilk haline yani 2 elemanlı haline döner.

# Listeler index mantığı ile çalışmaktadır. Yani bir liste içeriisnde ki birinci elemen sıfırıncı index'te tutulur.
# Örneğin:
# print(futbol_takimlari[1])
# Kodunu çalıştırırsak ekrana "Beşiktaş" yazdırılır. Bu mantıktan yola çıkarsak şunu diyebiliriz. Listeler sıfırncı index'ten başlayarak elemanlarını index'ler ve bu işlemi artı yönde bir bir arttırarak yaparlar.

# Python içerisinde built-in olarak bulunan listelere uygulanılan built-in fonksiyonlar bulunumaktadır. BUnlardan bazıları, insert(), remove() örnek olarak verilebilinir.
# print(futbol_takimlari)
#
#
# top_boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfiled', 'Rocky Marciano']
# append() => fonksiyonu ile listemizin sonuna yeni bir eleman ekleriz.
# top_boxers.append('George Forman')
# print(top_boxers)

# insert() => bu fonksiyon listenin her hangi bir index değerine eleman ekleme işlemini yerine getirir. İlk parametreye index değerini ikinci parametreye ise eklenecek değeri.
# favorite_boxer = input("Enter your favorite boxer: ")
# top_boxers.insert(3, favorite_boxer)
# print(top_boxers)

# clear() => fonksiyonu listenin alayını temizler.

# remove() => listeden silinecek item'ın yani değerin kendisini veriyoruz ve liseden onu silmektedir
# top_boxers.remove('Evander Holyfiled')
# print(top_boxers)

# pop() => verilen index değerinde ki elemanı siler
# top_boxers.pop(4)
# print(top_boxers)

# extend() => iki farklı listeyi birleştirmeye yarayan fonksiyondur.
# current_boxers = ['Tyson Fury', 'Deantony Wilder', 'Antony Jasua']
# top_boxers.extend(current_boxers)
# print(top_boxers)
#
#
# movie_list = ['Fight Club', 'Matrix', 'Interstaller', 'Inception', 'Fringe']
#
# for movie in movie_list:
#     print(movie)


# lenght_movie_list = len(movie_list)
# for i in range(lenght_movie_list):
#     print(movie_list[i])


# region Example - 1
# Bir liste içerisinde kullanıcının belirlediği kadar random sayı ile dolduralım
# Üretilecek sayıların aralık bilgisini kullanıcıdan alalım.
# Bu üretilen sayılardan kaç tanesi çift kaç tanesi tek bulup ekrana yazdıralım.
# from random import randint
#
# sayi_listesi = []
# cift_sayilar = 0
# tek_sayilar = 0
# uretilecek_sayi_miktari = int(input('Kaç tane sayı üretilsin: '))
# baslangic_araligi = int(input("Üretilecek sayılar kaçtan başlasın: "))
# bitis_araligi = int(input("Üretilecek sayılar kaçta bitsin: "))
# for i in range(uretilecek_sayi_miktari):
#     uretilen_sayi = randint(baslangic_araligi, bitis_araligi)
#     if uretilen_sayi not in sayi_listesi:
#         sayi_listesi.append(uretilen_sayi)
#     else:
#         i -= 1
#     print(f'{i+1}. adımda üretilen sayı: {uretilen_sayi}')
#
# for item in sayi_listesi:
#     if item % 2 == 0:
#         cift_sayilar += 1
#     else:
#         tek_sayilar += 1
#
# print(f'Üretilen çift sayı miktarı: {cift_sayilar}\nÜretilen tek sayı miktarı: {tek_sayilar}')
# endregion


# region Example - 2
# 2 farklı liste içerisine random olarak 10 adet sayı ile dolduralım.
# Sayılar 0 ile 100 arasında üretilsin.
# Listenin karşılıklı gelen index'lerinde tutulan değerleri toplayarak 3. bir listeye ekleyelim.
# Listeler içerisinde index mantığı ile dolaşarak bu soruyu çözelim.
# from random import randint
# lst_1 = []
# lst_2 = []
# lst_3 = []
# for i in range(10):
#     lst_1.insert(i, randint(0, 100))
#     lst_2.insert(i, randint(0, 100))
#
#     lst_3.insert(i, lst_1[i] + lst_2[i])
#
#     print(f'{lst_1[i]} + {lst_2[i]} = {lst_1[i] + lst_2[i]}')
#
# print(lst_3)
# endregion


# region Example - 4
# Kullancıdan alınan söz öbeğini harf harf bir liste içerisne kayıt edin.
# Boşluk karakterinin listeye eklenmesini istemiyoruz.
# word = input("Say something .... : ")
# characters = []
# for char in word:
#     if char == ' ':
#         continue
#     else:
#         characters.append(char)
#
# print(characters)
# endregion


# region Example - 4
# Kullancıdan alınan söz öbeğinde ki sesli harfleri bir listeye dolduralım
# sesli_harfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
# yakalanan_sesli_harfler = []
# yakalanan_sayilar = []
# cumle = input("Lütfen bir cümle yazın: ")
# for karakter in cumle:
#     if karakter in sesli_harfler:
#         yakalanan_sesli_harfler.append(karakter)
#     elif karakter == ' ':
#         continue
#     elif karakter.isdigit():  # isdigit() fonksiyonu ilgili karakterin sayı olup olmadığına bakar. sayı ise true değilse false döndürür.
#         yakalanan_sayilar.append(karakter)
#
# print(yakalanan_sesli_harfler)
# print(yakalanan_sayilar)
# endregion


# region Example - 5
# Kullanıcıdan full adı alınacak. Örneğin Burak Yılmaz
# 3 ve üzeri tam ad olma durumunu göz önünde bulundurun. BU senaryoda ilk isim ve soy isim kullanılsın.
# burak.yilmaz@bilgeadam.com
# endregion
# full_name = input("Please type into full name: ").lower()
# splited_full_name_list = full_name.split(" ")
# mail_address = f'{splited_full_name_list[0]}.{splited_full_name_list[-1]}@bilgeadam.com'
# print(mail_address)

# region Example - 6
# Sign in olurken kullanıcının şifresini kontrol edelim.
# Şifre en az 16 karakterli olacak.
# Noktalama işareti ieçrecek. Python'da hazır yapısı var.
# En az bir tane büyük harf
# En az bir küçük harf
# en az bir rakarm içeriyorsa
# şifre uygundur. her hangi birini içermiyorsa uygun değildir.
from string import punctuation
# password = input("Please type your password: ") .Bu1ffffffffffffffffffffffffffffffffffffffffffff
# isDigit = False
# isUpper = False
# for char in password:
#     if len(password) >= 16:
#         pass
#     if char in punctuation:
#         pass
#     if char.islower():
#         pass
#     if char.isupper():
#         pass
#     if char.isdigit():
#         pass
#
#     if isDigit = True or isUpper = False
# # endregion

print(punctuation)

qwe = input("Type: ")

for i in qwe:
    print(type(i))