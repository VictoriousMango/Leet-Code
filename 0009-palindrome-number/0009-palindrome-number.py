class Solution:
    def isPalindrome(self, x: int) -> bool:
        p_checker = [i for i in str(x)]
        loop = len(p_checker)//2 if len(p_checker)%2 == 0 else (len(p_checker)+1)//2
        for i in range(loop):
            if p_checker[i] != p_checker[-(i+1)]:
                return False
        return True
            
        