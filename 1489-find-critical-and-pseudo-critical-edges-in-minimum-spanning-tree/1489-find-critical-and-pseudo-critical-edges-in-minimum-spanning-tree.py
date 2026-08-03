class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = []
        for i, (u, v, w) in enumerate(edges):
            new_edges.append((w, u, v, i))
        new_edges.sort()

        def kruskal(skip=-1, force=-1):
            dsu = DSU(n)
            weight = 0
            cnt = 0

            if force != -1:
                w, u, v, _ = new_edges[force]
                if dsu.union(u, v):
                    weight += w
                    cnt += 1

            for i, (w, u, v, _) in enumerate(new_edges):
                if i == skip:
                    continue
                if dsu.union(u, v):
                    weight += w
                    cnt += 1

            return weight if cnt == n - 1 else float("inf")

        mst_weight = kruskal()

        critical = []
        pseudo = []

        for i in range(len(new_edges)):
            if kruskal(skip=i) > mst_weight:
                critical.append(new_edges[i][3])
            elif kruskal(force=i) == mst_weight:
                pseudo.append(new_edges[i][3])

        return [critical, pseudo]