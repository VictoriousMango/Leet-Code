class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        num = roman[s[0]]
        s = [i for i in s]
        for i in range(1, len(s)):
            if roman[s[i-1]] < roman[s[i]]:
                num -= 2*roman[s[i-1]]
            num += roman[s[i]]      
        return num