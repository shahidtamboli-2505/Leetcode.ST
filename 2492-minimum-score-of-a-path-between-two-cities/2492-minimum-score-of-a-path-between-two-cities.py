from collections import defaultdict

class Solution(object):
    def minScore(self, n, roads):
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        ans = [float("inf")]

        def dfs(node):
            visited.add(node)

            for nei, w in graph[node]:
                ans[0] = min(ans[0], w)
                if nei not in visited:
                    dfs(nei)

        dfs(1)
        return ans[0]