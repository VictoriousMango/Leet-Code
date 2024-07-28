class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list()
        checker = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for i in s:
            if len(brackets) and brackets[-1] in checker.keys():
                if checker[brackets[-1]] == i:
                    brackets.pop()
                else:
                    brackets.append(i)
            else:
                brackets.append(i)
        return not len(brackets)