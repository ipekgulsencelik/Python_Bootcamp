# ---------------------------------------------------------
# Problem: 1672. Richest Customer Wealth
# Difficulty: Easy
# Link: https://leetcode.com/problems/richest-customer-wealth/
# ---------------------------------------------------------

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        """
        Bu fonksiyon, bankadaki müşterilerin hesaplarını temsil eden
        'accounts' matrisindeki her satırı inceler ve her müşterinin
        toplam parasını hesaplar. En zengin müşterinin toplam parasını döndürür.

        accounts: 2D liste (matris)
            Örnek:
                [
                    [1, 2, 3],   → 1. müşteri
                    [3, 2, 1]    → 2. müşteri
                ]
        """

        # Her satırın toplamını al ve en büyüğünü döndür
        # return max(sum(customer) for customer in accounts)

        max_wealth = 0  # Şu ana kadar bulunan en yüksek toplam (başlangıçta sıfır)

        # accounts yapısındaki her müşteri için döngü:
        # 'customer' → örneğin [1, 2, 3]
        for customer in accounts:

            # sum(customer):
            # listenin tüm elemanlarını toplar
            # Örnek:
            # customer = [1, 2, 3] → sum(...) = 6
            total = sum(customer)

            # Bu müşterinin toplam parası (total),
            # şu ana kadarki en yüksek (max_wealth) değerden fazlaysa
            # yeni en büyük değer olarak bunu güncelle.
            if total > max_wealth:
                max_wealth = total

        # Döngü bittiğinde tüm müşteriler incelenmiş olur.
        # Artık max_wealth → en zengin müşterinin toplam parasıdır.
        return max_wealth


# Time Complexity: O(n * m)
#   n = müşteri sayısı
#   m = her müşterideki hesap sayısı
#   Tüm elemanlara birer kez bakıldığı için n*m kadar işlem yapılır.

# Space Complexity: O(1)
#   Ekstra büyük bir veri yapısı kullanılmadı.
#   Sadece birkaç değişken → max_wealth ve total.