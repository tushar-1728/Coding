class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        res = []
        len1 = len(nums1)
        len2 = len(nums2)
        rlen = len1+len2
        i = j = 0
        while (i < len1 and j < len2):
            if(nums1[i] <= nums2[j]):
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while (i < len1):
            res.append(nums1[i])
            i += 1
        while (j < len2):
            res.append(nums2[j])
            j += 1
        if (rlen % 2 == 0):
            temp1 = rlen//2
            temp2 = temp1-1
            median = (res[temp1]+res[temp2])/2
        else:
            temp = rlen//2
            median = res[temp]
        return median
