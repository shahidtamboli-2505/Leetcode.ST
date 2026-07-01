from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values, edges, maxTime):

        graph = defaultdict(list)

        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        visited = [0] * len(values)

        ans = [values[0]]
        visited[0] = 1

        def dfs(node, time, score):

            if node == 0:
                ans[0] = max(ans[0], score)

            for nxt, cost in graph[node]:

                if time + cost > maxTime:
                    continue

                first = False

                if visited[nxt] == 0:
                    first = True
                    score += values[nxt]

                visited[nxt] += 1

                dfs(nxt, time + cost, score)

                visited[nxt] -= 1

                if first:
                    score -= values[nxt]

        dfs(0, 0, values[0])

        return ans[0]