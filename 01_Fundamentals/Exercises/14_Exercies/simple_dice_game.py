
#! Basit Barbut Oyunu
# first person login olucak. karşısına bir bot atanacak. yani bir isim listesi oluşturalım içinden randam isim getirelim.
# makina her oyuncu için otomatik olarak zar atıcak.
# büyük atan kazanacak

# from random import randint, choice
#
# bot_list = ['Anna', 'Hüseyin', 'Tomas']
# users = [
#     {'username': 'beast', 'password': '123', 'safe': 1000},
#     {'username': 'bear', 'password': '987', 'safe': 1000},
#     {'username': 'savage', 'password': '345', 'safe': 1000},
# ]
#
#
# def get_bot_player():
#     return choice(bot_list)
#
#
# def roll_dicle():
#     return randint(1, 6) + randint(1, 6)
#
#
# def generate_daily_chip():
#     return randint(100, 1001)
#
#
# def login(user_name: str, password: str):
#     # Burada users lisemiz içerisinde user user dolaşıyoruz. her bir user'ın tipi sözlüktür.  Bu bağlamda her bir user'ı döngüye itarate ediyoruz. user dict tipinde olduğundan sadece sözlüklere uygulana bilen get() fonksiyonu aracılığıyla username ve password anahtarlarında tutulan value'lara erişerek kullanıcıdan gelen ve parametrelerle karşıaldığımız değerler eşit ise ilgili adımda ki user'ı return ediyoruz ki onu uygulamanın diğer safhalarında kullanabilelim.
#     for user in users:
#         if user.get('username') == user_name and user.get('password') == password:
#             return user  # burda user objesini kendimize döndürdük ki uygulamanın geri kalan safhasında bu kullanıcıdan faydalana bilelim. Örneğin kullanıcı yani user bahis yapıcak para kazanıcak yada kayıp edecek böylece devamlı safe anahtarına erişerek durumlara göre para eklenilecek yada silinecek.
#     else:
#         # parametreler vasıtasıyla karşıladığımız username ve password bilgilerine sahip bir kullanıcı yoksa none döndük.
#         return None
#
#
# def odd_is_valid(odd: int, current_safe: int):
#     if 500 <= odd <= current_safe:
#         return True
#     else:
#         return False
#
#
# def main():
#     # Kullanıcının login olmasını düşündük. Bu yüzden bir login fonksiyonu yazdık. Yazdığımız bu fonksiyon 2 parametre almaktadır. Bunlardan birincisi user name bir diğeri ise password'tür. Ayrıca bu fonksiyon login olmak isteyn kullanıcının bütün bilgilerini bize return etmektedir. Bu bağlamda fonksiyon sonucunda dönen değeri 'login_result' isimli değişkene assigned ettik. login_result değişkeni üzerine gelirseniz onun dictionary tipin olduğunnu göreceksiniz. Çünkü 'users' listemizin her bir elemanı bir sözlüktü. BUrada kullanıcının tüm bilgilerini dönmemizin sebebi ise bu kullanıcının bilgilerini ayrı ayrı noktalar kullanmak istememizdir. Örneğin oyun esnasında kullanıcının user name ve safe gibi bilgileri sık sık başvuracağız.
#     login_result = login(
#         input('User Name: '),
#         input('Password: ')
#     )
#     # yukarıda ki login() fonksiyonu tetiklendiğinde bize ya sözlük tipinde user yada none dönücek. aşağıda ki if bloğunda bunun kontrolünü yapıyoruz.
#     if login_result is None:
#         print('Please check your information..!')
#     else:
#         # şayet login_result değişkeni none değilse bir kullanıcı yakalandı demektir. bu yakalanan kullanıcıya chip heidye etmek için custom generate_daily_chip() fonksiyonundan faydalandık. generate_daily_chip() fonksiyonunu incelersek randint() built-in fonksiyonu ile random sayı üretiyoruz ve chip_daily değişkenine atıyoruz ki gene uygulamanın değişik safhalarında bu bilgilen sabit bir değer üzerinden faydalanalım çünkü bu fonksiyon içerisinde random değer üretilmektedir.
#         chip_daily = generate_daily_chip()
#         # Bu adımda günlük üretilen chip miktarını login olmuş kullanıcının kasasına ekleme işlemi için sözlüklerin built-in methodu olan update() fonksiyonunu kullanıyoruz. ilk adında 'safe' anahar sözcüğünü parametre olarak veriyoruz. hali hazırda ki kasa miktarını get() fonksiyonu ile yakalıyoruz ve yukarıda yarattığımız chip_daily değişkeni ile toplayarak güncel kasayı elde ediyoruz.
#         login_result.update(
#             {'safe': login_result.get('safe') + chip_daily}
#         )
#         print(f'Congurulation..! You earn {chip_daily} chips..!')
#         bot_name = get_bot_player()  # login olmuş kullanıcının karşısına random olarak bir bot atadık. bunun için bir bot_list hazırlanmıştık bu liste içerisinde isimler bulunmaktadır. bu isimler içerisinden choice() built-in fonksiyonu aracılığıyla random bir isimi alarak player_name isimli değişkene atadık.
#         player_name = login_result.get(
#             'username')  # login olmuş kullanıcının ismini sıklıkla kullanacağımdan ötürü burada sözlüklere uygulana bilen built-in get() fonksiyonu ise 'username' anahtarı üzerinde tutulan değeri çağırarak player_name isimli değişkene atadık.
#         while True:
#             if login_result.get('safe') <= 500:
#                 print('Your safe is under the minimum odd..!')
#                 break
#             else:
#                 odd = int(input('Please enter your odd: '))
#
#                 is_valid_odd = odd_is_valid(odd, login_result.get('safe'))
#
#                 if is_valid_odd is True:
#                     roll_1 = roll_dicle()
#                     roll_2 = roll_dicle()
#
#                     print(f'{player_name} rolled ==> {roll_1}')
#                     print(f'{bot_name} rolled ==> {roll_2}')
#
#                     if roll_1 > roll_2:
#                         print(f'{player_name} has victor..!')
#                         login_result.update(
#                             {'safe': login_result.get('safe') + (odd * 3)}
#                         )
#                     elif roll_2 > roll_1:
#                         print(f'{bot_name} has victor..!')
#                         login_result.update(
#                             {'safe': login_result.get('safe') - (odd * 2)}
#                         )
#                     else:
#                         print(f'Player tie..!')
#                         login_result.update(
#                             {'safe': login_result.get('safe') - odd}
#                         )
#                 else:
#                     print('Odd is not valid.')
#
#
# main()