# class Solution:
#     # @param A : integer
#     # @return a strings
def findDigitsInBinary(self, A):
    res = ""
    while(A != 0):
        temp = A%2
        res += str(temp)
        A = A//2
    res = res[::-1]
    return res

print(findDigitsInBinary(6))
