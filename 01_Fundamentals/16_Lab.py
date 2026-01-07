
#! *args vs **kwargs

#? Method yada fonksiyonların SINIRSIZ sayıda parametre almasını nasıl temin ederiz?
# *args (positional) :
#   - Belirsiz sayıda parametre almak için kullanılır
#   - Fonksiyon içinde TUPLE olarak gelir
#   - Parametreler sıralıdır (index ile erişilebilir)

# Not:
#   "args" bir anahtar kelime değildir, bir isimlendirmedir.
#   Best practice olduğu için genelde *args kullanılır.
#   (*params, *numbers vb. da yazılabilir ama önerilmez)

# region Unlimited Parameters with *args
#todo: Kullanıcının isteğine bağlı olarak girdiği değerlerin toplamını alan bir fonksiyon yazınız.
# def sum_all(*args):  # args anahtar sözcüğü yerine params, keywords vb ifadelerde kullanılabilinir.
#     """
#     Kullanıcıdan gelen belirsiz sayıda değeri toplar.

#     Args:
#         *args (int): İstendiği kadar tam sayı

#     Returns:
#         int: Girilen sayıların toplamı
#     """
#     toplam = 0

#     for i in args:
#         toplam += i

#     return toplam


# Kullanıcı istediği kadar parametre gönderebilir
# print(sum_all(1, 2, 3))   # 6
# print(sum_all(9, 8, 12, 45, 23))  # 97
# print(sum_all(56, 12, 2, 35, 40, 55, 6, 77, 89, 9))
# print(sum_all())  # 0
# endregion


# region Find Prime Numbers with *args
#todo: Kullanıcıdaına alınan sayıların sırasıyla asal olanlarını saptayarak bir liste halinde döndüren fonksiyon yazınız.
# def find_prime_numbers(*args: int):
#     """
#     Girilen sayılar arasından asal olanları liste olarak döndürür.

#     Args:
#         *args (int): İstenilen kadar sayı

#     Returns:
#         list[int]: Asal sayı listesi
#     """
#     prime_numbers = []  # kullanıcıdan gelen sayılar içerisinden asal olanlar yakalandıkça burada ki listede depolanacak.
#     is_prime = True

#     for argument in args:  # args'nin buradaki tipi tuple'dir. bu tuple'ın birinci elemanı da listedir. yani bu adımda argument tipi listedir.
#         for arg in argument:  # iç döngüde ise artık gönderilen listenin elemanları içerisinde dolaşıyorum.
#             if arg > 1:
#                 for bolen in range(2, arg):  # burada range fonksiyonu ile 2'den başlayarak arg üzerinde anlık olarak tutulan değere göre bir liste hazırlıyorum. burada ki mantık sayının asal olma durumunu kontorl etmek için var. yani 2'den başlayarak sayının kendisine kadar bölenler oluşturup sayının kendisine bölüyoruz ki asal olup olmadığını anlayalım.
#                     if arg % bolen == 0:
#                         is_prime = False  # range() fonksiyonunda bir noktaya dikkat ediniz. range hep 2'den başlayacaktır. zaten bir sayı 2'ye tam bölünüyorsa asal değeldir. bu yüzden direk break edip bir sonraki bölene geçiyoruz.
#                         break
#                     else:
#                         is_prime = True

#                 if is_prime:
#                     prime_numbers.append(arg)

#     return prime_numbers


# values = []

# while True:
#     process = input("Enter a number (press 'e' to exit): ").strip().lower()
#     if process == 'e':
#         break
#     else:
#         value = int(process)
#         values.append(value)

# Aşağıda fonksiyonumuza bir liste halinde parametreleri gönderiyoruz. 
# '*args' anahtar sözcüğü tuple olarak karşııyordu biz şuan liste gönderdik. 
# Bu yüzden methodun içerisinde nested for loop kurduk.
# print(find_prime_numbers(values))
# endregion


# region Concatenation String
# def concat_str(*args, separator: str = " "):
#     """
#      Gelen tüm değerleri string'e çevirip ayraç ile birleştirir.

#     Args:
#         *args (str): Birleştirilecek kelimeler
#         separator (str): Ayırıcı karakter (keyword-only)

#     Returns:
#         str: Birleşmiş string
#     """
#     return separator.join(args)

# print(concat_str("burak", "yilmaz", "36"))
# print(concat_str("bugün", "sınıf", "mevcudu", "çok", "az"))
# print(concat_str("burak", "yilmaz", "36", separator="-"))
# endregion


# region *args - log system

# from datetime import datetime

# def sys_log(*args):
#     """
#     Sistem loglarını ekrana basar.

#     Args:
#         *args (str): Log mesajları
#     """
#     for msg in args:
#         print(f'System Log: {msg}\nLog Date: {datetime.now()}')


# sys_log("Status Code --> 200", "DB Connection has been lost", "Passive")
# endregion


# **kwargs:
#   - Anahtar = değer (key=value) şeklinde parametre alır
#   - Dictionary olarak gelir

