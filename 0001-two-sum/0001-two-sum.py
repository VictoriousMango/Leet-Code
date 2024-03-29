class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = dict()
        for i in range(len(nums)):
            if nums[i] in solution.keys():
                return [i, solution[nums[i]]]
            solution[target - nums[i]] = i
        