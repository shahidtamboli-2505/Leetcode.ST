class Solution:
    def getHappyString(self, n, k):
        ans = ""

        def backtrack(curr):
            if ans:
                return

            if len(curr) == n:
                self.k -= 1
                if self.k == 0:
                    self.ans = "".join(curr)
                return

            for ch in "abc":
                if not curr or curr[-1] != ch:
                    curr.append(ch)
                    backtrack(curr)
                    curr.pop()

        self.k = k
        self.ans = ""
        backtrack([])
        return self.ans