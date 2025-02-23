class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_allValues = set(i for i in range(1, len(nums)+1))
        return list(set_allValues.difference(set(nums)))