import sys


def comb(n):  # 팀별 조합을 뽑는 함수
    # 한 쪽을 뽑으면 다른 한쪽은 정해진다.
    temp = {0}  # 한 쪽 팀을 담을 set
    div = n // 2  # 뽑는 인원수

    def comb_in(i, div, temp):
        global min_diff
        global start_ab
        global link_ab
        if len(temp) == div:  # 한 조가 짜여지면
            other = pp.difference(temp)  # 나머지 인원들로 조 형성
            perm(list(temp), 0, 0)  # 팀 1의 능력치
            perm(list(other), 0, 1)  # 팀 2의 능력치
            diff = abs(start_ab - link_ab)  # 능력치합의 차
            min_diff = min(min_diff, diff)  # 기존 최소 능력치와 비교 갱신
            start_ab = link_ab = 0  # 각 팀 능력치 합 초기화
            return
        else:
            for j in range(i, n):  # 한 조에 인원이 찰 때까지
                temp.add(j)  # j 번 선수 선택
                comb_in(j + 1, div, temp)  # 다음 선수를 고르기
                temp.discard(j)  # 원상복귀
    comb_in(1, div, temp)


def perm(lst, i, op):  # 조의 능력치를 구하는 함수
    global start_ab
    global link_ab
    if i == 2:  # 2명이 선택되면
        if op:  # 링크 조일 때
            link_ab += ab_lst[lst[0]][lst[1]]
        else:  # 스타스 조일 때
            start_ab += ab_lst[lst[0]][lst[1]]
    else:
        for j in range(i, len(lst)):  # 순열 찾기
            lst[i], lst[j] = lst[j], lst[i]
            perm(lst, i + 1, op)
            lst[i], lst[j] = lst[j], lst[i]


n = int(input())
ab_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

pp = set([i for i in range(n)])  # 사람 번호(편의상 0 ~ n - 1)
min_diff = 10000  # 결과값(최소차)
start_ab = link_ab = 0  # 스타트 팀과 링크 팀의 능력치 합

comb(n)
print(min_diff)
