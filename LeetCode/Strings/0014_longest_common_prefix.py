# ================================================================
# 14. Longest Common Prefix
# Zorluk: Kolay
# Bağlantı: https://leetcode.com/problems/longest-common-prefix/
# ================================================================
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#   Input: strs = ["flower","flow","flight"]
#   Output: "fl"
#
# Example 2:
#   Input: strs = ["dog","racecar","car"]
#   Output: ""
#   Explanation: There is no common prefix among the input strings.
# ===============================================================

# Çözüm: Horizontal Scanning


# region Solution
def longest_common_prefix(strs):
    """
    Returns the longest common prefix among a list of strings.

    Approach (Horizontal Scanning):
        - İlk stringi başlangıç prefix'i olarak kabul ederiz.
        - Listedeki her bir string ile bu prefix'i karşılaştırırız.
        - Eğer mevcut string bu prefix ile başlamıyorsa:
              prefix = prefix[:-1]  (sondan bir karakter kırpılır)
        - Prefix tamamen boşalırsa ortak prefix yoktur → "" döneriz.
        - Diğer tüm stringler prefix ile başlıyorsa sonuç bulunmuştur.
    """

    # Edge case: boş liste → direkt return
    if not strs:
        return ""

    # İlk string referans prefix olarak alınır
    prefix = strs[0]

    # Diğer stringlerle prefix karşılaştırılır
    for s in strs[1:]:
        # prefix, s ile başlamadığı sürece prefix küçültülür
        while not s.startswith(prefix):
            prefix = prefix[:-1]    # prefix'i sondan bir karakter azalt

            # prefix tamamen boşalırsa ortak prefix yoktur
            if prefix == "":
                return ""

    return prefix
# endregion


# Time Complexity: O(n * m)
#       n → string sayısı
#       m → en kısa string uzunluğu
#   - En kötü durumda:
#       Toplam işlem sayısı, dizideki tüm stringlerin toplam karakter uzunluğu kadar olacaktır.

# Space Complexity: O(1)
#   - Ek bir dizi, liste veya veri yapısı oluşturulmaz.
#   - Sadece:
#         * prefix → başlangıç stringine referans
#         * s      → döngüde işlenen mevcut string
#     gibi sabit miktarda değişken kullanılır.
#
#   - Bu nedenle ek bellek tüketimi sabit kabul edilir.