###### pypy3 정답 ######
import sys


def ladder(v):  # 사다리 내리기
    sv = v  # 시작 지점 저장
    start = 0  # 행 번호
    while start < h:
        if test_point[start][v] >= 0:  # 좌우 연결되어 있으면
            v = test_point[start][v]  # v(열 번호) 변경
        start += 1  # 한 칸 아래로

    if v == sv:  # 시작지점과 도착지점 열번호가 같으면
        return True  # True 반환
    return False


n, m, h = map(int, sys.stdin.readline().split())
point = [[-1] * n for _ in range(h)]  # 교차점 배열(세로선 가로선)
if m:  # 사전에 가로가 있으면
    # point 배열에 이동되는 위치를 기록
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        point[a][b] = b + 1
        point[a][b + 1] = b

possible = []  # 가로선을 만들 수 있는 위치를 담는 리스트
for i in range(h):
    for j in range(n - 1):
        if point[i][j] + point[i][j + 1] == -2:  # 양쪽 다 다른 가로선과 연결되어 있지 않으면
            possible.append((i, j))  # 추가

result = -1  # 출력 값
len_po = len(possible)

# 0개
test_point = [row[:] for row in point]
for k in range(n - 1):
    if not ladder(k):  # 한 번이라도 자기 자신을 만나지 않으면 종료
        break
else:  # 모두 일치할 때
    result = 0

# 1개
if result < 0:
    for lad in possible:
        ci, cj = lad
        # point 배열에 연결됨을 표현
        test_point[ci][cj] = cj + 1
        test_point[ci][cj + 1] = cj
        
        # 사다리
        for k in range(n - 1):
            if not ladder(k):
                break
        else:
            result = 1
            break
        
        # point 배열 원상복귀
        test_point[ci][cj] = -1
        test_point[ci][cj + 1] = -1

# 2개 (이중 for문 사용)
if result < 0:
    for i in range(len_po - 1):
        ci, cj = possible[i]
        test_point[ci][cj] = cj + 1
        test_point[ci][cj + 1] = cj

        for j in range(i + 1, len_po):
            ei, ej = possible[j]
            # 선택된 좌표가 다른 가로선과 겹친다면 다음으로 넘어감
            if test_point[ei][ej] >= 0 or test_point[ei][ej + 1] >= 0:
                continue

            test_point[ei][ej] = ej + 1
            test_point[ei][ej + 1] = ej

            for k in range(n - 1):
                if not ladder(k):
                    break
            else:
                result = 2
                break

            test_point[ei][ej] = -1
            test_point[ei][ej + 1] = -1

        if result == 2:
            break

        test_point[ci][cj] = -1
        test_point[ci][cj + 1] = -1

# 3개 (삼중 for문 사용)
if result < 0:
    for i in range(len_po - 2):
        ci, cj = possible[i]
        test_point[ci][cj] = cj + 1
        test_point[ci][cj + 1] = cj

        for j in range(i + 1, len_po - 1):
            ei, ej = possible[j]
            if test_point[ei][ej] >= 0 or test_point[ei][ej + 1] >= 0:
                continue

            test_point[ei][ej] = ej + 1
            test_point[ei][ej + 1] = ej

            for p in range(j + 1, len_po):
                pi, pj = possible[p]
                if test_point[pi][pj] >= 0 or test_point[pi][pj + 1] >= 0:
                    continue

                test_point[pi][pj] = pj + 1
                test_point[pi][pj + 1] = pj

                for k in range(n - 1):
                    if not ladder(k):
                        break
                else:
                    result = 3
                    break

                test_point[pi][pj] = -1
                test_point[pi][pj + 1] = -1

            if result == 3:
                break

            test_point[ei][ej] = -1
            test_point[ei][ej + 1] = -1

        if result == 3:
            break

        test_point[ci][cj] = -1
        test_point[ci][cj + 1] = -1

print(result)


###### 시간 초과 - 비트마스킹 ######
import sys
sys.stdin = open('input.txt')
from pprint import pprint


def ladder(v):
    sv = v
    start = 0
    while start < h:
        if test_point[start][v] >= 0:
            v = test_point[start][v]
        start += 1

    if v == sv:
        return True
    return False


n, m, h = map(int, sys.stdin.readline().split())
point = [[-1] * n for _ in range(h)]
if m:
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        point[a][b] = b + 1
        point[a][b + 1] = b

possible = []
for i in range(h):
    for j in range(n - 1):
        if point[i][j] + point[i][j + 1] == -2:
            possible.append((i, j))

len_po = len(possible)
t_cnt = 4

for i in range(1 << len_po):  # 2의 300승...
    cnt = 0
    test_point = [row[:] for row in point]
    for j in range(len_po):
        if i & (1 << j):
            ci, cj = possible[j]
            if test_point[ci][cj] >= 0 or test_point[ci][cj + 1] >= 0:
                continue
            cnt += 1
            if cnt >= t_cnt:
                continue

            ci, cj = possible[j]
            test_point[ci][cj] = cj + 1
            test_point[ci][cj + 1] = cj

    for k in range(n - 1):
        if not ladder(k):
            break

    else:
        t_cnt = cnt
        if t_cnt == 0:
            break

if 0 <= t_cnt < 4:
    print(t_cnt)
else:
    print(-1)
