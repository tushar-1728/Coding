class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        temp = bin(num)
        temp = temp[2::]
        c0 = 0
        c1 = 0
        for i in temp:
            if i == "0":
                c0 += 1
            else:
                c1 += 1
        if c1 == 1 and c0 % 2 == 0:
            return True
        else:
            return False