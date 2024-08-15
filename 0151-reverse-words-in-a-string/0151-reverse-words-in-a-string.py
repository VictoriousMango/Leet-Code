class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(map(str, s.split()))[::-1]
        # while '' in s:
        #     s.remove('')
        return ' '.join(s)