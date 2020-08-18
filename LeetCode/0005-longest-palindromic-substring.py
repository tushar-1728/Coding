class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palindrome = [0,0]
        for i in range(0, n):
            lindex = i - 1
            rindex = i + 1
            while lindex >= 0 and rindex <= n-1 and s[lindex] == s[rindex]:
                lindex -= 1
                rindex += 1
            if rindex - lindex > palindrome[1] - palindrome[0]:
                palindrome = [lindex, rindex]
        for i in range(n - 1):
            if s[i] == s[i+1]:
                lindex = i - 1
                rindex = i + 2
                while lindex >= 0 and rindex <= n-1 and s[lindex] == s[rindex]:
                    lindex -= 1
                    rindex += 1
                if rindex - lindex > palindrome[1] - palindrome[0]:
                    palindrome = [lindex, rindex]
        return s[palindrome[0] + 1: palindrome[1]]


b = Solution()
print(b.longestPalindrome("abadea"))