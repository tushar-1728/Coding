from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            key = tuple(sorted(i))
            d[key] = d.get(key, []) + [i]
        return list(d.values())


b = Solution()
print(b.groupAnagrams(['bat', 'cat', 'tea', 'eat']))