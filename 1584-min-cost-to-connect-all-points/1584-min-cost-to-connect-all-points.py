class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        minDist = [float('inf')] * n
        minDist[0] = 0

        ans = 0

        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or minDist[i] < minDist[u]):
                    u = i

            visited[u] = True
            ans += minDist[u]

            x1, y1 = points[u]
            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist < minDist[v]:
                        minDist[v] = dist

        return ans
        