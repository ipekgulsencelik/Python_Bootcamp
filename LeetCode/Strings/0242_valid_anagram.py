# ================================================================
# 242. Valid Anagram
# Zorluk: Kolay
# Bağlantı: https://leetcode.com/problems/valid-anagram/
# ================================================================
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# Example 1:
#   Input : s = "anagram", t = "nagaram"
#   Output: true
#
# Example 2:
#   Input : s = "rat", t = "car"
#   Output: false
#
# Anagram:
#       - İki kelimenin aynı harfleri aynı sayıda içermesi gerekir.
#       - Harflerin sırası önemli değildir.

# Çözüm: Counter (Pythonic ve en kısa çözüm)

from collections import Counter   # ✔ Counter import edilmeli

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        İki string'in anagram olup olmadığını kontrol eder.

        Parametreler:
            s (str): Birinci kelime
            t (str): İkinci kelime

        Dönüş:
            bool — True: anagram ise, False: değilse
        """

        # Counter(s) → s içindeki her harfin sayısını tutan bir map
        # İki Counter eşitse, harfler ve adetleri birebir aynıdır → anagramdır.
        return Counter(s) == Counter(t)

        # region Alternative — Sorting
        # Uzunluklar farklıysa zaten anagram olamaz
        # if len(s) != len(t):
        #     return False

        # Sıralanmış hâllerini kıyasla
        # return sorted(s) == sorted(t)
        # endregion


# Time Complexity: O(n)
#   - Counter(s) ve Counter(t) işlemleri toplam O(n) zaman alır.

# Space Complexity: O(1)
#   - sadece küçük harfler kullanılıyor → en fazla 26 farklı anahtar tutulur.
#   - Bu nedenle ek bellek sabit kabul edilir.

# Time Complexity (Sorting):  O(n log n)
#   - sorted(s) ve sorted(t) her biri O(n log n) zaman alır.

# Space Complexity (Sorting):  O(n)
#   - sorted() fonksiyonu yeni bir liste döndürdüğü için, orijinal string uzunluğu kadar ek bellek kullanılır.