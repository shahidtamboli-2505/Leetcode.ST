from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source])
        visited = {source}

        while q:
            node = q.popleft()

            if node == destination:
                return True

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return False