class Solution:
    def convert(self, text: str, num_rows: int) -> str:
        n = len(text)
        arr = []
        res = ""
        for i in range(num_rows):
            arr.append([])
        i = 0
        while(i < n):
            temp = 0
            while(temp < num_rows and i < n):
                arr[temp].append(text[i])
                temp += 1
                i += 1
            temp -= 2
            while(temp > 0 and i < n):
                arr[temp].append(text[i])
                temp -= 1
                i += 1
        for i in range(num_rows):
            temp = "".join(arr[i])
            res += temp
        return res


b = Solution()
print(b.convert("PAYPALISHIRING", 5))