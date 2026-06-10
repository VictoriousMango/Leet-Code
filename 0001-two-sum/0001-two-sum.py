class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for idx, ele in enumerate(nums):
            if target-ele in hashmap:
                return [hashmap[target-ele], idx]
            if ele not in hashmap:
                hashmap[ele]=idx

        