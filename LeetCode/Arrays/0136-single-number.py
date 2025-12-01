# ---------------------------------------------------------
# Problem: 136. Single Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/single-number/
# ---------------------------------------------------------

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Verilen tam sayı listesindeki tüm elemanlardan
        sadece 1 tanesi tek sayıda (1 kez) bulunur,
        diğer tüm elemanlar 2'şer kez bulunur.
        Görev: Bu 'tek' olan sayıyı bulup döndürmek.

        Örnek:
            nums = [4, 1, 2, 1, 2]  → 4
        """

         """
        Bu çözümde LISTE yerine SET (küme) kullanarak
        tek geçilen sayıyı buluruz.

        Mantık:
            - Bir sayı ilk kez geliyorsa sete ekle
            - Aynı sayı ikinci kez geliyorsa setten çıkar
            - Çift tekrar eden tüm sayılar sonunda yok olur
            - Sette yalnızca TEK geçen sayı kalır → sonuç

        Örnek:
            nums = [4, 1, 2, 1, 2]
            İşlem:
                {} → {4} → {4,1} → {4,1,2} → {4,2} → {4}
            Cevap = 4
        """

        seen = set()  # benzersiz elemanları tutan küme

        for num in nums:
            if num in seen:
                # ikinci kez geliyorsa → yok et
                seen.remove(num)
            else:
                # ilk kez geliyorsa → ekle
                seen.add(num)

        # sette tek bir sayı kalır → pop() ile alınır
        return seen.pop()


# Time Complexity:  O(n)
#   - 'in', 'add', 'remove' işlemleri amortized O(1)

# Space Complexity: O(n)
#   - Sette en fazla n/2 eleman birikebilir