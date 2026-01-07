
#! Fonksiyonlar
# Fonksiyon, belirli bir işi yapan ve tekrar tekrar kullanılabilen isimlendirilmiş kod bloğudur.

# Method vs Function:
#   - Python’da “method” genelde bir class’ın içinde tanımlı fonksiyondur.
#   - “function” bağımsız tanımlanır.
#   - Çalışma mantıkları benzerdir: parametre alır, işlem yapar.

# Methodlar ile çalışma prensibi aşağı yukarı aynıdır. 
# Methodlar gibi parametre alırlar ve üzerlerine yüklenmiş işleri yerine getirirler. 
# Aralarında ki tek fark fonksiyonlar yaptıkları işler sonucunda değer döndürürler yani bize işlem sonuçlarını return ederler. 
# Böylelikle elde ettiğimiz sonuçalrı başka işlemelere sokabiliriz.

# Amaç:
#   ✔ Kod tekrarını önlemek - Aynı işlemi tekrar tekrar yazmamak
#   ✔ Okunabilirliği artırmak
#   ✔ Daha temiz kod yazmak
#   ✔ Bakımı kolaylaştırmak
#   ✔ Hataların tek yerden düzeltilmesi
#   ✔ Test edilebilirlik

# Fonksiyonlar 2 şekilde olabilir:
#   - Değer döndürmeyen (print ile gösteren)  -> return yoktur (None döner)
#   -  Değer döndüren (return ile sonuç veren) -> sonucu başka işlemlerde kullanılır

#   def       → fonksiyon tanımlar


# region Greeting Function
# def greeting_people():
#     print("Hello..!")

# greeting_people()
# greeting_people()
# greeting_people()
# greeting_people()
# greeting_people()
# endregion


# Parametre, fonksiyona DIŞARIDAN gönderilen değerdir. Fonksiyon bu değerleri kullanarak işlem yapar.

# Type hint:
#   - ZORUNLU DEGILDIR
#   - Sadece bilgi verir
#   - Kodun okunabilirliğini artırır

# Not: Type hint Python’u “zorlamaz”, yanlış tip verilirse runtime’da hata çıkar.


# region Sum Two Numbers Function
# def sum_two_number(a: int, b: int):
#     """
#     Bu fonksiyon 2 tane tam sayı toplar.

#     Args:
#         a (int): integer tipinde tam sayı
#         b (int): integer tipinde tam sayı
#     """
#     print(a + b)

# sum_two_number(2, 4)

# ❌ HATALI: string + int toplanamaz
# sum_two_number(a='fsd', b=10)

# sum_two_number(a=-1, b=13)

# Kullanıcıdan input: input() her zaman STR döner, bu yüzden int() gerekir.
# sum_two_number(
#     a=int(input("Tam Sayi: ")),
#     b=int(input("Tam Sayi: "))
# )
# endregion


# region Random Example
# from random import randint

# random_value = randint(a=100, b=1000)
# print(random_value)
# endregion


# region Create E-mail
#todo: Kullanıcıdan fullname ve domain name alarak, kurumsal mail adresi oluşturunuz.
# def create_email(full_name: str, domain_name: str = '@skilledhub.com'):
#     """
#     Verilen ad-soyad bilgisinden kurumsal e-mail adresi oluşturur.

#     Args:
#         full_name (str): Kullanıcının adı ve soyadı
#         domain_name (str): Mail domaini (default: @skilledhub.com)

#     Returns:
#         None (ekrana yazdırır)
#     """
#     # Ad-soyadı küçük harfe çevirip boşluklardan ayırıyoruz
#     names = full_name.lower().split(" ")

#     print(f'Mail Address: {names[0]}.{names[-1]}{domain_name}')


# Default domain kullanılır
# create_email(
#     full_name="Burak Yilmaz"
# )   # burak.yilmaz@skilledhub.com

# Özel domain gönderilir
# create_email(
#     full_name="Adal Su Uygur",
#     domain_name="@xyz.com"
# )   # adal.uygur@xyz.com
# endregion


# region Multiply
# todo: 3 tane sayıyı çarpan bir fonksiyon yazınız
# Default değer 1 verilirse, parametre gelmese bile çarpım bozulmaz.
# def multiply(x: int = 1, y: int = 1, z: int = 1):
#     """
#     Üç sayıyı birbiriyle çarpar.
#     Varsayılan değerler 1'dir.

#     Args:
#         x (int): Birinci sayı
#         y (int): İkinci sayı
#         z (int): Üçüncü sayı
#     """
#     print(x * y * z)


# multiply(x=2, y=3)        # 2 * 3 * 1 = 6
# multiply(2, 3, 4)         # 24
# multiply()                # 1
# endregion


# region Calculate Area Disk
# todo: daire alanını hesaplayan bir fonksiyon yazınız.
# def calculate_area_disk(radius: int | float, pi: float = 3.14):
#     """
#     Verilen yarıçapa göre dairenin alanını hesaplar.

#     Args:
#         radius (int | float): Dairenin yarıçapı
#         pi (float, optional): Pi sayısı. Varsayılan 3.14

#     Returns:
#         None (ekrana yazdırır)
#     """
#     print(radius * pi)


# calculate_area_disk(
#     radius=1.2
# )
# endregion


# print:
#   - Sadece ekrana yazar (görüntüleme amaçlıdır)
#   - Fonksiyonun sonucunu "dışarı taşımaz" (geri dönen değer None olur)
#   - Test etmek / başka yerde kullanmak zordur

# return:
#   - Değeri fonksiyon DIŞINA döndürür (çıktı üretir)
#   - Sonradan kullanılabilir (değişkene atanır, başka fonksiyona gider)
#   - Test edilebilir, yeniden kullanılabilir (SRP/SoC uyumlu)

# Returnable (Değer Döndüren) Fonksiyonlar

# region Greeting
# def greeting(full_name: str) -> str:
#     """
#     Verilen isim bilgisini kullanarak bir selamlama mesajı üretir.

#     Args:
#         full_name (str): Selamlanacak kişinin adı

#     Returns:
#         str: 'hello <isim>...!' formatında selamlama metni
#     """
#     full_name = full_name.strip()  # baştaki/sondaki boşlukları temizler

#     # Guard Clause (mini doğrulama)
#     if not full_name:
#         return "hello...! (isim boş geldi)"

 #    return f"hello {full_name}...!"


# print(greeting(full_name='burak'))
# print(greeting(full_name='hakan'))
# endregion


# region Power Number
# def pow_number(x: int, pow: int) -> int:
#     """
#     Bir tamsayının verilen kuvvetini (üs) hesaplar.

#     Matematiksel karşılık:
#         xⁿ  →  x ** n

#     Args:
#         x (int): kuvveti alınacak sayı (taban)
#         pow (int): kuvvet değeri (üs)

#     Returns:
#         int: x sayısının pow kuvveti sonucu
#     """
#     # Python'da ** operatörü üs alma işlemini yapar
#     # x ** pow → x'in pow kadar kendisiyle çarpılması
#     return x ** pow


# result_1 = pow_number(x=3, pow=2)   # 3² = 9
# print(result_1) 

# result_2 = pow_number(x=2, pow=2) # 2² = 4
# print(result_2)
# endregion


# region Sum Numbers
# todo: kullanıcıdan alınan 3 adet sayıyı toplayan fonksiyonu yazınız

# def sum_numbers(x: int = 0, y: int = 0, z: int = 0) -> int:
#     """
#     Kullanıcıdan alınan üç adet tam sayıyı toplayan fonksiyon.

#     Args:
#         x (int): Birinci sayı (varsayılan 0)
#         y (int): İkinci sayı (varsayılan 0)
#         z (int): Üçüncü sayı (varsayılan 0)

#     Returns:
#         int: Girilen sayıların toplamı
#     """
#     return x + y + z


# sum_result = sum_numbers(
#     x = int(input('Tam Sayı: ')),
#     y = int(input('Tam Sayı: ')),
#     z = int(input('Tam Sayı: '))
# )

