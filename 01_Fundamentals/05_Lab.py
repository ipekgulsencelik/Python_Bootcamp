
#! List
# Uygulama içerisinde anlık olarak bizim için değer tutan yapılardır. 
# List'ler RAM üzerinde tutulduğu için, uygulama çalıştığı sürece üzerine eklenen yeni değerleri tutarlar. 
# Birden fazla tipte değerleri içerisinde barındırabilirler. 
# Uygulama kapatıldığında ise ilk yaratıldıkları hale dönerler. 

# lst = ['burak', 12, True, 'hakan', 3.14, False]

# 0. indeks -> listenin ilk elemanı
# print(lst[0])     # Çıktı: 'burak'

# 3. indeks -> 4. eleman
# print(lst[3])     # Çıktı: 'hakan'

# -1. indeks -> listenin son elemanı (ters indeksleme)
# print(lst[-1])    # Çıktı: False

# Listeler verileri kalıcı olarak depolamazlar. 
# RAM'de depolanırlar. Uygulama kapatıldığında RAM'de temizlik olur.
# Listelerin referansları RAM'in heap alanında saklanır.

# region Sample
# futbol_takimlari = ['Galatasaray', 'Beşiktaş']
# Bu liste içerisine uygulama run time'da iken 2 yeni takım daha eklenilsin
# futbol_takimlari.append('Fenerbahçe')
# futbol_takimlari.append('Trabzonspor')

# Uygulama run time iken artık listemiz 4 elemanlıdır. 
# Lakin uygulama kapatıldığında listemiz ilk haline yani 2 elemanlı haline döner.

# Listeler index mantığı ile çalışmaktadır. 
# Yani bir liste içerisindeki birinci eleman sıfırıncı index'te tutulur.
# Örneğin:
# print(futbol_takimlari[1])
# Kodunu çalıştırırsak ekrana "Beşiktaş" yazdırılır. 

# Listeler sıfırıncı index'ten başlayarak elemanlarını index'ler ve artı yönde bir bir arttırır.

# print(futbol_takimlari)
# endregion

# Aşağıdaki iki örnekte bir liste içerisindeki index mantığı gösterilmektedir. 
# Listelerdeki index mantığı sıfırdan başlar ve pozitif yönde vektörel olarak artarak devam eder.
# sayilar = [2, 2132, 45, 98]
# print(sayilar[1])  # sayilar listesinin 1. index'sinde tutulan değeri teslim eder.

# kelime = "burak yılmaz"
# print(kelime[6])  # kelime ifadesinin 6. index'sinde bulunan değeri teslim eder.

# boxers = ['Mike Tyson', 'Muhammed Ali', 'Lennox Lewis', 'Evander Holyfield', 'George Foreman']
# print(type(boxers))
# print(boxers)

# Python içerisinde built-in olarak bulunan listelere uygulanabilen built-in fonksiyonlar bulunmaktadır.
# Bunlardan bazıları insert(), remove() gibi fonksiyonlardır.

# region Add New Item
# append() -> Listenin SONUNA yeni bir eleman ekler.
# boxers.append('Rocky Marciano')
# print(boxers)
# endregion


# region Example 1
# sayilar = []  # burada içi boş bir liste tanımladık
# for i in range(1, 10):
#     sayilar.append(i)  # append() fonksiyonu ilgili listeye her bir adımda i sayacının üzerinde tutuğu değeri eklemeye yaradı.
# print(sayilar)
#
# print([x for x in range(1, 10)])
# endregion


# region Example 2
# rakamların karesini hesaplayarak bir listeye dolduralım
# rakamlar = []
# for i in range(1, 10):
#     rakamlar.append(i ** 2)
# print(rakamlar)
#
# print([i * i for i in range(1, 10)])
# endregion


# region Example 3
# 50 - 100 arasında 3'e tam bölünen sayıların karesini alarak bir listeye ekleyelim
# sayilar = []
# for i in range(50, 101):
#     if i % 3 == 0:
#         sayilar.append(i ** 2)
# print(sayilar)

# print([i ** 2 for i in range(50, 101) if i % 3 == 0])
# endregion


