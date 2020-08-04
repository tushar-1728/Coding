class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        n = len(s)
        i = 0
        # print(n)
        while i < n:
            lst = [-1] * 128
            count = 0
            for j in range(i,n):
                # print(i, j)
                if lst[ord(s[j])] == -1:
                    count += 1
                    lst[ord(s[j])] = j
                else:
                    if count > m:
                        m = count
                    i = lst[ord(s[j])]
                    break
            if count > m:
                m = count
            i += 1
        return m


b = Solution()
inp = input()
print(b.lengthOfLongestSubstring(inp))