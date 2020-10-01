from typing import List
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        res = 0
        if n > 0:
            prev = timeSeries[0]
            for i in range(1, n):
                curr = timeSeries[i]
                diff = curr - prev
                if diff < duration:
                    res += diff
                else:
                    res += duration
                prev = curr
            res += duration
        return res

b = Solution()
print(b.findPoisonedDuration([1,2,3,4,5], 5))