# region Insert New Item Specific Index
# insert() => listenin herhangi bir index değerine eleman ekleme işlemini yerine getirir. 
# İlk parametreye index değerini ikinci parametreye ise eklenecek değeri.
# favorite_boxer = input("Enter your favorite boxer: ")
# boxers.insert(3, favorite_boxer)
# print(boxers)
# endregion


# region Add New Item Specific Index
# Kullanıcıdan yeni bir boksör ismi alıyoruz
# boxer_name = input('Boxer Name: ')

# Kullanıcıdan elemanın hangi index'e eklenmesini istediğini alıyoruz
# index_value = int(input('Index Value: '))

# insert() -> Belirtilen index'e yeni eleman ekler.
# Mevcut elemanları sağa kaydırır, listeyi bozmadan araya yerleştirir.
# boxers.insert(index_value, boxer_name)
# print(boxers)
# endregion


# region Merge Two Lists
# extend() => iki farklı listeyi birleştirmeye yarayan fonksiyondur.
# royal_division = ['Anthony Joshua', 'Tyson Fury', 'Deontay Wilder']

# extend() -> Bir listenin elemanlarını diğer listenin SONUNA ekler.
# Yani royal_division içindeki her eleman teker teker boxers listesine dahil edilir.
# boxers.extend(royal_division)
# print(boxers)
# endregion


# region Read An Item
# Boxers listesinin 2. indexinde bulunan veriyi ekrana basıyoruz
# Dikkat: Index 0'dan başlar, yani 2. index listedeki 3. elemandır.
# print(boxers[2])
# endregion


# region Update Item
# 5. index'te bulunan elemanı "Joe Frazeir" ile değiştiriyoruz
# Liste üzerinde doğrudan atama (assignment) yaparak güncelleme yapılır.
# boxers[5] = 'Joe Frazier'
# print(boxers)
# endregion


# region Remove Item By Index - 1
# pop(index) → Belirtilen index'teki elemanı siler.
# 0. index elemanını silelim
# boxers.pop(0)
# print(boxers)
# endregion


# region Remove Item by Index - 2
# pop(index) → Verilen index'teki elemanı siler.
# Eğer index verilmezse listenin son elemanını siler.
# Örnek: 4. index'teki elemanı silme
# boxers.pop(4)
# print(boxers) 
# endregion


# region Remove Item by Value
# remove() → Listeden silinecek ELEMANIN DEĞERİNİ veririz.
# İlk eşleşen elemanı bulup siler.
# Eğer listede yoksa hata verir.
# Örnek: 'Evander Holyfield' değerini listeden silme
# boxers.remove('Evander Holyfield')
# print(boxers)  
# endregion


# region Remove Item By Itself
# remove(value) → Değerin kendisini vererek silme işlemi yapılır.
# 'Lennox Lewis' değerini listeden silelim
# boxers.remove('Lennox Lewis')
# print(boxers)
# endregion


# clear() => fonksiyonu listenin alayını temizler.


# region Loop Over List (for each)
# Listedeki her elemanı tek tek gezer ve yazdırır
# for boxer in boxers:
#     print(boxer)
# endregion


# region Loop Over List (for each) - Example 
# movie_list = ['Fight Club', 'Matrix', 'Interstellar', 'Inception', 'Fringe']
#
# for movie in movie_list:
#     print(movie)
# endregion


# region Loop with Index (range + len)
# len() → Bir listenin, stringin veya koleksiyonun ELEMAN SAYISINI verir.
# Örn: len([10, 20, 30])  → 3
# Örn: len("burak")       → 5
#
# range() → Bir sayı aralığı üretir (0'dan başlar).
# range(5)  → 0,1,2,3,4 üretir (5 dahil değil)
# range(len(boxers)) → index üzerinden listeyi dolaşmamızı sağlar.
#
# for i in range(len(boxers)):
#     print(f'{i}. indexteki değer --> {boxers[i]}')
# endregion


# region Loop with Index (range + len) - Example
# length_movie_list = len(movie_list)
# for i in range(length_movie_list):
#     print(movie_list[i])
# endregion


