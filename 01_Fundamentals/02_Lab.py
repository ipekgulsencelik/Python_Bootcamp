
#! Karar Mekanizması (If-Else)
# Uygulamalarımızda belirli şartlar doğrultusunda şartın sağlaması yada sağlamaması durumuna göre uygulamaka farklı işlem yapılmasını temin etmektedir.

# region Sample
# if 3 > 2:
#     print("Merhaba..!")
# else:
#     print("Salve..!")
#
#
# print("Hello..!")
# endregion

# region Example 
#  x = int(input("Tam Sayı: "))
#  y = int(input("Tam Sayı: "))
#
# if x > y:
#     print(f"{x} büyüktür..!")
# else:
#     print(f"{y} büyüktür..!")
# endregion

# region Example 1
#  x = int(input("Tam Sayı: "))
#  y = int(input("Tam Sayı: "))
#
# if x > y:
#     print(f"{x} büyüktür..!")
# elif x == y:
#     print(f"{x}, {y} değerine eşittir..!")
# else:
#     print(f"{y} büyüktür..!")
# endregion


# region Example 2
# Kullancıdan alınan sayı pozitif mi negatif mi nötr mü?
# x = int(input("Tam sayı giriniz: "))
#
# if x > 0:
#     print(f"{x} pozitiftir..!")
# elif x == 0:
#     print(f"{x} nötr..!")
# else:
#     print(f"{x} negatiftir..!")
# endregion


# region Example 3
# Kullanıcıdan alınan sayı çift mi tek mi?
# Not: Mod işlemi için "%" sembolünü kullanabilirsiniz
# x = int(input("Lütfen bir tam sayı giriniz: "))
#
# if x % 2 == 0:
#     print(f"{x} çifttir..!")
# else:
#     print(f"{x} tekrir..!")
# endregion


# region Example 4
# Kullanıcıdan alınan mevsim bilgisine göre ayları ekrana basan uygulamayı yazınız
# mevsim = input("Lütfen mevsim girin: ").lower()  # burada lower() fonksiyonu ile kullanıcıdan gelen bilgiyi küçük harflere dönüştürerek mevsim değişkenine atamamız gerekmektedir.
#
# if mevsim == "kış":
#     print("aralık-ocak-şubat")
# elif mevsim == "ilkbahar":
#     print("mart-nisan-mayıs")
# elif mevsim == "yaz":
#     print("haziran-temmuz-ağustos")
# elif mevsim == "sonbahar":
#     print("eylül-ekim-kasım")
# else:
#     print("Böyle bir mevsim yok uzaylı mısın?")
# endregion


#! and - or


# region Example 5
# Kullanıcıdan alınan 3 adet sayıyı büyüklük olarak karşılaştırın. büyük olan sayıyı ekrana yazalım
# x = int(input("Sayı giriniz: "))
# y = int(input("Sayı giriniz: "))
# z = int(input("Sayı giriniz: "))
# message = ""  # burada message değişkenini içerisini boş yaptım.
#
# if x > y and x > z:
#     message = f"{x} en büyüktür..!"
# elif y > x and y > z:
#     message = f"{y} en büyüktür..!"
# elif z > x and z > y:
#     message = f"{z} en büyüktür..!"
# else:
#     message = "büyük sayı yoktur. Sayılar birbirine eşit olabilir..!"
#
# print(message)
# endregion


# region Example 6
# Kullanıcıdan bir adet ürün alalım
#? domates, biber yada patlican ise sebze reyonuna
#* tablet, bilgisayar, telefon ise teknoloji reyonuna
#! şampuan, diş macunu, parfüm ise kozmetik reyonuna
#
# urun = input("Aradığınız ürünü girin: ").lower()
# mesaj = ""
#
# if urun == "domatas" or urun == "biber" or urun == "patlican":
#     mesaj = "Aradığınız ürün sebze reyonunda"
# elif urun == "tablet" or urun == "bilgisayar" or urun == "telefon":
#     mesaj = "Aradığınız ürün teknoloji reyonunda"
# elif urun == "şampuan" or urun == "diş macunu" or urun == "parfüm":
#     mesaj = "Aradığınız ürün kişisel bakım retonunda"
# else:
#     mesaj = "Aradığınız ürün bulunmamaktadır..!"
#
# print(mesaj)
# endregion


