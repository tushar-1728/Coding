class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lst = [-1]
        count = 0
        length = 0
        for i in range(len(s)):
            if s[i] == "(":
                lst.append(i)
            elif s[i] == ")":
                if lst:
                    lst.pop()
                    if not(lst):
                        lst.append(i)
                    length = i - lst[-1]
                    if length > count:
                        count = length
        if length > count:
            count = length
        return count


b = Solution()
print(b.longestValidParentheses(")()(()"))
print(b.longestValidParentheses(")()()()"))
print(b.longestValidParentheses(")())())"))
