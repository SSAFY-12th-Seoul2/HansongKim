import sys


def moving(bod, idx):  # 2048 이동시키는 함수
    bd = [row[:] for row in bod]  # 기존 보드판 복사

    # 전체적으로
    # 값이 있을 때
    ## 그 다음칸들을 확인
    ## 다음칸들에 값이 있을 때
    ### 현 위치와 같은 값이면 2배로 하고, 그 위치는 지움
    ### 다른 값이면 바로 종료
    # 값이 없을 때
    ## sel이란 기록용 변수 선언
    ## 다음 칸들 탐색
    ## 현 위치에 기록할 값이 있다면 sel에 저장
    ## sel 값이 채워졌으면, 그 다음 값이 동일하면 현 위치에 sel * 2 저장

    if idx == 1:
        # 위쪽으로 밀기
        for q in range(n):
            for p in range(n - 1):
                if bd[p][q]:
                    for w in range(p + 1, n):
                        if bd[p][q] == bd[w][q]:
                            bd[p][q] *= 2
                            bd[w][q] = 0
                            break
                        elif bd[w][q] > 0:
                            break

                else:
                    sel = 0
                    for w in range(p + 1, n):
                        if bd[w][q]:
                            if not sel:
                                sel = bd[w][q]
                                bd[p][q] = sel
                                bd[w][q] = 0
                            else:
                                if bd[w][q] == 0:
                                    continue

                                if bd[w][q] == sel:
                                    bd[w][q] = 0
                                    bd[p][q] = sel * 2
                                break

    elif idx == 2:
        # 아래쪽으로 밀기
        for q in range(n):
            for p in range(n - 1, 0, -1):
                if bd[p][q]:
                    for w in range(p - 1, -1, -1):
                        if bd[p][q] == bd[w][q]:
                            bd[p][q] *= 2
                            bd[w][q] = 0
                            break
                        elif bd[w][q] > 0:
                            break

                else:
                    sel = 0
                    for w in range(p - 1, -1, -1):
                        if bd[w][q]:
                            if not sel:
                                sel = bd[w][q]
                                bd[p][q] = sel
                                bd[w][q] = 0
                            else:
                                if bd[w][q] == 0:
                                    continue

                                if bd[w][q] == sel:
                                    bd[w][q] = 0
                                    bd[p][q] = sel * 2
                                break

    elif idx == 3:
        # 왼쪽으로 밀기
        for p in range(n):
            for q in range(n - 1):
                if bd[p][q]:
                    for w in range(q + 1, n):
                        if bd[p][q] == bd[p][w]:
                            bd[p][q] *= 2
                            bd[p][w] = 0
                            break
                        elif bd[p][w] > 0:
                            break

                else:
                    sel = 0
                    for w in range(q + 1, n):
                        if bd[p][w]:
                            if not sel:
                                sel = bd[p][w]
                                bd[p][q] = sel
                                bd[p][w] = 0
                            else:
                                if bd[p][w] == 0:
                                    continue

                                if bd[p][w] == sel:
                                    bd[p][w] = 0
                                    bd[p][q] = sel * 2
                                break

    else:
        # 오른쪽으로 밀기
        for p in range(n):
            for q in range(n - 1, 0, -1):
                if bd[p][q]:
                    for w in range(q - 1, -1, -1):
                        if bd[p][q] == bd[p][w]:
                            bd[p][q] *= 2
                            bd[p][w] = 0
                            break
                        elif bd[p][w] > 0:
                            break

                else:
                    sel = 0
                    for w in range(q - 1, -1, -1):
                        if bd[p][w]:
                            if not sel:
                                sel = bd[p][w]
                                bd[p][q] = sel
                                bd[p][w] = 0
                            else:
                                if bd[p][w] == 0:
                                    continue

                                if bd[p][w] == sel:
                                    bd[p][w] = 0
                                    bd[p][q] = sel * 2
                                break

    return bd


def exponent(num):  # num이 2의 몇 제곱인지 구하는 함수
    val = 0
    while num > 1:
        num //= 2
        val += 1

    return val


def choice(v, bod, tm):  # 다음 방향을 선택하고, 최대값을 반환하는 함수
    # 1 * 1이면 변동 없으므로 바로 반환
    if n == 1:
        return board[0][0]

    # 가능한 최대값에 도달한다면 조기 종료
    # 초기 보드의 최댓값 지수에 +5를 한 것이 가능한 최대값
    if tm == maybe_max:
        return tm

    cm = max(max(row) for row in bod)  # 현재 bd의 최대값
    # 기존 최대값 tm에 도달할 수 없을 때 조기 종료
    if cm < tm // (2 ** (5 - v)):
        return tm

    # 5번을 모두 움직이면 종료
    if v == 5:
        return cm

    for d in range(4):  # 방향을 모두 돌아보며 다음으로 넘어간다.
        tm = max(tm, choice(v + 1, moving(bod, d), tm))

    return tm


n = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

origin_max = max(max(row) for row in board)  # 초기 보드 최대값
maybe_max = 2 ** (exponent(origin_max) + 5)  # 이론상 최대값

result = choice(0, board, 0)
print(result)
