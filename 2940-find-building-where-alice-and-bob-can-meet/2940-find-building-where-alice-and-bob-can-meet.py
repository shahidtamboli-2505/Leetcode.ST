from bisect import bisect_right

class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n = len(heights)
        ans = [-1] * len(queries)

        new_queries = [[] for _ in range(n)]

        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a

            if a == b:
                ans[i] = a
            elif heights[a] < heights[b]:
                ans[i] = b
            else:
                new_queries[b].append((heights[a], i))

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()

            for h, idx in new_queries[i]:
                l, r = 0, len(stack) - 1
                res = -1

                while l <= r:
                    mid = (l + r) // 2
                    if heights[stack[mid]] > h:
                        res = stack[mid]
                        l = mid + 1
                    else:
                        r = mid - 1

                ans[idx] = res

            stack.append(i)

        return ans