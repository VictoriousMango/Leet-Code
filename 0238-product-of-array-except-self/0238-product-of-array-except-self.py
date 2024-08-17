class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        answer = [1 for i in range(len(nums))]
        prefix = 1
        postfix = 1
        # Multiplying Left Sub-string
        for i in range(len(nums)):
            if i >= 1:
                prefix *= nums[i-1]
            answer[i] *= prefix
        
        # Multiplying Right Sub-string
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                postfix *= nums[i+1]
            answer[i] *= postfix
        return answer       
        