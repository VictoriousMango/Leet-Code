class Solution:
    def reverse(self, x: int) -> int:
        result = int(''.join([i for i in str(x)][::-1])) if x >= 0 else -1*(int(''.join([i for i in str(x)[1:]][::-1])))
        if result < -2**31 or result > ((2**31) -1):
            return 0
        return result
        