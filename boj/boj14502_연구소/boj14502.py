import sys
from collections import deque


def comb(sl, n, m):  # 벽을 세울 위치의 조합을 찾는 함수
    tp = []

    def comb_in(sl, tp, sw, n, m):
        global max_safe
        if len(tp) == 3:  # 위치 3곳을 모두 골랐으면
            max_safe = max(bfs(tp, n, m), max_safe)  # 안전구역 확인 및 갱신
            return
        else:
            for w in range(sw, sl):
                tp.append(w)  # 빈 구역 하나의 인덱스 번호 추가
                comb_in(sl, tp, w + 1, n, m)  # 다음 구역 확인
                tp.pop()  # 테스트 끝난 구역 반환
    comb_in(sl, tp, 0, n, m)


def bfs(wall, n, m):  # bfs를 이용하여 바이러스가 퍼지는 범위를 확인 후 안전구역 탐색하는 함수
    cnt = 0
    test_lab = [row[:] for row in lab]  # test용 실험실 리스트
    virus_d = deque(virus)  # 바이러스가 담길 deque
    for p in range(3):
        test_lab[space[wall[p]][0]][space[wall[p]][1]] = 1  # 먼저 정한 위치에 벽을 세운다.
    while virus_d:  # 바이러스 퍼짐 탐색
        ci, cj = virus_d.popleft()
        for w in range(4):  # 델타 활용 바이러스가 퍼진 좌표 탐색(deque에 추가)
            ni = ci + di[w]
            nj = cj + dj[w]
            if 0 <= ni < n and 0 <= nj < m and not test_lab[ni][nj]:
                virus_d.append((ni, nj))  # 바이러스가 퍼진 위치 추가
                test_lab[ni][nj] = 2  # 바이러스가 퍼진 곳은 2로 변환
    # 바이러스가 모두 퍼진 후 안전구역 확인
    for x in range(n):
        for y in range(m):
            if test_lab[x][y] == 0:  # 안전 구역이면
                cnt += 1  # 구역 수 +1
    return cnt  # 안전 구역 수 반환


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

space = []  # 빈 구역 리스트
virus = []  # 바이러스가 있는 위치 리스트
# 연구실을 순회하며, 빈 구역과 바이러스 위치를 각각 확인한다.
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            space.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

s_len = len(space)  # 빈 구역의 개수
max_safe = 0  # 안전구역의 최대치(결과값)
comb(s_len, n, m)

print(max_safe)
