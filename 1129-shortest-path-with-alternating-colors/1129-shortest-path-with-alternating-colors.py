from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):

        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]

        for u, v in redEdges:
            red[u].append(v)

        for u, v in blueEdges:
            blue[u].append(v)

        INF = float('inf')
        dist = [[INF] * 2 for _ in range(n)]

        q = deque()

        dist[0][0] = 0
        dist[0][1] = 0

        q.append((0, 0))  # Last edge = Red
        q.append((0, 1))  # Last edge = Blue

        while q:
            node, color = q.popleft()

            if color == 0:
                for nei in blue[node]:
                    if dist[nei][1] == INF:
                        dist[nei][1] = dist[node][0] + 1
                        q.append((nei, 1))
            else:
                for nei in red[node]:
                    if dist[nei][0] == INF:
                        dist[nei][0] = dist[node][1] + 1
                        q.append((nei, 0))

        ans = []

        for r, b in dist:
            d = min(r, b)
            ans.append(-1 if d == INF else d)

        return ans