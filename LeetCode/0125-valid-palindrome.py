class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = ""
        for i in s:
            if i.isalnum():
                t += i
        t1 = t[::-1]
        if t == t1:
            return True
        else:
            return False