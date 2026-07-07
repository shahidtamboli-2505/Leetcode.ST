class Solution(object):
    def allPathsSourceTarget(self, graph):
        ans = []
        path = [0]
        target = len(graph) - 1

        def dfs(node):
            if node == target:
                ans.append(path[:])
                return

            for nei in graph[node]:
                path.append(nei)
                dfs(nei)
                path.pop()

        dfs(0)
        return ans