from string import punctuation

# ===============================================================
# KULLANICI VE ÜRÜN YÖNETİMİ UYGULAMASI
# ===============================================================
# Bu programda:
#
# 1) Register (Kayıt Olma)
#    - Yeni kullanıcı adı alınır.
#    - Aynı kullanıcı adı varsa uyarı verilir.
#    - Şifre kuralları kontrol edilir:
#         * En az 8 karakter
#         * En az 1 rakam
#         * En az 1 büyük harf
#         * En az 1 küçük harf
#         * En az 1 noktalama işareti
#    - Şifre kurallara uygunsa kullanıcı listeye eklenir.
#
# 2) Login (Giriş)
#    - Maksimum 3 deneme hakkı vardır.
#    - Kullanıcı adı ve şifre doğruysa giriş yapılır.
#    - 3 hakkı biten kullanıcı programdan çıkarılır.
#
# 3) Product Operations (Ürün İşlemleri)
#    * Bu menüye sadece giriş yapmış kullanıcı erişebilir.
#    * Menü seçenekleri:
#
#      3.1) Tüm ürünlerin toplam fiyatını hesapla
#           products listesindeki tüm fiyatlar toplanır.
#
#      3.2) Sadece Laptop olan ürünlerin fiyat toplamı
#           Ürün adı "Laptop" olanların fiyatları toplanır.
#
#      3.3) Ürün arama
#           - Kullanıcıdan ürün adı alınır.
#           - products listesi içinde adı eşleşen ürünler bulunur.
#           - Bulunan sonuçlar önce listeye atılır ve ekrana yazdırılır.
#
#      3.4) Fiyatı 200 TL altında olan ürünleri listele
#           - Tüm ürünler gezilir.
#           - Fiyatı 200’den küçük olanlar listeye eklenir.
#           - Liste boş değilse ekrana yazdırılır.
#
#      3.5) Ana menüye dön
#
# 4) Exit
#    - Program sonlanır.
#
# Amaç:
# - Kullanıcı kaydı oluşturmak
# - Kullanıcı girişini doğrulamak
# - Giriş yapmış kullanıcıya ürün işlemlerini sunmak
# - Listeler kullanarak filtreleme, arama ve toplama işlemlerini yapmak
# ===============================================================

users = [
    ['beast', '123'],
    ['bear', '987'],
    ['keko', '567'],
]

products = [
    ["Laptop", 850],
    ["Smartphone", 499],
    ["Headphones", 79],
    ["Keyboard", 45],
    ["Monitor", 220],
    ["Mouse", 25],
    ["Smartwatch", 150],
    ["Tablet", 310],
    ["External Hard Drive", 95],
    ["Webcam", 60],
    ["Laptop", 856],
]

is_logged_in = False   # Kullanıcı giriş yaptı mı?
current_user = None    # Giriş yapan kullanıcının adı

