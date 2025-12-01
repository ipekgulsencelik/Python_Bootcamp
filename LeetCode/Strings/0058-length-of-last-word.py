# ---------------------------------------------------------
# Problem: 58. Length of Last Word
# Difficulty: Easy
# Link: https://leetcode.com/problems/length-of-last-word/
# ---------------------------------------------------------

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Bu fonksiyon verilen string içindeki *son kelimenin*
        uzunluğunu döndürür.

        Örnek:
            "Hello World"  → 5
            "   fly me   to   the moon  " → 4
        """
        # Tek satırda tüm işlem:
        # 1) rstrip → sondaki boşlukları at
        # 2) split → kelimelere ayır
        # 3) [-1] → son kelime
        # 4) len → uzunluk
        # return len(s.rstrip().split()[-1])

        # rstrip(): String'in sadece sağ tarafındaki(sonundaki) tüm boşlukları temizler.
        # Eğer bunu yapmazsak split() sonuna "" (boş string) ekleyebilir.
        cleaned = s.rstrip()

        # split(): Boşluklara göre tüm kelimeleri listeye böler.
        # Birden fazla boşluk olursa onları yok sayar.
        words = cleaned.split()

        # [-1]: Listenin son elemanı → son kelime.
        last_word = words[-1]

        # 4) len(): Son kelimenin uzunluğu.
        return len(last_word)