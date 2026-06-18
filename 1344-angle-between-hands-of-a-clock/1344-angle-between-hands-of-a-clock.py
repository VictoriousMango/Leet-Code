class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 30*(hour%12) + 0.5*(minutes)
        min_angle = 30*(minutes/5)
        diff = abs(hour_angle - min_angle)
        return min(diff, 360-diff)