# print(sum_result)
# endregion


# region Remove Duplicate Word
# todo: bir söz öbeğinde ki tekrar eden kelimelerden arındırarak string formatında çıktı veren fonksiyonu yazın
# ? Sample Input  --> 'merhaba ben burak burak ben merhaba'
# * Sample Output --> 'merhaba ben burak'

# set()
#   - Python'da TEKRARSIZ elemanlardan oluşan bir veri yapısıdır.
#   - Sırasızdır (index yoktur).
#   - Aynı elemandan birden fazla barındıramaz.
#   - Index ile erişilemez

# def remove_duplicate_word(sentence: str) -> str:
#     """
#     Verilen cümledeki tekrar eden kelimeleri kaldırır 

#     Varsayılan davranış:
#         - Kelimelerin ilk geçtiği sırayı KORUR (Path I)

#     Args:
#         sentence (str): Tekrar eden kelimeler içerebilen giriş cümlesi

#     Returns:
#         str: Tekrar eden kelimelerden arındırılmış çıktı cümlesi
#     """

#     # Path I — Sıra korunur
#     """ 
#     lst = []

#     for word in sentence.split():
#         if word not in lst:
#             lst.append(word)

#     str_output = ' '.join(lst)
#     return str_output
#     """

#     # Path II — set kullanımı (sıra korunmaz)
#     """ 
#     lst_1 = [word for word in sentence.split()]
#     lst_2 = set(lst_1)
#     str_output = ' '.join(lst_2)

#     return str_output 
#     """

#     # Path III — tek satır (sıra korunmaz)
#     return ' '.join(set([word for word in sentence.split()]))


# result = remove_duplicate_word(
#     sentence='merhaba ben burak burak ben merhaba'
# )

# print(result)
# endregion


# region Even-Odd Number
#todo: Sayının tek mi çift mi olduğunu kontrol eden bir fonksiyon yazınız
# def is_even_or_odd(sayi: int):
#     """
#     Verilen sayının tek mi çift mi olduğunu kontrol eder.

#     Args:
#         sayi (int): Kontrol edilecek sayı

#     Returns:
#         str: Sayının tek veya çift olduğunu belirten mesaj
#     """
#     # % (mod) operatörü → bölümden kalanı verir
#     if sayi % 2 == 0:
#         return f'{sayi} cifttir..!'
#     else:
#         return f'{sayi} tektir..!'


# print(is_even_or_odd(3))    # 3 tektir..!

# sonuc = is_even_or_odd(2)   # return edilen değer değişkende tutulur
# print(sonuc)  # 2 cifttir..!
# endregion


# region Find Even - Odd
# SRP (Single Responsibility Principle) & SoC (Separation of Concern)
# todo: Kullanıcıdan üretilecek rastgele sayı miktarını ve end point alınız.
# todo: çift olanları even_list, tek olanları odd_list içine ekleyerek çıktı veren fonksiyon yazınız.

# from random import randint


# def number_generator(amount: int, start_point: int, end_point: int) -> list[int]:
#     """
#     Belirtilen aralıkta rastgele sayılar üretir.

#     Args:
#         amount (int): Üretilecek rastgele sayı adedi
#         start_point (int): Başlangıç değeri (dahil)
#         end_point (int): Bitiş değeri (dahil)

#     Returns:
#         list[int]: Rastgele üretilmiş sayı listesi
#     """
#     return [randint(a=start_point, b=end_point) for _ in range(amount)]


# def find_even_odd(number_lst: list[int]) -> tuple[list[int], list[int]]:
#     """
#     Verilen sayı listesini çift ve tek olarak ayırır.

#     Args:
#         number_lst (list[int]): Kontrol edilecek sayı listesi

#     Returns:
#         tuple[list[int], list[int]]:
#             even_list → çift sayılar
#             odd_list  → tek sayılar
#     """
#     even_lst = []
#     odd_lst = []

#     for number in number_lst:
#         if number % 2 == 0:
#             even_lst.append(number)
#         else:
#             odd_lst.append(number)

#     return even_lst, odd_lst


