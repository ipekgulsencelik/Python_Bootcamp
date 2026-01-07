
#! File I/O
# Dosya açma, dosyaya veri yazma, dosyadan veri okuma gibi işlemler File I/O kapsamında değerlendirilir.

# Dosya oluşturmak ve kullanmak için open() fonksiyonu kullanılır

# File Create & Initial Write (Write Mode - "w")
# Amaç:
# - Dosya yoksa oluşturmak
# - Dosya varsa içeriğini TAMAMEN silip yeniden yazmak

# ⚠️ UYARI:
# "w" modu geri dönüşü olmayan veri kaybına yol açabilir.

# file = open(file='new_file.txt',
#             mode='w',
#             encoding="utf-8')
# yukarıda open() fonksiyonuna 3 adet değer gönderdik. SIrasıyla;
# 1. parametre oluşturulacak dosyanın adını ve uzantısını içerir
# 2. parametre oluşturulacak dosyanın ne amaçla kullanıldığını belirtir 
#   - biz burada 'w' kullandık. bu ne anlama geliyor, dosya içerisine bir şeyler yazacağız.
# 3. parametre oluşturulan dosyaya türkçe karakter desteği verdik.

# Uyarı:  Yaratılacak dosyaya herhangi bir lokasyon bilgisi vermediğimiz için default olarak projenin bulunduğu dizinde yaratılacak
# Uyarı: Şayet ilgili isimde bir dosya varsa aynı dosyadan bir daha yaratmaz var olan dasyanın içerisinde bulunan bilgileri uçurur ve son gelen bilgileri ekler.

# file.write('Burak Yılmaz\nSoftware Developer')
# file.close()


# region File Create & Initial Write (Write Mode)
# Dosya oluşturma & ilk veri yazma
# try:
#     # Dosyayı write modunda aç (varsa içeriği siler)
#     file = open(file='new_file.txt', mode="w", encoding="utf-8")

#     # Dosyaya ilk verileri yaz
#     file.write(
#         "Full Name: Burak Yılmaz\n"
#         "Occupation: Software Developer\n"
#     )

#     # Dosyayı manuel olarak kapat
#     file.close()

# except PermissionError as err:
#     # Dosyaya yazma izni yoksa
#     print(f"Permission error: {err}")
# except FileNotFoundError as err:
#     # Genelde yanlış path / klasör yoksa olur
#     print(f"File/Path error: {err}")
# endregion


# File Append (Append Mode - "a")
# Amaç:
# - Var olan dosyanın SONUNA veri eklemek
# - Mevcut içeriği KORUMAK

# Not:
# - Dosya yoksa otomatik oluşturulur
# - FileExistsError pratikte oluşmaz (x moduna özgüdür)

# a (Append): var olan dosyamız içerisine yeni bilgileri var olan bilgileri kaybetmeden üzerine yazmak için kullanıyoruz.
# file = open(file='new_file.txt',
#             mode='a',
#             encoding='utf8')
# file.write('\nProgramming Skills: (Python, C#)')
# file.close()

# region File Append with with Exception Handling
# Dosyaya yeni bilgi ekleme (append)
# try:
#     # Dosyayı append modunda aç
#     file = open(file='new_file.txt', mode="a", encoding="utf-8")

#     # Dosyanın sonuna yeni bilgiler ekle
#     file.write(
#         "Full Name: İpek Yılmaz\n"
#         "Occupation: Art Historian\n"
#     )

#     # Dosyayı manuel olarak kapat
#     file.close()

# except PermissionError as err:
#     # Dosyaya yazma izni yoksa
#     print(f"Permission error: {err}")
# endregion


# File Read (Read Mode - "r")
# Amaç:
# - Dosyanın tüm satırlarını liste olarak almak
# - Her satır ayrı bir string olarak gelir

# try:
#     file_name = input('type the name of the file you want to read: ')
#     file = open(file=file_name, mode='r', encoding='utf-8')
#     print(file)
# except FileNotFoundError as err:
#     print(f'File does not found..!\n{err}')
# finally:
#     file.close()

# file = open(file='new_file.txt',
#             mode='r',
#             encoding='utf-8')
# texts = file.readlines()
# print(texts)

# Not:
# file.read()        ->     tüm dosyayı tek string olarak okur
# file.readline()    ->     tek satır okur
# file.readlines()   ->     tüm satırları liste olarak döndürür


# region File Read with Exception Handling
# Dosyadan veri okuma
# try:
#     # Dosyayı okuma modunda aç
#     file = open(file='new_file.txt', mode="r", encoding="utf-8")

#     # Dosyadaki tüm satırları oku
#     for line in file.readlines():   # -> list[str]
#         # Satır sonu karakterlerini temizleyerek yazdır
#         # strip(): \n gibi satır sonlarını temizler
#         print(line.strip())

#     # Dosyayı manuel olarak kapat
#     file.close()

# except FileNotFoundError:
#     print("File not found.")
# endregion


# region File Append with Context Manager
# Amaç:
# - Dosyayı append modunda açmak
# - Otomatik close() sağlamak

# ✅ EN GÜVENLİ YÖNTEM
# - Hata olsa bile dosya kapanır
# - finally gerekmez

# with open(file='new_file.txt', mode='a', encoding='utf-8') as file:
#     # Dosyanın SONUNA veri ekler (append)
#     file.write(
#         "Full Name: Hakan Yılmaz\n"
#         "Occupation: Chemist\n"
#     )
# # endregion

# Dosya açma, açılan dosya içerisine data kayıt etme, vakti gelince dosyadan okuma vb. işlemler yapmak için kullanılan bir modüldür.