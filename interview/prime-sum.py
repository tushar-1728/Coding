class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        import math
        a = []
        temp = int(math.sqrt(A))
        temp1 = []
        for i in range(A+1):
            a.append(1)
        a[0] = 0
        a[1] = 0
        for i in range(temp+1):
            if(a[i] == 1):
                for j in range(i+i, A+1, i):
                    a[j] = 0
        print(a)
        for i in range(A+1):
            if(a[i] == 1 and a[A-i] == 1):
                return [i, A-i]
B = Solution()
print(B.primesum(3))