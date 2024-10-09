import sys


def find_top(x):
    if top[x] == x:
        return x

    first = find_top(top[x])
    return first


def union(x, y):
    root_x = find_top(x)
    root_y = find_top(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        top[root_y] = root_x
    else:
        top[root_x] = root_y


# Kruskal 방식으로 풀이
n, m = map(int, sys.stdin.readline().split())
if m < n - 1:  # 주어진 도로가 (건물 - 1)개보다 적다면 모두 연결할 수 없으므로
    result = -1  # 결과값 -1
else:
    roads = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    total = sum(road[2] for road in roads)  # 가중치들의 총합
    roads.sort(key=lambda x: x[2])  # 가중치 오름차순으로 정렬

    top = [i for i in range(n + 1)]  # 해당 건물에 연결된 도로의 시작점 저장

    cnt = 0  # 연결된 도로 개수
    wei = 0  # 연결된 도로들의 가중치 합

    # 도로를 가중치 순으로 순회하며
    # 연결되어있지 않은 경우 연결
    for a, b, c in roads:
        # 출발점이 다르면 연결되지 않음
        if find_top(a) != find_top(b):
            union(a, b)  # a와 b 건물과 연결된 시작점을 동일하게 한다.
            cnt += 1  # 연결했으니 +1
            wei += c  # 그 때의 가중치 더함
            if cnt == n - 1:  # 최소 연결 조건이 만족되면 끝냄
                break

    test = 0
    for i in range(n + 1):
        # 각자의 시작 건물을 확인
        if find_top(i) == i:
            # 자기자신이 시작건물이면 test 1 증가
            test += 1
        
        # 건물이 모두 연결되었다면, 시작 건물과 더미인 0번 건물만 자기 자신이 나와야함
        # 따라서 test가 2가 아니면 모든 건물이 연결되지 않은 것
        if test > 2:
            result = -1
            break
    else:  # 모든 건물이 연결되었으면
        result = total - wei  # 최대 가중치 합에서 현 case 가중치 뺀것을 결과로

print(result)
