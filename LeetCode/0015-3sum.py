class Solution:
    def threeSum(self, nums):
        n = len(nums)
        d = dict()
        if n%2 == 0:
            h = n//2
        else:
            h = (n+1)//2
        for i in range(n):
            base = nums[i]
            for j in range(i):
                tot = base + nums[j]
                if tot in d.keys():
                    d[tot].append([i, j])
                else:
                    d[tot] = [[i,j]]
            for j in range(i, n):
                tot = base + nums[j]
                if tot in d.keys():
                    d[tot].append([i, j])
                else:
                    d[tot] = [[i,j]]
        print(d)
        print(nums)


b = Solution()
b.threeSum([1,2,3])
