import sys


def comb(si, m):
    if si == m:

    pass


n, m = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

home = []
chick = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

chk_idx = [i for i in range(len(chick))]
set_j = []

