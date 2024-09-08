import sys


def chain(nn):  # 특정 톱니와 같이 돌아가는 톱니를 확인하는 함수
    visit[nn] = 1  # 현 톱니는 돌아감 (1)
    nr = nn + 1  # 다음 번호 톱니
    na = nn - 1  # 이전 번호 톱니
    # 다음 번호나 이전 번호의 톱니가 있고, 맞닿는 톱니의 극이 서로 다르다면
    # 그 톱니가 돌아감을 확인한다.
    if 0 < nr <= 4 and visit[nr] == 0 and cog[nn][idx[nn][1]] != cog[nr][idx[nr][2]]:
        chain(nr)
    if 0 < na <= 4 and visit[na] == 0 and cog[nn][idx[nn][2]] != cog[na][idx[na][1]]:
        chain(na)


def check(stg, ii):  # 12시 방향을 판별하여 점수를 계산하는 함수
    if stg == '1':  # S극이면
        return 2 ** (ii - 1)  # 2^(톱니번호 - 1) 의 점수를 반환
    return 0  # N극이면 0 반환


# 첫번째 톱니 회전에 따른 방향
rr = (0, 1, -1, 1, -1)
lr = (0, -1, 1, -1, 1)

cog = {}  # 톱니의 N, S 배열을 담을 리스트
for i in range(1, 5):  # 톱니 상태 받아오기
    cog[i] = list(sys.stdin.readline().rstrip())
# 각 톱니의 12시, 3시, 9시 방향 인덱스 번호
idx = {1: [0, 2, 6],
       2: [0, 2, 6],
       3: [0, 2, 6],
       4: [0, 2, 6]}
for i in range(int(sys.stdin.readline())):
    visit = [0] * 5  # 시작 톱니로부터의 연결 확인 리스트
    n, r = map(int, sys.stdin.readline().split())
    chain(n)

    if r == rr[n]:  # 다른 톱니들이 돌아가는 방향 선택
        rot = rr
    else:
        rot = lr

    for j in range(1, 5):
        if visit[j] and rot[j] == 1:  # j번 톱니가 돌아가고, 그 방향이 시계방향이면
            for k in range(3):
                idx[j][k] = (idx[j][k] - 1) % 8  # 인덱스 번호를 1씩 감함
        elif visit[j] and rot[j] == -1: # j번 톱니가 돌아가고, 그 방향이 시계반대방향이면
            for k in range(3):
                idx[j][k] = (idx[j][k] + 1) % 8  # 인덱스 번호를 1씩 더함

score = 0  # 최종 점수
for i in range(1, 5):
    score += check(cog[i][idx[i][0]], i)  # 12시 방향을 판별하여 점수 계산

print(score)
