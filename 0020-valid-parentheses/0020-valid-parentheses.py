class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list()
        for i in s:
            if len(brackets):
                if (brackets[-1] == "(" and i == ")") \
                    or (brackets[-1] == "{" and i == "}") \
                    or (brackets[-1] == "[" and i == "]"):
                    brackets.pop()
                else:
                    brackets.append(i)
            else:
                brackets.append(i)
        return not len(brackets)