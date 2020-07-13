class Solution:
    def longestCommonPrefix(self, strs):
        if(len(strs) > 0):
            strs.sort(key=len)
            size = len(strs)
            temp = strs[0]
            i = 1
            j = len(temp)
            while(i < size and j >= 0):
                if(strs[i].startswith(temp)):
                    i += 1
                else:
                    j -= 1
                    temp = temp[:j:]
            return temp
        else:
            return ""

b = Solution()
print(b.longestCommonPrefix(["dog","racecar","car"]))