# region Loop Over String Characters
# Bir string aslında karakterlerden oluşan bir listedir
# Her karakter tek tek yazdırılır
# for ch in 'burak':
#     print(ch, end='-')   # karakterleri yan yana yazdır, araya - koy
# endregion


# region Loop Over String Index
# Stringlerin de index’i vardır, tıpkı listeler gibi
# for i in range(len('burak')):
#     print(i)
# endregion


# region Craft Mail Addresses
#! users = ['Burak Yılmaz', 'Rana Nur Ceylan', 'İpek Yılmaz', 'Kerim Abdurrahman Burak Yılmaz']
#
#? users listesindeki kullanıcılardan kurumsal mail adresi craft ediyoruz.
#* sample mail address --> rana.ceylan@outlook.com
#todo: craft mail address, mail_address listesine eklenerek ekrana basılacak
#? Hint: split(), bir listenin uzunluğu ne olursa olsun son elemana nasıl get ederim
# mail_addresses = []
# domain_name = '@outlook.com'

# for user in users:
    # 1) Küçük harfe çevir → "kerim abdurrahman burak yılmaz"
    # 2) split() → ['kerim', 'abdurrahman', 'burak', 'yılmaz']
    # user_names = user.lower().split(' ')    # ['burak','yılmaz']

    # İlk isim → user_names[0]
    # Son isim → user_names[-1]
    # mail_address = f"{user_names[0]}.{user_names[-1]}{domain_name}"

    # Oluşan mail adresini listeye ekleyelim
    # mail_addresses.append(mail_address)

# print(mail_addresses)

# ÇIKTI: ['burak.yılmaz@outlook.com', 'rana.ceylan@outlook.com', 'ipek.yılmaz@outlook.com', 'kerim.yılmaz@outlook.com']
# endregion


# region Example 4
# Kullanıcıdan bir söz öbeği alalım. Boşluk olmayacak şekilde karakter karakter ekrana yazdıralım.
# word = input("Enter a word: ")
# lst = []
# for i in range(0, len(word), 1):
#     if word[i] != " ":
#         lst.append(word[i])
# print(lst)
# Yukarıdaki örnekte bir string ifade içerisinde kurduğumuz döngü vasıtasıyla 
# index mantığıyla adım adım içerisinde dolaşarak çözüme gittik.

# lst_1 = []
# for char in word:
#     if char == " ":
#         continue
#     lst_1.append(char)
# print(lst_1)
# Bu örnekte ise bir ifade içerisindeki her bir karakteri doğrudan döngüye gönderdik. 
# Yani adım adım karakterlerin kendisini gönderdik.

# Bu örnek üzerinden şu yorumu yapabiliriz. 
# C#, Java, JavaScript gibi programlama dillerinde sayaç mantığı ile çalışan for döngüsü varken,
# Python programlama dilinde for hem sayaç (index) hem de iterable (foreach) mantığı ile çalışabilir.
# Yukarı da saydığımız programlama dillerinde iterable mantığını yürütmek için 
# bir başka döngü tipi olan foreach kullanılmaktadır.

# endregion


# region Example - 5
# Kullanıcıdan alınan söz öbeğini harf harf bir liste içerisine kayıt edin.
# Boşluk karakterinin listeye eklenmesini istemiyoruz.
# word = input("Say something... : ")

# characters = []   # Harfleri tutacağımız liste

# for char in word:
#     if char == ' ':            # Eğer boşluksa, listeye ekleme
#         continue
#     else:
#         if char not in characters:   # Eğer listede yoksa ekle
#             characters.append(char)

# print(characters)
# endregion


# region Example - 6
# Kullanıcıdan alınan söz öbeğindeki sesli harfleri bir listeye dolduralım
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


# region Character Classification
#! end-user bir söz öbeği alalım
#? sample --> buRaIk yi?lm2aZu
#* sesli harfleri --> sesli_harfler = []
#* sessiz harfleri --> sessiz_harfler = []
#* yazım hatalarını --> typo_characters = []
#* space karakteri ignore edilecek.
#* ilgili listelerdeki hiçbir eleman tekrar etemeyecek

# Sesli ve sessiz harflerin tutulacağı listeler
# sesli_harfler = []
# sessiz_harfler = []

