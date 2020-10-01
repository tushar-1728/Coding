from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = dict()
        res = []
        temp = 0
        for i in equations:
            for j in i:
                if j not in d.keys():
                    d[j] = temp
                    temp += 1
        graph = []
        n = temp
        for i in range(n):
            graph.append([-1] * (n))
            graph[i][i] = 1
        for i in range(len(equations)):
            x, y = equations[i]
            graph[d[x]][d[y]] = values[i]
            graph[d[y]][d[x]] = round(1 / values[i], 6)
        for k in range(n):
            for i in range(n):
                    for j in range(n):
                        if i != k and j != k and graph[i][j] == -1:
                            if graph[i][k] != -1 and graph[k][j] != -1:
                                graph[i][j] = round(graph[i][k] * graph[k][j], 6)
        for i in queries:
            x, y = i
            # print(x, y)
            x = d.get(x, -1)
            y = d.get(y, -1)
            # print(x, y)
            if x > -1 and y > -1:
               res.append(graph[x][y])
            else:
                res.append(-1.0)
        # for i in graph:
            # print(i)
        return res



b = Solution()
print(b.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))
print(b.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))