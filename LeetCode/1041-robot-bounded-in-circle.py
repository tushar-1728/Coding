class Solution:
    def isRobotBounded(self, instr: str) -> bool:
        pos = [0, 0]
        direc = 0
        for i in instr:
            if i == "G":
                if direc == 0:
                    pos[1] += 1
                elif direc == 1:
                    pos[0] -= 1
                elif direc == 2:
                    pos[1] -= 1
                elif direc == 3:
                    pos[0] += 1
            elif i == "L":
                direc = (direc + 1) % 4
            elif i == "R":
                direc = (direc - 1) % 4
        # print(pos, direc)
        if(direc != 1 or pos == [0,0]):
            return True
        return False


b = Solution()
print(b.isRobotBounded("GGLLGG"))
