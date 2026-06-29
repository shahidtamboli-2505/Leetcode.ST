class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return

        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1


class Solution:
    def largestComponentSize(self, nums):
        dsu = DSU()
        factor_map = {}

        for num in nums:
            x = num
            d = 2

            while d * d <= x:
                if x % d == 0:
                    if d in factor_map:
                        dsu.union(num, factor_map[d])
                    else:
                        factor_map[d] = num

                    while x % d == 0:
                        x //= d
                d += 1

            if x > 1:
                if x in factor_map:
                    dsu.union(num, factor_map[x])
                else:
                    factor_map[x] = num

        count = {}

        ans = 0

        for num in nums:
            root = dsu.find(num)
            count[root] = count.get(root, 0) + 1
            ans = max(ans, count[root])

        return ans