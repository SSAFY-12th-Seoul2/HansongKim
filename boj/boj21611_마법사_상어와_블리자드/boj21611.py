import sys


def board_to_arr():  # 2차원 보드를 1차원 배열로 변경
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # board 받기
    visited = [[0 for _ in range(n)] for _ in range(n)]                       # 방문 기록 배열
    lst = [0] * lst_n                                                         # 1차원 배열 초기화
    gi = (0, 1, 0, -1)
    gj = (1, 0, -1, 0)
    ci, cj, w = 0, 0, 0                 # 현재위치 및 이동방향
    for p in range(lst_n - 1, -1, -1):  # (0, 0) 부터 시작하므로 값을 배열 끝에서부터 채움

        # w방향으로 진행할 수 있으면 진행
        # 불가능하면 w를 시계방향 90도 회전하고 재진행
        lst[p] = board[ci][cj]
        visited[ci][cj] = 1
        if 0 <= (ni := ci + gi[w]) < n and 0 <= (nj := cj + gj[w]) < n and not visited[ni][nj]:
            ci, cj = ni, nj
        else:
            w = (w + 1) % 4
            ci += gi[w]
            cj += gj[w]
    return lst


def blizzard(dd, ss):
    if dd == 1:    # 위쪽
        bn = 7
    elif dd == 2:  # 아래쪽
        bn = 3
    elif dd == 3:  # 왼쪽
        bn = 1
    else:          # 오른쪽
        bn = 5

    for p in range(1, ss + 1):
        idx = bn * p + 8 * (p * (p - 1) // 2)  # 문제의 칸 번호 == 1차원 배열의 인덱스 번호
                                               # 특정 방향으로 블리자드 마법을 쓸 때, 깨지는 칸의 인덱스 번호 규칙
        arr[idx] = 0                           # 블리자드 사용한 칸 0으로 변경


def erase_four():
    after = [0]
    cnt = 0

    if len(arr) > 1:
        cur = arr[1]
    else:
        return True, after
    check = 0                    # check : 폭발한 구슬 그룹의 개수
    for p in range(1, len(arr)):
        if arr[p] == 0:          # arr 값이 0이면 넘긴다          
            continue

        if arr[p] != cur:        # 현 위치 번호가 이전 번호와 달라졌을 때
            if cnt < 4:          # 4 미만이면 after 배열에 추가
                after.extend([cur] * cnt)
            else:                # 4 이상이면 bead의 이전 번호에 구슬 개수 추가
                bead[cur] += cnt
            cur = arr[p]         # 현 위치 번호로 갱신
            cnt = 1              # 구슬 개수도 1로 변경
        else:
            cnt += 1             # 현 위치 번호와 이전 번호가 같다면 개수만 1 증가

        if cnt == 4:             # 구슬 개수가 4개가 되었을 때만, check 증가
            check += 1

    else:                        # 위의 for문에서는 마지막 구슬 조합에 대한 처리가 없음
        if cnt >= 4:             # 마지막 구슬 조합이 4 이상이면
            bead[cur] += cnt     # 폭파하므로 bead에 추가
            return False, after  # False 반환
        after += [cur] * cnt     # 4 미만이면 after에 추가

    if check:                   # 위의 check가 0이 아니면 아직 확인 못한 4개 이상 구슬 조합이 있을 수 있으므로
        return False, after     # False 리턴
    return True, after          # 앞으로 폭파할 구슬 조합이 없을 때, True와 after 배열 리턴


def group_bead():               # 구슬 재조합
    new_arr = [0] * lst_n
    ix = 1
    new_arr[2] = arr[1]
    for p in range(1, lst_n):
        if arr[p] == 0:         # arr 값이 0이면 마지막 지점이므로 for문 종료
            break

        if arr[p] != new_arr[ix + 1]:  # 이전 번호와 다른 번호가 나타나면
            ix += 2                    # ix를 2 증가시키고 진행
            if ix >= lst_n:            # 그 ix가 n * n을 넘어가면 종료 (문제 조건)
                return new_arr

        new_arr[ix + 1] = arr[p]       # ix + 1번 칸에 현재 번호 기록
        new_arr[ix] += 1               # 개수는 ix에 기록

    new_arr = fill_zero(new_arr)       # new_arr 길이가 n*n 보다 작을 경우 뒤를 0으로 채움
    return new_arr


def fill_zero(f_arr):
    if len(f_arr) < lst_n:            # f_arr의 길이가 n*n보다 작으면
        diff = lst_n - len(f_arr)     # 그 차이만큼
        f_arr.extend([0] * diff)      # 0으로 채운다.
    return f_arr


n, m = map(int, sys.stdin.readline().split())
lst_n = n * n
arr = board_to_arr()      # 입력받은 2차원 보드를 1차원 배열로 변환(상어 위치가 0번 인덱스) 
bead = {1: 0, 2: 0, 3: 0} # 폭파된 구슬의 번호당 개수를 저장하는 딕셔너리

for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())
    blizzard(d, s)  # 구슬 파괴

    while True:  # 구슬이 폭팔을 멈출 때까지 반복하는 while문
        erasing = erase_four()
        arr = erasing[1][:]
        if erasing[0]:
            break

    if not any(arr):  # 모든 구슬이 폭발했으면 종료
        break

    arr = fill_zero(arr)  # 폭발로 감소한 arr을 n * n으로 늘리는 함수

    arr = group_bead()  # 구슬 재배치

result = 1 * bead[1] + 2 * bead[2] + 3 * bead[3]

print(result)
