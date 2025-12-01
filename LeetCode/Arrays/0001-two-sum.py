# ---------------------------------------------------------
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# ---------------------------------------------------------

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Görev:
            nums içindeki iki elemanın toplamı target oluyorsa
            bu iki elemanın indexlerini döndür.

        Yöntem:
            HashMap (dictionary) kullanıyoruz.
            - Daha önce gördüğümüz sayıları kaydediyoruz.
            - Yeni gelen sayı için 'tamamlayıcı' değeri kontrol ediyoruz.
        """

        seen = {}  # {sayı: index}

        # enumerate(nums) → hem index'i hem değeri aynı anda verir
        for i, num in enumerate(nums):
            diff = target - num  # hedefi tamamlayan sayı

            # Eğer diff daha önce görüldüyse çözüm bulundu
            if diff in seen:
                return [seen[diff], i]

            # Bu numarayı kaydet
            seen[num] = i
            
        return []


# Time Complexity: O(n)
#   - Her sayıyı yalnızca bir kez görüyoruz
#
# Space Complexity: O(n)
#   - HashMap en kötü durumda n eleman tutabilir