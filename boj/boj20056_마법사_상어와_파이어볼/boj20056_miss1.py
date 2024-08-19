import sys


def fire_move(n):
    for i in range(n):
        for j in range(n):
            if f_cnt[i][j] == 1:
                ni = (i + di[f_dir[i][j]] * f_speed[i][j]) % n
                nj = (j + dj[f_dir[i][j]] * f_speed[i][j]) % n
                f_massive[ni][nj] += f_massive[i][j]
                f_cnt[ni][nj] += 1
                f_speed[ni][nj] += sm
                if f_cnt[ni][nj] == 1:
                    f_dir[ni][nj] = f_dir[i][j]
                elif f_cnt[ni][nj] == 2:
                    f_dir[ni][nj] = (f_dir[ni][nj] % 2) - 2
                    f_dir[ni][nj] += ((f_dir[i][j] % 2) - 2)
                else:
                    f_dir[ni][nj] += ((f_dir[i][j] % 2) - 2)
                f_massive[i][j] = 0
                f_cnt[i][j] = 0
                f_speed[i][j] = 0
                f_dir[i][j] = 0
            else:
                if f_dir[i][j] == 246:
                    idx = 0
                else:
                    idx = 1
                while idx < 8:
                    ni = (i + di[idx] * f_speed[i][j]) % n
                    nj = (j + dj[idx] * f_speed[i][j]) % n
                    f_massive[ni][nj] += f_massive[i][j]
                    f_cnt[ni][nj] += 1
                    f_speed[ni][nj] += sm
                    if f_cnt[ni][nj] == 1:
                        f_dir[ni][nj] = f_dir[i][j]
                    elif f_cnt[ni][nj] == 2:
                        f_dir[ni][nj] = (f_dir[ni][nj] % 2) - 2
                        f_dir[ni][nj] += ((f_dir[i][j] % 2) - 2)
                    else:
                        f_dir[ni][nj] += ((f_dir[i][j] % 2) - 2)
                    if idx == 6 or idx == 7:

    for i in range(n):
        for j in range(n):
            if f_cnt[i][j] > 1:
                f_massive[i][j] //= 5
                if f_massive[i][j] != 0:
                    f_speed[i][j] //= f_cnt[i][j]
                    if f_dir[i][j] == f_cnt[i][j] * (-2) or f_dir[i][j] == f_cnt[i][j] * (-1):
                        f_dir[i][j] = 246
                    else:
                        f_dir[i][j] = 1357
                else:
                    f_cnt[i][j] = f_speed[i][j] = f_dir[i][j] = 0


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, sys.stdin.readline().split())
f_massive = [[0 for _ in range(n)] for _ in range(n)]
f_cnt = [[0 for _ in range(n)] for _ in range(n)]
f_speed = [[0 for _ in range(n)] for _ in range(n)]
f_dir = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, ma, sm, dm = map(int, sys.stdin.readline().split())
    f_massive[r - 1][c - 1] += ma
    f_cnt[r - 1][c - 1] += 1
    f_speed[r - 1][c - 1] += sm
    f_dir[r - 1][c - 1] = dm

if k == 1:
