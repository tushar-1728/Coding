class Solution:
    def countSubstrings(self, text: str) -> int:
        count = 0
        n = len(text)
        for i in range(len(text)):
            count += 1
            lindex = i-1
            rindex = i+1
            while(lindex >= 0 and rindex <n and text[lindex] == text[rindex]):
                count += 1
                lindex -= 1
                rindex += 1
        for i in range(len(text)-1):
            if(text[i] == text[i+1]):
                count += 1
                lindex = i-1
                rindex = i+2
                while(lindex >= 0 and rindex <n and text[lindex] == text[rindex]):
                    count += 1
                    lindex -= 1
                    rindex += 1
        return count


b = Solution()
print(b.countSubstrings("aaa"))