# ================================================================
# 217. Contains Duplicate
# Zorluk: Kolay
# Bağlantı: https://leetcode.com/problems/contains-duplicate/
# ================================================================
#
#  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# Example 1:
#   Input: nums = [1,2,3,1]
#   Output: true
#   Explanation: The element 1 occurs at the indices 0 and 3.
#
# Example 2:
#   Input : nums = [1,2,3,4]
#   Output: false
#   Explanation: All elements are distinct.
#
# Example  3:
#   Input : nums = [1,1,1,3,3,4,3,2,4,2]
#   Output: true
#
# Not:
#   - Amaç: Herhangi bir elemanın en az iki kez görünüp görünmediğini en hızlı şekilde tespit etmektir.

# Çözüm: HashSet Kullanımı (En Optimal Yaklaşım)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Dizi içinde tekrar eden bir eleman olup olmadığını kontrol eder.

        Parametre:
            nums (list[int]): Kontrol edilecek tam sayı dizisi.

        Dönüş:
            bool — True (tekrar varsa), False (tüm elemanlar benzersizse)
        """

        seen = set()   # Daha önce karşılaşılan değerleri tutan küme

        for num in nums:
            if num in seen:
                return True   # Daha önce gördüysek duplicate vardır
            seen.add(num)   # # İlk kez görülüyorsa kümeye ekle

        return False   # Hiç tekrar bulunmadıysa


# Time Complexity: O(n)
#   - Tüm liste bir kez dolaşılır.
#   - Set içinde arama ve ekleme ortalama O(1) maliyetlidir.

# Space Complexity: O(n)
#   - En kötü durumda tüm elemanlar kümeye eklenir (benzersizlerse).