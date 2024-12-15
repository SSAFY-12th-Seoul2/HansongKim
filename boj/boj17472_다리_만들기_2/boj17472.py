import sys
from collections import deque


# 섬에 번호를 매기는 함수
# bfs 알고리즘
def specify_num(si, sj, num):
    deq = deque()
    deq.append((si, sj))
    visited[si][sj] = 1
    while deq:
        ci, cj = deq.popleft()
        islands[ci][cj] = num  # 섬 번호 등록
        for ni, nj in ((ci, cj + 1), (ci + 1, cj), (ci, cj - 1), (ci - 1, cj)):
            if 0 <= ni < n and 0 <= nj < m and islands[ni][nj] and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                deq.append((ni, nj))


# 행마다 섬 간 거리 확인
def row_bridge():
    for p in range(n):
        start = islands[p][0]
        leng = 0
        for q in range(m):
            if start == 0 and islands[p][q]:
                start = islands[p][q]
                continue

            if islands[p][q] == 0:
                if start == 0:
                    continue
                leng += 1
                continue

            if start == islands[p][q]:
                leng = 0
                continue

            if start != islands[p][q]:
                if leng == 1:
                    leng = 0
                    start = islands[p][q]
                    continue

                a = min(start, islands[p][q])
                b = max(start, islands[p][q])
                if connect[(a, b)] > leng:
                    connect[(a, b)] = leng
                    leng = 0
                    start = islands[p][q]


# 열마다 섬 간 거리 확인
# 이중 for문에서 행과 열 위치만 바뀜
def col_bridge():
    for q in range(m):
        start = islands[0][q]
        leng = 0
        for p in range(n):
            # start에 아직 섬이 등록되지 않았고
            # 현재 위치에 섬이 있다면
            # start에 섬 번호 입력
            if start == 0 and islands[p][q]:
                start = islands[p][q]
                continue
            
            # 현제 위치가 바다일 때
            # start에 섬이 기록되어 있으면
            # 거리 leng 1 증가
            # start에 섬이 없으면
            # 다음 칸으로
            if islands[p][q] == 0:
                if start == 0:
                    continue
                leng += 1
                continue
            
            # start와 동일한 섬을 만나면
            # 거리 기록 초기화
            if start == islands[p][q]:
                leng = 0
                continue

            # start와 다른 섬을 만나면
            if start != islands[p][q]:
                # 거리가 1이면 초기화 하고 넘어감
                if leng == 1:
                    leng = 0
                    start = islands[p][q]
                    continue
                
                # 그 외에는 connect에 최소를 비교하여 기록
                a = min(start, islands[p][q])
                b = max(start, islands[p][q])
                if connect[(a, b)] > leng:
                    connect[(a, b)] = leng
                # 작업 완료 후 초기화
                leng = 0
                start = islands[p][q]


def find_b(v):  # 기준 섬을 찾는 함수
    if v == rooter[v]:
        return v

    rooter[v] = find_b(rooter[v])
    return rooter[v]


def union_b(x, y):  # 두 섬의 기준 섬을 통일시키는 함수
    root_x = find_b(x)
    root_y = find_b(y)

    # 두 섬의 기준이 다를 경우
    # 순위가 더 높은(rank에서 더 큰 값) 섬을 기준으로 기준 통일
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            rooter[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            rooter[root_x] = root_y
        else:
            rooter[root_y] = root_x
            rank[root_x] += 1


def kruskal():
    b_cnt = 0
    weight = 0
    for bridge in bridges:
        a, b, w = bridge
        if find_b(a) == find_b(b):  # 이미 기준 섬이 같으면 통과
            continue

        union_b(a, b)  # 기준 섬이 다르면 통일
        weight += w    # 총 거리에 추가
        b_cnt += 1     # 만든 다리 개수 하나 증가
        if b_cnt == island_num - 1:  # 최소 다리 개수 만족하면 종료
            break

    if b_cnt < island_num - 1:  # 최소 다리 개수보다 작으면 모두 연결된 것이 아니므로
        return -1               # -1 반환
    return weight               # 그 외에는 다리 총 거리 반환


n, m = map(int, sys.stdin.readline().split())
islands = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]  # 섬 번호를 매길 때 방문 기록 리스트
bridges = []  # 다리 시작과 끝 섬, 그 거리를 담을 다리 리스트

island_num = 0  # 섬 번호
for i in range(n):
    for j in range(m):
        if islands[i][j] and visited[i][j] == 0:
            island_num += 1                       # 섬 번호 설정
            specify_num(i, j, island_num)         # 섬 번호 islands에 기록

connect = {}  # 두 섬의 연결 관계를 담는 딕셔너리
for i in range(1, island_num):
    for j in range(i + 1, island_num + 1):
        connect[(i, j)] = 11  # 초기값 거리 11

row_bridge()  # 행마다 섬 간 거리 탐색
col_bridge()  # 열마다 섬 간 거리 탐색

# connect 정보를 bridges 리스트에 입력
for key, val in connect.items():
    if val == 11:  # 연결이 안된 경우 넘김
        continue

    aa, bb = key
    bridges.append([aa, bb, val])  # 연결이 될 수 있는 경우 bridges에 기록

bridges.sort(key=lambda x: x[2])  # 거리 오름차순으로 정렬
rooter = [i for i in range(island_num + 1)]  # 상위 섬(노드) 기록 리스트
rank = [0] * (island_num + 1)  # rank 기록 리스트

print(kruskal())
