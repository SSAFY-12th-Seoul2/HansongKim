import sys

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, sys.stdin.readline().split())
board = [[[] for _ in range(n)] for _ in range(n)] # 파이어볼을 쏘는 격자판
for _ in range(m):
    r, c, ma, sa, da = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1].append([ma, sa, da]) # 파이어볼이 떨어지는 격자판에
    # 질량, 속도, 방향 기록

for ti in range(k + 1):
    save_fire = [] # 파이어볼 도착지를 임시 저장하는 배열
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2: # 여러 파이어볼이 만났을 때
                odd_s = even_s = 0
                for fi in board[i][j]: # 모든 파이어볼 방향이 짝수(홀수)인지 판별
                    if fi[2] % 2 == 0:
                        even_s += 1
                    else:
                        odd_s += 1
                if even_s == len(board[i][j]) or odd_s == len(board[i][j]): # 파이어볼 방향이 통일되어있다면
                    go_fire = [0, 2, 4, 6] # 다음과 같은 방향 적용
                else:
                    go_fire = [1, 3, 5, 7] # 아니면 이와 같이 적용
                n_ma = n_sa = 0
                for fi in board[i][j]: # 모인 파이어볼의 질량합과 속도합 계산
                    n_ma += fi[0] # 질량합
                    n_sa += fi[1] # 속도합
                n_ma //= 5 # 발사될 때 적용되는 파이어볼 질량
                n_sa //= len(board[i][j]) # 발사될 때 적용되는 속도
                if n_ma == 0: # 질량 0 파이어볼일 때 소멸
                    board[i][j].clear() # 그 칸의 모든 내용 지우고
                    continue # 다음 칸으로
                for dit in go_fire: # 4방향의 파이어볼 정보를 save_fire에 저장
                    ni = (i + di[dit] * n_sa) % n # 이동할 row 좌표
                    nj = (j + dj[dit] * n_sa) % n # 이동할 col 좌표
                    save_fire.append([ni, nj, n_ma, n_sa, dit])
                    # save_fire에 이동 위치와 질량, 속도, 방향 기록
                board[i][j].clear() # 파이어볼 보냈으니 칸 내용 제거
            elif len(board[i][j]) == 1: # 하나의 파이어볼만 있을 때
                n_ma = board[i][j][0][0]
                n_sa = board[i][j][0][1]
                dit = board[i][j][0][2]
                # 출발과 도착의 질량, 속도, 방향이 동일
                ni = (i + di[dit] * n_sa) % n
                nj = (j + dj[dit] * n_sa) % n # 도착 위치 결정
                save_fire.append([ni, nj, n_ma, n_sa, dit])
                # save_fire에 저장
                board[i][j].clear() # 칸 내용 제거
    fire_sum = 0
    for new_f in save_fire: # 저장했던 도착위치 정보들을 이용하여
        ii = new_f[0]
        jj = new_f[1]
        fire_sum += new_f[2] ## 모든 파이어볼이 도착할 때의 질량 합
        board[ii][jj].append([new_f[2], new_f[3], new_f[4]])
        # 격자판에 새롭게 파이어볼 정보를 올린다.

    if ti == k:
        print(fire_sum)
