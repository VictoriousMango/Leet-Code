class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        for index in range(max(len(word1), len(word2))):
            if index < len(word1):
                ans+=word1[index]
            if index < len(word2):
                ans+=word2[index]
        return ans