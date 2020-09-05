from typing import List
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if votes:
            rank = dict()
            elem = votes[0]
            for i in elem:
                rank[i] = [0] * len(elem)
            for i in votes:
                for j in range(len(i)):
                    rank[i[j]][j] += 1
            print(rank)


b = Solution()
print(b.rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
print(b.rankTeams(["WXYZ","XYZW"]))
# print(b.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
print(b.rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))
print(b.rankTeams(["M","M","M","M"]))