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
        num = 0
        temp = 0
        s = [i for i in s]
        for i in range(len(s)):
            if i > 0:
                if roman[s[i-1]] == roman[s[i]]:
                    temp += 1
                else:
                    temp = 0
                if roman[s[i-1]] < roman[s[i]]:
                    num -= 2*roman[s[i-1]] - temp
                    print(f'{s[i-1]}{s[i]} = {roman[s[i]]}-{roman[s[i-1]]} = {roman[s[i]]-roman[s[i-1]]}')
            num += roman[s[i]]
            print(f'Total : {num}')
        return num