# nbr_generator = number_generator(amount=100, start_point=0, end_point=9)

# Not:
# find_even_odd fonksiyonu (even_list, odd_list) şeklinde tuple döndürür.
# tuple unpacking sayesinde bu değerler tek satırda ayrıştırılır.

# even_list, odd_list = find_even_odd(number_lst=nbr_generator)

# print(
#     f'Even List: {even_list}\n'
#     f'Odd  List: {odd_list}'
# )
# endregion


# region Sum Three Numbers and Square Result
# todo: Kullanıcıdan alınan 3 sayıyı toplayan bir fonksiyon yazınız. 
# todo: Toplama işleminin sonucunun karesini alıp ekrana basınız.

# NEDEN FONKSİYON?
#   - Toplama işlemini ayrı bir fonksiyonda yaptık
#   - Çünkü bu sonucu başka işlemlerde (kare alma gibi) tekrar tekrar kullanabilmek istiyoruz

# Aşağıda ki iş mantığını fonksiyon ile çözümledik ki,
# elde ettiğimiz sonucu başka bir işlemde yani kare hesaplama işleminde kullanabilelim.

# def sum_numbers(n1: int, n2: int, n3: int):
#     """
#     Üç sayıyı toplar ve sonucu döndürür.

#     Args:
#         n1 (int): 1. sayı
#         n2 (int): 2. sayı
#         n3 (int): 3. sayı

#     Returns:
#         int: Girilen sayıların toplamı
#     """
#     return n1 + n2 + n3

# Burada ki iş mantığını ister fonksiyon ile yapılsın ister method ile hiç fark etmez. 
# Çünkü burada genel iş tamamlanıyor ve sonucu kullanıcıya gösteriliyor. 
# Lakin bu iş sonucunda buradan elde edilen sonuç başka bir yerde kullanılacak olsaydı,
# burada ki kare hesaplama işinide fonksiyon ile yapılmalıydı.

# def square(number: int):
#     """
#     Verilen sayının karesini hesaplar ve ekrana yazdırır.

#     Args:
#         number (int): Karesi alınacak sayı
#     """
#     print(number ** 2)

# NOT:
# Eğer kare alma sonucu da başka işlemlerde kullanılacak olsaydı, 
# square fonksiyonu da print yerine return etmeliydi.

# Fonksiyonların birlikte kullanımı
# result = sum_numbers(2, 3, 4)   # 2 + 3 + 4 = 9
# square(result)                  # 9 ** 2 = 81
# endregion


# region Digit Frequency Counter
#! Rastgele rakamlardan oluşan bir liste generate ediniz.
#? liste içerisindeki her rakamın kaç kez geçtiğini(geçme sıklılığı) bulan ve 
#? Sonucu aşağıdaki formatta return eden fonksiyonu yazınız
# {
#     1: 10,
#     2: 30,
#     3: 12, ....
# }

# from random import randint
# from collections import Counter


# def number_generator(amount: int, start_point: int, end_point: int) -> list[int]:
#     """
#     Belirtilen aralıkta rastgele rakamlardan oluşan bir liste üretir.

#     Args:
#         amount (int): Üretilecek eleman sayısı
#         start (int): Minimum rakam (varsayılan 0)
#         end (int): Maksimum rakam (varsayılan 9)

#     Returns:
#         list[int]: Rastgele üretilmiş rakam listesi
#     """
#     return [randint(a=start_point, b=end_point) for _ in range(amount)]


# def find_frequency(numbers: list[int]) -> dict[int, int]:
#     """
#     Liste içerisindeki rakamların kaç kez geçtiğini hesaplar.

#     Args:
#         numbers (list[int]): Rakam listesi

#     Returns:
#         dict[int, int]: {rakam: geçme_sayısı}
#     """
    
#     # Path I — Klasik yöntem (if / else)
#     # frequency = {}

#     # for number in numbers:
#     #     if number in frequency.keys():
#     #         frequency[number] += 1
#     #     else:
#     #         frequency[number] = 1

#     # return frequency

