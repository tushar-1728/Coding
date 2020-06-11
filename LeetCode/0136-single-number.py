def singleNumber(nums):
    d = dict()
    for i in nums:
        if i in d.keys():
            d[i] = not((d[i]))
        else:
            d[i] = 1
    for i in d.keys():
    	if d[i] == 1:
    		return i

result = singleNumber([4,1,2,1,2])
print(result)