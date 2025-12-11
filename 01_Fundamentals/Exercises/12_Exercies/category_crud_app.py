# ===============================================================
#           CATEGORY CRUD APP — DICTIONARY + UUID
# ===============================================================
# AMAÇ:
#   ✔ Dictionary yapısını CRUD için kullanmak
#   ✔ uuid.uuid4() ile benzersiz ID üretmek
#   ✔ Kullanıcıdan input alarak sözlüğü yönetmek
#   ✔ ID üzerinden kayıt bulmak, güncellemek ve silmek
#   ✔ Basit bir menü tabanlı CLI uygulaması yazmak
# ===============================================================
#
# SORU:
#   Aşağıdaki categories sözlüğünü kullanarak:
#
#   1) Create New Record
#       - Kullanıcıdan name ve description bilgisi al
#       - ID alanını uuid.uuid4() ile üret (stringe çevir)
#       - Yeni kaydı categories sözlüğüne ekle
#
#   2) Update Existing Record
#       - Kullanıcıdan güncellenecek kaydın ID bilgisini al
#       - Bu ID sözlükte yoksa kullanıcıya "bulunamadı" mesajı ver
#       - Varsa:
#           * Mevcut name ve description bilgisini ekrana yaz
#           * Kullanıcıdan yeni name ve description iste
#           * Kullanıcı alanı boş bırakırsa eski değer korunsun
#           * Değer girerse güncellensin
#
#   3) Delete Record
#       - Kullanıcıdan silinecek kaydın ID bilgisini al
#       - ID yoksa uyarı ver
#       - ID varsa:
#           * Kayıt bilgilerini göster
#           * "Are you sure? (y/n)" sorusu ile silme onayı iste
#           * 'y' derse sil, aksi halde iptal et
#
#   4) Read Operations
#       4.1) Tüm kayıtları listele → ID + name + description
#       4.2) Name alanında case-insensitive arama yap
#       4.3) Quick Read → ID veya tam isim eşleşmesi ile kayıt getir
#
#   5) Program, kullanıcı "Exit" seçeneğini seçene kadar sürekli çalışsın.
#
# ===============================================================#


import uuid
import os


# region Config
# CLEAR_CMD → Terminal temizleme komutu:
#   - Windows → cls
#   - macOS / Linux → clear
CLEAR_CMD = "cls" if os.name == "nt" else "clear"

# Description için minimum karakter sayısı
MIN_DESC_LENGTH = 10

MENU_TEXT = """
=============================================
      CATEGORY MANAGEMENT - CRUD SYSTEM
=============================================
1) Create New Record
2) Update Existing Record
3) Delete Record
4) Read Operations
5) Exit
=============================================
"""

READ_MENU_TEXT = """
--- READ OPERATIONS ---
1) List all records
2) Search by name
3) Quick Read (ID or Name)
"""

SORT_MENU_TEXT = """
--- SORT OPTIONS ---
1) ID (ascending)
2) Name A-Z
3) Name Z-A
"""
# endregion


# region Initial Data
# Dictionary veri yapısı:
#   ✔ O(1) ortalama arama süresi
#   ✔ ID → Kayıt eşlemesi yapmak için ideal
#   ✔ Güncelleme, silme, ekleme işlemleri hızlı
#   ✔ Kayıt erişimi direkt anahtar üzerinden yapılır

# Uygulama başlangıcında elde hazır bulunan kategoriler:
categories = {
    'd912b8cf-0b59-4efb-bfcf-17356dd59c9b': {
        'name': 'Boxing Gloves',
        'description': 'Best boxing gloves'
    },
    '9ecfa748-ee8e-4ac3-a471-33e1fd9fe52c': {
        'name': 'MMA Gloves',
        'description': 'Best MMA gloves'
    }
}
# endregion


# ===============================================================
#                    MAIN APPLICATION LOOP
# ===============================================================
# Program, kullanıcı "Exit" seçeneğini seçene kadar çalışır.
# Her döngüde:
#   - Ekran temizlenir
#   - Menü gösterilir
#   - Kullanıcı seçimine göre ilgili CRUD adımı işlenir
# ===============================================================

