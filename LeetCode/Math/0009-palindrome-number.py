# ---------------------------------------------------------
# Problem: 9. Palindrome Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/palindrome-number/
# ---------------------------------------------------------

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Görev: Verilen sayının palindrom olup olmadığını kontrol et.
        Palindrom = tersten okunuşu da aynı olan sayı.

        Örnek:
            121  → True
            123  → False
            -121 → False
        """

        # Negatifler ve 0 ile biten sayılar (0 hariç) palindrom olamaz
        # Örnek: 10 → "01" != "10"
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Sadece sayının yarısını ters çeviriyoruz
        while x > reversed_half:
            # x'in en sağdaki basamağını al:
            # Örnek: x = 123 → digit = 3
            digit = x % 10

            # reversed_half'i bir basamak sola kaydırıp yeni basamağı ekliyoruz:
            # Örnek akış:
            #   reversed_half = 0, digit = 3 → 0*10 + 3 = 3
            #   reversed_half = 3, digit = 2 → 3*10 + 2 = 32
            #   reversed_half = 32, digit = 1 → 32*10 + 1 = 321
            reversed_half = reversed_half * 10 + digit

            # x'in en sağdaki basamağını düşür:
            # Örnek: x = 123 → x //= 10 → 12
            x //= 10

        # Döngü bittiğinde iki olasılık vardır:
        #
        # 1) ÇİFT basamaklı palindrome:
        #       Örnek: 1221
        #       Son durumda:
        #           x = 12
        #           reversed_half = 12
        #       Karşılaştırma:
        #           x == reversed_half → True
        #
        # 2) TEK basamaklı palindrome:
        #       Örnek: 12321
        #       Son durumda:
        #           x = 12
        #           reversed_half = 123
        #       Ortadaki tek basamak (3) reversed_half içinde ekstra olarak duruyor.
        #       Onu atmak için reversed_half // 10 yaparız:
        #           reversed_half // 10 = 123 // 10 = 12
        #       Karşılaştırma:
        #           x == reversed_half // 10 → True
        #
        # Palindrom ise bu iki koşuldan en az birini sağlar:
        return x == reversed_half or x == reversed_half // 10


# -------------------- COMPLEXITY ANALYSIS --------------------
# Time Complexity: O(log10(n))
# -------------------------------------------------------------
# - x sayısının her adımda bir basamağını siliyoruz (x //= 10).
# - Yani döngü, sayıdaki basamak sayısının yaklaşık yarısı kadar çalışır.
# - Bir sayının basamak sayısı, sayının büyüklüğüne göre logaritmik artar:
#       n ≈ 10^k  →  k ≈ log10(n)
# - Bu nedenle zaman karmaşıklığı:
#       O(log10(n))
#
# Örnek:
#   x = 12321 → 5 basamak
#   Döngü ≈ 3 adımda biter.
# -------------------------------------------------------------
#
# Space Complexity: O(1)
# -------------------------------------------------------------
# - Ekstra dizi, liste veya string KULLANMIYORUZ.
# - Sadece birkaç integer değişken kullanıyoruz:
#       x (güncellenen giriş),
#       reversed_half,
#       digit (geçici)
# - Girdi büyüdükçe ekstra bellek ihtiyacı artmıyor.
# - Bu yüzden bellek kullanımı sabittir:
#       O(1)
# ---------------------------------------------------------