import sys


def bfs(n, gi, gj):
    global rst # 국경을 연 나라가 있으면 True, 없으면 False
    imq = [] # bfs를 위한 queue
    all_in = [] # 연결된 나라의 좌표(pop된 좌표)들을 모으는 list
    visited[gi][gj] = 1 # 시작점 방문 표시
    imq.append((gi, gj)) # 시작점 queue에 추가
    s = cnt = 0 # s는 인구의 합, cnt는 국가(칸) 수
    while imq: # 연결된 국가가 있을 때
        ci, cj = imq.pop(0)
        s += grd[ci][cj] # 도착지의 인구 수를 s에 더함
        cnt += 1 # 들른 국가 수를 1 증가
        all_in.append((ci, cj)) # all_in에 현 위치 저장
        for k in range(4): # 델타로 현위치의 상하좌우가 연결되있는지 확인
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and (l <= abs(grd[ci][cj] - grd[ni][nj]) <= r):
                # 연결되있고, 아직 방문하지 않았으면
                visited[ni][nj] = 1 # 방문 표시
                imq.append((ni, nj)) # 해당 지점 queue에 추가
    a_pop = s // cnt # 연합 각 칸의 인구수
    if cnt >= 2: # 연합이 2칸 이상이면
        rst = True # 인구 이동이 있었으며(국경을 열었으며)
        cng_grd(a_pop, all_in) # 연합의 모든 칸을 a_pop으로 변경


def cng_grd(n_p, con):
    for cor in con: # 좌표를 모았던 all_in 리스트를 이용하여
        grd[cor[0]][cor[1]] = n_p # 연합의 각 칸을 변경


n, l, r = map(int, sys.stdin.readline().split())
grd = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

day = 0 # 인구 이동 일자
while True:
    rst = False
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(n, i, j)

    if rst: # 인구 이동이 있었다면
        day += 1 # 1일 증가
    else: # 아니면 종료
        break

print(day)