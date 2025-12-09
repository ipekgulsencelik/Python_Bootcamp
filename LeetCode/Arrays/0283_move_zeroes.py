# ================================================================
# 283. Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/
# ================================================================

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example 1:
#   Input:  nums = [0,1,0,3,12]
#   Output: [1,3,12,0,0]
#
# Example 2:
#   Input:  nums = [0]
#   Output: [0]
#
# Not:
#   - İşlem mutlaka "in-place" yapılmalıdır (yeni liste oluşturulamaz).
#   - Non-zero değerlerin sırası bozulmamalıdır.
#
# En Optimal Çözüm: Two-Pointer


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Listedeki tüm 0'ları sona taşır ve 0 olmayan elemanların
        sırasını korur. İşlem, liste üzerinde doğrudan (in-place) yapılır.

        Parametre:
            nums (list[int]): Üzerinde değişiklik yapılacak liste.
        """

        # j → 0 olmayan değerlerin yazılacağı pozisyon
        j = 0

        # Tüm 0 olmayan elemanları listenin başına sırayla tek tek yaz
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Kalan tüm pozisyonları 0 ile doldur
        while j < len(nums):
            nums[j] = 0
            j += 1


# Time Complexity:  O(n)
#   - Liste yalnızca 1 kez baştan sona taranır

# Space Complexity: O(1)
#   - No extra array is allocated; all modifications done in-place.