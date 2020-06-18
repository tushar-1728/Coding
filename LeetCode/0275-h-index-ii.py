class Solution:
    def hIndex(self, citations: List[int]) -> int:
		size = len(citations)
		maxi = 0
		for i in range(size-1, -1, -1):
			temp = min(citations[i], size-i)
			if(temp > maxi):
				maxi = temp
		return maxi