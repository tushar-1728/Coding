class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        if(s):
            count1 = 1
            count2 = 0
            for i in range(len(s)-1):
                if(int(s[i]+s[i+1]) < 27):
                    count2 += 1
            print(count1, count2)


b = Solution()
print(b.numDecodings("226"))