class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        result = ""
        tup = list(zip(word1, word2))
        for i in tup:
            result += "".join(i)
        if len1 > len2:
            result += word1[len2::]
        else:
            result += word2[len1::]
        return result

TC: O(n)
SC: O(n)