# Typo karakterlerin tutulacağı liste
# typo_characters = []

# word = input('Type something: ')

# Metindeki her karakteri dolaşalım
# for ch in word.lower():     # küçük harfe çevir
#     if ch.isalpha():                         # harf mi?
#         if ch not in sesli_harfler and ch not in sessiz_harfler: 
#             if ch in 'aeıioöuü':    # sesli harf kontrolü
#                 sesli_harfler.append(ch)
#             else:
#                 sessiz_harfler.append(ch)
#     else:
#         if ch == " ":   # boşlukları geç
#             continue 
#         if ch not in typo_characters:   # Harf değilse typo listesine ekle (bir kere)
#             typo_characters.append(ch)       
        
# Sonuçları yazdıralım
# print("\n--- SONUÇLAR ---")
# print("Sesli harfler :", sesli_harfler)
# print("Sessiz harfler:", sessiz_harfler)
# print("Typo karakterler:", typo_characters)
# endregion


# region Example - 7
# lst_1 ve lst_2 içerisine rastgele 10 sayı üretip doldurun
# Doldurma işlemini INDEX mantığına göre yapın
# Örneğin: lst_1[0] + lst_2[0] = lst_3[0]
# Her şey tek bir for loop içinde çözülecek
# Sayılar 0 ile 100 arasında üretilecek

# from random import randint

# lst_1 = []
# lst_2 = []
# lst_3 = []

# 10 eleman için döngü
# for i in range(10):
      # 0–100 arasında rastgele üretilen sayıları listelere index mantığıyla ekle
#     lst_1.insert(i, randint(a=0, b=100))
#     lst_2.insert(i, randint(a=0, b=100))

      # Aynı index'teki iki sayının toplamını lst_3'e ekle
#     lst_3.insert(i, lst_1[i] + lst_2[i])
#     print(f'{lst_1[i]} + {lst_2[i]} = {lst_1[i] + lst_2[i]}')

# print("List 1:", lst_1)
# print("List 2:", lst_2)
# print("List 3 (Toplamlar):", lst_3)
#endregion


# region Example - 8
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


# region Nested List Examples
# Çok boyutlu (nested) liste: ilçeler ve semtler
# ilceler = [
#     ['Sarıyer'],                            # 0. index
#     ['Etiler', 'Nispetiye', 'Ulus'],        # 1. index
#     ['Suadiye', ['Feneryolu', 'Erenköy']],  # 2. index
#     [['Beşiktaş', 'Maçka'], 'Harbiye', ['Nişantaşı']]  # 3. index
# ]

# 1. index'teki listenin 2. elemanı -> "Ulus"
# print(ilceler[1][2])

# 0. index'teki listenin 0. elemanı -> "Sarıyer"
# print(ilceler[0][0])

# 2. index'teki listenin 1. elemanının 0. elemanı -> "Feneryolu"
# print(ilceler[2][1][0])

# 3. index'teki listenin 1. elemanı -> "Harbiye"
# print(ilceler[3][1])

# 3. index → 0. index → 1. eleman -> "Maçka"
# print(ilceler[3][0][1])
# endregion


# region Slicing (Dilimleme)
# -------------------------------
# Slicing Açıklaması:
# liste[start : stop : step]
# start → başlangıç index'i (dahil)
# stop  → bitiş index'i (hariç)
# step  → adım (opsiyonel)
# -------------------------------

# fruits = [
#     "Apple", "Banana", "Orange", "Mango", "Pineapple",
#     "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
#     "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
#     "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
# ]

# print(fruits[2:7])     # 2. index’ten 7’ye kadar (7 dahil değil)
# print(fruits[:3])      # listenin başından 3. index’e kadar
# print(fruits[1::2])    # 1. index’ten başlayarak sona kadar, 2’şer adım ile (1,3,5,7...)
# print(fruits[::4])     # 0. index’ten başlayarak sona kadar, 4’er adım ile (0,4,8,12...)
# print(fruits[::-1])    # listenin tamamını ters çevirir (reverse)
# print(fruits[::-2])    # sondan başa doğru 2’şer adımla geri gider
# print(fruits[10::-3])  # 10. index’ten 0’a doğru, 3’er adım ile geri gider
# endregion


