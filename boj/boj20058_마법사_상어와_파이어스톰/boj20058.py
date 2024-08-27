import sys
from collections import deque


def bfs(i, j):  # 뭉쳐있는 얼음 개수 탐색
    iceq = deque()  # 탐색 좌표를 담을 덱 생성
    visited[i][j] = 1  # 시작지점 방문 확인
    iceq.append((i, j))  # 시작 지점 덱에 추가
    cntt = 0  # 뭉친 얼음 개수
    while iceq:  # 좌표가 덱에 있으면
        ci, cj = iceq.popleft()  # 현 좌표를 뽑고
        cntt += 1  # 얼음 개수 1 증가
        for k in range(4):  # 델타를 이용한 bfs 진행
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < sn and 0 <= nj < sn and ice[ni][nj] > 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                iceq.append((ni, nj))
    return cntt  # 개수 반환


def bingle(iq):  # 구역 돌리는 함수
    psn = 2 ** iq  # 구역 한 변의 길이
    old_ice = [row[:] for row in ice]  # 회전하기 전 얼음땅
    for i in range(0, sn, psn):
        for j in range(0, sn, psn):
            for x in range(psn):
                for y in range(psn):
                    ice[i + x][j + y] = old_ice[i + (psn - y - 1)][j + x] # 얼음땅 ice 갱신


def jurorook(ice):  # 녹은 지역 반영하는 함수
    mid_ice = [row[:] for row in ice]  # 얼음 땅 복사본(갱신될 얼음땅)
    for i in range(sn):
        for j in range(sn):
            if ice[i][j] > 0:  # 얼음이 있다면
                cnt = 0  # 주위 판단 count
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < sn and 0 <= nj < sn and ice[ni][nj] > 0:  # 얼음이 있으면
                        cnt += 1  # 횟수 1 증가
                if cnt <= 2:
                    mid_ice[i][j] -= 1  # 주변 2칸 이상 얼음이 없으면 녹음
    return mid_ice  # 갱신한 땅 반환


n, q = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(2 ** n)]
q_lst = list(map(int, sys.stdin.readline().split()))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
sn = 2 ** n  # 전체 구역 변 길이

for iq in q_lst:  # 회전
    bingle(iq)
    ice = jurorook(ice)

total = 0  # 얼음의 총 합
ice_block = 0  # 뭉친 최대 얼음 개수
visited = [[0] * sn for _ in range(sn)]  # bfs 방문 확인 리스트
for i in range(sn):
    for j in range(sn):
        total += ice[i][j]  # 얼음 양 합해주기
        if visited[i][j] == 0 and ice[i][j] > 0:
            ice_block = max(bfs(i, j), ice_block)  # bfs 결과와 기존 최대값 비교 갱신

print(total)
print(ice_block)
