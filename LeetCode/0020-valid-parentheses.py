class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if i in ['(', '{', '[']:
                res.append(i)
            elif i == ')' and (len(res) == 0 or res.pop() != '('):
                return False
            elif i == '}' and (len(res) == 0 or res.pop() != '{'):
                return False
            elif i == ']' and (len(res) == 0 or res.pop() != '['):
                return False
        if len(res) == 0:
            return True
        else:
            return False

b = Solution()
print(b.isValid("]"))