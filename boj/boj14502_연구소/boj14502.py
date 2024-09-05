import sys
from collections import deque


def comb(sl, n, m):
    tp = []

    def comb_in(sl, tp, sw, n, m):
        global max_safe
        if len(tp) == 3:
            max_safe = max(bfs(tp, n, m), max_safe)
            return
        else:
            for w in range(sw, sl):
                tp.append(w)
                comb_in(sl, tp, w + 1, n, m)
                tp.pop()
    comb_in(sl, tp, 0, n, m)


def bfs(wall, n, m):
    cnt = 0
    test_lab = [row[:] for row in lab]
    virus_d = deque(virus)
    for p in range(3):
        test_lab[space[wall[p]][0]][space[wall[p]][1]] = 1
    while virus_d:
        ci, cj = virus_d.popleft()
        for w in range(4):
            ni = ci + di[w]
            nj = cj + dj[w]
            if 0 <= ni < n and 0 <= nj < m and not test_lab[ni][nj]:
                virus_d.append((ni, nj))
                test_lab[ni][nj] = 2
    for x in range(n):
        for y in range(m):
            if test_lab[x][y] == 0:
                cnt += 1
    return cnt


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

space = []
virus = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            space.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

s_len = len(space)
max_safe = 0
comb(s_len, n, m)

print(max_safe)
