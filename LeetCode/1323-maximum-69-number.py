class Solution:
    def maximum69Number (self, num):
        num = list(str(num))
        i = 0
        while num[i] == "9":
            i += 1
        num[i] = "9"
        num = int("".join(num))
        return num


b = Solution()
print(b.maximum69Number(9669))
            