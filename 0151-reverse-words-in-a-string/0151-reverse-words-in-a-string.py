class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(' ')
        while '' in s:
            s.remove('')
        return ' '.join(s[::-1])