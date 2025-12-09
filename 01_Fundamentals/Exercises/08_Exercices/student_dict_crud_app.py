
#! Dictionary — In-Memory CRUD Application (No Functions)
# ===============================================================
# AMAÇ:
#   - Sözlük (dict) kullanarak temel CRUD (Create, Read, Update, Delete)
#     operasyonlarını bir “uygulama” mantığıyla göstermek.
#   - Tüm işlemler kullanıcıdan input alarak yapılır.
#   - Veriler RAM üzerinde (in-memory) tutulur.
#
# ÖZELLİKLER:
#   ✔ CREATE      → Yeni öğrenci ekle (ID Seçenekli: Auto / Manual)
#   ✔ READ        → Öğrencileri listele (ID / isim sıralı)
#   ✔ UPDATE      → Öğrenci ismini güncelle (+ UNDO UPDATE)
#   ✔ DELETE      → Öğrenciyi sil (onaylı, + UNDO DELETE)
#   ✔ SEARCH      → İsim üzerinden arama (parça eşleşme)
#   ✔ QUICK READ  → ID veya tam isimle tek öğrenci göster
#   ✔ BULK CREATE → Çoklu öğrenci ekleme (satır satır)
#   ✔ STATS       → Gelişmiş istatistik (toplam, en uzun/kısa, dağılım)
#   ✔ HISTORY     → İşlem geçmişini göster
# ===============================================================

import os   # Ekranı temizlemek için

# Windows'ta "cls", Mac/Linux'ta "clear" komutunu kullanarak ekranı temizlemek için
CLEAR_CMD = "cls" if os.name == "nt" else "clear"


# ===============================================================
# region Başlangıç Verisi (In-Memory "Database")
# ===============================================================
students = {
    1: "Burak",
    2: "Hakan",
    3: "Ipek"
}

# Son silinen kaydı tutmak için (ID, İsim)
last_deleted = None

# Son güncellenen kaydı tutmak için (ID, Eskiİsim, Yeniİsim)
last_updated = None

# İşlem geçmişi (string listesi)
history = []
# endregion
# ===============================================================


