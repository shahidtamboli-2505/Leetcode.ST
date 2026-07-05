class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10 ** 9 + 7
        n = len(board)

        dpScore = [[-1] * n for _ in range(n)]
        dpWays = [[0] * n for _ in range(n)]

        dpScore[0][0] = 0
        dpWays[0][0] = 1

        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if i == 0 and j == 0:
                    continue

                best = -1
                ways = 0

                for x, y in ((i - 1, j), (i, j - 1), (i - 1, j - 1)):
                    if 0 <= x < n and 0 <= y < n and dpScore[x][y] != -1:
                        if dpScore[x][y] > best:
                            best = dpScore[x][y]
                            ways = dpWays[x][y]
                        elif dpScore[x][y] == best:
                            ways = (ways + dpWays[x][y]) % MOD

                if best == -1:
                    continue

                val = 0
                if board[i][j].isdigit():
                    val = int(board[i][j])

                dpScore[i][j] = best + val
                dpWays[i][j] = ways

        if dpWays[n - 1][n - 1] == 0:
            return [0, 0]

        return [dpScore[n - 1][n - 1], dpWays[n - 1][n - 1]]