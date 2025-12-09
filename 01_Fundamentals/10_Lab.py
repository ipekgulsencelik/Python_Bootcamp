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