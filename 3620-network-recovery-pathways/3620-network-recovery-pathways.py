from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        maxCost = 0

        for u, v, c in edges:
            if (u == 0 or u == n - 1 or online[u]) and (v == 0 or v == n - 1 or online[v]):
                graph[u].append((v, c))
                indegree[v] += 1
                maxCost = max(maxCost, c)

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        deg = indegree[:]

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)

        INF = 10 ** 30

        def feasible(x):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue
                for v, c in graph[u]:
                    if c >= x and dist[u] + c < dist[v]:
                        dist[v] = dist[u] + c

            return dist[n - 1] <= k

        if not feasible(0):
            return -1

        lo, hi = 0, maxCost
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans