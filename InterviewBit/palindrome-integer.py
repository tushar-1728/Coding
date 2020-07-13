class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        t = list(str(A))
        t.reverse()
        t1 = ""
        for i in t:
            t1 += str(i)
        t1 = int(t1)
        # print(t1)
        if(t1 == A):
            return 1
        else:
            return 0

B = Solution()
print(B.isPalindrome(121))