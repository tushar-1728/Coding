def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    count = 0
    while(i < len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            count += 1
        else:
            i += 1
    while(count > 0):
    	nums.append(0)
    	count -= 1
    print(nums)

moveZeroes([0,1,0,3,12])
moveZeroes([0,0,1])