import sys


def dfs(si, sj, stt):
    cnt = 0
    if si == n - 1 and sj == n - 1:
        return 1
    for k in drt[stt]:
        ni = si + d[k][0]
        nj = sj + d[k][1]
        if 0 <= ni < n and 0 <= nj < n and not room[ni][nj]:
            if k == 2 and (room[ni - 1][nj] or room[ni][nj - 1]):
                continue
            cnt += dfs(ni, nj, k)
    return cnt


n = int(sys.stdin.readline())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

d = ((0, 1), (1, 0), (1, 1))
drt = ((0, 2), (1, 2), (0, 1, 2))

if room[-1][-1]:
    result = 0
else:
    result = dfs(0, 1, 0)
print(result)
