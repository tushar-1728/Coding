class Solution:
    def c_sum(self, n):
        res = 0
        while n > 0:
            res += (n%10) ** 2
            n //= 10
        return res


    def isHappy(self, n):
        if n < 10 and(n == 1 or n== 7):
            return True
        else:
            total = self.c_sum(n)
            while total > 9:
                total = self.c_sum(total)
            if total == 7 or total == 1:
                return True
            else:
                return False


b = Solution()
print(b.isHappy(19))