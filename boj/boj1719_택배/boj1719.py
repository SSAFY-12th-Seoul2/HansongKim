import sys
import heapq


def second(sv, poi):  # 두번째를 찾는 함수
    # 저장된 값이 시작점이면 그 때의 인덱스 값이 두번째 위치가 됨
    # 내가 간 지점이 이미 second함수로 보정이 되었을 경우, 자기 자신이 나오는 것이 두번째 위치
    if memo[sv][poi] in (poi, sv):
        return poi

    memo[sv][poi] = second(sv, memo[sv][poi])
    return memo[sv][poi]


def decide(v):  # 흔한 다익스트라
    lst = []
    heapq.heappush(lst, (0, v))  # 초기 위치를 가중치 0으로 하여 heappush

    while lst:
        cw, cv = heapq.heappop(lst)  # cw : cv까지의 가중치, cv : 현재 파악 위치
        if weight[cv] < cw:  # 이미 더 빠른 경로가 존재할 경우 건너뛰기
            continue

        for pw, nv in route[cv]:  # cv에 연결된 지점들을 탐색
            nw = cw + pw  # nv까지의 누적 가중치 합
            if weight[nv] <= nw:  # 이미 다음 지점까지의 더 빠른 경로가 있다면 건너뛰기
                continue

            weight[nv] = nw
            heapq.heappush(lst, (nw, nv))
            memo[v][nv] = cv  # memo 배열 nv 위치에 cv 저장


def fill_route(va, vb, w):  # 주어진 간선의 가중치와 위치를 저장하는 함수
    if route.get(va) is None:
        route[va] = []
    route[va].append((w, vb))


n, m = map(int, sys.stdin.readline().split())
route = {}  # 간선 정보 저장 딕셔너리
for _ in range(m):  # 양방향 간선 정보를 저장
    v1, v2, w_in = map(int, sys.stdin.readline().split())
    fill_route(v1, v2, w_in)
    fill_route(v2, v1, w_in)

memo = [[0] * (n + 1) for _ in range(n + 1)]  # 시작점별로 자신 이전 위치를 저장하는 배열

for i in range(1, n + 1):  # 누적 가중치 배열(초기값 1억)
    weight = [100000000] * (n + 1)
    decide(i)  # 매 지점을 시작점으로하여 다익스트라

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:  # 자기 자신이 도착점일 경우 '-'로 출력
            print('-', end=' ')
            continue
        print(second(i, j), end=' ')  # 그 외는 2번째 지점
    print()
