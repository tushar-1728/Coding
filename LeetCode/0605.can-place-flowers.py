#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, length = 0, len(flowerbed)
        if length == 1:
            if n == 0 or (n == 1 and flowerbed[i] == 0):
                return True
            return False
        else:
            while i < length and n > 0:
                if flowerbed[i] == 0:
                    if i == 0:
                        if flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            n -= 1
                            i += 2
                        else:
                            i += 3
                    elif i == length - 1:
                        if flowerbed[i-1] == 0:
                            flowerbed[i] = 1
                            n -= 1
                            i += 2
                        else:
                            i += 1
                    else:
                        if flowerbed[i-1] == flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            n -= 1
                            i += 2
                        elif flowerbed[i+1] == 1:
                            i += 3
                        else:
                            i += 1
                else:
                    i += 2
            if n == 0:
                return True
            return False
# @lc code=end

