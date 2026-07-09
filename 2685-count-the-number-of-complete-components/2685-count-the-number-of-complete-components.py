class Solution(object):
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                nodes = []
                dfs(i)

                vertices = len(nodes)
                edgeCount = sum(len(graph[node]) for node in nodes) // 2

                if edgeCount == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans