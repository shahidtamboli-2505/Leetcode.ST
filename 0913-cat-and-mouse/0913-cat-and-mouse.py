from typing import List
from collections import deque

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        # color[mouse][cat][turn]
        # 0 = draw, 1 = mouse wins, 2 = cat wins
        color = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        # degree[mouse][cat][turn]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = sum(1 for x in graph[c] if x != 0)

        q = deque()

        # Mouse reaches hole -> Mouse wins
        for c in range(1, n):
            color[0][c][0] = 1
            color[0][c][1] = 1
            q.append((0, c, 0, 1))
            q.append((0, c, 1, 1))

        # Cat catches mouse -> Cat wins
        for i in range(1, n):
            color[i][i][0] = 2
            color[i][i][1] = 2
            q.append((i, i, 0, 2))
            q.append((i, i, 1, 2))

        def parents(m, c, turn):
            if turn == 0:  # current turn is Mouse
                # Previous turn was Cat
                for pc in graph[c]:
                    if pc != 0:
                        yield m, pc, 1
            else:  # current turn is Cat
                # Previous turn was Mouse
                for pm in graph[m]:
                    yield pm, c, 0

        while q:
            m, c, turn, result = q.popleft()

            for pm, pc, pturn in parents(m, c, turn):

                if color[pm][pc][pturn] != 0:
                    continue

                # If previous player can make a move leading to their win
                if pturn == 0 and result == 1:
                    color[pm][pc][pturn] = 1
                    q.append((pm, pc, pturn, 1))

                elif pturn == 1 and result == 2:
                    color[pm][pc][pturn] = 2
                    q.append((pm, pc, pturn, 2))

                else:
                    degree[pm][pc][pturn] -= 1

                    if degree[pm][pc][pturn] == 0:
                        winner = 2 if pturn == 0 else 1
                        color[pm][pc][pturn] = winner
                        q.append((pm, pc, pturn, winner))

        return color[1][2][0]