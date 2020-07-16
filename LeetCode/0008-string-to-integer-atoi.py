class Solution:
    def myAtoi(self, s):
        s = s.lstrip()
        l = list("0123456789")
        if s:
            res = 0
            count = 0
            flag = 1
            for i in s:
                if(count == 0 and i in ["+", "-"]):
                    if(i == "+"):
                        flag = 1
                    elif(i == "-"):
                        flag = -1
                    count += 1
                elif(i in l):
                    res = res * 10 + int(i)
                    count += 1
                else:
                    break
            res *= flag
            b_value = 2**31
            if res < -(b_value):
                return -(b_value)
            elif res > b_value - 1:
                return b_value - 1
            return res
        return 0


b = Solution()
print(b.myAtoi("  0000000000012345678"))