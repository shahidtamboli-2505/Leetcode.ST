class Fenwick(object):
    def __init__(self, n):
        self.bit = [0] * (n + 2)

    def update(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        prefix = 0
        pref = [0]

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1
            pref.append(prefix)

        vals = sorted(set(pref))
        rank = {}
        for i, v in enumerate(vals):
            rank[v] = i + 1

        bit = Fenwick(len(vals))
        ans = 0

        bit.update(rank[0], 1)

        for p in pref[1:]:
            ans += bit.query(rank[p] - 1)
            bit.update(rank[p], 1)

        return ans