# ----------------- MAIN MENU -----------------
while True:
    print("\n=== MAIN MENU ===")
    print("1- Register")
    print("2- Login")
    print("3- Product Operations")
    print("4- Exit")

    choice = input("Your choice: ")

    # ----------------- REGISTER -----------------
    if choice == "1":
        print("\n=== REGISTER ===")
        new_username = input("Enter new username: ")

        # Aynı kullanıcı adı var mı kontrol et
        username_exists = False
        for user in users:
            if user[0] == new_username:
                username_exists = True
                break

        if username_exists:
            print("This username already exists, please try another one.")
            continue

        # PASSWORD CHECKING
        while True:
            new_password = input("Enter new password: ")

            has_digit = False
            has_upper = False
            has_lower = False
            has_punct = False

            # Check characters one by one
            for ch in new_password:
                if ch.isdigit():
                    has_digit = True
                if ch.isupper():
                    has_upper = True
                if ch.islower():
                    has_lower = True
                if ch in punctuation:
                    has_punct = True

            is_long_enough = len(new_password) >= 8

            # Eksik kuralları topla
            missing_rules = []

            if not is_long_enough:
                missing_rules.append("- Minimum 8 characters")
            if not has_digit:
                missing_rules.append("- At least 1 digit")
            if not has_upper:
                missing_rules.append("- At least 1 uppercase letter")
            if not has_lower:
                missing_rules.append("- At least 1 lowercase letter")
            if not has_punct:
                missing_rules.append(f"- At least 1 punctuation character ({punctuation})")

            # HATA VARSA
            if missing_rules:
                print("\n❌ Password is not strong enough!")
                print("Missing rules:")
                for item in missing_rules:
                    print(item)
                print("\nPlease try again.\n")
            else:
                # Şifre tüm kuralları geçti
                break

        users.append([new_username, new_password])
        print("✅ Registration successful! You can now login.")
    # ----------------- LOGIN -----------------
    elif choice == "2":
        print("\n=== LOGIN ===")

        MAX_ATTEMPTS = 3        # Toplam hak
        attempts_left = MAX_ATTEMPTS

        while attempts_left > 0 and not is_logged_in:
            username = input("Username: ")
            password = input("Password: ")

            login_success = False   # her denemede sıfırlanmalı

            # Kullanıcı doğrulama
            for user in users:
                if username == user[0] and password == user[1]:
                    login_success = True
                    is_logged_in = True
                    current_user = username
                    break

            if login_success:
                print(f"✅ Login successful, welcome {current_user}!")
            else:
                attempts_left -= 1
                print(f"❌ Incorrect username or password. Attempts left: {attempts_left}")

        # 3 hak da bitti ve login olmadıysa
        if not is_logged_in:
            print("\n❌ You have used all login attempts.")
            print("Program is terminating for security reasons...")
            exit()
   # ----------------- PRODUCT OPERATIONS -----------------
    elif choice == "3":
        # If not logged in → force login
        if not is_logged_in:
            print("\nYou must be logged in to access product operations.")
            print("Redirecting to login...\n")

            MAX_ATTEMPTS = 3
            attempts_left = MAX_ATTEMPTS

            while attempts_left > 0 and not is_logged_in:
                username = input("Username: ")
                password = input("Password: ")

                login_success = False

                for user in users:
                    if username == user[0] and password == user[1]:
                        login_success = True
                        is_logged_in = True
                        current_user = username
                        break

                if login_success:
                    print(f"✅ Login successful, welcome {current_user}!")
                else:
                    attempts_left -= 1
                    print(f"❌ Incorrect username or password. Attempts left: {attempts_left}")

            if not is_logged_in:
                print("\n❌ All login attempts used. Program will exit.")
                exit()

        # ---- Logged in, now product menu ----
        print(f"\n=== PRODUCT OPERATIONS ({current_user}) ===")

        while True:
            print("\n--- PRODUCT MENU ---")
            print("1- Total price of all products")
            print("2- Total price of all laptops")
            print("3- Search product by name")
            print("4- Products under 200 TL")
            print("5- Back to Main Menu")

            p_choice = input("Your choice: ")

            if p_choice == "1":
                total = 0
                for name, price in products:
                    total += price
                print(f"Total price of all products: {total} TL")

            elif p_choice == "2":
                laptop_total = 0
                for name, price in products:
                    if name.lower() == "laptop":
                        laptop_total += price
                print(f"Total laptop price: {laptop_total} TL")

            elif p_choice == "3":
                search = input("Enter product name: ").lower()

                # Eşleşen ürünleri listeye at
                found_products = []   # boş liste oluştur

                for name, price in products:
                    if name.lower() == search:     # birebir eşleşme (case-insensitive)
                        found_products.append([name, price])   # listeye ekle
                
                # Liste boş mu kontrol et
                if len(found_products) == 0:
                    print("Product not found.")
                else:
                    print("Matched products:")
                    for item in found_products:
                        print(f"- {item[0]} → {item[1]} TL")

            elif p_choice == "4":
                                
                cheap_products = []   # Liste oluştur

                for name, price in products:
                    if price < 200:
                        cheap_products.append([name, price])   # Listeye ekle
                
                # Liste boş mu kontrol et
                if len(cheap_products) == 0:
                    print("There are no products cheaper than 200 TL.")
                else:
                    print("Products under 200 TL:")
                    for item in cheap_products:
                        print(f"- {item[0]}: {item[1]} TL")

            elif p_choice == "5":
                print("Returning to Main Menu...")
                break

            else:
                print("Invalid choice, please select 1-5.")
    # ----------------- EXIT -----------------
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, enter 1-4.")