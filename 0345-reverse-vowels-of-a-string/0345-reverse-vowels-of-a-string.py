class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [i for i in s]
        ptr1 = 0
        ptr2 = len(s)-1
        V_regex = ['a', 'e', 'i', 'o', 'u']
        count = 0
        while ptr1 < ptr2:
            # print(f'{count} : {s[ptr1]}, {s[ptr1] in V_regex} - {s[ptr2]}, {s[ptr2] in V_regex}')
            if s[ptr1].lower() in V_regex and s[ptr2].lower() in V_regex:
                # print("Swapping required")
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                if ptr1 < len(s) and ptr2 > 0:
                    ptr1 +=1
                    ptr2 -=1
                
            if s[ptr1].lower() not in V_regex and ptr1 < len(s):
                ptr1 += 1
            if s[ptr2].lower() not in V_regex and ptr2 > 0:
                ptr2 -= 1
            count +=1
        # print(s)
        return ''.join(s)
