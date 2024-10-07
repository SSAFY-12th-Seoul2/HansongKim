# 김한송

## 바이러스를 놓을 수 있는 위치를 찾은 후
## 그 중 m개를 선택하여 바이러스를 놓고
## 퍼뜨려서 가장 작은 시간을 출력
## + case별 바이러스가 퍼지지 않은 곳이 있는지 판별

# mt = min_time

import sys
from collections import deque


def comb():
    virus_lst = []  # 선택한 바이러스 위치를 담을 리스트
		
		# 바이러스 놓을 위치 선택 함수
    def comb_in(v, u, v_lst, min_time):
		    # v : 바이러스 선택 횟수, u: 조합 탐색 시작 지점
		    # v_lst : 선택한 바이러스 위치 리스트, min_time : 바이러스 퍼짐 최소 시간
        if v == m:
            return bfs_virus(v_lst, min_time)  # 바이러스 위치 선택이 완료되면, 확산시킴
        for du in range(u, len(virus)):
            v_lst.append(virus[du])  # 바이러스 위치 하나 선택
            min_time = min(min_time, comb_in(v + 1, du + 1, v_lst, min_time))  # 다음으로 넘어감
            v_lst.pop()  # 사용한 위치 제거
        return min_time  # 최소 시간 반환

    return comb_in(0, 0, virus_lst, 5000)  # comb_in에서 구해진 최소 시간 반환 (초기 최소 시간 5000초)


# 바이러스 확산 함수
def bfs_virus(v_lst, mt):  
    test_lab = [row[:] for row in lab]  # 테스트용 모방 실험실
    visit = [[5000] * n for _ in range(n)]  # 도달 시간 기록 리스트
    for si, sj in v_lst:
        visit[si][sj] = 0  # 시작 지점 시간 0
        test_lab[si][sj] = 2  # 실험실에 바이러스 설치
        
    deq = deque(v_lst)  # 초기 바이러스 위치 덱으로 만듦
    new_mt = 5000  # new_mt : 반환될 새로운 최소 시간
    while deq:
        ci, cj = deq.popleft()
        if visit[ci][cj] >= mt:  # 시간이 이미 기존 최소시간을 넘어갔다면
            return mt  # 기존 최소 시간 반환하고 종료
        if not deq:  # 확산이 종료되는 마지막 지점이면
            new_mt = visit[ci][cj]  # 그 지점의 시간이 새로운 최소 시간
        for ni, nj in ((ci, cj + 1), (ci + 1, cj), (ci, cj - 1), (ci - 1, cj)):
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue
            if not test_lab[ni][nj]:  # 빈 공간이면
                visit[ni][nj] = visit[ci][cj] + 1  # 시간 기록
                test_lab[ni][nj] = 2  # 바이러스 전파
                deq.append((ni, nj))  # 덱에 추가
                
    # 바이러스가 모두 퍼졌는지 확인
    # `all(*iter)` : 인자가 모두 True면 True 반환, 하나라도 False면 False 반환
    # int형에서 0이 아니면 True로 인식, 0은 False
    if all([all(row) for row in test_lab]):
        return new_mt  # 모두 방문했으면 새로운 최소 시간 반환
    else:
        return mt  # 방문 안한 지점이 있으면, 처음 input된 시간 반환

################################################################################################

n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

virus = []  # 바이러스를 놓을 수 있는 위치(2)를 담는 리스트
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2: # 발견하면
            virus.append((i, j))  # virus에 추가
            lab[i][j] = 0  # 확인한 위치는 빈 공간으로 표시 변경
            # 추후 테스트용 연구실을 기존 연구실을 깊은 복사하여 만들기 위함

result = comb()
if result == 5000:  # 한번도 전체 확산이 안되었으면
    print(-1)  # -1 출력
else:  # 그 외는 최소 시간 출력
    print(result)