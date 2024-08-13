class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [i if (i+extraCandies) >= max(candies) else 0 for i in candies]