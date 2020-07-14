class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = list(s.split())
        if len(l) != 0:
            return len(l[-1])
        else:
            return 0
