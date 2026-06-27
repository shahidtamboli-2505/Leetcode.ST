from collections import Counter

class Solution:
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in cnt:
            if cnt[1] % 2 == 0:
                ans = max(ans, cnt[1] - 1)
            else:
                ans = max(ans, cnt[1])

        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt[cur] >= 2:
                length += 2
                cur = cur * cur

            if cnt[cur] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans