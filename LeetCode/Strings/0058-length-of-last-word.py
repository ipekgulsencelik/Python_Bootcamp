# ---------------------------------------------------------
# Problem: 58. Length of Last Word
# Difficulty: Easy
# Link: https://leetcode.com/problems/length-of-last-word/
# ---------------------------------------------------------

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
    
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
    
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Bu fonksiyon verilen string içindeki *son kelimenin*
        uzunluğunu döndürür.

        Örnek:
            "Hello World"  → 5
            "   fly me   to   the moon  " → 4
        """

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
    
        # Tek satırda tüm işlem:
        # 1) rstrip → sondaki boşlukları at
        # 2) split → kelimelere ayır
        # 3) [-1] → son kelime
        # 4) len → uzunluk
        # return len(s.rstrip().split()[-1])


# Time Complexity:  O(n)
#     - rstrip() ve split() fonksiyonlarının her ikisi de stringi birer kez tarar.

# Space Complexity: O(n)
#     - split() tüm kelimeleri tutan bir liste oluşturduğu için ek bellek kullanır.