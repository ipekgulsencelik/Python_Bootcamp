# ================================================================
# 169. Majority Element
# Zorluk: Kolay
# Bağlantı: https://leetcode.com/problems/majority-element/
# ================================================================
#
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# Example 1:
#   Input : nums = [3,2,3]
#   Output: 3
#   Explanation: There is no string in strs that can be rearranged to form "bat".
#   The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#   The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#
# Example 2:
#   Input : nums = [2,2,1,1,1,2,2]
#   Output: 2
#
# Önemli Not:
#   - Majority element'in her zaman var olduğu garanti edilmiştir.
#
# En Optimal Çözüm: Boyer–Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Dizide en çok tekrar eden majority element'i bulur.
        Majority element dizide n/2 defadan fazla görünen elemandır.

        Parametre:
            nums (list[int]): Majority element içeren dizi.

        Dönüş:
            int — majority element
        """

        count = 0       # mevcut adayın oy sayısı
        candidate = None

        for num in nums:
            # Sayı sıfırlanmışsa yeni aday seçilir
            if count == 0:
                candidate = num  # Yeni aday seçilir
            # Eğer num aday ise count arttırılır, değilse azaltılır
            count += 1 if num == candidate else -1

        return candidate  # Boyer-Moore algoritması sonucu


# Time Complexity: O(n)
#   - Dizi yalnızca 1 kez taranır.

# Space Complexity: O(1)
#   - Ekstra bellek kullanılmaz.