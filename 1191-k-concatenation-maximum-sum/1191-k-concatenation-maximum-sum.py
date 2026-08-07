class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(nums):
            curr = best = 0
            for x in nums:
                curr = max(0, curr + x)
                best = max(best, curr)
            return best

        if k == 1:
            return kadane(arr) % MOD

        total = sum(arr)
        max_two = kadane(arr * 2)

        if total > 0:
            return (max_two + (k - 2) * total) % MOD
        else:
            return max_two % MOD