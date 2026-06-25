class Solution:
    def findKthBit(self, n, k):
        if n == 1:
            return "0"

        mid = 1 << (n - 1)

        if k == mid:
            return "1"

        if k < mid:
            return self.findKthBit(n - 1, k)

        mirrored = (1 << n) - k
        bit = self.findKthBit(n - 1, mirrored)

        if bit == "1":
            return "0"
        return "1"