# region Unpacking - Unboxing
# İç içe listeler: [İsim, Yaş, Meslek]
# my_family = [
#     ['Burak Yılmaz', 36, 'Developer'],
#     ['Hakan Yılmaz', 39, 'Chemist'],
#     ['İpek Yılmaz', 41, 'Art Historian']
# ]

# Unpacking (dağıtma):
# Her alt listedeki 3 elemanı sırayla full_name, age, occupation değişkenlerine ayırır
# for full_name, age, occupation in my_family:
#     print(
#         f'Full Name: {full_name}\n'
#         f'Age: {age}\n'
#         f'Occupation: {occupation}\n'
#     )
# endregion


# region Punctuation
# string.punctuation → Python'ın hazır noktalama işaretleri setidir.
# Örn: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# from string import punctuation
# print("Python punctuation listesi:")
# print(punctuation)
# endregion


# region Character Type Checker
# qwe = input("Type something: ")

# for ch in qwe:
#     print(ch, " -> ", type(ch))
# endregion


# region Password Validation
# Sign in olurken kullanıcının şifresini kontrol edelim.
# Şifre en az 16 karakterli olacak.
# Noktalama işareti içerecek. Python'da hazır yapısı var.
# En az bir tane büyük harf
# En az bir küçük harf
# en az bir rakam içeriyorsa
# şifre uygundur. herhangi birini içermiyorsa uygun değildir.

# from string import punctuation

# password = input("Please type your password: ") 

# has_digit = False       # en az bir rakam var mı?
# has_upper = False       # en az bir büyük harf var mı?
# has_lower = False       # en az bir küçük harf var mı?
# has_punct = False       # en az bir noktalama işareti var mı?

# Şifrenin karakterlerini tek tek gez
# for char in password:
#     if char.isdigit():
#         has_digit = True
#     if char.isupper():
#         has_upper = True
#     if char.islower():
#         has_lower = True
#     if char in punctuation:
#         has_punct = True

# Uzunluk + tüm kurallar aynı anda sağlanmalı
# if len(password) >= 16 and has_digit and has_upper and has_lower and has_punct:
#     print("Şifre uygundur ✅")
# else:
#     print("Şifre uygun değildir ❌")
# endregion


# region Example Password Validation with Error
# Sign in olurken kullanıcının şifresini kontrol edelim.
# Şifre en az 16 karakterli olacak.
# Noktalama işareti içerecek. Python'da hazır yapısı var.
# En az bir tane büyük harf
# En az bir küçük harf
# en az bir rakam içeriyorsa
# şifre uygundur. herhangi birini içermiyorsa uygun değildir.

# from string import punctuation

# password = input("Please type your password: ")

# has_digit = False
# has_upper = False
# has_lower = False
# has_punct = False

# --- Character analysis ---
# for char in password:
#     if char.isdigit():
#         has_digit = True
#     if char.isupper():
#         has_upper = True
#     if char.islower():
#         has_lower = True
#     if char in punctuation:
#         has_punct = True

# Eksikleri tutacağımız boş liste
# errors = []

# if len(password) < 16:
#     errors.append("Password must be at least 16 characters.")
# if not has_digit:
#     errors.append("Must contain at least one digit.")
# if not has_upper:
#     errors.append("Must contain at least one uppercase letter.")
# if not has_lower:
#     errors.append("Must contain at least one lowercase letter.")
# if not has_punct:
#     errors.append("Must contain at least one punctuation character (!,@,#,?,*, etc.)")

# SONUÇ:
# if len(errors) == 0:
#     print("Password is valid ✅")
# else:
#     print("Password is NOT valid ❌")
#     print("Missing Requirements:")
#     for err in errors:
#         print(err)
# endregion


# region Labwork
# kullanıcı login olacak
# register olsun
# bütün ürünlerin toplam fiyatı nedir
# ürün adı laptop olan ürünlerin fiyatlarını toplayalım
# kullanıcı ürün search 
# fiyatı 200 TL altında olan ürünler listelensin