#     # Path II — dict.get() 
#     # get(number, 0):
#     #   -> varsa mevcut değeri al
#     #   -> yoksa 0 kabul et
#     # - üzerine +1 ekle

#     # freq_dict = {}

#     # for number in numbers:
#     #     freq_dict[number] = freq_dict.get(number, 0) + 1

#     # return freq_dict

#     # Path III - collections.Counter
#     # Counter iterable içindeki elemanların frekansını otomatik hesaplar
#     return dict(Counter(numbers))

# nbr_generator = number_generator(amount=100, start_point=0, end_point=9)
# result = find_frequency(numbers=nbr_generator)

# print("Üretilen Liste:")
# print(nbr_generator)

# print("\nRakam Frekansları:")
# print(result)
# endregion


# region Create Corporate Mail Address
# todo: Kullanıcıdan tam adını alınız ve kurumsal mail adresi oluşturan bir fonksiyon yazınız.

# def create_mail_address(full_name: str):
#     """
#     Verilen tam addan kurumsal mail adresi üretir.

#     Args:
#         full_name (str): Kullanıcının tam adı

#     Returns:
#         str: Oluşturulan mail adresi
#     """
#     return f"{full_name.lower().split(' ')[0]}.{full_name.lower().split(' ')[-1]}@bilgeadam.com"


# def show_information(mail_address: str):
#     """
#     Oluşturulan mail adresini ekrana yazdırır.

#     Args:
#         mail_address (str): Kurumsal mail adresi
#     """
#     print(f'Your e-mail is {mail_address}')


# result = create_mail_address('burak yılmaz')
# show_information(result)
# endregion


# todo: Sign In ve Sign Up
#! SRP (Single Responsibility Principle) ve SOC (Seperation of Concern)
#* Sign Up işleminde kullanıcının girdiği password valid mi? email valid mi? kontrol edilecek ve bu kurallardan geçerse üyelik işlemi tamamlanacak
#? Sign In yine password ve email login olacak.
# todo: tüm bu problem main() fonksiyonu içinde çalışacak
#! Aşağıda Sample Data Structe 
users = {
    'xyz.xyz@skilledhub.com': 'pwd',
    'qwe.qwe@skilledhub.com': '987'
}

def is_pwd_valid(password: str) -> bool:
    """
    Verilen parolanın temel karakter çeşitliliği kurallarını sağlayıp
    sağlamadığını kontrol eder.

    Bu fonksiyon, paroladaki **benzersiz karakterler** üzerinden (`set(password)`)
    kontroller yapar ve aşağıdaki şartların **tamamı** sağlanıyorsa `True` döndürür:

        - En az 1 adet büyük harf (A-Z)
        - En az 1 adet küçük harf (a-z)
        - En az 1 adet rakam (0-9)
        - En az 1 adet özel karakter (harf ve rakam dışı)

    Uygulama Detayları:
        - Parola `set(password)` ile benzersiz karakterlere indirgenir.
        - Her kural, `any()` kullanılarak ayrı ayrı kontrol edilir.
        - Karakter tekrarları dikkate alınmaz; yalnızca varlık kontrolü yapılır.
        - Boşluk karakteri özel karakter olarak kabul edilir
          (`isalnum()` → False).

    Notlar:
        - Bu fonksiyon yalnızca geçerlilik bilgisi döndürür; hangi kuralın
          başarısız olduğu bilgisi üretilmez (SRP uyumlu).
        - `set()` kullanımı nedeniyle karakter sırası ve tekrar sayısı korunmaz.
        - Çok uzun parolalarda, aynı parola üzerinde birden fazla dolaşım yapılır.

    Args:
        password (str): Kontrol edilecek parola.

    Returns:
        bool:
            - True  → Parola tüm kuralları sağlıyor
            - False → En az bir kural sağlanmıyor

    Time Complexity:
        O(n) — Parola uzunluğu kadar set oluşturma maliyeti +
               her `any()` çağrısı için en kötü durumda ek dolaşım

    Space Complexity:
        O(n) — Benzersiz karakterleri tutmak için set kullanılır

    Example:
        >>> is_pwd_valid("Abc1!")
        True

        >>> is_pwd_valid("abc123")
        False
    """
    ch_set = set(password)

    result = (
        any(ch.isupper() for ch in ch_set) and
        any(ch.islower() for ch in ch_set) and
        any(ch.isdigit() for ch in ch_set) and
        any(not ch.isalnum() for ch in ch_set)
    )

    return result


