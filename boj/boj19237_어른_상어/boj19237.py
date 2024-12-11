import sys
from collections import deque


def fill_smell(sn, ci, cj):
    board[ci][cj] = sn               # board 현재 상어위치에 냄새를 새기고
    shark_smell[sn].append((ci, cj)) # shark_smell에도 추가해준다.
    if len(shark_smell[sn]) > k:     # shark_smell이 k개를 넘어가면 가장 오래된 냄새를 지워야 한다.
        out_smell(sn)


# 냄새 지우는 함수
def out_smell(sn):
    if shark_smell[sn]:
        oi, oj = shark_smell[sn].popleft()  # 덱에서 가장 오래된 냄새가 있는 좌표를 반환
        if (oi, oj) == (-1, -1):            # (-1, -1)은 의미없는 좌표이므로 넘어감
            return

        if (oi, oj) not in shark_smell[sn]: # 상어가 뒤로 돌아가면 동일 좌표가 덱에 들어갈 수 있다.
            board[oi][oj] = 0               # 그런 경우가 아닐 때만 (oi, oj)의 냄새를 지운다.


# 상어 이동 함수
def move_shark(sn, ci, cj):
    drt = shark_head[sn]          # 상어 현재 이동방향
    nni, nnj, nw = -1, -1, -1     # 4방향 모두 냄새에 막혀있다면, 돌아갈 자기 냄새 칸
    for w in shark_dir[sn][drt]:
        ni = ci + di[w]
        nj = cj + dj[w]
        if 0 <= ni < n and 0 <= nj < n:
            if board[ni][nj] == 0:    # 냄새가 없으면
                shark_head[sn] = w    # 상어 이동방향을 w로 갱신하고
                shark[sn] = (ni, nj)  # 상어 위치도 이동하고 종료
                return
            elif board[ni][nj] == sn and nni == -1:
                nni, nnj, nw = ni, nj, w  # 4방향 모두 냄새가 있을 때를 대비하여, 처음 만난 자기냄새 칸 정보 기록
    else:
        # 위의 for문이 return 되지 않고 모두 돌았다면
        # 위에서 구한 nni, nnj, nw로 상어 이동
        shark_head[sn] = nw
        shark[sn] = (nni, nnj)


# shark : 상어 위치
# shark_head : 상어 진행 방향
# shark_dir : head에 따른 delta
# shark_smell : 상어 냄새 묻은 장소
# board : 수족관

di = (0, -1, 1, 0, 0)
dj = (0, 0, 0, -1, 1)

shark = {}
shark_dir = {}
shark_smell = {}

n, m, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
shark_head = [0] + list(map(int, sys.stdin.readline().split()))  # 상어의 현재 방향
for i in range(1, m + 1):
    shark_dir[i] = [[0, 0, 0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(4)]  # 상어 이동 방향
    shark_smell[i] = deque([(-1, -1)] * k)  # 상어 냄새 좌표(초기값은 (-1, -1)의 k개)

for i in range(n):
    for j in range(n):
        if board[i][j]:
            shark[board[i][j]] = (i, j)  # shark 딕셔너리에 상어 초기 위치를 저장한다.

s_time = 0  # 걸린 시간(출력값)
ban = set()  # 쫓겨난 상어 번호를 담는 set
while True:
    # 냄새를 뭍히고, k초 지난 냄새는 지우는 for문
    for i in range(1, m + 1):
        x, y = shark[i]
        # 쫓겨난 상어는 냄새 지우기인 out_smell을
        # 남은 상어는 묻히고 지우는 fill_smell 함수를 들어간다.
        if i in ban:
            out_smell(i)
            continue
        fill_smell(i, x, y)

    # 상어들이 이동하는 for문
    for i in range(1, m + 1):
        # 쫓겨난 상어 번호일 때는 넘어간다.
        # 남은 상어만 이동
        if i in ban:
            continue
        x, y = shark[i]
        move_shark(i, x, y)

    # 쫓겨날 상어를 찾는 이중 for문
    for i in range(1, m):
        # 이미 쫓겨난 상어는 배제하고 시작
        if i in ban:
            continue
        for j in range(i + 1, m + 1):
            # j번은 i번보다 무조건 크므로, 둘이 같은 공간에 있으면 j번 상어가 쫓겨난다.
            if shark[j] == shark[i]:
                ban.add(j)

    s_time += 1 # 1초 증가

    # 종료 조건 1. 1000초가 넘어가면 -1 출력
    if s_time > 1000:
        s_time = -1
        break

    # 종료 조건 2. 1번을 제외하고 모두 쫓겨나면 종료
    if len(ban) == m - 1:
        break

print(s_time)
