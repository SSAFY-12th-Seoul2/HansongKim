import sys

n = int(input())
xywh_lst = [[] for _ in range(n)]
set_list = [0 for _ in range(n)]
sum_set = {}
for num in range(n):
    xywh_lst[num] = list(map(int, sys.stdin.readline().split()))

for num in range(n-1, -1, -1):
    x, y, wid, hei = xywh_lst[num]
    cnt = 0
    for i in range(x, x + wid):
        for j in range(y, y + hei):
            if sum_set.get((i, j)) is None:
                sum_set[(i, j)] = 1
                cnt += 1
    set_list[num] = cnt

for k in range(n):
    print(set_list[k])