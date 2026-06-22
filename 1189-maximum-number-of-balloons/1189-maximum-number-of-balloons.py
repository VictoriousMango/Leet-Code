class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = {KEY: 0 for KEY in "balloon"}
        print(word)
        for i in text.lower():
            if i in word:
                word[i]+=1
        count = 0
        while word['b']>=1 and word['a'] >=1 and word['l']>=2 and word['o']>=2 and word['n']>=1:
            count+=1
            word['b']-=1 
            word['a']-=1 
            word['l']-=2 
            word['o']-=2 
            word['n']-=1
        return count