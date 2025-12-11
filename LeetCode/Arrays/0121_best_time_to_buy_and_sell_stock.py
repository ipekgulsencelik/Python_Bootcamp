# ================================================================
# 121. Best Time to Buy and Sell Stock
# Zorluk: Kolay
# Bağlantı: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# ================================================================
#
# You are given an array prices where prices[i] is the price of a given stock on the i'th day.
#
# You want to maximize your profit by choosing:
#   - a single day to buy one stock and 
#   - choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Example 1:
#   Input : prices = [7, 1, 5, 3, 6, 4]
#   Output: 5
#   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#   Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
#   Input : prices = [7, 6, 4, 3, 1]
#   Output: 0
#   Explanation: In this case, no transactions are done and the max profit = 0.
#
# Definition:
#   - Maksimum kar, "minimum alış fiyatı" ile "o fiyattan sonra gelen
#     maksimum satış fiyatı" arasındaki farktır.
#   - Amaç: Diziyi tararken en düşük alış fiyatını bulup, her adımda bu fiyattan
#           satış yapıldığında elde edilecek karı hesaplayarak maksimum karı belirlemektir.
#
# Çözüm: One-Pass Linear Scan (Optimal)
# ================================================================

from typing import List


# region Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Returns the maximum profit achievable by buying on one day and
        selling on a future day.

        Approach (One-Pass):
            - Bir 'min_price' değişkeni tutarak şimdiye kadarki en düşük fiyatı izleriz.
            - Her yeni fiyat için:
                * Bugün satış yapılsa kar ne olur? (price - min_price)
                * Bu kar, max_profit'ten büyükse güncellenir.
            - Eğer fiyat, min_price'tan küçükse:
                * Daha iyi bir alış fiyatı bulduğumuz için min_price güncellenir.
            - Dizi sonunda max_profit döndürülür.
        """

        min_price = float('inf')   # Şimdiye kadarki en düşük alış fiyatı
        max_profit = 0             # Maksimum elde edilen kar

        for price in prices:
            # Daha düşük bir alış fiyatı bulundu → alış noktasını güncelle
            if price < min_price:
                min_price = price
            else:
                # Bu fiyattan satarsak oluşan kar
                profit = price - min_price
                # Büyük kar varsa güncelle
                if profit > max_profit:
                    max_profit = profit

        return max_profit
# endregion


# Time Complexity: O(n)
#   - Dizi bir kez taranır
#   - Her adım sabit zamanlı işlemler yapar.

# Space Complexity: O(1)
#   - Sadece min_price ve max_profit değişkenleri tutulur.
#   - Ekstra dizi, liste veya yardımcı yapı yoktur.