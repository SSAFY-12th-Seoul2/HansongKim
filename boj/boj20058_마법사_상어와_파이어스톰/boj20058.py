import sys


def dfs(n, i, j):
    sn = 2 ** n
    iceq = [0] * (sn * sn)
    top = -1
    visited[i][j] = 1
    cntt = 1
    while True:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < sn and 0 <= nj < sn and ice[ni][nj] > 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                top += 1
                iceq[top] = (i, j)
                i = ni
                j = nj
                break
        else:
            if top != -1:
                i, j = iceq[top]
                top -= 1
                cntt += 1
            else:
                break
    return cntt


def bingle(n, iq):
    sn = 2 ** n
    psn = 2 ** iq
    for i in range(0, sn, psn):
        for j in range(0, sn, psn):
            bin_lst = [[] for _ in range(psn)]

            for x in range(i, i + psn):
                bin_lst[x - i] = ice[x][j: j + psn]
            bin_lst = list(map(list, zip(*bin_lst[::-1])))
            for x in range(i, i + psn):
                ice[x][j: j + psn] = bin_lst[x - i]


n, q = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(2 ** n)]
q_lst = list(map(int, sys.stdin.readline().split()))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for iq in q_lst:
    bingle(n, iq)

    mid_ice = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]
    for pp in range(2 ** n):
        mid_ice[pp] = ice[pp][:]

    for i in range(2 ** n):
        for j in range(2 ** n):
            if ice[i][j] > 0:
                cnt = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < 2 ** n and 0 <= nj < 2 ** n and ice[ni][nj] > 0:
                        cnt += 1
                if cnt <= 2:
                    mid_ice[i][j] = ice[i][j] - 1
    ice = mid_ice

total = 0
ice_block = 0
visited = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]
for i in range(2 ** n):
    for j in range(2 ** n):
        total += ice[i][j]
        if visited[i][j] == 0 and ice[i][j] > 0:
            ice_block = max(dfs(n, i, j), ice_block)

print(total)
print(ice_block)
