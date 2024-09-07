import sys
from collections import deque


def comb(mm, nn):  # 성에서 궁수 3명의 위치를 정하는 조합 함수
    tp = []  # 궁수 위치를 담을 리스트

    def comb_in(v, du, k, l, arr):
        global result
        if v == 3:  # 3명이 정해지면
            archer = [(l, arr[w]) for w in range(3)]  # 궁수 위치의 바로 위를 좌표로 저장
            result = max(result, check(archer, k, l + 1))  # 잡은 적 수 갱신
            return
        for u in range(du, k):  # 열 번호로 조합
            arr.append(u)  # 한 자리 추가
            comb_in(v + 1, u + 1, k, l, arr)  # 다음 자리 탐색
            arr.pop()  # 사용 후 자리 반환
    comb_in(0, 0, mm, nn, tp)


def check(lst, kk, ll):  # 잡은 적 수를 세는 함수
    cnt = 0  # 잡은 적의 수
    t_field = [row[:] for row in field]  # 테스트용 필드 리스트
    while is_zero(t_field):  # 적이 있는 동안
        kill = set()  # 잡은 적의 좌표를 저장할 set
        for ac in lst:  # 궁수마다
            kill.add(shoot(ac[0], ac[1], kk, ll, t_field))  # 잡은 적 좌표 추가
        for cor in kill:  # 잡은 적의 좌표가 있으면
            if cor[0] != -1:  # (-1) : 거리 내에 적이 없을 때 반환값 (제외)
                t_field[cor[0]][cor[1]] = 0  # 적을 잡는다 (0으로 바꿈)
                cnt += 1  # 잡은 횟수도 1 증가
        t_field = [[0] * kk] + t_field[:-1]  # 한 행씩 내려오기
    return cnt  # 잡은 적 수 반환


def is_zero(fld):  # check 함수에서 테스트 필드 리스트에 적이 있는지 판단
    rt = False
    for row in fld:  # 필드의 모든 행을 돌아보며
        if any(row):  # 적(1)이 하나도 없다면
            rt = True  # True 할당
    return rt  # 결과 반환


def shoot(si, sj, nk, nl, tfd):  # bfs를 이용해 잡을 적을 탐색하는 함수
    visited = [[0] * nk for _ in range(nl)]
    visited[si][sj] = 1  # 초기 위치는 거리 1 지점
    deq = deque([(si, sj)])
    while deq:
        ci, cj = deq.popleft()  # 현재 탐색 위치
        if visited[ci][cj] > d:  # 현 위치가 거리 너머면
            return -1, -1  # (-1, -1)로 반환
        elif tfd[ci][cj]:  # 적이 있는 위치여도
            return ci, cj  # 그 좌표를 반환
        for w in range(3):
            ni = ci + di[w]
            nj = cj + dj[w]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                deq.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1  # 거리를 입력


n, m, d = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

di = [0, -1, 0]
dj = [-1, 0, 1]  # 아래 방향은 고려하지 않음

result = 0  # 최종 결과값(최대로 잡은 적의 수)
comb(m, n - 1)

print(result)