while True:
    # region Menu
    os.system(CLEAR_CMD)
    print(MENU_TEXT)

    choice = input("Select an option (1-5): ").strip()
    # endregion


    # region Create Operation
    # -----------------------------------------------------------
    # 1) CREATE NEW RECORD
    # -----------------------------------------------------------
     # Adımlar:
    #   - Kullanıcıdan name al
    #   - Normalizasyon: boşluk temizleme, Türkçe karakter sadeleştirme
    #   - Duplicate kontrolü (case-insensitive)
    #   - description al → MIN_DESC_LENGTH kontrolü
    #   - uuid.UUID4() ile benzersiz ID üret
    #   - categories sözlüğüne ekle
    #
    # Açıklama:
    #   uuid.uuid4():
    #       - Rastgele benzersiz bir UUID üretir.
    #       - Dağıtık sistemlerde bile çakışma ihtimali düşüktür.
    #       - Otomatik üretildiği için insan hatasını azaltır.
    #       - type: UUID objesi → str() ile stringe çeviririz.
    #
    #   categories[new_id] = {...} yapısı ile yeni kayıt eklenir.
    # -----------------------------------------------------------
    if choice == "1":
        print("\n--- CREATE NEW CATEGORY ---")

        try:
            # NAME INPUT
            while True:
                raw_name = input("Name: ").strip()

                # Fazla boşlukları tek boşluğa indir
                raw_name = " ".join(raw_name.split())

                # Türkçe karakterleri sadeleştir
                raw_name = (
                    raw_name
                    .replace("ç", "c").replace("Ç", "C")
                    .replace("ğ", "g").replace("Ğ", "G")
                    .replace("ı", "i").replace("İ", "I")
                    .replace("ö", "o").replace("Ö", "O")
                    .replace("ş", "s").replace("Ş", "S")
                    .replace("ü", "u").replace("Ü", "U")
                )

                name = raw_name.title()

                # Boş isim engeli
                if not name:
                    print("\n❌ Name cannot be empty! Please enter a valid name.")
                    continue

                # Duplicate Name Check (case-insensitive)
                if any(info["name"].lower() == name.lower() for info in categories.values()):
                    print("\n❌ This category name already exists! Please enter a different name.")
                    continue

                break   # name geçerli
            
            # DESCRIPTION INPUT
            while True:
                description = input("Description: ").strip()

                if len(description) < MIN_DESC_LENGTH:
                    print(f"\n❌ Description must be at least {MIN_DESC_LENGTH} characters long!")
                    continue

                break   # Geçerli description

            # Benzersiz ID üret
            new_id = str(uuid.uuid4())

            categories[new_id] = {
                "name": name,
                "description": description
            }

            print("\n✔ New category created successfully!")
            print(f"→ Generated ID: {new_id}")

        except Exception as ex:
            print("\n❌ Unexpected error while creating record:", ex)

        input("\nPress ENTER to continue...")
    # endregion


    # region Update Operation
    # -----------------------------------------------------------
    # 2) UPDATE EXISTING RECORD
    # -----------------------------------------------------------
    # Adımlar:
    #   - Kullanıcıdan güncellenecek kaydın ID bilgisini al.
    #   - ID yoksa uyarı ver.
    #   - Varsa:
    #       * Mevcut bilgileri göster
    #       * Kullanıcıdan yeni name / description iste
    #       * Boş bırakılan alanlar için eski değeri koru
    #   - Yeni değer girerse normalize edilir + duplicate kontrolü yapılır
    # -----------------------------------------------------------
    elif choice == "2":
        print("\n--- UPDATE CATEGORY ---")

        try:
            id_input = input("Enter category ID: ").strip()

            if id_input not in categories:
                raise KeyError("Category ID not found!")
        
            current = categories[id_input]

            print("\nCurrent values:")
            print(f"Name       : {current['name']}")
            print(f"Description: {current['description']}")

            print("\nEnter new values (leave blank to keep current):")

            # Yeni isim al
            raw_new_name = input("New Name        : ").strip()
            new_desc = input("New Description : ").strip()

            # Name normalize sadece kullanıcı yeni isim girdiyse
            if raw_new_name:
                raw_new_name = " ".join(raw_new_name.split())

                raw_new_name = (
                    raw_new_name
                    .replace("ç", "c").replace("Ç", "C")
                    .replace("ğ", "g").replace("Ğ", "G")
                    .replace("ı", "i").replace("İ", "I")
                    .replace("ö", "o").replace("Ö", "O")
                    .replace("ş", "s").replace("Ş", "S")
                    .replace("ü", "u").replace("Ü", "U")
                )

                new_name = raw_new_name.title()

                # Duplicate engeli
                for cid, info in categories.items():
                    if cid == id_input:
                        continue
                    if info["name"].lower() == new_name.lower():
                        raise ValueError("This name already exists on another record!")

                # Güncelle
                categories[id_input]["name"] = new_name

            # Description boş değilse ve kısa değilse güncelle
            if new_desc:
                if len(new_desc) < MIN_DESC_LENGTH:
                    raise ValueError(f"Description must be at least {MIN_DESC_LENGTH} characters long!")
                categories[id_input]["description"] = new_desc

            print("\n✔ Category updated successfully!")

        except KeyError as ke:
            print("\n❌", ke)

        except ValueError as ve:
            print("\n❌", ve)

        except Exception as ex:
            print("\n❌ Unexpected error:", ex)

        input("\nPress ENTER to continue...")
    # endregion


    # region Delete Operation
    # -----------------------------------------------------------
    # 3) DELETE RECORD
    # -----------------------------------------------------------
    # Adımlar:
    #   - Kullanıcıdan silinecek kaydın ID'sini al
    #   - ID yoksa uyarı ver
    #   - Varsa:
    #       * Kullanıcıya "Are you sure? (y/n)" diye sor
    #       * 'y' derse kaydı sil
    #       * Diğer cevaplarda silme işlemini iptal et
    #
    # Açıklama:
    #   - Confirmation mekanizması yanlışlıkla silmeye karşı korur.
    # -----------------------------------------------------------
    elif choice == "3":
        print("\n--- DELETE CATEGORY ---")

        try:
            id_input = input("Enter category ID: ").strip()

            if id_input not in categories:
                raise KeyError("Category not found!")
            
            info = categories[id_input]
            
            print("\nCategory to be deleted:")
            print(f"ID          : {id_input}")
            print(f"Name        : {info['name']}")
            print(f"Description : {info['description']}")

            confirm = input("\nAre you sure? (y/n): ").lower().strip()

            if confirm == "y":
                del categories[id_input]
                print("\n✔ Category deleted successfully!")
            else:
                print("\n❗ Delete cancelled.")

        except KeyError as ke:
            print("\n❌", ke)

        except Exception as ex:
            print("\n❌ Unexpected error:", ex)

        input("\nPress ENTER to continue...")
    # endregion


    # region Read Operations
    # -----------------------------------------------------------
    # 4) READ OPERATIONS
    # -----------------------------------------------------------
    # Alt Menü Seçenekleri:
    #   4.1) List all - Tüm kayıtları listele:
    #       - ID, Name, Description göster
    #       - Kullanıcıya sıralama seçeneği sunulur:
    #           * ID (ASC)
    #           * Name A-Z
    #           * Name Z-A
    #
    #   4.2) Search by name:
    #       - Case-insensitive arama yapılır
    #
    #   4.3) Quick Read:
    #       - Kullanıcı ID veya tam isim yazar
    #       - Birebir eşleşme aranır
    # -----------------------------------------------------------
    elif choice == "4":
        print(READ_MENU_TEXT)

        read_choice = input("Select option (1-3): ").strip()

        # 4.1 List All Records
        if read_choice == "1":
            print("\n--- CATEGORY LIST ---\n")

            if not categories:
                print("⚠ No categories found.")
            else:
                print(SORT_MENU_TEXT)
                sort_choice = input("Select sort option (1-3): ").strip()

                # Default: insertion order (dict'te mevcut sıra)
                items = categories.items()

                if sort_choice == "1":
                    # ID'ye göre sıralama
                    items = sorted(categories.items(), key=lambda item: item[0])
                elif sort_choice == "2":
                    # Name A-Z
                    items = sorted(categories.items(), key=lambda item: item[1]["name"].lower())
                elif sort_choice == "3":
                    # Name Z-A
                    items = sorted(categories.items(), key=lambda item: item[1]["name"].lower(), reverse=True)
                else:
                    print("\n⚠ Invalid sort selection, default order will be used.\n")

                for cid, info in items:
                    print(f"ID          : {cid}")
                    print(f"Name        : {info['name']}")
                    print(f"Description : {info['description']}")
                    print("-" * 40)

            input("\nPress ENTER to continue...")

        # 4.2 Search by Name
        elif read_choice == "2":
            try:
                name_query = input("\nEnter product name (or part of it): ").strip().lower()

                if not name_query:
                    raise ValueError("Search keyword cannot be empty!")

                print("\n--- SEARCH RESULTS ---")
                found = False

                for cid, info in categories.items():
                    if name_query in info["name"].lower():
                        print(f"\nID          : {cid}")
                        print(f"Name        : {info['name']}")
                        print(f"Description : {info['description']}")
                        print("-" * 40)
                        found = True

                if not found:
                    print("\n❌ No matching products found.")

            except ValueError as ve:
                print("\n❌", ve)

            input("\nPress ENTER to continue...")

        # 4.3 QUICK READ (ID or exact Name)
        elif read_choice == "3":

            query = input("\nEnter ID or exact Name: ").strip()

            if not query:
                print("\n❌ Input cannot be empty!")
                input("\nPress ENTER to continue...")

            else:
                found = False

                # 1) ID ile birebir eşleşme
                if query in categories:
                    info = categories[query]
                    print("\n--- QUICK READ RESULT (by ID) ---")
                    print(f"ID          : {query}")
                    print(f"Name        : {info['name']}")
                    print(f"Description : {info['description']}")
                    print("-" * 40)
                    found = True

                else:
                    # 2) Name birebir eşleşme (case-insensitive)
                    query_lower = query.lower()
                    for cid, info in categories.items():
                        if info["name"].lower() == query_lower:
                            print("\n--- QUICK READ RESULT (by Name) ---")
                            print(f"ID          : {cid}")
                            print(f"Name        : {info['name']}")
                            print(f"Description : {info['description']}")
                            print("-" * 40)
                            found = True
                            break

                if not found:
                    print("\n❌ No record found for:", query)

                input("\nPress ENTER to continue...")

        else:
            print("\n❌ Invalid selection!")
            input("\nPress ENTER to continue...")
    # endregion


    # region Exit
    elif choice == "5":
        print("\nExiting program...")
        break
    # endregion


    # region Invalid Choice
    else:
        print("\n❌ Invalid selection!")
        input("\nPress ENTER to continue...")
    # endregion