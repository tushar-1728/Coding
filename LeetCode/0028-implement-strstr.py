class Solution:
    def strStr(self, haystack, needle):
        if needle:
            return haystack.find(needle)
        else:
            return 0

b = Solution()
print(b.strStr(haystack = "hello", needle = "ll"))