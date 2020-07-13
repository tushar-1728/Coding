class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if(A == 1):
            return 1
        import math
        a = int(math.sqrt(A))
        for i in range(2,a+1):
            temp = math.log(A, i)
            temp = round(temp, 10)
            # print(temp)
            if(math.ceil(temp) == int(temp)):
                return 1
        return 0

b = Solution()
print(b.isPower(625*25))