def is_mail_valid(mail_address: str) -> bool:
    """
    Verilen e-posta adresinin temel geçerlilik ve benzersizlik
    kontrollerini yapar.

   Bu fonksiyon, e-posta adresi için iki ana kontrol uygular:

        1. Format Kontrolü:
            - E-posta adresinin '@' sembolü içerip içermediği kontrol edilir.
            - '@' sembolü yoksa `TypeError` fırlatılır.

        2. Benzersizlik Kontrolü:
            - E-posta adresinin daha önce kayıtlı olup olmadığı kontrol edilir.
            - Eğer adres `users` koleksiyonunda mevcutsa `ValueError` fırlatılır.

    Hata Yönetimi:
        - `TypeError` ve `ValueError` hataları `try/except` bloğu içinde yakalanır.
        - Hata durumunda, exception mesajı **string olarak** ekrana yazdırılır (`print`).
        - Hata durumunda fonksiyon `False` döndürür.
        - Tüm kontroller başarılıysa `True` döndürülür.

    Notlar:
        - Fonksiyon yalnızca geçerli / geçersiz bilgisini döndürür;
          hata detayını çağırana iletmez (SRP uyumlu).
        - E-posta doğrulaması basit seviyededir; regex veya RFC 5322
          uyumlu detaylı bir doğrulama yapılmaz.
        - `users` değişkeninin fonksiyonun çağrıldığı kapsamda
          tanımlı olması beklenir.

    Args:
        mail_address (str): Kontrol edilecek e-posta adresi.

    Returns:
        bool:
            - True  → E-posta adresi geçerli ve kullanılabilir
            - False → Format hatası veya adres zaten kayıtlı

    Example:
        >>> is_mail_valid("user@example.com")
        True

        >>> is_mail_valid("userexample.com")
        The mail address must contain the "@" symbol...!
        False

        >>> is_mail_valid("admin@example.com")
        This email address already has been taken..!
        False
    """
    try:
        if '@' not in mail_address:
            raise TypeError('The mail address must contain the "@" symbol...!')

        if mail_address in users.keys():
            raise ValueError('This email address already has been taken..!')

        return True
    except (TypeError, ValueError) as err:
        print(err)
        return False


def sign_in(mail_address: str, password: str) -> str:
    """
    Kayıtlı bir kullanıcının sisteme giriş (Sign In) işlemini gerçekleştirir.

    Bu fonksiyon, kayıtlı kullanıcıların tutulduğu `users` sözlüğü üzerinde
    dolaşarak verilen e-posta adresi ve parola bilgilerini doğrular.

    Akış:
        1. `users` sözlüğündeki her bir kayıt üzerinde döngüye girilir.
        2. Sözlükteki anahtar (e-posta adresi) ile girilen `mail_address`
           karşılaştırılır.
        3. Eşleşme sağlanırsa, ilgili değerde tutulan parola ile girilen
           `password` karşılaştırılır.
        4. Hem e-posta hem parola eşleşirse:
            - Kullanıcıya özel bir karşılama mesajı döndürülür.
        5. Hiçbir kayıt eşleşmezse:
            - Geçersiz giriş mesajı döndürülür.

    Notlar:
        - Fonksiyon yalnızca metin mesajı döndürür; kullanıcı nesnesi
          veya oturum bilgisi üretmez.
        - Parola doğrulaması düz metin (plain text) üzerinden yapılır.
        - `users` sözlüğünün şu formatta olması beklenir:
              {
                  "user@example.com": "Password123!",
                  ...
              }

    Args:
        mail_address (str): Giriş yapmak isteyen kullanıcının e-posta adresi.
        password (str): Kullanıcının parolası.

    Returns:
        str:
            - "Welcome, <mail_address>..!" → Giriş başarılı
            - "Invalid Credentials..!"      → Giriş başarısız

    Time Complexity:
        O(n) — Kullanıcı sayısı kadar döngü yapılır

    Space Complexity:
        O(1) — Ek veri yapısı kullanılmaz

    Example:
        >>> sign_in("user@example.com", "Abc1!")
        'Welcome, user@example.com..!'

        >>> sign_in("user@example.com", "wrongpass")
        'Invalid Credentials..!'
    """
    for key, values in users.items():
        if key == mail_address and values == password:
            return f'Welcome, {mail_address}..!'
    return 'Invalid Credentials..!'


