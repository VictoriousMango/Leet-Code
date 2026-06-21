class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs = sorted(costs)
        while True:
            if count >= len(costs):
                break
            if coins >= costs[count]:
                coins-=costs[count]
                count+=1
            else:
                break
        return count