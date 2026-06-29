class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1


class Solution:
    def friendRequests(self, n, restrictions, requests):
        dsu = DSU(n)
        ans = []

        for u, v in requests:
            ru = dsu.find(u)
            rv = dsu.find(v)

            if ru == rv:
                ans.append(True)
                continue

            possible = True

            for x, y in restrictions:
                rx = dsu.find(x)
                ry = dsu.find(y)

                if (rx == ru and ry == rv) or (rx == rv and ry == ru):
                    possible = False
                    break

            if possible:
                dsu.union(ru, rv)
                ans.append(True)
            else:
                ans.append(False)

        return ans