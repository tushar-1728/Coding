from typing import List
import itertools
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        blocks = [(k, len(list(v)))
                  for k, v in itertools.groupby(tree)]
        n = len(blocks)
        curr = blocks[0][0]
        s1 = {curr}
        length, temp = 1, blocks[0][1]
        res = 0
        for i in range(1, n):
            prev = curr
            curr = blocks[i][0]
            if curr in s1:
                temp += blocks[i][1]
                print("app1")
            elif length == 1:
                s1.add(curr)
                temp += blocks[i][1]
                length += 1
                print("app2")
            else:
                s1 = {prev, curr}
                if temp > res:
                    res = temp
                    temp = blocks[i-1][1] + blocks[i][1]
                print("app3")
        if temp > res:
            res = temp
        print(blocks)
        return res


b = Solution()
# print(b.totalFruit([1,2,1]))
# print(b.totalFruit([0,1,2,2]))
# print(b.totalFruit([1,2,3,2,2]))
# print(b.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
# print(b.totalFruit([0,1,6,6,4,4,6]))
print(b.totalFruit([4,7,7,0,8,3,8,2,5]))