# region **kwargs - Get User Information
# def get_info(**kwargs):
#     """
#     Kullanıcı bilgilerini keyword arguments ile alır.

#     Args:
#         **kwargs:
#             full_name (str): Kullanıcının tam adı
#             occupation (str): Mesleği
#             alias (str): Takma adı

#     Returns:
#         str: Formatlanmış bilgi metni
#     """
#     return (
#         f'Full Name: {kwargs.get("full_name")}\n'
#         f'Occupation: {kwargs.get("occupation")}\n'
#         f'Alias: {kwargs.get("alias")}'
#     )


# print(get_info(full_name="Burak Yılmaz"))
# print(get_info(full_name="Hakan Yılmaz", occupation="Chemist"))
# print(get_info(full_name="İpek Yılmaz", occupation="Art Historian", alias="keko"))
# endregion


# region **kwargs - Log Formatting
# from socket import gethostname, gethostbyname
# from datetime import datetime


# def log(**kwargs) -> str:
#     """
#     Sistem log bilgilerini keyword arguments ile formatlar.

#     Args:
#         **kwargs:
#             msg (str): Log mesajı
#             ip_address (str): IP adresi
#             machine_name (str): Makine adı
#             exception_date (datetime): Hata zamanı

#     Returns:
#         str: Formatlanmış log çıktısı
#     """
#     message = kwargs.get("msg", "No message")
#     ip_address = kwargs.get("ip_address", "0.0.0.0")
#     machine_name = kwargs.get("machine_name", "unknown")
#     exception_date = kwargs.get("exception_date", datetime.now())

#     return (
#         f"Message        : {message}\n"
#         f"IP Address     : {ip_address}\n"
#         f"Machine Name   : {machine_name}\n"
#         f"Exception Date : {exception_date}"
#     )


# print(
#     log(
#         msg="Internal Gateway Error",
#         ip_address=gethostbyname(gethostname()),
#         machine_name=gethostname(),
#         exception_date=datetime.now()
#     )
# )
# # endregion


# ------------------------------------------------------------
# *args vs **kwargs
# ------------------------------------------------------------
# *args   → tuple   → sıralı değerler
# **kwargs → dict   → anahtarlı değerler
# ------------------------------------------------------------

# region *args + **kwargs - LOG
# from socket import gethostname, gethostbyname
# from datetime import datetime


# def log(*args, **kwargs) -> str:
#     """
#     *args    -> sınırsız sayıda LOG mesajı alır (positional)
#     **kwargs -> log'a ait metadata alır (ip, machine, date vs.)

#     Neden bu yapı?
#     - Mesajlar bazen birden fazla olur (ör: "DB Lost", "Retrying", "Timeout")
#     - Metadata bazen gönderilir bazen gönderilmez (ip, machine, exception_date)
#     - Bu yüzden default değerlerle güvenli şekilde çalışır.

#     Mantık:
#         1) args içindeki mesajları bir blok halinde birleştir
#         2) kwargs içinden metadata çek
#         3) kwargs'ta fazla alan kaldıysa 'Extras' olarak bas (debug)

#     Args:
#         *args: Log mesajları (sıralı değerler). Tuple olarak gelir.
#         **kwargs: Log metadata bilgileri (dict olarak gelir).

#     Returns:
#         str: Formatlanmış log çıktısı
#     """

#     # 1️⃣ *args -> mesajları birleştir
#     # args tuple gelir. İçinde str/int/bool olabilir.
#     # join sadece string kabul ettiği için map(str, args) ile tüm elemanları string'e çevirilir.
#     # args boşsa (log() gibi çağrılırsa), "No message" basıyoruz.
#     message_block = " || ".join(map(str, args)) if args else "No message"

#     # 2️⃣ **kwargs -> metadata
#     # kwargs dict gelir. Key yoksa patlamasın diye get() + default kullanıyoruz.
#     ip_address = kwargs.get("ip_address", "0.0.0.0")
#     machine_name = kwargs.get("machine_name", "unknown")
#     exception_date = kwargs.get("exception_date", datetime.now())

#     return (
#         f"Message        : {message_block}\n"
#         f"IP Address     : {ip_address}\n"
#         f"Machine Name   : {machine_name}\n"
#         f"Exception Date : {exception_date}"
#     )

# Örnek 1: Sadece mesajlar (metadata yok)
# print("---- EXAMPLE 1 ----")
# print(log("Internal Gateway Error", "Retrying...", 503))
# print()

# Örnek 2: Mesaj + metadata
# print(
#     log(
#         "Internal Gateway Error",
#         "DB Connection Lost",
#         "Retrying...",
#         ip_address=gethostbyname(gethostname()),
#         machine_name=gethostname(),
#         exception_date=datetime.now()
#     )
# )
# print()

# Örnek 3: Hiç mesaj yok -> default "No message"
# print("---- EXAMPLE 3 ----")
# print(log(ip_address="127.0.0.1"))
# endregion


