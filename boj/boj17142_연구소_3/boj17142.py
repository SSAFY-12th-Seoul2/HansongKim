import sys
from collections import deque


def comb():
    virus_lst = []
		
		# 바이러스 놓을 위치 선택 함수
    def comb_in(v, u, v_lst, min_time):
        if v == m:
            return bfs_virus(v_lst, min_time)
        for du in range(u, len(virus)):
            v_lst.append(virus[du])
            min_time = min(min_time, comb_in(v + 1, du + 1, v_lst, min_time))
            v_lst.pop()
        return min_time

    return comb_in(0, 0, virus_lst, 5000)  # 최소 시간 초기값 5000


# 바이러스 확산 함수
def bfs_virus(v_lst, mt):
    test_lab = [row[:] for row in lab]
    visit = [[5000] * n for _ in range(n)]
    for si, sj in v_lst:
        visit[si][sj] = 0
        test_lab[si][sj] = 3  # 활성화된 바이러스를 3으로 설정 (비활성은 2)
    deq = deque(v_lst)
    while deq:
        ci, cj = deq.popleft()
        if test_lab[ci][cj] == 3 and visit[ci][cj] >= mt:  # 활성화된 바이러스 도착시간이 기존보다 길 경우 종료
            return mt
        for ni, nj in ((ci, cj + 1), (ci + 1, cj), (ci, cj - 1), (ci - 1, cj)):
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue
                
            # 빈 공간과 비활성 바이러스를 만났을 때를 구분하여 진행
            if not test_lab[ni][nj] and visit[ni][nj] == 5000:  # 빈 공간이고 한 번도 방문 안했으면
                visit[ni][nj] = visit[ci][cj] + 1  # 시간 기록
                test_lab[ni][nj] = 3  # 활성화
                deq.append((ni, nj))  # 덱에 추가
            if test_lab[ni][nj] == 2 and visit[ni][nj] == 5000:  # 비활성 바이러스가 있고 방문 안했으면
                visit[ni][nj] = visit[ci][cj] + 1  # 시간 기록
                deq.append((ni, nj))  # 덱에 추가
                
    if all([all(row) for row in test_lab]):  # 전부 퍼졌으면
        return find_max(test_lab, visit)  # 그 때의 걸린 시간 반환
    else:
        return mt  # 그 외는 input 시간 반환


# 모두 확산되었을 때, 걸린 시간을 구하는 함수
def find_max(t_lab, visited):
    case_max = 0  # 결과값 (걸린 시간)
    for p in range(n):
        for q in range(n):
            if t_lab[p][q] == 3:  # 활성화 바이러스에서만 시간 비교
                case_max = max(case_max, visited[p][q])
    return case_max


n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus.append((i, j))  # 바이러스 초기 위치 모음

result = comb()
if result == 5000:  # 모두 채우지 못할 때
    print(-1)
else:
    print(result)