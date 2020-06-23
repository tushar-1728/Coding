class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # n = 5
        # k = 9
        from math import ceil
        inp = []
        opt = ""
        temp = 1
        for i in range(1, n+1):
            inp.append(i)
            temp *= i
        temp //= n
        while(len(inp) > 1):
            temp1 = int(ceil(k/temp) - 1)
            opt += str(inp[temp1])
            inp.pop(temp1)
            k = k - (temp * temp1)
            temp = temp // len(inp)
        opt += str(inp[0])
        print(opt)