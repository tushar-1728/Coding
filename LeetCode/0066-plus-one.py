class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        res = []
        if len(digits) != 0:
            for i in digits:
                s += str(i)
            s = int(s) + 1
            while(s != 0):
                res.insert(0, s%10)
                s //= 10
        return res
