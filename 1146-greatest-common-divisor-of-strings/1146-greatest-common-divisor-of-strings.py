class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        if str2 not in str1:
            return ""
        elif str2*(len(str1)//len(str2)) == str1:
            return str2
        else:
            for i in range(len(str2)):
                if str2[:len(str2)-i]*(len(str1)//len(str2[:len(str2)-i])) == str1 \
                    and str2[:len(str2)-i]*(len(str2)//len(str2[:len(str2)-i])) == str2:
                    return str2[:len(str2)-i]
            else:
                return ''

            # index = 0
            # GCD = ""
            # while index < min(len(str1), len(str2)):
            #     if str1[index] == str2[index]:
            #         GCD += str1[index]
            #         index+= 1
            #         if GCD*(len(str1)//len(GCD)) == str1:
            #             return GCD
            #     else:
            #         return ""
            # return ""
                