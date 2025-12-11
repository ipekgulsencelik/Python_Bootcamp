# ================================================================
# 53. Maximum Subarray
# Zorluk: Kolay
# Bağlantı: https://leetcode.com/problems/maximum-subarray/
# ================================================================
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# Example 1:
#   Input : nums = [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6
#   Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.
#
# Example 2:
#   Input : nums = [1]
#   Output: 1
#   Explanation: The subarray [1] has the largest sum 1.
#
# Example 3:
#   Input : nums = [5,4,-1,7,8]
#   Output: 23
#   Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.
#
# Definition:
#   - Maximum Subarray:
#       Bir dizideki **ardışık (contiguous)** elemanlardan oluşan
#       alt dizilerden en büyük toplamlı olanının toplamını bulmaktır.
#
# Çözüm: Kadane's Algorithm (One-Pass, Optimal)
# ================================================================

from typing import List


# region Solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Returns the maximum sum of a contiguous subarray.

        Approach (Kadane's Algorithm):
            - current_sum, o ana kadar devam eden en iyi alt dizi toplamını tutar.
            - max_sum, şu ana kadar gördüğümüz en büyük toplamdır.
            - Her eleman için iki seçenek vardır:
                1) Mevcut alt diziye devam etmek: current_sum + nums[i]
                2) Yeni alt diziye bu elemandan başlamak: nums[i]
            - Hangisi büyükse current_sum ona eşitlenir.
            - max_sum da current_sum ile kıyaslanarak güncellenir.
        """

        # Başlangıçta hem current_sum hem max_sum ilk elemandır.
        current_sum = nums[0]
        max_sum = nums[0]

        # İlk eleman zaten alındığı için diziyi index 1'den itibaren dolaşırız
        for num in nums[1:]:
            # Mevcut alt diziye devam mı, yoksa sıfırdan bu elemanla başlamak mı daha iyi?
            current_sum = max(num, current_sum + num)

            # Global maksimumu güncelle
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
# endregion


# Time Complexity: O(n)
#   - Dizi tek geçişte dolaşılır.
#   - Her adımda sabit sayıda işlem yapılır.

# Space Complexity: O(1)
#   - current_sum ve max_sum olmak üzere sabit sayıda değişken tutulur.
#   - Ekstra dizi, liste veya veri yapısı kullanılmaz.