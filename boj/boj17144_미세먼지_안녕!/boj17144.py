import sys


def spread(r, c): # 미세먼지 확산 함수
    zero_room = [[0 for _ in range(c)] for _ in range(r)] # 확산된 결과만을 담는 배열
    zero_room[air_cln[0]][0] = -1
    zero_room[air_cln[1]][0] = -1 # 공기청정기 위치
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0: # 방에 미세먼지가 있다면
                cnt = 0
                sp = room[i][j] // 5 # 나누어지는 미세먼지 양
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1: # 방 안이며 공기청정기가 아니라면
                        zero_room[ni][nj] += sp # 주변부 미세먼지 증가
                        cnt += 1 # 처음 퍼진 곳의 미세먼지 양을 줄이기 위한 횟수
                zero_room[i][j] += (room[i][j] - cnt * sp)
    return zero_room


def rotation(r, c, dir): # 공기청정기 바람이 회전한 결과를 내는 함수
    if dir: # 공기청정기 하단
        area = [0] * (2 * (r - air_cln[dir] + c + 10)) # 방 미세먼지 수치 변경을 위한 저장용 배열
    else: # 공기청정기 상단
        area = [0] * (2 * (air_cln[dir] + c + 10))
    idx = 0 # 시작 방향 인덱스 번호
    fr = air_cln[dir]
    fc = 1 # 공기청정기 우측 시작 좌표
    first = 0 # area 배열에서 바람이 불기 전의 인덱스
    rear = 1 # area 배열에서 바람이 불고 난 후의 인덱스
    while room[fr][fc] != -1: # 공기청정기를 만나기 전까지 계속 돈다.
        area[rear] = room[fr][fc] # rear에 기존 미세먼지 수치를 넣고
        room[fr][fc] = area[first] # first에 있는 값으로 재할당해준다.
        first += 1
        rear += 1
        nfr = fr + di[idx] 
        nfc = fc + dj[idx] # 다음 번 행, 열 좌표
        if nfc == c or nfr == -1 or nfc == -1 or nfr == r: # 다음 번이 방을 벗어난다면
            first -= 1
            rear -= 1
            room[fr][fc] = area[rear]
            if dir: # 방향 인덱스 수정(공기청정기 하단)
                idx += 1 
            else: # 방향 인덱스 수정(공기청정기 하단)
                idx = (idx + 3) % 4
            continue
        else: # 방안이면 그대로 갱신
            fr = nfr
            fc = nfc


r, c, t = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

air_cln = [0, 0]
ac = 0
for i in range(r):
    if room[i][0] == -1:
        air_cln[ac] = i
        ac += 1

for _ in range(t):
    # 확산
    room = spread(r, c)
    # 작동
    ## 윗 지점
    rotation(r, c, 0)
    ## 아랫 지점
    rotation(r, c, 1)

misae = 0
for p in range(r):
    for q in range(c):
        misae += room[p][q]

print(misae + 2)