# users = [
#     ['beast', '123'],
#     ['bear', '987'],
#     ['keko', '567'],
# ]

# products = [
#     ["Laptop", 850],
#     ["Smartphone", 499],
#     ["Headphones", 79],
#     ["Keyboard", 45],
#     ["Monitor", 220],
#     ["Mouse", 25],
#     ["Smartwatch", 150],
#     ["Tablet", 310],
#     ["External Hard Drive", 95],
#     ["Webcam", 60],
#     ["Laptop", 856],
# ]

# while True:
#     first_process = input('Sign In --> 1\nSign Up -- 2\nTuşlayınız: ')
    
#     match first_process:
#         case '1':
#             kullanici_adi = input('User Name: ')
#             sifre = input('Password: ')
            
#             is_success = False
#             for user in users:
#                 if user[0] == kullanici_adi and user[1] == sifre:
#                     is_success = True
#                     break
            
#             if is_success:
#                 print(f'Giriş başarılı..!\nHoşgeldiniz, {kullanici_adi}')
#                 while True:
#                     second_process = input('İşlem Adı Giriniz: ')
                    
#                     match second_process:
#                         case 'toplam fiyat':
#                             total = 0
#                             for product in products:
#                                 total += product[1]
#                             print(f'Toplam Fiyatlar: {total}')
#                         case 'laptop toplam fiyat':
#                             total = 0
#                             for product in products:
#                                 if product[0] == 'Laptop':
#                                     total += product[1]
#                             print(f'Toplam Fiyatlar: {total}')
#                         case 'ürün ara':
#                             urun_adi = input('Ürün adı giriniz: ')
#                             for product in products:
#                                 if product[0] == urun_adi:
#                                     print(f'Ürün Adı: {product[0]}\nFiyatı: {product[1]}')
#                             else:
#                                 print('Aradığınız ürün bulunmamaktadır..!')
#                         case 'fiyat aralığına göre ara':
#                             alt = int(input('Alt limit fiyato: '))
#                             ust = int(input('Üst limit fiyato: '))
#                             for product in products:
#                                 if product[1] >= alt and product[1] <= ust:
#                                     print(f'Ürün Adı: {product[0]}\nFiyatı: {product[1]}')
#                         case 'çıkış':
#                             print('Uygulama kapatılıyor...!')
#                             break
#                         case _:
#                             print('Lütfen doğru işlem türü giriniz..!')
#             else:
#                 print('Kullanıcı adı yada şifre hatalı..!')
#         case '2':
#             kullanici_adi = input('User Name: ')
#             sifre = input('Password: ')

#             is_exist = False
#             for user in users:
#                 if user[0] == kullanici_adi:
#                     is_exist = True
#                     break

#             if is_exist:
#                 print('Kullanıcı adı zaten var.')
#             else:
#                 new_user = [kullanici_adi, sifre]
#                 users.append(new_user)
#                 print('Üyelik işleminiz tamamlandı.')
#         case _:
#             print('Lütfen uygun işlem numarasını giriniz..!')
# endregion

# region enumerate() Example
# enumerate() fonksiyonu, bir liste üzerinde dönerken
# hem index'i hem de liste elemanını aynı anda almamızı sağlar.
# Örneğin:
#   boxers[0] → 'Mike Tyson'
#   boxers[1] → 'Muhammed Ali'
# fakat enumerate ile aynı anda şu şekilde çekebiliriz:
#   index, item = 0, 'Mike Tyson'

# boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewix', 'Evender Holyfiled', 'George Foreman']

# enumerate(boxers) → (index, item) döner
# for index, item in enumerate(boxers):
#     print(
#         f'Index Value: {index}\n'
#         f'Item Value: {item}'
#     )
# endregion

#! List Comprehensions
# List Comprehension, uzun döngüler yazmadan hızlıca liste üretmenin en Pythonic yoludur.
# Daha Pythonic - daha hızlı - daha temiz kod sağlar.

# ⭐ Neden Önemli?
# ✔ Daha kısa kod                    → daha az hata ihtimali
# ✔ Daha hızlı çalışır               → optimize edilmiş yapı
# ✔ Okunabilirliği artırır           → tek satırda açık mantık
# ✔ Transform işlemleri için ideal   → veri dönüştürme
# ✔ Filtreleme yapabilir             → if eklenebilir
# ✔ Veri üretimi/parsing için mükemmel

