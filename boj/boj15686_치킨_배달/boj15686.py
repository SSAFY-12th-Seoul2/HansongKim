import sys


def comb(m):  # 치킨 집의 조합을 구하는 함수
    cob_lst = [0] * m  # 조합 결과를 담을 리스트

    def make_comb(top, si):  # 조합 생성 함수
        if top == m:  # top이 cob_lst 최대 길이라면
            cal_min(cob_lst)  # 그 조합을 이용하여 최소 비교
            return
        else:
            for sj in range(si, l_chk):
                cob_lst[top] = chk_idx[sj]
                make_comb(top + 1, sj + 1)
                cob_lst[top] = 0

    make_comb(0, 0)


def cal_min(lst):  # 기존 최소와 새로운 최소를 비교하는 함수
    global min_chk  # 기존 최소 거리
    s = 0  # 거리의 합
    for p in range(l_hom):  # 각 집마다
        min_hom_chk = min([dis_lst[p][q] for q in lst])  # 최소 치킨 거리 계산
        s += min_hom_chk  # s에 더함
    min_chk = min(min_chk, s)  # 최소 치킨 거리 갱신


n, m = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

home = []  # 집의 좌표를 받을 배열
chick = []  # 치킨집의 좌표를 받을 배열
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])  # 집추가
        elif city[i][j] == 2:
            chick.append([i, j])  # 치킨집 추가

l_chk = len(chick)  # 치킨집 수
l_hom = len(home)   # 집 수
dis_lst = [[0 for _ in range(l_chk)] for _ in range(l_hom)]  # 각 집과 치킨집 거리를 저장할 배열
for i in range(l_hom):
    for j in range(l_chk):
        hv = home[i]
        cv = chick[j]
        dis_lst[i][j] = abs(hv[0] - cv[0]) + abs(hv[1] - cv[1])  # 거리 계산

chk_idx = [i for i in range(l_chk)]  # 치킨집 번호를 자체 설정
min_chk = 10000

comb(m)
print(min_chk)
