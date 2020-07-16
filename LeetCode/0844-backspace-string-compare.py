class Solution:
    def backspaceCompare(self, S, T):
        s = list()
        t = list()
        for i in S:
            if i == "#":
                if s:
                    s.pop()
            else:
                s.append(i)
        for i in T:
            if i == "#":
                if t:
                    t.pop()
            else:
                t.append(i)
        # print(s, t)
        if s == t:
            return True
        return False


b = Solution()
print(b.backspaceCompare("y#fo##f", "y#f#o##f"))