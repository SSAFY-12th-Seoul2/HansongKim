import sys
from collections import deque


def perm(v, p_lst, inn):
    if v == 8:
        player = p_lst[:3] + [player_score[0]] + p_lst[3:]
        possible[i].add(player)
        return
    else:
        for u in range(v, 8):
            p_lst[v], p_lst[u] = p_lst[u], p_lst[v]
            perm(v + 1, p_lst, inn)
            p_lst[v], p_lst[u] = p_lst[u], p_lst[v]


def baseball():


n = int(input())
inning = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
n_start = [0] * (n + 1)

possible = {}
for i in range(n):
    possible[i] = set()
    player_score = inning[i]
    perm(0, player_score[1:], i)

max_score = 0