# region Example 7
#todo: kullanıcıdan username ve password alalım. 
# username 'beast', password '123' ise hoşgeldiniz, değilse hatalı kullanıcı bilgileri.
#
# username = input('User name: ')
# password = input('Password: ')
#
# if username == 'beast' and password == '123':
#     print('Hoşgeldiniz..!')
# else:
#     print('Hatalı kullanıcı bilgileri..!')
# endregion


#! Nested If (İç İçe If)


# region Example 8
# kullanıcı uygulamaya login olacak
# kullanıcı kilo, boy bilgisi girecek ve BMI değerine göre durum feedback verilecek
#
# username = input("User name: ")
# password = input("Password: ")
#
# if username == 'beast' and password == '123':
#     print(f'{username}, welcome..!')
#
#     height = float(input("Height: "))
#     weight = float(input("Weight: "))
#
#     bmi = weight / (height ** 2)
#     status = ''
#
#     if 0 < bmi <= 18.5:   #! 0 < bmi and bmi <= 18.5
#         status = 'lean'
#     elif 18.6 <= bmi <= 24.9:     #? 18.5 <= bmi and bmi <= 24.9
#         status = 'normal'
#     elif 25 <= bmi <= 29.9:
#         status = 'weighted'
#     elif 30 <= bmi <= 34.9:
#         status = 'overweighted'
#     elif 35 <= bmi <= 39.9:
#         status = 'obesity'
#
#     print(
#         f'User Name: {username}\n'
#         f'BMI: {bmi}\n'
#         f'Status: {status}'
#     )
#
# else:
#     print('Invalid credentials..!')
# endregion


# region Example 9
# Kullanıcıdan username ve password ve rol bilgilerini alalım. username beast password 123 ve rol admin yada manager ise yönetici sayfasına yönlendiriliyorsunuz rol member ise kullanıcı sayfasına yöneldiriliyorsunuz
# username = input("Kullanıcı adı: ")
# password = input("Şifre: ")
# rol = input("Rol: ")
#
# if username == "beast" and password == "123":
#     if rol == "admin" or rol == "manager":
#         print("Yönetici sayfasına yönlendiriliyorsunuzu..!")
#     elif rol == "member":
#         print("Kullanıcı sayfasına yönlendiriliyorusunuz..!")
#     else:
#         print("Yetkiniz bulunmamaktadır..!")
# else:
#     print("Kullanıcı bilgileriniz yanlış..!")
# endregion


# region Example 10
# Kullancıdan aracının kaç gündür trafikte olduğu bilgisini alalım ve aracın hangi servis aralığında olduğunu feedback olarak verelim
# day = int(input("Aracınız kaç gündür yolda? "))
#
# if 1 < day <= 365:  # day > 1 and day <= 365
#     print("1. servis aralığında")
# elif 366 <= day < 365 * 2:
#     print("2. servis aralığında")
# elif 365 * 2 <= day <= 365 * 3:
#     print("3. servis aralığında")
# endregion


# region Example 11
# Kullanıcıdan araç tipini ve hız bilgisini alalım. Şayet otomobil ise ve hız da 60 ve üzeri cezalı 60 altın da ise ceza yok
# Motorsiklet ile otomobil aynı şekilde değerlendirilsin.
# Kamyon 40 ve üzeri cezalı altında bir hıza sahip ise ceza yok.
# print("Menü")
# print("otomobil")
# print("kamyon")
# print("motorsiklet")
# arac_turu = input("Araç türü: ")
# hiz = int(input("Hız: "))
# if arac_turu == "otomobil":
#     if hiz >= 60:
#         print("Cezalısın..!")
#     else:
#         print("Ceza yok..!")
# elif arac_turu == "kamyon":
#     if hiz >= 80:
#         print("Cezalısın..!")
#     else:
#         print("Ceza yok..!")
# elif arac_turu == "motorsiklet":
#     if hiz >= 40:
#         print("Cezalısın..!")
#     else:
#         print("Ceza yok..!")
# else:
#     print("Lütfen menüde ki araç türlerinden birini giriniz..!")
# endregion


# region Example 12
# Bir kitap 5 TL
# Kullanıcı 1-10 arasında kitap alırsa yüzde 5 indirim
# 11- 20 yüzde 10 indirim
# 21-30 yüzde 15 indirim
# 31- 40 yüzde 20 indirim
# 41 - 50 yüzde 25 indirim
# Müşterinin ödeyeceği toplam tutarı ekrana yazdırırnız
# amount = int(input("How many book you buy?"))
# book_price = 5
#
# if amount <= 0: 
#     print("You can't buy minus book..!")
# elif 1 <= amount <= 10:  # amount >= 1 and amount <= 10
#     print(f"Total Price: {amount * book_price * 0.95}")
# elif 11 <= amount <= 20:
#     print(f"Total Price: {amount * book_price * 0.90}")
# elif 21 <= amount <= 30:
#     print(f"Total Price: {amount * book_price * 0.85}")
# elif 31 <= amount <= 40:
#     print(f"Total Price: {amount * book_price * 0.80}")
# elif 41 <= amount <= 50:
#     print(f"Total Price: {amount * book_price * 0.75}")
# else:
#     print("You can't buy too much book..!")
# endregion


# region Example 13
# Harf notu hesaplayan uygulamyı yazın
# vize yüzde 30
# final yüzde 60
# ödev yüzde 10 harf notunu etkilesin
# vize = float(input("Vize: "))
# final = float(input("Final: "))
# odev = float(input("Odev: "))
#
# if (0 <= vize <= 100) and (0 <= final <= 100) and (0 <= final <= 100):
#     ort = vize * 0.3 + final * 0.6 + odev * 0.1
#
#     if 90 <= ort <= 100:
#         print("Harf Notu: AA")
#     elif 80 <= ort <= 89:
#         print("Harf Notu: BA")
#     elif 70 <= ort <= 79:
#         print("Harf Notu: BB")
#     elif 60 <= ort <= 69:
#         print("Harf Notu: CC")
#     elif 50 <= ort <= 59:
#         print("Harf Notu: DC")
#     elif 40 <= ort <= 49:
#         print("Harf Notu: DD")
#     else:
#         print("Harf Notu: FF")
# else:
#     print("Lütfen doğru not girermisiniz..!")
# endregion

# region Labwork 1
# Bir kitap 5 TL
#? Kullanıcıdan satın aldığı kitap sayısını alalım
#* Alınan kitap sayısı 1 ile 5 arasında ise yüzde 5 iskonto
#* Alınan kitap sayısı 6 ile 10 arasında ise yüzde 10 iskonto
#? Alınan kitap sayısı 11 ile 15 arasında ise yüzde 15 iskonto
#* Alınan kitap sayısı 16 ile 20 arasında ise yüzde 20 iskonto
#! toplam fiyata alınan kitap sayısına göre indirim uygulanarak ödenecek toplam tutar ekrana yazdırılsın
#
# Kullanıcıdan alınan kitap sayısını alalım
# kitap_sayisi = int(input("Kaç kitap satın aldınız? "))
#
# Kitap fiyatı
# kitap_fiyati = 5
# toplam_fiyat = kitap_sayisi * kitap_fiyati
#
# İndirim oranı belirleme
# if 1 <= kitap_sayisi <= 5:
#     indirim_orani = 0.05
# elif 6 <= kitap_sayisi <= 10:
#     indirim_orani = 0.10
# elif 11 <= kitap_sayisi <= 15:
#     indirim_orani = 0.15
# elif 16 <= kitap_sayisi <= 20:
#     indirim_orani = 0.20
# else:
#     indirim_orani = 0  # 20’den fazla kitapta indirim yok
#
# İndirimli toplamı hesapla
# indirim_miktari = toplam_fiyat * indirim_orani
# odenecek_tutar = toplam_fiyat - indirim_miktari
#
# print(f"Toplam tutar: {toplam_fiyat:.2f} TL")
# print(f"İndirim oranı: %{indirim_orani * 100}")
# print(f"Ödenecek tutar: {odenecek_tutar:.2f} TL")
# endregion


