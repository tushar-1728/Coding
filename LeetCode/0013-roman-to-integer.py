class Solution:
    def romanToInt(self, s):
        d = dict()
        d['I'] = [1, None]
        d['V'] = [5, 'I']
        d['X'] = [10, 'I']
        d['L'] = [50, 'X']
        d['C'] = [100, 'X']
        d['D'] = [500, 'C']
        d['M'] = [1000, 'C']
        prev = -1
        curr = -1
        total = 0
        for i in s:
            prev = curr
            curr = i
            if prev == d[curr][1]:
                total += (d[curr][0] - 2*d[prev][0])
            else:
                total += d[curr][0]
        return total
            
b = Solution()
print(b.romanToInt("MCMXCIV"))