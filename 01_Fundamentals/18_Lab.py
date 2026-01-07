
# Bu çalışmada, bir uygulamada alınan hataların not defterine kayıt edilmesi yapılacaktır.
# Log => Yani yazılım terminolojisinde ki "log" olarak ifade edilen işlem uygulanacaktır. 
# 'log' türkçeye çevrildiğinde günlük anlamına gelmektedir. 
# 'log' çok önemli ve hayat kurtacak bir mekanizmadır. 
# Örneğin, uygulamada kim ne yapmış, ne zaman ne yaratmış, ne görüntülemiş, ne silmiş, 
# yani uygulamada kim ne nane yemiş ise bunları not altına aldığımız yapıya 'log'.

# Log => Yazılımda olan biteni kayıt altına alma işidir.
# Hangi hata oldu, nerede oldu, ne zaman oldu, hangi bilgisayarda oldu gibi bilgiler log'a yazılır.

# Bu çalışmada alınan hataları basit bir kriptografi algoritması ile kriptolayarak saklayacacağız.
# Ayrıca python'ın çok kuvvetli bir modülü olan socket modülünden faydalanacağız. 

# Neden socket modülünü kullanacağız? 
# Çünkü hatanın alındığı pc'nin adını ve ip address'de log içerisinde kullanacağız.

# Bu çalışmada:
# - Email kontrolü yapılacak
# - Email geçersiz ise ValueError fırlatılacak
# - Bu hata AES(EAX) ile şifrelenerek log.txt dosyasına yazılacak
# - Ayrıca hatanın alındığı pc adı ve ip adresi de log'a eklenecek

from socket import gethostname, gethostbyname       # PC adı ve IP adresi almak için
from datetime import datetime                       # Hata zamanını log’a eklemek için
from Crypto.Cipher import AES                       # AES şifreleme için
from Crypto.Random import get_random_bytes          # Random AES key üretmek için


# region Logger Function
def sys_log(**kwargs) -> str:
    """
    Email kontrolü yapar.
    Email geçersiz ise hatayı AES ile şifreleyip log'a yazar.

    Beklenen kwargs:
        file            : log dosyası yolu (str)
        machine_name    : pc adı (str)
        ip_address      : ip adresi (str)
        exception_date  : datetime veya string
        email_address   : kontrol edilecek email (str)

        Returns:
        str:
            - Email valid ise başarı mesajı
            - Email invalid ise ValueError mesajı
    """

    # kwargs.get(key, default) => key yoksa default döndürür.
    # sistem bilgilerini kwargs’tan alıyoruz.
    machine_name = kwargs.get("machine_name", "unknown-machine")    # PC adı
    ip_address = kwargs.get("ip_address", "unknown-ip")             # IP adresi
    error_date = kwargs.get("exception_date", datetime.now())       # Hata zamanı

    try:
        # a+ ile dosya yoksa oluşturulur
        with open(file=kwargs.get('file'), mode="a+", encoding="utf-8") as file:
            file.seek(0)                      # okuma imleci başa
            first_bytes = file.read(80)       # dosyanın başından azıcık oku
            if "Application Exception Logs" not in first_bytes:
                file.write("Application Exception Logs\n")
                file.write("=" * 60 + "\n")
        try:
            if "@" not in kwargs.get('email_address'):
                raise ValueError('Invalid email address..!')
            
            return 'Your email address is valid..!'
        except ValueError as error:
            # AES için 16 byte (128-bit) random key üretiyoruz
            aes_key = get_random_bytes(16)

            # AES(EAX) cipher objesi oluşturuyoruz
            aes_obj = AES.new(key=aes_key, mode=AES.MODE_EAX)

            # ⚠️ DİKKAT:
            # Burada gerçek hatayı (error mesajını) şifrelemek yerine
            # sabit bir metin şifreleniyor: b'valueerrorhappen'
            # Yani logda gerçek hata yazmayacak.
            chipper_text = aes_obj.encrypt(b'valueerrorhappen')

            with open(file=kwargs.get('file'), mode='a', encoding='utf-8') as file:
                # Şifreli metni stringe çevirip yazıyoruz
                file.write(str(chipper_text))
                file.write(" || ")
                file.write(f'Machine Name: {machine_name}')
                file.write(" || ")
                file.write(f'Ip Address: {ip_address}')
                file.write(" || ")
                file.write(f'Error Date: {error_date}')
                file.write(" || ")
            
            return str(error)
    except IOError as error:
        print(f'{error.__doc__}')
# endregion


# region Test / Run
print(
    sys_log(
        file='log.txt',                                # log dosyası adı
        machine_name=gethostname(),                    # bilgisayar adı (pc name)
        ip_address=gethostbyname(gethostname()),       # pc name -> ip resolve
        exception_date=datetime.now(),                 # hata zamanı
        email_address='qwe.qwezxc.com'                 # '@' yok => invalid
    )
)
# endregion