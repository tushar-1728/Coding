from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = min(height[i], height[j]) * (j - i)
        # print(area)
        while i < j:
            temp = min(height[i], height[j]) * (j - i)
            if temp > area:
                area = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area


b = Solution()
print(b.maxArea([1,8,6,2,5,4,8,3,7]))