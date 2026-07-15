import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue

            for nei, wt in graph[node]:
                if time + wt < dist[nei]:
                    dist[nei] = time + wt
                    heapq.heappush(heap, (dist[nei], nei))

        ans = max(dist[1:])

        return ans if ans != float('inf') else -1