def sign_up(mail_address: str, password: str) -> str:
    """
    Yeni bir kullanıcı kaydı (Sign Up) işlemini gerçekleştirir.

    Bu fonksiyon, kullanıcı kaydı için gerekli olan doğrulama
    kontrollerini ilgili yardımcı fonksiyonlar aracılığıyla yapar:
        - `is_pwd_valid()` → Parola güvenlik kurallarını kontrol eder
        - `is_mail_valid()` → E-posta adresinin geçerliliğini ve
          kullanılabilirliğini kontrol eder

    Akış:
        1. Verilen parola `is_pwd_valid()` ile doğrulanır.
        2. Verilen e-posta adresi `is_mail_valid()` ile doğrulanır.
        3. Her iki kontrol de başarılıysa:
            - Kullanıcı `users` sözlüğüne eklenir
            - Başarılı kayıt mesajı döndürülür
        4. Herhangi bir kontrol başarısız olursa:
            - Kullanıcı eklenmez
            - Hata mesajı döndürülür

    Notlar:
        - Kullanıcı bilgileri `users` adlı sözlükte saklanır.
        - Parola **düz metin (plain text)** olarak kaydedilir;
        - Fonksiyon yalnızca sonuç mesajı döndürür;
          hata detayları ilgili doğrulama fonksiyonlarında ele alınır.
        - Bu fonksiyon bir *orchestrator* görevi görür ve
          doğrulama mantığını kendi içinde barındırmaz (SRP uyumlu).

    Args:
        mail_address (str): Kayıt edilecek e-posta adresi.
        password (str): Kullanıcının parolası.

    Returns:
        str:
            - "Your membership has been completed..!" → Kayıt başarılı
            - "Invalid credentials..!"               → Doğrulama hatası

    Example:
        >>> sign_up("user@example.com", "Abc1!")
        'Your membership has been completed..!'

        >>> sign_up("userexample.com", "abc")
        'Invalid credentials..!'
    """
    if is_pwd_valid(password=password) and is_mail_valid(mail_address=mail_address):
        users[mail_address] = password
        return 'Your membership has been completed..!'
    else:
        return 'Invalid credentials..!'


