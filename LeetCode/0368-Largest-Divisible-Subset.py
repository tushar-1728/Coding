class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if(len(nums) == 0):
            return nums
        else:
            nums.sort()
            size = len(nums)
            slist = []
            for i in range(size):
                s = [-1, 1]
                slist.append(s)
            # print(slist)
            for i in range(size-2, -1, -1):
                # flag = 0
                for j in range(i+1, size):
                    # print("i:", i, "j:", j)
                    if((nums[j] % nums[i] == 0) and (slist[j][1] >= slist[i][1])):
                        # print("true")
                        slist[i][0] = j
                        slist[i][1] = 1+slist[j][1]
                        # if(flag == 0):
                        #   slist[i][1] += 1
                        # flag = 1
            # print(nums)
            # print(slist)
            res = []
            a = max(slist, key=lambda x: x[1])
            # print(a)
            res.append(nums[slist.index(a)])
            while(a[0] != -1):
                res.append(nums[a[0]])
                a = slist[a[0]]
                # print(a)
            return res
