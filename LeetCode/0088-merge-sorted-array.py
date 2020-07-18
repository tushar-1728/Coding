class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        temp = [0] * (m+n)
        k = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp[k] = nums1[i]
                i += 1
            else:
                temp[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            temp[k] = nums1[i]
            k += 1
            i += 1
        while j < n:
            temp[k] = nums2[j]
            k += 1
            j += 1
        for i in range(m + n):
            nums1[i] = temp[i]
        print(nums1)


b = Solution()
b.merge(nums1 = [4,0,0,0], m = 1, nums2 = [2,5,6], n = 3)