def main():
    """
    Uygulamanın ana giriş noktasıdır (CLI – Command Line Interface).

    Bu fonksiyon, kullanıcıdan alınan işlem komutlarına göre
    ilgili kimlik doğrulama akışlarını sürekli olarak çalıştırır.
    Program, kullanıcı tarafından manuel olarak sonlandırılana
    kadar (`Ctrl + C`) çalışmaya devam eder.

    Desteklenen işlemler:
        - "sign in" → Kayıtlı kullanıcı giriş işlemi
        - "sign up" → Yeni kullanıcı kayıt işlemi

    Akış:
        1. Sonsuz bir döngü (`while True`) başlatılır.
        2. Kullanıcıdan bir işlem adı (`process`) alınır.
        3. Girilen değer `match-case` yapısı ile değerlendirilir.
        4. Seçilen işleme göre:
            - Gerekli kullanıcı girdileri (mail, password) alınır
            - İlgili fonksiyon (`sign_in` veya `sign_up`) çağrılır
            - Dönen sonuç ekrana yazdırılır
        5. Tanımlı olmayan bir işlem girilirse:
            - Kullanıcı uyarılır ve döngü devam eder.

    Notlar:
        - Bu fonksiyon yalnızca **kullanıcı etkileşimi ve yönlendirme**
          görevini üstlenir.
        - Doğrulama, kayıt ve giriş mantığı ayrı fonksiyonlara
          devredilmiştir (Separation of Concerns).
        - `match-case` yapısı Python 3.10+ sürümlerinde desteklenir.
        - Döngüden çıkmak için özel bir `exit` veya `quit` komutu
          tanımlanmamıştır; program `Ctrl + C` ile sonlandırılır.
        - Parola girişi düz `input()` ile alınmaktadır; gizli giriş
          (masked input) uygulanmamıştır.

    Returns:
        None

    Example:
        >>> main()
        Type process name: sign up
        Mail Address: user@example.com
        Password: Abc1!
        Your membership has been completed..!
    """
    while True:
        process = input('Type process name: ')

        match process:
            case 'sign in':
                print(
                    sign_in(
                        mail_address=input('Mail Address: '),
                        password=input('Password: ')
                    )
                )
            case 'sign up':
                print(
                    sign_up(
                        mail_address=input('Mail Address: '),
                        password=input('Password: ')
                    )
                )
            case _:
                print('Type a valid process name..!')


main()


# region Login with Captcha (uuid4)
# LOGIN operasyonu:
#   ✔ username kontrolü
#   ✔ password kontrolü
#   ✔ captcha kontrolü

# Captcha üretimi:
#   - uuid4() ile örn: b905e6f7-c3be-4bea-9f82-f9f54fbbd246 üretilir
#   - '-' karakterine göre split edilir
#   - ilk parçanın ilk 4 karakteri captcha olarak kullanılır

# from uuid import uuid4

# users = [
#     {'username': 'beast', 'password': '123'},
#     {'username': 'bear', 'password': '987'},
#     {'username': 'savage', 'password': '345'},
# ]


# def generated_captcha() -> str:
#     """
#     Bu fonksiyon bize captcha üretir.
#     :return: string ifade döner.
#     """
#     created_captcha = str(uuid4())   # uuid4() fonksiyonu UUID tipinde bir obje döndürmektedir.
    # dönen ifade incelendiğinde '-' sembollerinden kolaylıkla split edilerek istenilen bir parçasının alınabileceği görülmektedir. 
    # Ama burada şöyle bir problem vardır. split() fonksiyonu sadece string ifadelere uygulanabilmektedir. 
    # Bu sebepten ötürü burada uuid4() fonksiyonun bize döndürdüğü değeri str() fonksiyonu aracılığıyla string tipine dönüştürülür.

#     splited_captcha_list = created_captcha.split('-')  # Yukarıda ki satırda izah ettiğimiz gibi artık 'created_captcha' string tipinde olduğuna göre ona split fonksiyonu uygulanabilinir. 
    # '-' sembolünden split edilir. split() fonksiyonu bize bir liste döndüğünden artık istediğimiz index'te tutulan value erişerek onu kullanabiliriz.

#     return splited_captcha_list[0]  # arzu ettiğimiz değer 1 index'te olması nedeniyle burada bu değeri kendimize return ettik.
#     # return str(uuid4()).split('-')[1]


# def login(user_name: str, password: str, user_captcha: str, constant_capth: str):
#     """
#     Kullanıcı adı, şifre ve captcha kontrolü yapar.

#     Returns:
#         bool: login başarılıysa True, değilse False
#     """
#    for user in users:
#         if user.get('username') == user_name and user.get('password') == password and user_captcha == constant_capth:
#             print('Welcome..!')
#             break
#     else:
#         print('check information..!')


# def main():
#     captch = generated_captcha()
#     print(f'Captcha: {captch}')

#     login(
#         input('User Name: '),
#         input('Password: '),
#         input('Captcha: '),
#         captch    # yukarıda ürettiğmiz captch'yı methodumuza gönderiyoruz ki 
        # diğer satırda kullanıcının girdiği bilgi ile üretilen bilgiyi login methodu içerisinde mukayese edelim.
#     )


# main()
# endregion