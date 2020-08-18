class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n1 = len(nums)
        temp1 = pow(2, n1)
        result = []
        for i in range(temp1):
            temp2 = bin(i)[2::]
            n2 = len(temp2)
            print(temp2, end=" ")
            temp3 = []
            for j in range(len(temp2)):
                if temp2[j] == "1":
                    temp3.append(nums[n2 - j - 1])
            result.append(temp3)
        return result