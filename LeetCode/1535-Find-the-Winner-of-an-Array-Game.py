from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        d = dict()
        count = 0
        while(count < k and count < n):
            if(arr[0] > arr[1]):
                count += 1
                arr.append(arr.pop(1))
            else:
                count = 1
                arr[0], arr[1] = arr[1], arr[0]
                arr.append(arr.pop(1))
        return arr[0]


b = Solution()
print(b.getWinner(arr = [1,9,8,2,3,7,6,4,5], k = 7))
print(b.getWinner(arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000))
print(b.getWinner(arr = [2,1,3,5,4,6,7], k = 2))