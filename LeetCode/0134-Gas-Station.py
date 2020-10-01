from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if(n >= 1):
            for i in range(n):
                if gas[i] >= cost[i]:
                    r_gas = gas[i] - cost[i]
                    j = i + 1
                    if(j == n):
                        j = 0
                    while r_gas >= 0 and j != i:
                        r_gas += gas[j] - cost[j]
                        j += 1
                        if j == n:
                            j = 0
                    if r_gas >= 0:
                        return i
        return -1


b = Solution()
print(b.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
print(b.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))