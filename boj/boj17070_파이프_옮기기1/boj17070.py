import sys


def dfs(si, sj, stt):  # 재귀 dfs
    cnt = 0  # 경우의 수
    if si == n - 1 and sj == n - 1:  # 끝지점 도착하면
        return 1  # 1 반환(cnt에 더해짐)
    for k in drt[stt]:
        ni = si + d[k][0]
        nj = sj + d[k][1]
        if 0 <= ni < n and 0 <= nj < n and not room[ni][nj]:  # 범위 안에 있고 벽이 아니면
            if k == 2 and (room[ni - 1][nj] or room[ni][nj - 1]):  # 대각일 경우만 추가 판단
                continue  # 조건 만족 안하면 넘어감
            cnt += dfs(ni, nj, k)  # 갈 수 있으면 다음 판단으로
    return cnt  # 가능한 경우의 수 반환


n = int(sys.stdin.readline())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

d = ((0, 1), (1, 0), (1, 1))  # 파이프의 진행 방향
drt = ((0, 2), (1, 2), (0, 1, 2))  # 현재 방향에서 나아갈 수 있는 경우 [d 참조]

if room[-1][-1]:  # 처음부터 끝에 갈 수 없으면
    result = 0  # 결과 0
else:
    result = dfs(0, 1, 0) # 그 외는 dfs로 판단
print(result)
