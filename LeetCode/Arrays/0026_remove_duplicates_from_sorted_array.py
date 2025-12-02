# ---------------------------------------------------------
# Problem: 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# ---------------------------------------------------------

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Görev:
            - Sıralı (non-decreasing) bir tamsayı dizisinden tekrar eden elemanları kaldır.
            - Her unique eleman yalnızca 1 kez görünsün.
            - İşlemi in-place yap (yeni liste kullanmadan).
            - Unique eleman sayısını (k) döndür.

        Neden Bu Soruda "Two-Pointer" Kullanıyoruz?
            - Dizi sıralı olduğu için duplicate elemanlar YAN YANADIR.
            - Bu sayede:
                * i → diziyi tamamen dolaşır
                * k → unique elemanların yazılacağı index
            - i ilerlerken her yeni farklı değer bulunduğunda:
                nums[k] = nums[i]
              şeklinde dizinin başına doğru “temiz” bir liste oluşturulur.

        Pointer Görevleri:
            - i pointer:
                Diziyi baştan sona tarar → tüm elemanlara bakar.
            - k pointer:
                Şimdiye kadar bulunan unique elemanların tutulduğu pozisyon.
                Aynı zamanda unique sayısını temsil eder.

        Önemli Not:
            nums[i] != nums[i - 1] kontrolü yalnızca sıralı dizilerde işe yarar.
            Çünkü duplicate elemanlar mutlaka art arda gelir.

        Döndür:
            k → toplam benzersiz (unique) eleman sayısı
        """

        # Eğer dizi tek elemanlıysa zaten unique
        if len(nums) <= 1:
            return len(nums)

        # k → dizinin başına yazılan unique elemanların sayısı
        k = 1

        # i -> diziyi gezen pointer (1'den başlıyoruz;
        # ilk eleman zaten unique kabul edildi)
        for i in range(1, len(nums)):
            # nums[i] önceki elemandan farklı ise -> yeni bir unique değer
            if nums[i] != nums[i - 1]:  # Bir öncekiyle aynı değilse
                nums[k] = nums[i]   # Unique elemanı başa yaz
                k += 1  # bir sonraki unique yazım noktası ve unique sayısı

        # print("Unique Count (k): ", k)
        # print("Modified nums (first k):", nums[:k])
        # print("Ignored nums (rest):    ", nums[k:])
        
        # for i in range(k, len(nums)):
        #     nums[i] = "_"

        # print(f"Unique Count (k): {k}, Modified nums = {nums}")

        return k       


# Time Complexity: O(n)
#   - Döngü diziyi yalnızca 1 kez baştan sona tarar.

# Space Complexity: O(1)
#   - Ekstra liste YOK. İşlem tamamen bir dizi üzerinde yapılır (in-place)