import sys
from collections import deque


def bridge(t_arr):  # 다리를 연결하는 함수
    distance = [[int(1e9)] * n for _ in range(n)]  # 거리 기록 배열
    ti, tj = t_arr[0]  
    nn = island_class[ti][tj]  # 섬 번호 nn
    for ti, tj in t_arr:
        distance[ti][tj] = 0  # nn번 섬의 테투리의 거리를 0으로 설정

    while t_arr:
        ci, cj = t_arr.popleft()
        if island_class[ci][cj] < nn:  # 자기 섬번호보다 작은 섬을 처음 만나면
            # 자기 번호보다 큰섬은 이미 이전 섬에서 출발할 때 판단했음
            return distance[ci][cj] - 1  # 최소 거리 반환

        for ni, nj in ((ci, cj + 1), (ci + 1, cj), (ci, cj - 1), (ci - 1, cj)):
            # 범위 내에 있고 본인 섬이 아니며, 기록상 거리가 더 가까우면
            if 0 <= ni < n and 0 <= nj < n and island_class[ni][nj] != nn and distance[ni][nj] > distance[ci][cj] + 1:
                distance[ni][nj] = distance[ci][cj] + 1  # 거리 갱신하고
                t_arr.append((ni, nj))  # 덱에 추가
    return int(1e9)  # 오류 등의 상황시 리턴값


def bfs(si, sj, nn):  # 각 섬의 범위와 테두리를 찾는 함수
    deq = deque()  # 섬 범위를 담을 덱
    island_class[si][sj] = nn  # 섬번호(음수)
    deq.append((si, sj))  # 시작 위치 추가
    teduri = deque()  # 테두리를 담을 덱
    while deq:
        ci, cj = deq.popleft()
        flag = 0  # 한 번 담은 테투리를 판별하는 변수
        for ni, nj in ((ci, cj + 1), (ci + 1, cj), (ci, cj - 1), (ci - 1, cj)):
            if 0 <= ni < n and 0 <= nj < n:
                # 섬이고 방문하지 않았으면
                if islands[ni][nj] and not island_class[ni][nj]:
                    island_class[ni][nj] = nn
                    deq.append((ni, nj))

                # ci, cj가 테투리고 아직 teduri에 담지 않았다면
                elif not islands[ni][nj] and not flag:
                    teduri.append((ci, cj))  # 담고
                    flag = 1  # 깃발 세우기
    return teduri  # 테두리 반환


n = int(sys.stdin.readline())
islands = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

island_class = [[0] * n for _ in range(n)]  # 섬번호 기록 배열
teduris = []  # 각 섬의 테두리 덱을 담을 리스트
num = 0  # 섬번호 변수

for i in range(n):
    for j in range(n):
        if islands[i][j] and not island_class[i][j]:
            num -= 1  # 나중에 거리가 자연수로 기록되므로 섬번호는 음수로
            teduris.append(bfs(i, j, num))

min_connect = int(1e9)  # 최소거리(출력값)
for teduri in teduris[:-1]:  # 마지막 섬은 이미 이 전에 고려됨
    min_connect = min(min_connect, bridge(teduri))  # 최소 거리 갱신

print(min_connect)
