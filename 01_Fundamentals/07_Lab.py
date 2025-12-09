
#! Any Function
# Liste içinde en az bir True varsa True döner.
# Genellikle veri kontrolü ve validasyon için kullanılır.

# ⭐ Nerede Kullanılır?
# Şifre doğrulama
# Kullanıcı giriş validasyonu
# Form kontrolü
# Veri kontrolü 
# En az bir şartın sağlanıp sağlanmadığını kontrol eder    
# Çoklu koşulları kontrol etmek için idealdir


# region ANY Example — Sample
# any() → İçerideki koşul EN AZ BİR kez True olursa True döner.

# numbers = [3, 19, 90, 45, 32]

# Burada generator expression kullanıyoruz:
#   (number > 80 for number in numbers)
# Bu ifade her elemanı tek tek kontrol eder.
# numbers içinde 90 olduğu için sonuç True olur.

# result = any(number > 80 for number in numbers)

# print("80'den büyük bir sayı var mı?:", result)
# endregion


# region ANY Function — String Matching in List
# programming_language = ['python', 'java', 'go']

# print(
#     any(pl == 'python' for pl in programming_language)
# )
# # Output: True

# print(
#     any(pl == 'C#' for pl in programming_language)
# )
# Output: False
# endregion


# region Any Function — Nested For & String Check (Password)
# Bir şifre listesindeki herhangi bir şifrede en az 1 harf var mı?
#
# Çalışma Mantığı:
#   1) for pwd in passwords  → her şifreyi al
#   2) for ch in pwd         → şifredeki her karakteri kontrol et
#   3) ch.isalpha()          → karakter harf ise True
#   4) any(...)              → içlerinden en az biri harfse True döner
#
# Böylece listedeki PAROLA’LARIN herhangi birinde harf olup olmadığı bulunur.

# passwords = ["123", "98a", "12q", "987"]

# ✔ Tek satırlık zip gibi nested comprehension ile ANY kontrolü
# print(any(ch.isalpha() for pwd in passwords for ch in pwd))

# Nested For ile uzun yazım — aynı sonuca ulaşan versiyon
# print("\n📌 Nested for ile karakter bazlı kontroller:")
# for pwd in passwords:
#     for ch in pwd:
#         # any(ch.isalpha()) → yanlış kullanım olur.
#         # Çünkü any() bir iterable ister, tek bir boolean değil.
#         # Bu nedenle sadece ch.isalpha() yazmak doğrusudur.
#         print(f"'{ch}' harf mi?:", ch.isalpha())
# endregion


# region Password Validation — Rule Based Check
#! Password is valid
#? En az 16 karakterli olmalı
#* En az bir büyük harf içermeli
#* En az 1 küçük harf içermeli
#todo En az 1 noktalama işareti içermeli
#? En az 1 rakam içermeli
#todo HINT: string kütüphanesinde noktalama işaretleri hazır olarak var.
#todo Sample PWD: beast?Beast1beast
#
# Kullanılan Fonksiyonlar:
#   - len(password) → karakter sayısı
#   - str.isupper() → büyük harf mi?
#   - str.islower() → küçük harf mi?
#   - str.isdigit() → rakam mı?
#   - ch in punctuation → noktalama kontrolü
#
# any() → Döngüdeki koşullardan en az 1’i True ise True döner.

# from string import punctuation

# pwd = input("Password giriniz: ")

# Flag (bayrak) başlangıçta geçerli kabul ederiz
# is_valid = True

# if len(pwd) < 16:
#     print("❌ Password must be at least 16 characters.")
#     is_valid = False

# if not any(ch.isupper() for ch in pwd):
#     print("❌ Password must contain at least one uppercase letter.")
#     is_valid = False

# if not any(ch.islower() for ch in pwd):
#     print("❌ Password must contain at least one lowercase letter.")
#     is_valid = False

# if not any(ch.isdigit() for ch in pwd):
#     print("❌ Password must contain at least one digit.")
#     is_valid = False

# if not any(ch in punctuation for ch in pwd):
#     print("❌ Password must contain at least one punctuation symbol.")
#     is_valid = False

# if is_valid:
#     print("✔ Password is VALID")
# else:
#     print("❌ Password is INVALID")

# if (
#     len(pwd) >= 16 and
#     any(ch.isupper() for ch in pwd) and
#     any(ch.islower() for ch in pwd) and
#     any(ch.isdigit() for ch in pwd) and
#     any(ch in punctuation for ch in pwd)
# ):
#     print("✔ Password is VALID")
# endregion