class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(' ')[::-1]
        while '' in s:
            s.remove('')
        return ' '.join(s)