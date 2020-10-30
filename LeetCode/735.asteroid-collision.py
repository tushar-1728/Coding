#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        res = []
        top, i = -1, 0
        while i < n:
            if top == -1:
                res.append(asteroids[i])
                top += 1
                i += 1
            elif res[top] > 0 and asteroids[i] < 0:
                if abs(res[top]) == abs(asteroids[i]):
                    top -= 1
                    i += 1
                    res.pop()
                elif abs(res[top]) < abs(asteroids[i]):
                    top -= 1
                    res.pop()
                else:
                    i += 1
            else:
                res.append(asteroids[i])
                top += 1
                i += 1
        return res

# @lc code=end

