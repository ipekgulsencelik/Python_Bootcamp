# ---------------------------------------------------------
# Problem: 412. Fizz Buzz
# Difficulty: Easy
# Link: https://leetcode.com/problems/fizz-buzz/
# ---------------------------------------------------------

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        FizzBuzz Problemi:
            - Hem 3 hem 5'in katı → "FizzBuzz"
            - Sadece 3'ün katı   → "Fizz"
            - Sadece 5'in katı   → "Buzz"
            - Hiçbirine uymuyorsa → sayının kendisi (string)
        Amaç: 1'den n'e kadar bu kurallara göre bir liste döndürmek.
        """

        # list comprehension + conditional expression
        # return [
        #     "FizzBuzz" if i % 15 == 0
        #     else "Fizz" if i % 3 == 0
        #     else "Buzz" if i % 5 == 0
        #     else str(i)
        #     for i in range(1, n + 1)
        # ]

        result = []  # Çıktıları burada biriktireceğiz

        for i in range(1, n + 1):

            # En özel durum önce kontrol edilir (3 ve 5 birlikte)
            if i % 15 == 0:
                result.append("FizzBuzz")

            # Sadece 3'e bölünüyorsa
            elif i % 3 == 0:
                result.append("Fizz")

            # Sadece 5'e bölünüyorsa
            elif i % 5 == 0:
                result.append("Buzz")

            # Hiçbirine uymuyorsa → sayı
            else:
                result.append(str(i))

        return result


# Time Complexity:  O(n)   → Döngü n kez çalışır
# Space Complexity: O(n)   → Sonuç listesi n eleman içerir