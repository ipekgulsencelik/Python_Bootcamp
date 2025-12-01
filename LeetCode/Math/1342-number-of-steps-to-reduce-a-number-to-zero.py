# ---------------------------------------------------------
# Problem: 1342. Number of Steps to Reduce a Number to Zero
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# ---------------------------------------------------------

class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        Bu fonksiyon verilen 'num' sayısını 0'a indirmek için
        gereken adım sayısını döndürür.

        Kurallar:
            - Eğer sayı çiftse → 2'ye böl
            - Eğer sayı tekse  → 1 çıkar

        Örnek:
            Input : 14
            Adımlar:
                14 → 7  (çift → yarıya böl)
                7  → 6  (tek → bir azalt)
                6  → 3  (çift → yarıya böl)
                3  → 2  (tek → bir azalt)
                2  → 1  (çift → yarıya böl)
                1  → 0  (tek → bir azalt)
            Sonuç: 6 adım
        """

        steps = 0  # Yapılan işlem sayısını tutan sayaç

        # num sıfır olana kadar devam eder
        while num > 0:

            # Eğer sayı çiftse → 2'ye böl
            if num % 2 == 0:
                num //= 2  # tam bölme (ondalık yok)

            # Yoksa sayı tekse → 1 çıkar
            else:
                num -= 1

            # Her işlem bir adımdır
            steps += 1

        # Toplam adım sayısını döndür
        return steps

# Time Complexity:  O(log n)   → Sayı her bölmede yarıya düşüyor
# Space Complexity: O(1)       → Ekstra bellek kullanılmıyor