# ===============================================================
# region Ana Döngü (Uygulama Çalışma Süreci)
# ===============================================================
while True:
    os.system(CLEAR_CMD)

    print("-" * 60)
    print("📌 STUDENT CRUD APPLICATION (Dictionary Based — No Functions)")
    print("-" * 60)
    print("1) Yeni öğrenci ekle (CREATE, ID Seçenekli)")
    print("2) Öğrencileri listele (READ)")
    print("3) Öğrenci güncelle (UPDATE)")
    print("4) Öğrenci sil (DELETE)")
    print("5) Öğrenci ara (SEARCH, parça eşleşme)")
    print("6) İstatistikleri göster (STATS)")
    print("7) Tek öğrenci görüntüle (QUICK READ)")
    print("8) Çoklu öğrenci ekle (BULK CREATE)")
    print("9) Son güncellemeyi geri al (UNDO UPDATE)")
    print("10) Son silme işlemini geri al (UNDO DELETE)")
    print("11) İşlem geçmişini göster (HISTORY)")
    print("12) Çıkış")
    print("-" * 60)

    choice = input("Seçiminiz (1-12): ").strip()

    # ===========================================================
    # region CREATE — Yeni Kayıt Ekle (AUTO / MANUAL ID)
    # ===========================================================
    if choice == "1":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("🟢 CREATE — Yeni Öğrenci Ekle (ID Seçenekli)")
        print("=" * 60)

        print("ID oluşturma yöntemini seçin:")
        print(" 1) Otomatik ID (önerilen)")
        print(" 2) Manuel ID gir")
        id_mode = input("Seçim (1/2): ").strip()

        student_id = None

        if id_mode == "2":
            # Manuel ID
            try:
                manual_id = int(input("\nYeni öğrenci ID: "))
            except ValueError:
                print("⚠ Geçersiz ID! Lütfen sayısal bir değer girin.")
                input("\nDevam etmek için Enter'a basın...")
                continue

            if manual_id in students:
                print(f"⚠ Bu ID zaten kayıtlı! (Mevcut isim: {students[manual_id]})")
                input("\nDevam etmek için Enter'a basın...")
                continue

            student_id = manual_id
            print(f"✔ Manuel ID seçildi: {student_id}")

        elif id_mode == "1":
            # Otomatik ID
            if students:
                student_id = max(students.keys()) + 1
            else:
                student_id = 1
            print(f"✔ Otomatik oluşturulan ID: {student_id}")
        else:
            # 1 veya 2 dışında bir şey girildiyse
            print("⚠ Geçersiz seçim! Lütfen sadece 1 veya 2 girin.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        name = input("Öğrencinin adı: ").strip()
        if not name:
            print("⚠ İsim boş olamaz.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        students[student_id] = name
        print(f"✅ Öğrenci eklendi: ID={student_id}, İsim={name}")

        # History log
        history.append(f"CREATE → ID={student_id}, İsim={name}")

        input("\nDevam etmek için Enter'a basın...")

    # endregion CREATE
    # ===========================================================


    # ===========================================================
    # region READ — Kayıtları Listele
    # ===========================================================
    elif choice == "2":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("🔵 READ — Öğrencileri Listele")
        print("=" * 60)

        if not students:
            print("📭 Kayıtlı öğrenci bulunmuyor.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        print("Sıralama türü seçin:")
        print(" 1) ID'ye göre (varsayılan)")
        print(" 2) İsme göre (A-Z)")
        sort_choice = input("Seçim (1/2): ").strip()

        if sort_choice == "2":
            items = sorted(students.items(), key=lambda x: x[1].lower())
        else:
            items = sorted(students.items(), key=lambda x: x[0])

        print("\n📚 Kayıtlı Öğrenciler:")
        for student_id, name in items:
            print(f" - ID: {student_id:<3} | İsim: {name}")

        input("\nDevam etmek için Enter'a basın...")

    # endregion READ
    # ===========================================================


    # ===========================================================
    # region UPDATE — Kayıt Güncelle
    # ===========================================================
    elif choice == "3":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("🟡 UPDATE — Öğrenci Güncelle")
        print("=" * 60)

        if not students:
            print("📭 Güncellenecek öğrenci yok. Önce kayıt ekleyin.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        print("Mevcut öğrenciler:")
        for student_id, name in sorted(students.items(), key=lambda x: x[0]):
            print(f" - ID: {student_id:<3} | İsim: {name}")

        try:
            student_id = int(input("\nGüncellenecek öğrenci ID: "))
        except ValueError:
            print("⚠ Geçersiz ID! Lütfen sayısal bir değer girin.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        if student_id not in students:
            print("⚠ Bu ID'ye sahip bir öğrenci bulunamadı.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        old_name = students[student_id]
        print(f"Mevcut isim: {old_name}")
        new_name = input("Yeni isim: ").strip()

        if not new_name:
            print("⚠ Yeni isim boş olamaz.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        students[student_id] = new_name
        print(f"✅ Güncelleme başarılı! Yeni isim: {new_name}")

        # Son güncellemeyi geri almak için sakla
        last_updated = (student_id, old_name, new_name)

        # History log
        history.append(f"UPDATE → ID={student_id}, {old_name} → {new_name}")

        input("\nDevam etmek için Enter'a basın...")

    # endregion UPDATE
    # ===========================================================


    # ===========================================================
    # region DELETE — Kayıt Sil
    # ===========================================================
    elif choice == "4":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("🔴 DELETE — Öğrenci Sil")
        print("=" * 60)

        if not students:
            print("📭 Silinecek öğrenci yok. Önce kayıt ekleyin.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        print("Mevcut öğrenciler:")
        for student_id, name in sorted(students.items(), key=lambda x: x[0]):
            print(f" - ID: {student_id:<3} | İsim: {name}")

        try:
            student_id = int(input("\nSilinecek öğrenci ID: "))
        except ValueError:
            print("⚠ Geçersiz ID! Lütfen sayısal bir değer girin.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        if student_id not in students:
            print("⚠ Bu ID'ye sahip bir öğrenci bulunamadı.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        deleted_name = students[student_id]
        confirm = input(f"⚠ {deleted_name} silinsin mi? (e/h): ").strip().lower()

        if confirm != "e":
            print("❌ Silme işlemi iptal edildi.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        students.pop(student_id)

        # Son silinen kaydı geri almak için sakla
        last_deleted = (student_id, deleted_name)

        # History log
        history.append(f"DELETE → ID={student_id}, İsim={deleted_name}")

        print(f"🗑 Silinen öğrenci: ID={student_id}, İsim={deleted_name}")
        input("\nDevam etmek için Enter'a basın...")

    # endregion DELETE
    # ===========================================================


    # ===========================================================
    # region SEARCH — Kayıt Ara (Parça Eşleşme)
    # ===========================================================
    elif choice == "5":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("🔍 SEARCH — Öğrenci Ara (Parça Eşleşme)")
        print("=" * 60)

        if not students:
            print("📭 Aranacak öğrenci yok.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        query = input("Aranacak isim (tam ya da parça): ").strip().lower()
        if not query:
            print("⚠ Arama ifadesi boş olamaz.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        found = []
        for student_id, name in students.items():
            if query in name.lower():
                found.append((student_id, name))

        if not found:
            print("❌ Eşleşen öğrenci bulunamadı.")
        else:
            print("✅ Eşleşen öğrenciler:")
            for sid, name in sorted(found, key=lambda x: x[0]):
                print(f" - ID: {sid:<3} | İsim: {name}")

        input("\nDevam etmek için Enter'a basın...")

    # endregion SEARCH
    # ===========================================================


    # ===========================================================
    # region STATS — Gelişmiş İstatistikler
    # ===========================================================
    elif choice == "6":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("📊 STATS — İstatistikler")
        print("=" * 60)

        if not students:
            print("📭 Henüz hiç öğrenci yok.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        total = len(students)

        lengths = [(sid, name, len(name)) for sid, name in students.items()]

        longest = max(lengths, key=lambda x: x[2])
        shortest = min(lengths, key=lambda x: x[2])

        total_chars = sum(len(name) for _, name in students.items())
        avg_length = total_chars / total

        # İsim uzunluğuna göre dağılım
        length_distribution = {}
        for _, name in students.items():
            l = len(name)
            length_distribution[l] = length_distribution.get(l, 0) + 1

        # İlk harfe göre dağılım
        first_letter_counts = {}
        for _, name in students.items():
            if name:
                first_letter = name[0].upper()
                first_letter_counts[first_letter] = first_letter_counts.get(first_letter, 0) + 1

        if first_letter_counts:
            most_common_letter = max(first_letter_counts.items(), key=lambda x: x[1])
        else:
            most_common_letter = None

        print(f"👥 Toplam öğrenci sayısı      : {total}")
        print(f"📏 En uzun isim              : {longest[1]} "
              f"(ID: {longest[0]}, Uzunluk: {longest[2]})")
        print(f"📐 En kısa isim              : {shortest[1]} "
              f"(ID: {shortest[0]}, Uzunluk: {shortest[2]})")
        print(f"📊 Ortalama isim uzunluğu    : {avg_length:.2f} karakter")

        print("\n📚 İsim uzunluğu dağılımı (uzunluk → kişi sayısı):")
        for length_value, count in sorted(length_distribution.items()):
            print(f"  - {length_value:>2} harfli: {count} öğrenci")

        if most_common_letter:
            letter, count = most_common_letter
            print("\n🔠 En çok kullanılan ilk harf : "
                  f"'{letter}' ({count} öğrenci bu harfle başlıyor)")

        print("\n🔤 İlk harfe göre genel dağılım:")
        for letter, count in sorted(first_letter_counts.items()):
            print(f"  - {letter} ile başlayan: {count} öğrenci")

        input("\nDevam etmek için Enter'a basın...")

    # endregion STATS
    # ===========================================================


    # ===========================================================
    # region QUICK READ — Tek Öğrenci Göster (ID / İsim)
    # ===========================================================
    elif choice == "7":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("📖 QUICK READ — Tek Öğrenci Görüntüle")
        print("=" * 60)

        if not students:
            print("📭 Gösterilecek öğrenci yok. Önce kayıt ekleyin.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        print("Arama türü seçin:")
        print(" 1) ID ile bul")
        print(" 2) İSİM ile bul (tam eşleşme)")
        search_mode = input("Seçim (1/2): ").strip()

        if search_mode == "1":
            try:
                student_id = int(input("\nÖğrenci ID: "))
            except ValueError:
                print("⚠ Geçersiz ID! Lütfen sayısal bir değer girin.")
                input("\nDevam etmek için Enter'a basın...")
                continue

            if student_id not in students:
                print("❌ Bu ID'ye sahip öğrenci bulunamadı.")
            else:
                name = students[student_id]
                print("\n✅ Kayıt bulundu:")
                print("-" * 40)
                print(f" ID   : {student_id}")
                print(f" İsim : {name}")
                print("-" * 40)

        elif search_mode == "2":
            query = input("\nÖğrencinin tam adını girin: ").strip()
            if not query:
                print("⚠ İsim boş olamaz.")
                input("\nDevam etmek için Enter'a basın...")
                continue

            matches = []
            for sid, name in students.items():
                if name.lower() == query.lower():
                    matches.append((sid, name))

            if not matches:
                print("❌ Bu isimde öğrenci bulunamadı.")
            elif len(matches) == 1:
                sid, name = matches[0]
                print("\n✅ Tek kayıt bulundu:")
                print("-" * 40)
                print(f" ID   : {sid}")
                print(f" İsim : {name}")
                print("-" * 40)
            else:
                print("\nℹ Bu isimle birden fazla öğrenci bulundu:")
                print("-" * 40)
                for sid, name in sorted(matches, key=lambda x: x[0]):
                    print(f" ID: {sid:<3} | İsim: {name}")
                print("-" * 40)
        else:
            print("⚠ Geçersiz seçim! 1 veya 2 girin.")

        input("\nDevam etmek için Enter'a basın...")

    # endregion QUICK READ
    # ===========================================================


    # ===========================================================
    # region BULK CREATE — Çoklu Öğrenci Ekle
    # ===========================================================
    elif choice == "8":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("🟢 BULK CREATE — Çoklu Öğrenci Ekle")
        print("=" * 60)

        if not students:
            print("ℹ Şu anda hiç öğrenci yok. İlk kayıtlar toplu eklenecek.")
        else:
            print(f"ℹ Mevcut öğrenci sayısı: {len(students)}")

        print("\nHer satıra bir öğrenci adı yazın.")
        print("Boş satır bırakırsanız giriş işlemi biter.\n")

        if students:
            next_id = max(students.keys())
        else:
            next_id = 0

        added_count = 0

        while True:
            name = input("Öğrenci adı (bitirmek için Enter): ").strip()

            if not name:
                break

            next_id += 1
            students[next_id] = name
            added_count += 1

            print(f"   ✔ Eklendi → ID={next_id}, İsim={name}")

        if added_count == 0:
            print("\nℹ Hiç öğrenci eklenmedi.")
        else:
            print(f"\n✅ Toplam {added_count} öğrenci eklendi.")

            # History log
            history.append(f"BULK CREATE → {added_count} öğrenci eklendi.")

        input("\nDevam etmek için Enter'a basın...")

    # endregion BULK CREATE
    # ===========================================================


    # ===========================================================
    # region UNDO UPDATE — Son Güncellemeyi Geri Al
    # ===========================================================
    elif choice == "9":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("↩ UNDO UPDATE — Son Güncellemeyi Geri Al")
        print("=" * 60)

        if last_updated is None:
            print("ℹ Geri alınacak bir güncelleme bulunmuyor.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        sid, old_name, new_name = last_updated

        if sid not in students:
            print("⚠ Bu ID'ye ait kayıt artık mevcut değil (silinmiş olabilir).")
            input("\nDevam etmek için Enter'a basın...")
            continue

        print("Son güncelleme bilgisi:")
        print(f" ID        : {sid}")
        print(f" Eski İsim : {old_name}")
        print(f" Yeni İsim : {students[sid]}")

        confirm = input("\nBu güncellemeyi geri almak istiyor musunuz? (e/h): ").strip().lower()
        if confirm != "e":
            print("❌ Geri alma iptal edildi.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        students[sid] = old_name
        last_updated = None

        # History log
        history.append(f"UNDO UPDATE → ID={sid}, {new_name} → {old_name}")

        print(f"✅ Güncelleme geri alındı. ID={sid}, İsim tekrar: {old_name}")
        input("\nDevam etmek için Enter'a basın...")

    # endregion UNDO UPDATE
    # ===========================================================


    # ===========================================================
    # region UNDO DELETE — Son Silmeyi Geri Al
    # ===========================================================
    elif choice == "10":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("↩ UNDO DELETE — Son Silinen Öğrenciyi Geri Al")
        print("=" * 60)

        if last_deleted is None:
            print("ℹ Geri alınacak bir silme işlemi yok.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        sid, name = last_deleted
        print("Son silinen kayıt:")
        print(f" ID   : {sid}")
        print(f" İsim : {name}")

        confirm = input("\nBu kaydı geri yüklemek istiyor musunuz? (e/h): ").strip().lower()
        if confirm != "e":
            print("❌ Geri alma iptal edildi.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        if sid in students:
            print("⚠ Bu ID ile zaten başka bir kayıt mevcut, geri alma yapılamıyor.")
        else:
            students[sid] = name
            last_deleted = None

            # History log
            history.append(f"UNDO DELETE → ID={sid}, İsim={name} geri yüklendi.")

            print(f"✅ Kayıt geri yüklendi: ID={sid}, İsim={name}")

        input("\nDevam etmek için Enter'a basın...")

    # endregion UNDO DELETE
    # ===========================================================


    # ===========================================================
    # region HISTORY — İşlem Geçmişini Göster
    # ===========================================================
    elif choice == "11":
        os.system(CLEAR_CMD)
        print("=" * 60)
        print("🧾 HISTORY — İşlem Geçmişi")
        print("=" * 60)

        if not history:
            print("ℹ Henüz hiçbir işlem yapılmadı.")
            input("\nDevam etmek için Enter'a basın...")
            continue

        print(f"Toplam {len(history)} işlem kaydı var.")
        limit_input = input("Kaç kayıt görmek istersiniz? (Boş bırak = hepsi): ").strip()

        if limit_input:
            try:
                limit = int(limit_input)
            except ValueError:
                limit = len(history)
        else:
            limit = len(history)

        if limit <= 0:
            limit = 1

        print("\nSon işlemler (yeniden eskiye doğru):\n")
        count = 0
        for item in reversed(history):
            print(f" - {item}")
            count += 1
            if count >= limit:
                break

        input("\nDevam etmek için Enter'a basın...")

    # endregion HISTORY
    # ===========================================================


    # ===========================================================
    # region EXIT — Uygulamadan Çıkış
    # ===========================================================
    elif choice == "12":
        os.system(CLEAR_CMD)
        print("👋 Uygulamadan çıkılıyor... Görüşmek üzere!")
        break
    # endregion EXIT
    # ===========================================================


    # ===========================================================
    # region GEÇERSİZ SEÇİM
    # ===========================================================
    else:
        print("⚠ Geçersiz seçim! Lütfen 1-12 arasında bir değer girin.")
        input("\nDevam etmek için Enter'a basın...")
    # endregion GEÇERSİZ SEÇİM

# endregion Ana Döngü
# ===============================================================