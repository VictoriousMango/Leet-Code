class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for index in range(min(len(word1), len(word2))):
            result += word1[index] + word2[index]
        index+=1
        while len(word1)-index > 0:
            result += word1[index]
            index+=1
        while len(word2)-index > 0:
            result += word2[index]
            index+=1
        return result
        