import heapq

class Graph:

    def __init__(self, n, edges):
        self.n = n
        self.graph = [[] for _ in range(n)]

        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge):
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1, node2):
        dist = [float('inf')] * self.n
        dist[node1] = 0

        pq = [(0, node1)]

        while pq:
            d, node = heapq.heappop(pq)

            if node == node2:
                return d

            if d > dist[node]:
                continue

            for nei, wt in self.graph[node]:
                nd = d + wt
                if nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(pq, (nd, nei))

        return -1