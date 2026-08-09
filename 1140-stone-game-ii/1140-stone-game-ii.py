class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            # All piles already taken
            if i >= n:
                return 0

            # Can take all remaining piles
            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            for X in range(1, 2 * M + 1):
                next_M = max(M, X)

                # Current player gets:
                # total remaining - what opponent can get
                current = suffix[i] - dp(i + X, next_M)

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)