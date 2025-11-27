
# region List Comprehensions
# List Comprehension, uzun döngüler yazmadan hızlıca liste üretmenin en Pythonic yoludur.
# Daha Pythonic - daha hızlı - daha temiz kod sağlar.

# ⭐ Neden Önemli?
# Daha kısa kod
# Daha az hata
# Çok daha hızlı çalışır
# Bir listeyi başka listeye dönüştürme (transform) için birebirdir  
# Filtreleme → Koşul ekleme yapabilirsin  
# Veri üretme, parsing, API verisi işleme için çok uygundur  
# Okunabilirliği artırır

# 📌 TEMEL YAPI:
#     [ yeni_deger for eleman in liste if kosul ]

# Normal yöntem:
squares = []
for i in range(1, 6):
    squares.append(i * i)

# List comprehension ile:
squares_lc = [i * i for i in range(1, 6)]
print("Squares:", squares_lc)   # [1, 4, 9, 16, 25]

# Koşullu kullanım:
even_numbers = [n for n in range(1, 20) if n % 2 == 0]
print("Even numbers:", even_numbers)
# endregion


# region lambda function
# İsimsiz, tek satırlık fonksiyon yazma yöntemidir.
# Fonksiyon tanımı yazmadan hızlı işlem yapar.

# ⭐ Neden Önemli?
# map(), filter(), sorted() gibi fonksiyonlarda çok kullanılır  
# Gereksiz fonksiyon tanımlamayı ortadan kaldırır  
# Kodun temiz görünmesini sağlar  
# Inline (satır içi) kullanım için idealdir  
# Matematiksel işlemlerde pratiklik sağlar

square = lambda x: x * x
print(square(5))   # 25

sum_two = lambda a, b: a + b
print(sum_two(3, 7))  # 10

# Sıralama için lambda kullanımı:
students = [('Ali', 50), ('Ayşe', 80), ('Mehmet', 60)]
students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)

add_text = lambda t: t.upper() + "!"
print(add_text("hello"))
# endregion


# region zip()
# Birden fazla listeyi eleman eleman birleştirir.
# Çoklu veriyi tek yapıda tutmak için mükemmeldir.

# ⭐ Neden Önemli?
# İsim + yaş + şehir gibi çoklu veri eşlemelerinde muazzamdır
# Birden fazla listeyi sütun gibi birleştirir  
# Excel tablosu mantığıyla çalışır  
# Tablolama, raporlama için çok kullanılır  
# Çok satırlı veriyle uğraşırken veri eşleştirme sağlar  

names = ['Ali', 'Veli', 'Ayşe']
scores = [90, 80, 100]

combined = list(zip(names, scores))
print(combined)
# [('Ali', 90), ('Veli', 80), ('Ayşe', 100)]
# endregion


# region map()
# Listedeki her elemana bir fonksiyon uygular.
# Veri dönüştürme, matematiksel işlem gibi alanlarda çok güçlüdür.

# ⭐ Neden Önemli?
# Veri dönüştürme için MÜTHİŞTİR  
# API’den gelen veriyi temizlemede kullanılır  
# String → int → float dönüşümünde çok kullanılır  
# Matematiksel işlemleri toplu yapar

# Formül:
#     map(fonksiyon, liste)

numbers = [1, 2, 3, 4, 5]

# Her elemanın karesini al
results = list(map(lambda x: x * x, numbers))
print(results)   # [1, 4, 9, 16, 25]

# int dönüşümü örneği
str_nums = ['1', '2', '3']
int_nums = list(map(int, str_nums))
print(int_nums)
# endregion


# region filter()
# Belirli koşulu sağlayan elemanları döndürür.
# Arama, filtreleme, validasyon gibi işlemler için idealdir.

# ⭐ Neden Önemli?
# Veri filtreleri
# Fiyat filtreleme
# Kullanıcı doğrulama
# Temiz veri oluşturma
# Hatalı veriyi ayırmak 
# Büyük veride performansı iyidir  
# Koşul bazlı veri çekme sağlar  

# Formül:
#     filter(kosul_fonksiyonu, liste)

numbers = [10, 15, 20, 25, 30]

# 20’den küçük olanlar
filtered = list(filter(lambda x: x < 20, numbers))
print(filtered)  # [10, 15]

