class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        size = 4 * self.n

        self.left = [''] * size
        self.right = [''] * size
        self.pref = [0] * size
        self.suff = [0] * size
        self.best = [0] * size
        self.length = [0] * size

        self.build(1, 0, self.n - 1, s)

    def build(self, node, l, r, s):
        self.length[node] = r - l + 1

        if l == r:
            self.left[node] = self.right[node] = s[l]
            self.pref[node] = 1
            self.suff[node] = 1
            self.best[node] = 1
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid, s)
        self.build(node * 2 + 1, mid + 1, r, s)

        self.merge(node)

    def merge(self, node):
        left_node = node * 2
        right_node = node * 2 + 1

        self.left[node] = self.left[left_node]
        self.right[node] = self.right[right_node]

        self.pref[node] = self.pref[left_node]
        self.suff[node] = self.suff[right_node]

        self.best[node] = max(
            self.best[left_node],
            self.best[right_node]
        )

        # Boundary characters are same
        if self.right[left_node] == self.left[right_node]:

            self.best[node] = max(
                self.best[node],
                self.suff[left_node] + self.pref[right_node]
            )

            # Entire left segment has same character
            if self.pref[left_node] == self.length[left_node]:
                self.pref[node] = (
                    self.length[left_node] +
                    self.pref[right_node]
                )

            # Entire right segment has same character
            if self.suff[right_node] == self.length[right_node]:
                self.suff[node] = (
                    self.length[right_node] +
                    self.suff[left_node]
                )

    def update(self, node, l, r, idx, ch):
        if l == r:
            self.left[node] = ch
            self.right[node] = ch
            self.pref[node] = 1
            self.suff[node] = 1
            self.best[node] = 1
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx, ch)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, ch)

        self.merge(node)


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: list[int]
    ) -> list[int]:

        tree = SegmentTree(s)
        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, len(s) - 1, idx, ch)
            ans.append(tree.best[1])

        return ans