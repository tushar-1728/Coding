from math import ceil, floor, log2
t = int(input())
for i in range(t):
	inp = int(input())
	if(inp == 0):
		print("YES")
	else:
		inp = log2(inp)
		if(ceil(inp) == floor(inp)):
			print("YES")
		else:
			print("NO")