# sadece çiftler
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
# endregion


# region any()
# Liste içinde en az bir True varsa True döner.
# Genellikle veri kontrolü ve validasyon için kullanılır.

# ⭐ Nerede Kullanılır?
# Şifre doğrulama
# Kullanıcı giriş validasyonu
# Form kontrolü
# Veri kontrolü 
# En az bir şartın sağlanıp sağlanmadığını kontrol eder    
# Çoklu koşulları kontrol etmek için idealdir

values = [False, 0, '', 3 > 1]
print(any(values))  # True  (çünkü 3 > 1 → True)

nums = [n > 10 for n in [2, 5, 12, 3]]
print(any(nums))   # True (12 > 10)
# endregion


# region set
# Tekrar eden elemanları otomatik temizleyen koleksiyondur.
# Kesişim, birleşim, fark gibi matematiksel işlemleri destekler.

# ⭐ Neden Önemli?
# Tekrarlı veriyi temizlemek
# Kesişim, birleşim yapmak
# Performanslı arama 
# Listeden çok daha hızlıdır  

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)   # {1, 2, 3, 4, 5}

# set ile kesişim, birleşim:
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Birleşim → {1,2,3,4,5}
print(a & b)  # Kesişim → {3}
print(a - b)  # Fark → {1,2}
# endregion


#! Tuple (Demetler)
# List objesi ile benzer bir mantığa sahiptir. 
# Lakin listlere uyguladığımız built-in fonksiyonları içermezler.
# Index mantıkları ortaktır.
# Hem listeler hemde tuple'lar dilimleme (slicing) işlemi yapılabilinir.
# Demetler, list objesi gibi RAM'de tutulmaktadırlar. Yani uygulama run time'da iken üzerine ekeldiğimiz değerler, uygulama sonlandırıldığında uçar gidirler.

# Listelere benzer ama değiştirilemez (immutable) yapılardır.

# ⭐ Neden Önemli?
# Sabit veri tutmada
# Koordinat, konum, renk gibi sabitlerde 
# Hızlı çalışır

tuple_1 = ('Beşiktaş', 'Galatasaray', 'Adana Demir Spor', 'Trabzon Spor', 'Fenerbahçe')
tuple_2 = (12, 34.5, 'b', 'Eagels', 'Red Skins', 'Patriot', 'Seahwak')

tuple_3 = tuple_1 + tuple_2
print(tuple_3)

# Dilimleme
print(tuple_3[0:3])  # output => ('Beşiktaş', 'Galatasaray', 'Adana Demir Spor')
print(tuple_3[3:5])  # output => ('Trabzon Spor', 'Fenerbahçe')
print(tuple_3[::2])  # output => ('Beşiktaş', 'Adana Demir Spor', 'Fenerbahçe', 34.5, 'Eagels', 'Patriot')
print(tuple_3[-1])  # output => 'Seahwak'
print(tuple_3[:5])  # ('Beşiktaş', 'Galatasaray', 'Adana Demir Spor', 'Trabzon Spor', 'Fenerbahçe')
print(tuple_3[::-1])  # ('Seahwak', 'Patriot', 'Red Skins', 'Eagels', 'b', 34.5, 12, 'Fenerbahçe', 'Trabzon Spor', 'Adana Demir Spor', 'Galatasaray', 'Beşiktaş')
print(tuple_3[::-2])  # ('Seahwak', 'Red Skins', 'b', 12, 'Trabzon Spor', 'Galatasaray')
print(tuple_3[3::2])  # ('Trabzon Spor', 12, 'b', 'Red Skins', 'Seahwak')


tuple_4 = ('Sariyer', ('Erenköy', 'Suadiye'), ('Yeniköy', 'Bebek', ('Ulus', 'Etiler')))
print(tuple_4[0])  # Sariyer
print(tuple_4[1][1])  # Suadiye
print(tuple_4[2][2][0])  # Ulus

my_family = [
    ('Burak Yılmaz', 34, 'beast'),
    ('Hakan Yılmaz', 37, 'bear'),
    ('İpek Yılmaz', 39, 'keko')
]

for x, y, z in my_family:
    print(f'Full Name: {x}\nAge: {y}\nUser Name: {z}')