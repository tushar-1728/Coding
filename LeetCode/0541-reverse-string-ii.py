class Solution:
	def reverseStr(self, s, k):
		l = list()
		count = 0
		for i in s:
			if count == 0:
				l1 = list()
			l1.append(i)
			count += 1
			if(count == k):
				l.append(l1)
				count = 0
		if len(l1) != k:
			l.append(l1)
		for i in range(len(l)):
			if i%2 == 0:
				l[i].reverse()
		res = ""
		for i in l:
			for j in i:
				res += j
		# print(l)
		return (res)


b = Solution()
print(b.reverseStr(s = "abcdefg", k = 2))