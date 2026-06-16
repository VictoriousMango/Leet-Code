class Solution:
    def processStr(self, s: str) -> str:
        result = ''
        for i in s:
            if i.islower():
                result+=i
            if i == "*":
                result=result[:-1]
            if i == "#":
                result+=result
            if i == "%":
                result = result[::-1]
        return result
        