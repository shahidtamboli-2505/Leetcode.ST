class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)

        # dp[j] = whether s3[:i+j] can be formed
        # using s1[:i] and s2[:j]
        dp = [False] * (n + 1)
        dp[0] = True

        # First row: only s2 is used
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # Only s1 is used
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                dp[j] = (
                    (dp[j] and s1[i - 1] == s3[i + j - 1])
                    or
                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                )

        return dp[n]