class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        tab = []
        for i in range(n):
            tab.append([0]*n)
            tab[i][i] = 1
        for i in range(n, -1, -1):
            for j in range(i+1, n):
                if(s[i] == s[j]):
                    tab[i][j] = tab[i+1][j-1] + 2
                else:
                    tab[i][j] = max(tab[i+1][j], tab[i][j-1])
        return tab[0][n-1]


b = Solution()
print(b.longestPalindromeSubseq("bbbab"))