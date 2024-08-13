import sys

n, m = map(int, sys.stdin.readline().split())
r, c, drt = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

cnt = 0
while True:
    if lst[r][c] == 0: # 만약 내 위치가 더러우면
        cnt += 1 # 청소 횟수 1 올리고
        lst[r][c] = 2 # 닦았습니다!!
    for k in range(1, 5): # 청소기는 매 칸 진행방향 왼쪽부터 진행 판단
        nr = r + di[drt - k]
        nc = c + dj[drt - k]
        if 0 <= nr < n and 0 <= nc < m and lst[nr][nc] == 0: # 다음 방향이 갈 수 있다면
            r = nr # 행 갱신
            c = nc # 열 갱신
            if drt - k >= 0: # 방향 인덱스가 0 이상이면
                drt -= k # 방향 인덱스 갱신
            else: # 음수면
                drt = 4 + (drt - k) # 양수로 바꾸어 갱신
            break
    else: # break 되지 않으면(갈 곳이 없으면)
        back_drt = (drt + 2) % 4 # 후진 방향
        r += di[back_drt]
        c += dj[back_drt]
        if not(0 <= r < n and 0 <= c < m) or lst[r][c] == 1:
            break # 후진이 안된다면 break
print(cnt)
