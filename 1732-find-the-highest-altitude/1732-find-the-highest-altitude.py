class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        curr_altitude = 0
        for g in gain:
            curr_altitude += g
            result = max(curr_altitude, result)
        return result
        