# Python projelerinde özellikle:
# - API verilerini dönüştürürken
# - büyük listeleri işlerken
# - filtreleme yaparken
# - nested list (matris) oluştururken
# çok tercih edilir.

# 📌 TEMEL YAPI:
#     [ yeni_deger for eleman in liste if kosul ]

# region Number Generator
# 0–9 arasındaki sayıları bir listeye ekleyiniz.
# range(10) → 0'dan 9'a kadar sayıları üretir.

# List Comprehension — Pythonic Yöntem
# lst = [i for i in range(10)]
# print("List Comprehension:", lst)

# ✔️ Klasik yöntem (döngü + append)
# lst_1 = []
# for i in range(10):
#     lst_1.append(i)

# print("Klasik Yöntem:", lst_1)
# endregion


# region Random Number Generator
# 0 ile 100 arasında rastgele üretilmiş 10 adet tam sayıdan oluşan bir liste oluşturunuz.

# Bilgi:
#   randint(a, b) → a ve b DAHİL olmak üzere rastgele tam sayı üretir.
#   range(10)     → 10 tekrar oluşturur (0–9)

# from random import randint

# Klasik yöntem (döngü + append)
# lst = []                    

# for _ in range(10):          # '_' → değer kullanmadığımız yerlerde tercih edilir
#     random_number = randint(0, 100)   # 0–100 arasında rastgele sayı üret
#     lst.append(random_number)         # sayıyı listeye ekle

# print("Döngü ile üretilen liste: ", lst)

# List Comprehension (Tek satırda üretim)
# random_list = [randint(0, 100) for _ in range(10)]
# print("List Comprehension ile üretilen liste: ", random_list)

# print([randint(0, 100) for _ in range(10)])
# endregion


# region  Squared Numbers
# 0–9 arasındaki sayıların karesini hesaplayıp bir listeye ekleyiniz.

# Bilgi:
#   i ** 2     → i sayısının karesi

# print([i ** 2 for i in range(10)])
# endregion


# region Even Numbers — 0 to 100
# 0–100 arasındaki ÇİFT sayıları listeye ekleyiniz.

# Bilgi:
#   i % 2 == 0  → sayının çift olup olmadığını kontrol eder.
#   range(0, 101) → 0'dan 100'e kadar tüm sayıları üretir.

even_numbers = [i for i in range(0, 101) if i % 2 == 0]
print(even_numbers)
# endregion


# region Fruit List — Filtering Fruits Containing 'a'

# fruits = [
#     "Apple", "Banana", "Orange", "Mango", "Pineapple",
#     "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
#     "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
#     "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
# ]

# print(fruits)

# İçinde 'a' harfi geçen meyveleri filtreleyiniz.

# ✔ List Comprehension ile çözüm
# print([fruit for fruit in fruits if 'a' in fruit.lower()])

# Aynı işlemin klasik döngü ile yapılmış hali

# lst = []   # filtrelenen meyveler bu listeye eklenecek

# for fruit in fruits:
#     if 'a' in fruit.lower():
#         lst.append(fruit)

# print(lst)
# endregion


# region Fruit Check — Contains "an"
# Meyve ismi içinde "an" geçiyorsa True, geçmiyorsa False

# Ternary (koşullu ifade) yapısı:
#   True if koşul else False

# Örnek:
#   'adult' if age >= 18 else 'child'

# print([True if 'an' in fruit.lower() else False for fruit in fruits])
# endregion


# region Multiplication Table — 1 to 10
# 1–10 arasındaki sayıların çarpım tablosunu oluşturunuz.

# Bilgi:
#   Nested loop (iç içe döngü) kullanılır:
#       i → dış döngü (1'den 10'a kadar)
#       j → iç döngü (1'den 10'a kadar)
#   Her j döngüsünde i × j hesaplanır ve yazdırılır.

# Classic Approach — Nested Loops
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
#     print('=========================')

