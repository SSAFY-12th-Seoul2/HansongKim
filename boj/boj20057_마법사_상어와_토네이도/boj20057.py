import sys


def rotation(n, mid, w, go):  # 칸을 이동하는 함수
    ci, cj = mid, mid  # 시작점(중앙)
    while True:
        if w % 2 == 0:  # 델타 w의 인덱스가 짝수면 진행 횟수를 1 증가
            go += 1
        for _ in range(go):  # 델타 전진
            ni = ci + di[w]
            nj = cj + dj[w]
            if ni >= 0 and nj >= 0:
                scatter(n, ni, nj, w)  # 모래량 계산
                ci = ni
                cj = nj  # 현 위치를 다음 위치로 변경
            else:  # 마지막 칸을 넘어가면
                return  # 함수 종료
        w = (w + 1) % 4  #  한 방향으로 모두 갔고 마지막이 아니면, 델타 조정


def scatter(n, ti, tj, w):  # 모래를 흩뿌리는 함수
    global out_sand
    r_tio = ro_ra[w]  # 델타가 w일 때의 칸 모래 비율
    cal_a = 0  # a의 모래양을 구하기 위한 나머지 합
    y_sand = lst[ti][tj]  # Y 위치 모래량
    for p in range(5):
        for q in range(5):
            nni = ti + p - 2
            nnj = tj + q - 2  # 현 위치의 주변 5*5 인덱스 번호
            if r_tio[p][q] > 0:  # 배율이 있을 때
                if 0 <= nni < n and 0 <= nnj < n:  # N * N 이내 지점이면
                    lst[nni][nnj] += int(y_sand * r_tio[p][q])  # 그 위치에 모래 추가
                else:  # 밖이면
                    out_sand += int(y_sand * r_tio[p][q])  # 나간 모래량에 추가
                cal_a += int(y_sand * r_tio[p][q])
    dti = ti + di[w] 
    dtj = tj + dj[w]  # A 위치 좌표
    a_sand = y_sand - cal_a  # A 위치에 추가되는 모래량
    if 0 <= dti < n and 0 <= dtj < n:  # 범위 내면
        lst[dti][dtj] += a_sand  # 그 위치에 추가
    else:  # 범위 밖이면
        out_sand += a_sand  # 나간 모래량에 추가


di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]  # 델타
ratio = [[0, 0, 0.02, 0, 0],
         [0, 0.1, 0.07, 0.01, 0],
         [0.05, 0, 0, 0, 0],
         [0, 0.1, 0.07, 0.01, 0],
         [0, 0, 0.02, 0, 0]]  # 왼쪽으로 갈 때 모래 비율

n = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ro_ra = [ratio] + [[] for _ in range(3)]  # 네 방향에 대해 모래 비율을 담을 리스트
for i in range(1, 4):  # 90도, 180도, 270도 일 때의 모래 비율 리스트 생성
    ro_lst = [[0] * 5 for _ in range(5)]  # 각 상황의 모래 비율 리스트
    ra_lst = ro_ra[i - 1]  # 이전 각도 리스트
    for j in range(5):
        for k in range(5):
            ro_lst[j][k] = ra_lst[k][4 - j] # 90도 회전
    ro_ra[i] = [row[:] for row in ro_lst]  # ro_ra에 입력

out_sand = 0  # 나간 전체 모래 량

mid = n // 2  # 중앙 인덱스 번호
rotation(n, mid, 0, 0)  # 이동하며 나간 모래량 구하기

print(out_sand)
