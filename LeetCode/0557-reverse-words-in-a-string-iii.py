class Solution:
	def reverseWords(self, s):
		res = ""
		for i in s.split():
			res += (i[::-1] + " ")
			# print(i)
		res = res.rstrip()
		return res

b = Solution()
print(b.reverseWords("Let's take LeetCode contest"))