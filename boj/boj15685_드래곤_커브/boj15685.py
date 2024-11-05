import sys

"""
1 : l
2 : llr
3 : llrllrr
4 : llrllrrlllrrlrr
"""


def get_drt(gen):  # n 세대일 때의 드래곤 커브가 나아가는 방향을 구하는 함수
    if memo.get(gen):  # 이미 memo에 n 세대 정보가 있으면 그대로 반환
        return memo[gen]
        
    f_half = get_drt(gen - 1)  # 세대 방향 정보의 앞부분
    # 뒷부분은 앞부분을 역순으로 나열한 후, 그 반대 방향을 적어주면 된다.
    s_half = ''
    for pp in f_half[::-1]:
        s_half += attr[pp][0]
    
    # 앞부분과 뒷부분 그리고 그 중간에 왼쪽 방향을 넣으면, 해당 세대의 방향정보가 된다.
    return f_half + 'l' + s_half


def next_point(si, sj, drt, gen):  # 방향정보를 기반으로 다음 꼭지점으로 넘어가 carve를 진행하는 함수
    carve(si, sj)
    ci = si + di[drt]
    cj = sj + dj[drt]
    carve(ci, cj)
    
    drts = get_drt(gen)  # 세대에 따른 방향정보 구하기
    for ll in drts:
        drt = (drt + attr[ll][1]) % 4  # 다음 델타 방향
        ci += di[drt]
        cj += dj[drt]
        carve(ci, cj)


def carve(ci, cj):  # 꼭지점 ci, cj가 있을 때, 주변 4칸의 꼭지점 정보를 갱신하는 함수
    for dp, dq, loc in fill:
        if 0 <= (fi := ci + dp) < 100 and 0 <= (fj := cj + dq) < 100 and not field[fi][fj][loc]:
            field[fi][fj][loc] = True
    

di = (0, -1, 0, 1)
dj = (1, 0, -1, 0)

fill = ((-1, -1, 'rb'), (-1, 0, 'lb'), (0, -1, 'rt'), (0, 0, 'lt'))  # 꼭지점 기준

n = int(sys.stdin.readline())
curve = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# field의 lt, rt, lb, rb는 각 칸의 꼭지점 정보
field = [[{'lt': False, 'rt': False, 'lb': False, 'rb': False} for _ in range(100)] for _ in range(100)]
memo = {1: 'l', 2: 'llr', 3: 'llrllrr', 4: 'llrllrrlllrrlrr'}  # 세대 별 방향정보 기록 딕셔너리

attr = {'l': ('r', 1), 'r': ('l', -1)}  # 방향에 대한 속성들 (반대 방향, 델타 변경 값)

for j, i, d, g in curve:
    if g == 0:  # 0세대일 때
        carve(i, j)  # 시작 꼭지점을 각 칸에 기록
        ni = i + di[d]
        nj = j + dj[d]
        carve(ni, nj)  # 그 다음 꼭지점을 각 칸에 기록
    else:  # 1세대 이상일 때 (방향 지정이 가능할 때)
        next_point(i, j, d, g)

cnt = 0     
# 네 꼭지점이 모두 True인 점을 셈   
for i in range(100):
    for j in range(100):
        if all(field[i][j].values()):
            cnt += 1
            
print(cnt)
