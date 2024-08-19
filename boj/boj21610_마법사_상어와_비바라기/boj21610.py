import sys


def move_cloud(n, dm, s): # 매 번 최종 결과(새로운 구름)를 내는 함수
    # 기본적으로는 현재 구름의 이동 위치를 저장
    m_cloud = [[0 for _ in range(n)] for _ in range(n)] # 현재 구름이 이동할 위치를 담는 배열
    d = dm % 8 # 0~7번으로 방향 인덱스를 활용하기 위함
    for i in range(n):
        for j in range(n):
            if cloud[i][j]: # 구름이 있다면
                ni = (i + s * di[d]) % n
                nj = (j + s * dj[d]) % n # 사전 제시된 속도와 방향을 이용하여 이동
                m_cloud[ni][nj] = 1 # 구름 위치를 1로 함
                lst[ni][nj] += 1 # 구름이 있으니 바구니에 물양도 +1
    dia_wtr(n, m_cloud)
    return new_cloud(n, m_cloud) # 최종 구름 위치 반환


def dia_wtr(n, mc): # 비가 내린 곳의 대각 방향 확인 함수
    for p in range(n):
        for q in range(n):
            if mc[p][q] == 1: # 이번에 비가 내렸으면
                dit = 0 # 왼쪽 아래부터 탐색
                while dit < 8: # 4 방향 탐색할 때까지 돈다.
                    np = p + di[dit]
                    nq = q + dj[dit]
                    if 0 <= np < n and 0 <= nq < n and lst[np][nq] > 0:
                        lst[p][q] += 1 # 수량 증가
                    dit += 2


def new_cloud(n, mc): # 최종적으로 새롭게 생긴 구름을 찾는 함수
    n_cloud = [[0 for _ in range(n)] for _ in range(n)] # 이번 새롭게 올라오는 구름
    for p in range(n):
        for q in range(n):
            if lst[p][q] >= 2 and mc[p][q] == 0: # 수량이 2 이상이고, 이번에 비가 내리지 않았다면
                lst[p][q] -= 2 # 수량이 줄고
                n_cloud[p][q] = 1 # 구름 생성
    return n_cloud


n, m = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

di = [1, 0, -1, -1, -1, 0, 1, 1]
dj = [-1, -1, -1, 0, 1, 1, 1, 0]
cloud = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n-2, n):
    for j in range(2):
        cloud[i][j] = 1

for w in range(m):
    dm, si = map(int, sys.stdin.readline().split())
    cloud = move_cloud(n, dm, si)

rain_s = 0
for row in lst:
    rain_s += sum(row) # 수량 합

print(rain_s)
