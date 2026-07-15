import heapq

class Solution:
    def minimumWeight(self, n, edges, src1, src2, dest):
        graph = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            rev[v].append((u, w))

        def dijkstra(start, g):
            INF = float('inf')
            dist = [INF] * n
            dist[start] = 0
            pq = [(0, start)]

            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue

                for nei, wt in g[node]:
                    nd = d + wt
                    if nd < dist[nei]:
                        dist[nei] = nd
                        heapq.heappush(pq, (nd, nei))

            return dist

        d1 = dijkstra(src1, graph)
        d2 = dijkstra(src2, graph)
        d3 = dijkstra(dest, rev)

        ans = float('inf')

        for i in range(n):
            if d1[i] != float('inf') and d2[i] != float('inf') and d3[i] != float('inf'):
                ans = min(ans, d1[i] + d2[i] + d3[i])

        return -1 if ans == float('inf') else ans