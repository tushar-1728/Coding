#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
from typing import List
class Solution:
    def helper(self, text, hashmap):
        int_map = dict()
        count_map = dict()
        p_len = factor = 10
        p_val = hashmap[text[0]]
        factor1 = factor ** (p_len-1)
        for i in range(1, p_len):
            p_val = p_val * factor + hashmap[text[i]]
        count_map[p_val] = count_map.get(p_val, 0) + 1
        int_map[p_val] = text[:p_len]
        for i in range(p_len, len(text)):
            p_val = (p_val - hashmap[text[i-p_len]] * factor1) * 10 + hashmap[text[i]]
            count_map[p_val] = count_map.get(p_val, 0) + 1
            int_map[p_val] = text[i-p_len+1:i+1]
        return int_map, count_map


    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        if len(s) > 10:
            hashmap = {"A":0,"C":1,"G":2, "T":3}
            int_map, count_map = self.helper(s, hashmap)
            for i in count_map.keys():
                if count_map[i] > 1:
                    res.append(int_map[i])
        return res
# @lc code=end

