import sys
# sys.stdin = open("input.txt")


def beam(v, rm):  # cctv 발각 지점을 찾는 함수
    if v == len(cctv):  # 모든 cctv 방향을 결정하면
        return cnt_zero(rm)  # 그 때의 사각지대 확인
    min_space = 100000000
    si = cctv[v][0]
    sj = cctv[v][1]
    num = room[si][sj]  # cctv 번호 확인
    for ws in dirs[num]:
        test_rm = [row[:] for row in rm]  # test room 복사
        for w in ws:
            ci, cj = si, sj  # 현재 위치 설정
            while True:  # 각 방향별 dfs
                ni = ci + di[w]
                nj = cj + dj[w]
                if 0 <= ni < n and 0 <= nj < m:
                    if test_rm[ni][nj] == 0 or test_rm[ni][nj] == -1:  # 빈 공간
                        test_rm[ni][nj] = -1
                        ci, cj = ni, nj
                    elif 0 < test_rm[ni][nj] < 6:  # 다른 cctv
                        ci, cj = ni, nj
                    else:  # 벽 만나면
                        break
                else:  # 인덱스 벗어나면
                    break
        min_space = min(beam(v + 1, test_rm), min_space)  # 최소 사각 갱신
    return min_space


def cnt_zero(rm):  # 0의 개수 세는 함수
    cnt = 0
    for p in range(n):
        for q in range(m):
            if rm[p][q] == 0:
                cnt += 1
    return cnt


di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)  # 델타

dirs = {1: ((0,), (1,), (2,), (3,)),
        2: ((0, 2), (1, 3)),
        3: ((0, 1), (1, 2), (2, 3), (3, 0)),
        4: ((0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)),
        5: ((0, 1, 2, 3),)}  # 각 cctv 번호별 델타 인덱스


n, m = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cctv = []
for i in range(n):
    for j in range(m):
        if 0 < room[i][j] < 6:
            cctv.append((i, j))  # cctv 모음

result = beam(0, room)
print(result)
