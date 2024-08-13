import sys

def find_updice(col):
    if col == 0:
        next_col = 5
    elif col == 1:
        next_col = 3
    elif col == 2:
        next_col = 4
    elif col == 3:
        next_col = 1
    elif col == 4:
        next_col = 2
    else:
        next_col = 0
    return next_col
# 주사위의 아랫면 숫자의 열 인덱스를 받으면, 윗면 숫자 열 인덱스를 반환


n = int(input())
dice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 주사위 전개도
result = [[0 for _ in range(n + 1)] for _ in range(6)] # 1 ~ 6까지 출발했을 때(아랫면)의 윗면
max_sum = 0 # 합의 최대
for num in range(1, 7): # 시작(아랫면)을 1~6 돌며
    i = 0
    result[num - 1][i] = num # 결과 처음에 num값 할당
    s = 0
    while i < n:
        cj = dice[i].index(result[num - 1][i]) # dice i열에서 아랫면 숫자 인덱스 추출
        nj = find_updice(cj) # 윗면 인덱스 획득
        result[num - 1][i + 1] = dice[i][nj] # result 배열에 윗면 숫자 입력
        ano_case = [0, 0, 0, 0, 0, 0]
        for j in range(6):
            if j != cj and j != nj:
                ano_case[j] = dice[i][j] # 아랫면, 윗면을 제외하고 나머지 숫자중
        s += max(ano_case) # max 값을 합에 더한다.
        i += 1 # 다음 행으로
    if max_sum < s:
        max_sum = s # 최대 합 갱신

print(max_sum)