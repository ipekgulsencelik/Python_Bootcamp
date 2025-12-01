# ---------------------------------------------------------
# Problem: 27. Remove Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-element/
# ---------------------------------------------------------

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Görev:
            nums listesinden val değerine eşit olan elemanları kaldırmak.
            İşlem 'in-place' yapılır. (Yeni liste oluşturulmaz.)
            Dönüş değeri: val olmayan elemanların sayısı.

          Mantık (Two Pointers):
            - i : diziyi baştan sona tarar
            - k : val olmayan elemanların yazılacağı indeks
            nums[i] != val ise:
                nums[k] = nums[i]  → elemanı öne taşı
                k += 1             → yazılacak pozisyonu ilerlet

        Sonunda k, dizideki val olmayan eleman sayısıdır.
        """

        k = 0  # val olmayan eleman sayısı / aynı zamanda yazma pointer'ı

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # elemanı öne yaz
                k += 1             # sayacı arttır

        return k  # val olmayan eleman sayısı


# Time Complexity: O(n) - Diziyi bir kere dolaşıyoruz
# Space Complexity: O(1) - Ekstra liste yok, sabit bellek (in-place çözüm)