import sys


def perm(si, k):
    if si == k:
        rotation(rcs_idx)
        cal_min()
        print(min_val)
        return
    else:
        for j in range(si, k):
            rcs_idx[si], rcs_idx[j] = rcs_idx[j], rcs_idx[si]
            perm(si + 1, k)
            rcs_idx[si], rcs_idx[j] = rcs_idx[j], rcs_idx[si]


def rotation(idx_l):
    for idx in idx_l:
        old_lst = [row[:] for row in lst]
        r = rcs[idx][0]
        c = rcs[idx][1]
        s = rcs[idx][2]
        sr = r - 1 - s
        sc = c - 1 - s
        lr = sr + 2 * s
        lc = sc + 2 * s
        for _ in range(s):
            for i in range(sr, lr + 1):
                for j in range(sc, lc + 1):
                    if i == sr and j > sc:
                        lst[i][j] = old_lst[i][j - 1]
                    elif i == lr and j < lc:
                        lst[i][j] = old_lst[i][j + 1]
                    elif j == sc and i < lr:
                        lst[i][j] = old_lst[i + 1][j]
                    elif j == lc and i > sr:
                        lst[i][j] = old_lst[i - 1][j]
            sr += 1
            lr -= 1
            sc += 1
            lc -= 1


def cal_min():
    global min_val
    for ro in lst:
        min_val = min(min_val, sum(ro))


n, m, k = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
rcs = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

rcs_idx = [0 for _ in range(k)]
min_val = 100000000
perm(0, k)

print(min_val)
