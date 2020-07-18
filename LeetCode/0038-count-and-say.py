class Solution:
    def say(self, res):
        curr = prev = res[0]
        count = 1
        curr_res = ""
        for i in range(1, len(res)):
            prev = curr
            curr = res[i]
            if prev == curr:
                count += 1
            else:
                curr_res += (str(count) + str(prev))
                count = 1
        if count != 0:
            curr_res += (str(count) + str(curr))
        return(curr_res)
    def countAndSay(self, n):
        res = "1"
        for i in range(2, n+1):
            res = self.say(res)
        return res


b = Solution()
print(b.countAndSay(2))
