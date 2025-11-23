# -----------------------------------------------------------------------------
# GEOMETRİ VE HARF NOTU HESAPLAMA UYGULAMASI
# Bu program login sistemine sahiptir. Giriş başarılı olursa kullanıcı geometri hesaplama veya harf notu hesaplama uygulamalarına erişebilir.
# kare, dikdörtgen, üçgen, daire, yamuk, 
# vize final notundan ortalama hesabı ve harf notu gösterme
# Program tamamen fonksiyonsuz (procedural) olarak yazılmıştır.
# -----------------------------------------------------------------------------

USERNAME = "Admin"
PASSWORD = "1234"

# ---------------------------------------------------------
# LOGIN KISMI
# ---------------------------------------------------------

# Kullanıcıdan kullanıcı adı ve şifre alınır
username = input("Username: ")
password = input("Password: ")

# Giriş bilgileri doğruysa uygulamaya girer
if username == USERNAME and password == PASSWORD:
    print("Welcome to the app")
else:
    # Giriş hatalıysa program sonlandırılır
    print("Wrong credentials. Program is shutting down.")
    exit()

# ---------------------------------------------------------
# ANA MENÜ
# ---------------------------------------------------------

while True:
    # Kullanıcıdan menü seçimi alınır
    applications = input(
        "G for Geometry app\n"
        "H for Grade app\n"
        "S to stop the program\n"
        "Please enter a character: "
    ).lower()

    # -----------------------------------------------------
    # GEOMETRİ UYGULAMASI (MATCH-CASE KULLANILDI)
    # -----------------------------------------------------
    if applications == "g":
        while True:
            # Kullanıcıdan şekil türü istenir
            shape = input(
                "Please enter your shape "
                "(square, rectangle, triangle, trapezoid, circle)\n"
                "(Türkçe de kabul edilir: kare, dikdortgen, ucgen, yamuk, daire)\n"
                "R for returning the previous menu: "
            ).lower()

            # Ana menüye dönüş
            if shape == "r":
                print("Returning to the main menu...")
                break

            try:
                # match-case ile şekil seçimi
                match shape:
                    # ---------------- Kare ----------------
                    case "square" | "kare":
                        shape_name = "Square"
                        # Kullanıcı kenar uzunluğunu girer
                        edge = float(input("Enter edge length: "))
                        # Alan ve çevre hesaplanır
                        area = edge ** 2
                        perimeter = 4 * edge
                    # ---------------- Dikdörtgen ----------------
                    case "rectangle" | "dikdortgen":
                        shape_name = "Rectangle"
                        edge_first = float(input("Enter first edge: "))
                        edge_second = float(input("Enter second edge: "))

                        area = edge_first * edge_second
                        perimeter = 2 * (edge_first + edge_second)
                    # ---------------- Üçgen ----------------
                    case "triangle" | "ucgen":
                        shape_name = "Triangle"
                        edge_first = float(input("Enter first edge: "))
                        edge_second = float(input("Enter second edge: "))
                        edge_third = float(input("Enter third edge: "))
                        # Çevre
                        perimeter = edge_first + edge_second + edge_third
                        # Heron formülü
                        s = perimeter / 2
                        area = (s * (s - edge_first) * (s - edge_second) * (s - edge_third)) ** 0.5
                    # ---------------- Yamuk ----------------
                    case "trapezoid" | "yamuk":
                        shape_name = "Trapezoid"
                        edge_top = float(input("Enter top edge: "))
                        edge_bottom = float(input("Enter bottom edge: "))
                        edge_side_1 = float(input("Enter first side edge: "))
                        edge_side_2 = float(input("Enter second side edge: "))
                        h = float(input("Enter vertical height: "))

                        area = (edge_top + edge_bottom) * h / 2
                        perimeter = edge_top + edge_bottom + edge_side_1 + edge_side_2
                    # ---------------- Daire ----------------
                    case "circle" | "daire":
                        shape_name = "Circle"
                        pi = 3.1415
                        r = float(input("Enter circle's radius: "))
                        area = pi * (r ** 2)
                        perimeter = 2 * pi * r
                    # ---------------- Geçersiz giriş ----------------
                    case _:
                        print("There is a mistake in your entry, please try again.")
                        continue

                # Sonuçlar gösterilir
                print(
                    f"Desired shape: {shape_name}\n"
                    f"Perimeter: {perimeter:.2f}\n"
                    f"Area: {area:.2f}"
                )

            except (TypeError, ValueError) as err:
                # Kullanıcı yanlış türde giriş yaparsa hata yakalanır
                print("There is a mistake in your entry, please try again.")
                print(err)

    # -----------------------------------------------------
    # HARF NOTU UYGULAMASI
    # -----------------------------------------------------
    elif applications == "h":
        while True:
            choice = input("Press R to return to main menu, C to calculate a grade: ").lower()

            # Ana menüye dönüş
            if choice == "r":
                print("Returning to the main menu...")
                break
            # Not hesaplama işlemi
            elif choice == "c":
                while True:
                    try:
                        # Notlar alınır
                        midterm_first = int(input("Enter first midterm grade: "))
                        midterm_second = int(input("Enter second midterm grade: "))
                        final = int(input("Enter final grade: "))

                        # Notların 0–100 aralığında olması gerekli
                        if not all(0 <= x <= 100 for x in [midterm_first, midterm_second, final]):
                            print("There is a mistake in your entry, please try again.")
                            continue

                        # Ortalama hesaplama
                        grade = midterm_first * 0.3 + midterm_second * 0.3 + final * 0.4

                        # Varsayılan geçme durumu
                        is_pass = True

                        # Harf notu hesaplama
                        if 0 <= grade <= 30:
                            letter_grade = "FF"
                            is_pass = False
                        elif 30 < grade <= 45:
                            letter_grade = "DD"
                            is_pass = False
                        elif 45 < grade <= 50:
                            letter_grade = "DC"
                        elif 50 < grade <= 60:
                            letter_grade = "CC"
                        elif 60 < grade <= 70:
                            letter_grade = "CB"
                        elif 70 < grade <= 85:
                            letter_grade = "BB"
                        elif 85 < grade <= 90:
                            letter_grade = "BA"
                        elif 90 < grade <= 100:
                            letter_grade = "AA"

                        # Sonuç ekrana yazdırılır
                        print(f"Your average is {grade:.2f} and its equivalent letter grade is: {letter_grade}")
                        print("You passed this course." if is_pass else "You failed this course.")

                        break

                    except (TypeError, ValueError) as err:
                        print("There is a mistake in your entry, please try again.")
                        print(err)
            else:
                print("There is a mistake in your entry, please try again.")

    # -----------------------------------------------------
    # PROGRAMDAN ÇIKIŞ
    # -----------------------------------------------------
    elif applications == "s":
        print("Program is closing.")
        break
    # Geçersiz menü seçeneği
    else:
        print("There is a mistake in your entry, please try again.")