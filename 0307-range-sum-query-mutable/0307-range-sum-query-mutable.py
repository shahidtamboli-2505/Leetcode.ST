class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i in range(self.n):
            self._update_bit(i + 1, nums[i])

    def _update_bit(self, index, delta):
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def _query(self, index):
        s = 0
        while index > 0:
            s += self.bit[index]
            index -= index & -index
        return s

    def update(self, index, val):
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update_bit(index + 1, delta)

    def sumRange(self, left, right):
        return self._query(right + 1) - self._query(left)