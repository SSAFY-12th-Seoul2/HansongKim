import sys


def comb(si, m):
    global min_chk
    if si == m and (set(chk_idx[:m]) not in set_lst):
        set_lst.append(set(chk_idx[:m]))
        dis_s = 0
        for p in range(l_hom):
            m_dis = 10000
            for q in chk_idx[:m]:
                m_dis = min(m_dis, dis_lst[p][q])
            dis_s += m_dis
        min_chk = min(min_chk, dis_s)
    else:
        for sj in range(si, l_chk):
            chk_idx[si], chk_idx[sj] = chk_idx[sj], chk_idx[si]
            comb(si + 1, m)
            chk_idx[si], chk_idx[sj] = chk_idx[sj], chk_idx[si]


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

l_chk = len(chick)
l_hom = len(home)
dis_lst = [[0 for _ in range(l_chk)] for _ in range(l_hom)]
for i in range(l_hom):
    for j in range(l_chk):
        hv = home[i]
        cv = chick[j]
        dis_lst[i][j] = abs(hv[0] - cv[0]) + abs(hv[1] - cv[1])

chk_idx = [i for i in range(l_chk)]
min_chk = 10000
set_lst = []

comb(0, m)
print(min_chk)
