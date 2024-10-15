import sys

# Kruscal 방식 사용

def find_top(x):  # 대표값을 찾는 함수
    if top[x] == x:
        return x

    # 여기서 top 배열을 갱신하지 않으면
    # 정점이 최대 10,000개이므로
    # 재귀 한도가 초과되었습니다...
    # 기존에는 `first = find_top(top[x])로 임의의 변수로 반환`
    top[x] = find_top(top[x])
    return top[x]
    
    
def union(x, y):  # 두 지점의 대표값을 일치시키는 union 함수
    root_x = find_top(x)
    root_y = find_top(y)
    
    if root_x == root_y:
        return
        
    if root_x < root_y:
        top[root_y] = root_x
    else:
        top[root_x] = root_y
        

v, e = map(int, sys.stdin.readline().split())
roads = [tuple(map(int, sys.stdin.readline().split())) for _ in range(e)]
roads.sort(key=lambda x: x[2])  # 가중치 순으로 오름차순

top = [i for i in range(v + 1)]

cnt = 0
wei = 0
for a, b, c in roads:
    if find_top(a) != find_top(b):
        cnt += 1
        union(a, b)
        wei += c
        if cnt == v - 1:  # 최소 간선을 모으면 종료
            break

print(wei)