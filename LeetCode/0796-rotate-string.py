class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        a = list(A)
        b = list(B)
        if a == b:
            return True
        for i in range(len(A)):
            a.append(a.pop(0))
            # print(a)
            if a == b:
                return True
        return False
        