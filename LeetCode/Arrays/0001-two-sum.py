# ---------------------------------------------------------
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# ---------------------------------------------------------

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
            complement = target - num  # hedefi tamamlayan sayı

            # Eğer complement daha önce görüldüyse çözüm bulundu
            if complement in seen:
                return [seen[complement], i]

            # Bu numarayı kaydet
            seen[num] = i

        # LeetCode'a göre her zaman çözüm var, bu satır teknik olarak çalışmaz
        return []


# Time Complexity: O(n)
#   - Her sayıyı yalnızca bir kez görüyoruz
#
# Space Complexity: O(n)
#   - HashMap en kötü durumda n eleman tutabilir