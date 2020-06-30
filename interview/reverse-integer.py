class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if(A>=0):
            sign = 1
        else:
            sign = -1
            A = A*sign
        t = list(str(A))
        t.reverse()
        t1 = ""
        for i in t:
            t1 += str(i)
        t1 = int(t1)
        if t1 > 2147483648:
            return 0
        return t1*sign

B = Solution()
print(B.reverse(2147483649))
