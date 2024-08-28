import sys


def perm(si, k):
    if si == k:
        n_lst = rotation(rcs_idx)
        cal_min(n_lst)
        return
    else:
        for j in range(si, k):
            rcs_idx[si], rcs_idx[j] = rcs_idx[j], rcs_idx[si]
            perm(si + 1, k)
            rcs_idx[si], rcs_idx[j] = rcs_idx[j], rcs_idx[si]


def rotation(idx_l):
    new_lst = [row[:] for row in lst]
    mid_lst = [row[:] for row in lst]
    for idx in idx_l:
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
                        new_lst[i][j] = mid_lst[i][j - 1]
                    elif i == lr and j < lc:
                        new_lst[i][j] = mid_lst[i][j + 1]
                    elif j == sc and i < lr:
                        new_lst[i][j] = mid_lst[i + 1][j]
                    elif j == lc and i > sr:
                        new_lst[i][j] = mid_lst[i - 1][j]
            mid_lst = [row[:] for row in new_lst]
            sr += 1
            lr -= 1
            sc += 1
            lc -= 1
    return new_lst


def cal_min(n_lst):
    global min_val
    for ro in n_lst:
        min_val = min(min_val, sum(ro))


n, m, k = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
rcs = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

rcs_idx = [i for i in range(k)]
min_val = 100000000
perm(0, k)

print(min_val)
