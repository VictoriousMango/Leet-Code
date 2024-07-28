class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        loop = min(len(i) for i in strs)
        for index in range(loop):
            char_to_check = set(word[index] for word in strs)
            if len(char_to_check) == 1:
                prefix += list(char_to_check)[0]
            else:
                return prefix
        return prefix
