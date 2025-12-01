# ---------------------------------------------------------
# Problem: 1342. Number of Steps to Reduce a Number to Zero
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# ---------------------------------------------------------

# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# Example 1:
# Input: num = 14
# Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.

# Example 2:
# Input: num = 8
# Output: 4
# Explanation: 
# Step 1) 8 is even; divide by 2 and obtain 4. 
# Step 2) 4 is even; divide by 2 and obtain 2. 
# Step 3) 2 is even; divide by 2 and obtain 1. 
# Step 4) 1 is odd; subtract 1 and obtain 0.

# Example 3:
# Input: num = 123
# Output: 12

class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        Bu fonksiyon verilen 'num' sayısını 0'a indirmek için
        gereken adım sayısını döndürür.

        Kurallar:
            - Eğer sayı çiftse → 2'ye böl
            - Eğer sayı tekse  → 1 çıkar

        Örnek:
            Input : 14
            Adımlar:
                14 → 7  (çift → yarıya böl)
                7  → 6  (tek → bir azalt)
                6  → 3  (çift → yarıya böl)
                3  → 2  (tek → bir azalt)
                2  → 1  (çift → yarıya böl)
                1  → 0  (tek → bir azalt)
            Sonuç: 6 adım
        """

        steps = 0  # Yapılan işlem sayısını tutan sayaç

        # num sıfır olana kadar devam eder
        while num > 0:

            # Eğer sayı çiftse → 2'ye böl
            if num % 2 == 0:
                num //= 2  # tam bölme (ondalık yok)

            # Yoksa sayı tekse → 1 çıkar
            else:
                num -= 1

            # Her işlem bir adımdır
            steps += 1

        # Toplam adım sayısını döndür
        return steps

# Time Complexity:  O(log n)   → Sayı her bölmede yarıya düşüyor
# Space Complexity: O(1)       → Ekstra bellek kullanılmıyor