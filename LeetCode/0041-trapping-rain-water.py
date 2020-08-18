class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        n = len(height)
        while i < n and height[i] == 0:
            i += 1
        ltemp = rtemp = 0
        larr = []
        rarr = []
        print(i)
        for j in range(i, n):
            if height[j] > ltemp:
                ltemp = height[j]
            if height[n-j+i-1] > rtemp:
                rtemp = height[n-j+i-1]
            larr.append(ltemp)
            rarr.insert(0, rtemp)
        res = 0
        for j in range(i, n):
            temp = min(larr[j-i], rarr[j-i]) - height[j]
            res += temp
        # print(res)
        # print(larr)
        # print(rarr)
        return res


b = Solution()
print(b.trap([0,1,0,2,1,0,1,3,2,1,2,1]))