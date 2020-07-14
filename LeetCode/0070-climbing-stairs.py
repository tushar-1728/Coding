class Solution:
    def climbStairs(self, n: int) -> int:
        l = [0,1,2]
        i = 3
        while i <= n:
            l.append(l[i-1] + l[i-2])
            i += 1
        return l[n]