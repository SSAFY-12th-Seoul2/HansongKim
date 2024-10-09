import sys


def find_top(x):  # 도로로 연결된 지점의 시작점을 찾는 함수
    if top[x] == x:
        return x

    first = find_top(top[x])
    return first


def union(x, y):  # 두 지점을 연결하는(시작점을 동일하게 하는) 함수
    root_x = find_top(x)  # x에 연결된 도로의 시작점
    root_y = find_top(y)  # y에 연결된 도로의 시작점

    if root_x == root_y:
        return

    # 문제에 두 지점을 연결한 도로가 2개 이상인 구간이 있어서
    # 작은 지점대신 x 시작점으로 통일하였음
    top[root_y] = root_x  # x, y에 연결된 도로의 시작점이 다르다면, x를 상위로 둠


n, m = map(int, sys.stdin.readline().split())
gender = [''] + list(sys.stdin.readline().split())
if m < n - 1:  # 애초에 모든 대학을 이을 수 없는 경우
    result = -1
else:
    roads = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    roads.sort(key=lambda x: x[2])  # 거리를 오름차순으로 정렬

    top = [i for i in range(n + 1)]  # 시작 대학 기록지

    cnt = 0  # 연결된 도로 수
    wei = 0  # 그 때의 거리 합
    for a, b, c in roads:
        # 연결되지 않았고
        # 특징(M, W)이 다를 때만 판단
        if find_top(a) != find_top(b) and gender[a] != gender[b]:
            union(a, b)
            cnt += 1
            wei += c
            if cnt == n - 1:
                break

    test = 0
    for i in range(n + 1):
        if find_top(i) == i:
            test += 1

        # 시작점인 대학이 2개를 넘어가면 모든 대학이 이어진 것이 아님
        if test > 2:
            result = -1
            break
    else:  # 모두 이어졌을 때만 거리 합을 출력
        result = wei

print(result)
