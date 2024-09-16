import sys


def move(ti):
    cnt = 0  # 내구도가 0인 칸의 개수
    si = 0  # 첫번째 칸의 번호
    while True:
        # 컨베이어 벨트 1칸 회전
        si = (si - 1) % (2 * n)
        # 로봇도 이동
        for p in range(n - 2, -1, -1):
            if not robot[p]:
                continue
            robot[p + 1] = True
            robot[p] = False
        # 로봇 하차
        if robot[n - 1]:
            robot[n - 1] = False
        
        # 로봇 이동(먼저 올라온 순)
        for p in range(n - 2, -1, -1):
            bi = (si + p + 1) % (2 * n)
            # 다음 칸이 내구도가 없거나 로봇이 있을 경우 이동 X
            if belt[bi] == 0 or robot[p + 1]:
                continue
            # 지금 칸에 로봇이 없으면 통과
            if not robot[p]:
                continue
            # 로봇 이동
            robot[p + 1] = True
            robot[p] = False
            # 내구도 감소
            belt[bi] -= 1
            if not belt[bi]:
                cnt += 1
        # 로봇 하차
        if robot[n - 1]:
            robot[n - 1] = False
        
        # 1번 위치에 로봇 올리기
        if belt[si] and not robot[0]:
            robot[0] = True
            belt[si] -= 1
            if not belt[si]:
                cnt += 1
               
        # 0 판단
        if cnt >= k:
            return ti  # 걸린 시간 반환
        ti += 1  # 끝나지 않았으면 시간 증가


n, k = map(int, sys.stdin.readline().split())
belt = list(map(int, sys.stdin.readline().split()))

robot = [False] * n  # n번 칸까지의 로봇의 위치(True면 있음)
print(move(1))
