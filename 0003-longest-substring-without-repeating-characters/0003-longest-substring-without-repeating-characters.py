class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len([i for i in s]) == len(set([i for i in s])):
            return len(s)
        subString = dict()
        subStringCount = 1
        subString[subStringCount] = ''
        for index in range(len(s)):
            for i in s[index:]:
                if subStringCount not in subString:
                    subString[subStringCount] = ''
                if i not in subString[subStringCount]:
                    subString[subStringCount] += i
                else:
                    subStringCount += 1
                    break
                    # subString[subStringCount] = i
        print(subString)
        return max([len(subString[i]) for i in subString])