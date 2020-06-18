class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        table = list()
        for i in range(n):
            table.append([10001]*i + [0] + [10001]*(n-i-1))
        for i in flights:
            table[i[0]][i[1]] = i[2]
        dist = []
        for i in range(n):
            dist.append(table[src][i])
        visited = [False]*n
        stops = [K]*n
        for i in range(n):
            mini = 10001
            for j in range(n):
                if(dist[j] < mini and visited[j] == False):
                    mini = dist[j]
                    minInd = j
            visited[minInd] = True
            for j in range(n):
                if(stops[j] > 0 and visited[j] == False and dist[j] > dist[minInd]+table[minInd][j]):
                    dist[j] = dist[minInd]+table[minInd][j]
                    stops[j] -= 1

        if(dist[dst] < 10001):
            return dist[dst]
        else:
            return -1