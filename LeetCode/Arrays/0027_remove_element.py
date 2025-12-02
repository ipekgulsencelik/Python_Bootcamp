# ---------------------------------------------------------
# Problem: 27. Remove Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-element/
# ---------------------------------------------------------

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

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

        for num in nums:
            if num != val:
                nums[k] = num       # elemanı öne yaz
                k += 1              # sayacı arttır

        # print(f"Total elements NOT equal to val (k): {k}")
        # print(f"Final nums array (first k matter):   {nums}")
        # print(f"First k elements: {nums[:k]}")
        # print(f"Ignored elements: {nums[k:]}")

        return k  # val olmayan eleman sayısı


# Time Complexity: O(n) 
#   - liste yalnızca 1 kez baştan sona taranır

# Space Complexity: O(1) 
#   - Ekstra liste yok, sabit bellek (in-place çözüm)