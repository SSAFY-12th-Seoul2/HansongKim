# 행과 열번호가 빠른 '1'의 위치순으로
# 색종이를 가장 작은 것부터 붙이는 방식으로 진행

import sys


def paste(idx, ch, cnt, min_cnt, cft):  # 색종이 붙이는 함수
    if cnt >= min_cnt:  # 이미 최소로 붙인 횟수를 넘어갔다면 조기 종료
        return min_cnt

    if idx == one_len - 1:  # 마지막 '1' 위치일 때
        # 1 * 1이 남아있으면 붙이고 반환
        # 없다면 26(초기값)을 반환
        if cft[1]:
            return cnt + 1
        else:
            return 26

    ci, cj = one_list[idx]  # 현재 '1' 위치
    for n in range(1, 6):  # 1번부터 5번 색종이까지
        # 색종이가 판을 벗어나면 종료(더 큰 색종이 또한 불가능)
        if ci + (n - 1) >= 10 or cj + (n - 1) >= 10:
            return min_cnt

        new_ch = ch[:]  # 체크 배열 복사본
        new_cft = cft[:]  # 색종이 개수 배열 복사본

        # 색종이의 범위만큼 확인한다.
        # 빈 칸이 있으면 붙일 수 없으므로 종료(더 큰 것도 붙일 수 없음)
        # 이미 붙여진 곳도 종료
        ## 붙일 수 있을 경우에만 붙이고 체킹한다.
        for p in range(ci, ci + n):
            for q in range(cj, cj + n):

                if paper[p][q] == 0:
                    return min_cnt
                else:
                    side = one_list.index((p, q))
                    if new_ch[side]:
                        return min_cnt

                    new_ch[side] = True

        # 색종이가 부족하다면, 붙였다는 행위를 취소하고
        # 다음 크기의 색종이로 넘어감
        new_cft[n] -= 1
        if new_cft[n] < 0:
            continue
        
        # 붙였으면 다음 위치로 이동한다.
        # 붙여지지 않은 위치를 찾아 이동한다.
        # 이동에는 재귀함수를 활용하며, 반환 값으로 최소값을 갱신한다.
        ## 다음 위치가 없다면 기존 최소값과 현재 색종이까지 붙인 값중
        ## 최소값 갱신하여 반환
        for iw in range(idx + 1, one_len):
            if new_ch[iw]:
                continue

            min_cnt = min(min_cnt, paste(iw, new_ch, cnt + 1, min_cnt, new_cft))
            break
        else:
            return min(min_cnt, cnt + 1)

    return min_cnt


paper = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
confetti = [0] + [5 for _ in range(5)]  # 색종이 크기별 개수

one_list = []  # '1'의 위치를 담는 리스트
for i in range(10):
    for j in range(10):
        if paper[i][j]:
            one_list.append((i, j))

one_len = len(one_list)  # '1'의 개수
result = 0  # 출력값 (초기값 0)

# 1 위치가 있을 때만 고려한다.
if one_len > 0:
    check = [False] * one_len
    result = paste(0, check, 0, 26, confetti)

# 최대로 붙일 수 있는 색종이 개수는 25개이다.
# 초과하면 붙일 수 없으므로 -1을 출력한다
if result > 25:
    print(-1)
else:
    print(result)
