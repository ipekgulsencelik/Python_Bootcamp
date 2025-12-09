# ===============================================================
# MAP + LAMBDA — E-MAIL GENERATION 
# ===============================================================
# AMAÇ:
#   3–4 kelimelik isimlerden bile e-mail üretmek (inline işlem)
#
# TEKNİK:
#   ✔ map()  → listedeki her elemana bir işlem uygular
#   ✔ lambda → küçük, isimsiz fonksiyon tanımı için
#
# NOT:
#   - İsimler 1, 2, 3 veya 4 kelimeden oluşabilir
#   - Boşluklar '.' ile değiştirilir
#   - Türkçe karakterler sadeleştirilir (ç→c, ğ→g, ı→i, ö→o, ş→s, ü→u)
# ===============================================================


# region Generate Outlook E-mail from Full Names — map + lambda

domain_name = "@outlook.com"

full_names = [
    "Burak Yılmaz",
    "  Hakan    Yilmaz  ",
    "İpek Gülşen Çelik",
    "Ali Veli Hasan Mehmet"
]

# NOT:
#   - strip()        → kenar boşlukları(baş/son boşlukları) temizler
#   - lower()        → küçük harfe çeviririr
#   - replace(...)   → Türkçe karakterleri düzeltir
#   - split()        → birden fazla boşluğu tek boşluğa indirir ve kelimeleri liste yapar
#   - replace(" ", ".") → isimleri nokta ile birleştirir

# Normalize → temizle, küçült, Türkçe karakterleri düzelt, split et
emails_list = list(
    map(
        lambda x: (
            # 1) Kenar boşlukları temizle + küçült
            x.strip().lower()
            # 2) Türkçe karakterleri sadeleştir
            .replace("ç", "c").replace("ğ", "g").replace("ı", "i")
            .replace("ö", "o").replace("ş", "s").replace("ü", "u")
            .replace("İ", "i")
            # 3) Fazla boşlukları tek boşluğa indir
            .split()      # ["ali","veli","hasan","mehmet"]
        ),                 
        full_names
    )
)

# emails_list şu anda:
# [
#   ['burak','yilmaz'],
#   ['hakan','yilmaz'],
#   ['ipek','gulsen','celik'],
#   ['ali','veli','hasan','mehmet']
# ]

# Şimdi listeleri '.' ile birleştirip domain ekliyoruz:
# ilk ve son kelime → ad.soyad + @domain
emails_list = list(
    map(lambda lst: lst[0] + "." + lst[-1] + domain_name, emails_list)
)

print("=== FULL NAME → E-MAIL GENERATION ===")
print("İsim listesi :", full_names)
print("Üretilen mail listesi:")
for mail in emails_list:
    print("  -", mail)

# endregion