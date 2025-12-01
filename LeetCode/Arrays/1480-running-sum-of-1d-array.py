# ---------------------------------------------------------
# Problem: 1480. Running Sum of 1D Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
# ---------------------------------------------------------

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        Bu fonksiyon verilen listenin 'running sum' yani
        kümülatif toplamını döndürür.

        Örnek:
            nums = [1, 2, 3]
            Çıktı = [1, 3, 6]
        """

        running = []     # Sonuç listesi
        current_sum = 0  # O ana kadarki toplam

        for num in nums:
            current_sum += num   # elemanı toplama ekle
            running.append(current_sum)  # sonucu listeye ekle

        return running

# Time Complexity: O(n)  - diziyi bir kez dolaşıyor
# Space Complexity: O(n) - yeni bir liste oluşturuyor
