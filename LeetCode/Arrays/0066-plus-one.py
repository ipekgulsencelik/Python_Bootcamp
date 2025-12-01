# ---------------------------------------------------------
# Problem: 66. Plus One
# Difficulty: Easy
# Link: https://leetcode.com/problems/plus-one/
# ---------------------------------------------------------

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Verilen 'digits' listesi bir sayıyı temsil eder.
        Amacımız bu sayıya 1 ekleyip sonucu yine basamak listesi
        olarak döndürmektir.

        Örnek:
            [1,2,3] → 123 + 1 = 124 → [1,2,4]
            [9,9]   → 99 + 1  = 100 → [1,0,0]
        """

       # Listeyi ters çevirerek sağdan sola işlem yapmayı kolaylaştırıyoruz
        digits = digits[::-1]

        for i in range(len(digits)):

            # 9 değilse doğrudan +1 yapıp geri döneriz
            if digits[i] != 9:
                digits[i] += 1
                return digits[::-1]   # tekrar orijinal sıraya döndür

            # 9 ise elde var → o basamak 0 olur
            digits[i] = 0

        # Tüm basamaklar 9 ise:
        # Örn: [9,9,9] → [1,0,0,0]
        return [1] + digits[::-1]


# Time Complexity: O(n)  - Listeyi sağdan sola bir kez dolaşır
# Space Complexity: O(1)  - Ekstra büyük yapı yok