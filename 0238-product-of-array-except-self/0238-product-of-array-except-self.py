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
        # index_pre = 0
        # index_post = len(nums)-1
        # prefix = [nums[index_pre]]
        # postfix = [nums[index_post]]
        # index_pre, index_post = index_pre+1, index_post-1
        # while index_pre < len(nums):
        #     prefix.append(nums[index_pre] * prefix[index_pre-1])
        #     postfix.append(nums[index_post] * postfix[index_pre-1])
        #     index_pre+=1
        #     index_post-=1
        # print(prefix)
        # postfix = postfix[::-1]
        # print(postfix)
        # return [prefix[i]*postfix[i] for i in range(len(nums))]
            

            


        return []
        