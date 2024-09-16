import sys
from collections import deque


def eat_fish(si, sj, size, cnt):  # 먹이를 찾으러 가는 함수
    if check(size):  # 먹을 수 있는 물고기가 없으면
        return 0  # 시간 0초 반환
    visit = [[-1] * n for _ in range(n)]  # 도달 시간 리스트
    deq = deque()
    lo_sub = []  # 초당 탐색하는 위치를 담을 리스트 (정렬을 위함)
    visit[si][sj] = 0  # 시작 지점 0
    deq.append((si, sj))
    while deq:
        ci, cj = deq.popleft()
        if 0 < tank[ci][cj] < size:  # 상어가 먹을 수 있는 먹이를 찾으면
            tank[ci][cj] = 0  # tank를 0으로
            cnt += 1  # 먹은 수 1 증가
            if cnt == size:  # 자기 크기만큼 먹으면
                return visit[ci][cj] + eat_fish(ci, cj, size + 1, 0)
            else:  # 아직 자기 크기만큼 못 먹으면
                return visit[ci][cj] + eat_fish(ci, cj, size, cnt)
        for ni, nj in ((ci + 1, cj), (ci, cj - 1), (ci, cj + 1), (ci - 1, cj)):
            if ni < 0 or ni >= n or nj < 0 or nj >= n:  # 구역 내인지 판단
                continue
            if visit[ni][nj] != -1:  # 방문 한 지점인지 판단
                continue
            if tank[ni][nj] > size:  # 상어보다 큰 것을 만났을 때 판단
                continue
            visit[ni][nj] = visit[ci][cj] + 1  # 위의 상황 외에는 도달 시간 기록
            lo_sub.append((ni, nj))  # 좌표를 리스트에 추가
        if not deq and lo_sub:  # 이전 시간에 저장한 위치는 다 돌고, 갈 위치는 있을 때
            lo_sub.sort()  # 앞으로 갈 위치 정렬
            deq.extend(lo_sub)  # 갈 위치 덱에 추가
            lo_sub = []  # 다음에 갈 위치 초기화
    return 0  # 위의 상황 외에는 먹이를 먹을 수 없으므로 0초 반환


def check(sz):  # 지금 크기로 먹을 수 있는 물고기가 있는지 판단하는 함수
    for p in range(n):
        for q in range(n):
            if 0 < tank[p][q] < sz:  # 내가 먹을 수 있는 물고기가 있으면
                return False 
    return True  # 물고기가 없으면 True


n = int(sys.stdin.readline())
tank = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

tm = 0
for i in range(n):
    for j in range(n):
        if tank[i][j] == 9:  # 아기 상어 위치를 찾아서
            tank[i][j] = 0  # tank 현 위치를 0으로 만들고
            tm = eat_fish(i, j, 2, 0)  # 먹이 찾으러 탐색
            break

print(tm)
