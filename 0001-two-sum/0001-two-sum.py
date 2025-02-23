class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                temp = nums[i]
                nums[i] = "taken"
                return [i, nums.index(target-temp)]
