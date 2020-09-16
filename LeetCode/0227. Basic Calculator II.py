class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace('/', '//')
        # print(s)
        return eval(s)


b = Solution()
print(b.calculate("14/3*2"))