# List Comprehension Approach — 10×10 Table
# table = [[f"{i} x {j} = {i * j}" for j in range(1, 11)] for i in range(1, 11)]
# for row in table:
#     print(*row, sep="\t")
# endregion


# region Lambda Function — Introduction
# Lambda Nedir?
#   İsimsiz, tek satırlık fonksiyon yazma yöntemidir.
#   Fonksiyon tanımı (def) yazmadan hızlıca işlem yapmayı sağlar.
#
# Neden Önemlidir?
# ---------------------------------------------------------
# ✔ map(), filter(), sorted() gibi fonksiyonlarla sık kullanılır
# ✔ Gereksiz fonksiyon tanımlamayı ortadan kaldırır
# ✔ Kodun sade ve temiz görünmesini sağlar
# ✔ Inline (satır içi) kullanım için idealdir
# ✔ Matematiksel işlemlerde çok pratiktir

# Basit bir lambda fonksiyonu — kare alma
# square = lambda x: x * x
# print(square(5))   # 25

# Lambda ile iki sayıyı toplama
# sum_two = lambda a, b: a + b
# print(sum_two(3, 7))  # 10

# Metin dönüştürme — lambdada string işlemleri
# add_text = lambda t: t.upper() + "!"
# print(add_text("hello"))  # HELLO!
# endregion


#! Filter
# Belirli koşulu sağlayan elemanları döndürür.
# Arama, filtreleme, validasyon gibi işlemler için idealdir.

# ⭐ Neden Önemli?
# ✔ Veri filtreleme (ör: pozitif sayıları seçmek)
# ✔ Fiyat filtreleme (ör: 200 TL altındakileri listelemek)
# ✔ Kullanıcı doğrulama (ör: e-posta formatı doğru mu?)
# ✔ Temiz veri oluşturma
# ✔ Hatalı veriyi ayırma
# ✔ Büyük veri setlerinde performanslı filtreleme
# ✔ Koşula bağlı veri seçimi

# Temel Formül:
#     filter(kosul_fonksiyonu, liste)

# Açıklama:
#   - filter() → Koşulu sağlayan elemanları döndürür.
#   - Sonuç bir "iterator" olduğu için genelde list() ile çevrilir.


# region Filter Function — Basic Sample
# Verilen numbers listesinden 20'den küçük olan sayıları filtreleyiniz.

# filter() çıktısı bir iterator olduğundan list() ile listeye çevrilir.

# numbers = [10, 15, 20, 25, 30]

# filtered = list(filter(lambda x: x < 20, numbers))
# print(filtered)   # [10, 15]
# endregion


# region Random Number Generation — Fill List With Numbers
# 1000 adet rastgele sayı üretetiniz.
# a = -100  → minimum değer
# b =  100  → maksimum değer
# randint(a, b) → a ve b dahil olmak üzere rastgele tam sayı üretir.

# list comprehension ile hızlıca 1000 elemanlı liste üretiyoruz.

# from random import randint

# numbers = [randint(a=-100, b=100) for i in range(1000)]
# print("Tüm Sayılar:", numbers)

# Yukarıda oluşturulan liste içerisinden sadece POZİTİF (0'dan büyük) olanları listeleyelim.

# Path I → List Comprehension
# Şartlı list comprehension:

# positive_numbers = [number for number in numbers if number > 0]
# print("Pozitif Sayılar (List Comprehension):", positive_numbers)

# Path II → filter() fonksiyonu

# filter(function, iterable)
#    → function True döndürürse eleman listeye alınır.

# lambda x: x > 0  → pozitif sayıları seçer
# filter sonucu 'iterator' döner, listeye çevirmek gerekir.

# temp_lst = filter(lambda x: x > 0, numbers)
# positive_numbers = list(temp_lst)
# print("Pozitif Sayılar (filter):", positive_numbers)
# endregion


# region Filter Function — Extract Even Numbers
# filter() fonksiyonu ile çift sayıları filtreleyerek sonucu liste olarak ekrana yazdırınız.

#   - filter sonucu bir iterator olduğu için list() ile listeye çeviriyoruz

# print(
#      list(
#       filter(lambda x: x % 2 == 0, numbers)
#      )
# )
# endregion