# region complex_function — *args + keyword-only + **kwargs
def complex_function(a, b, *args, name="Varsayılan", **kwargs):
    """
    Karma (complex) parametre yapısına sahip fonksiyon örneği.

    Bu fonksiyon; sabit (zorunlu) parametreler, sınırsız sayıda
    positional parametre (*args), keyword-only parametre ve
    sınırsız keyword parametreleri (**kwargs) birlikte kullanır.

    PARAMETRE SIRASI (ÇOK ÖNEMLİ):
        1️⃣ Zorunlu parametreler       -> a, b
        2️⃣ *args (positional)        -> sınırsız, tuple
        3️⃣ keyword-only parametreler -> name
        4️⃣ **kwargs (keyword)        -> sınırsız, dict

    Args:
        a (int):
            Fonksiyonun ilk zorunlu parametresi.
            Positional veya keyword olarak verilebilir.

        b (int):
            Fonksiyonun ikinci zorunlu parametresi.
            Positional veya keyword olarak verilebilir.

        *args (tuple):
            a ve b'den sonra gelen ekstra positional değerler.
            Tuple tipindedir ve sıralıdır.

        name (str):
            Keyword-only parametredir.
            *args'ten sonra geldiği için positional olarak VERİLEMEZ.
            Default değeri "Varsayılan"dır.

        **kwargs (dict):
            name dışında gönderilen tüm keyword parametreleri toplar.
            Key = value şeklindedir.

    Returns:
        None
    """

    # ZORUNLU PARAMETRELER (a, b)
    print(f"Sabitler (a, b): {a}, {b}")

    # *args -> Tuple (sınırsız positional parametre)
    # Örnek çağrı: complex_function(1, 2, 3, 4, 5)
    # Bu durumda: args == (3, 4, 5)
    print(f"Args (Tuple): {args}")

    # keyword-only parametre (name)
    # *args'ten sonra tanımlandığı için name mutlaka key=value şeklinde verilmelidir.
    print(f"İsim (name): {name}")

    # **kwargs -> Dict (sınırsız keyword parametre)
    # name haricinde gönderilen tüm keyword'ler burada toplanır.    #
    # Örnek: city="Istanbul", age=25    #
    # kwargs == {"city": "Istanbul", "age": 25}
    print(f"Kwargs (Dict): {kwargs}")


complex_function(
    1,                      # a
    2,                      # b
    3, 4, 5,                # *args
    name="Python",          # keyword-only
    city="Istanbul",        # **kwargs
    age=25                  # **kwargs
)
# endregion


# region Argument Unpacking (Liste ve Sözlük Açma)
def my_sum(a, b, c):
    """
    Üç adet parametre alan basit bir toplama fonksiyonu.

    Amaç:
        - Argument Unpacking kavramını göstermek
        - * (list/tuple unpacking) ve ** (dict unpacking) farkını netleştirmek

    Args:
        a (int): 1. sayı
        b (int): 2. sayı
        c (int): 3. sayı

    Returns:
        int: a + b + c
    """
    return a + b + c


# 1️⃣ SENARYO: LIST / TUPLE UNPACKING  (* operatörü)
# * operatörü, iterable (list, tuple, set) içindeki elemanları sırasıyla (positional) fonksiyon parametrelerine dağıtır.

my_list = [10, 20, 30]  # my_sum(10, 20, 30)

# ÖNEMLİ:
# - Eleman sayısı, parametre sayısıyla birebir aynı olmalı
# - Fazla veya eksik eleman -> TypeError
print(f"Liste Açma Sonucu: {my_sum(*my_list)}")


# 2️⃣ SENARYO: DICTIONARY UNPACKING  (** operatörü)
# ** operatörü, sözlükteki key=value çiftlerini keyword argument olarak fonksiyona dağıtır.

my_dict = {
    "a": 5,
    "b": 15,
    "c": 25
}   # my_sum(a=5, b=15, c=25)

# KRİTİK KURAL:
# - Dictionary key'leri, fonksiyon parametre isimleriyle birebir aynı olmak ZORUNDADIR.
# - Aksi halde TypeError oluşur.
print(f"Sözlük Açma Sonucu: {my_sum(**my_dict)}")
# endregion


# region ÖZET
"""
*  (Unpacking)
    - List / Tuple / Iterable açar
    - Positional parametrelere gider
    - SIRAYA göre çalışır

** (Unpacking)
    - Dictionary açar
    - Keyword parametrelere gider
    - İSİM eşleşmesi zorunludur

Ne zaman kullanılır?
    - Fonksiyon parametrelerini dinamik bir yapıdan almak
    - API response / config dict'lerini direkt fonksiyona vermek
    - *args / **kwargs ile birlikte esnek fonksiyonlar yazmak
"""
# endregion


# ------------------------------------------------------------
# KISA ÖZET
# ------------------------------------------------------------
# def           → fonksiyon tanımlar
# return        → değer döndürür
# print         → ekrana yazar
# *args         → sınırsız sıralı parametre (tuple)
# **kwargs      → anahtar-değer parametreleri (dict)
# decorator     → fonksiyona ek davranış kazandırır
# ------------------------------------------------------------