# region Labwork 2
#todo: kullanıcıdan araç türü ve hız alalım
#? araç türü otomobil, hız 60'tan büyükse cezalı değilse ceza yok
#* araç türü kamyon, hız 40'tan büyükse cezalı değilse ceza yok
#! araç türü motorsiklet, hız 70'ten büyükse cezalı değilse ceza yok
#
# Kullanıcıdan araç türü ve hızını alalım
# arac_turu = input("Araç türünü giriniz (otomobil/kamyon/motosiklet): ").lower()
# hiz = int(input("Hızınızı giriniz (km/s): "))
#
# vehicle = input('Type your vehicle: ').lower()
# speed = float(input('Speed: '))
#
# if speed > 0:
#     if vehicle == 'car':
#         if speed >= 60:
#             print('Penalty..!')
#         else:
#             print('No penalty..!')
#     elif vehicle == 'truck':
#         if speed >= 40:
#             print('Penalty..!')
#         else:
#             print('No penalty..!')
#     elif vehicle == 'motorcycle':
#         if speed >= 70:
#             print('Penalty..!')
#         else:
#             print('No penalty..!')
#     else:
#         print('Please type a proper vehicle type..!')
# else:
#     print('Invalid speed value..!')
# endregion


#! match-case

# region Example 14
# todo: Kullanıcıdan mevsim bilgisi alıyoruz.
# ? kullanıcıdan gelen mevsim bilgisine göre ayları ekrana yazdırıyoruz.
#
# season = input('Type a season: ').lower()
#
# match season:
#     case 'winter':
#         print('December-January-February')
#     case 'spring':
#         print('March-April-May')
#     case 'summer':
#         print('June-July-August')
#     case 'autumn' | 'fall':     # # '|' ifadesi match-case içinde OR için kullanılır
#         print('September-October-November')
#     case _:
#         print('There is no such season..!')
# endregion

# match-case, durum (status) kontrolü için sıklıkla tercih edilir.

# boxing_gloves_status = 'Passive'

# match boxing_gloves_status:
#     case 'Active':
#         pass
#     case 'Passive':
#         pass
#     case 'Modified':
#         pass
#     case _:
#         print('None')

# match-case içerisinde "and" kullanımı

# region Example 15
# kitap_miktari = int(input('Satın Alınan Kitap Sayısı: '))
#
# if kitap_miktari < 0:
#     print('Eksi kitap sayısı olamaz.')
# else:
#     match kitap_miktari:
#         case _ if 1 <= kitap_miktari <= 5:
#             print(f'Ödenecek Tutar: {5 * kitap_miktari * 0.95}')
#         case _ if 6 <= kitap_miktari <= 10:
#             print(f'Ödenecek Tutar: {5 * kitap_miktari * 0.90}')
#         case _ if 11 <= kitap_miktari <= 15:
#             print(f'Ödenecek Tutar: {5 * kitap_miktari * 0.85}')
#         case _ if 16 <= kitap_miktari <= 20:
#             print(f'Ödenecek Tutar: {5 * kitap_miktari * 0.80}')
#         case _:
#             print('En fazla 20 kitap satın alabilirsiniz.')
# endregion


#! Ternary If

""" 
age = int(input('Age: '))

status = 'adult' if age >= 18 else 'child'
print(status) 
"""

""" 
number = int(input('Number: '))
print(f"Status: {'positive' if number > 0 else 'negative'}")
"""

#! Nested Ternary If
""" 
exam_score = 75
result = 'AA' if exam_score >= 80 else 'BB' if exam_score >= 60 else 'CC'
print(f'Result: {result}')

# yukarı satırdaki nested ternary if'in normal yazılmış hali
if exam_score >= 80:
    print('AA')
else:
    if exam_score >= 60:
        print('BB')
    else:
        print('CC')
"""


#! Try-Except-Finally 

# region Example 16
# try:
#     bolunen = int(input('Bolunen: '))
#     bolen = int(input('Bolen: '))
#     sonuc = bolunen / bolen
#     print(f'Sonuc: {sonuc}')
# except (ZeroDivisionError, ValueError) as err:
#     print('Bir tam sayı sıfıra bölünemez..!')
#     #! kendimize mail gönderiyoruz
#     #* log --> uygulamada ne oldu ne bitti bunların kayıtlarının tutulmasına "log" denir
#     print(f'{err}')
# finally:
#     print('Ne olursa olsun çalışırım')
#
#
# x = 5
# y = 10
# result = x + y
# print(result)
# endregion


# Bazı durumlarda bilerek Exception kendimiz raise ederiz

# region Example 17
# try:
#     mail_address = input('Type mail address: ')
#
#     if '@' not in mail_address:
#         raise TypeError('Mail address has to contain "@" symbol..!')
# except TypeError as err:
#     print(err)
# endregion