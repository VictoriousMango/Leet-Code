class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        answer = ''
        numbers = [str(i) for i in range(10)]
        sign = ["+", '-']
        for i in range(len(s)):
            if s[i] in numbers:
                answer+=s[i]
            elif i == 0 and s[i] in sign:
                answer+=s[i]
            else:
                break
        if answer in sign:
            return 0
        if answer != '':
            if int(answer) > (2**31)-1:
                return (2**31)-1
            elif int(answer) < -2**31:
                return -2**31
            else:
                return int(answer)
        else:
            return 0