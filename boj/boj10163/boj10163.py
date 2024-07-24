import sys

n = int(input())
xywh_lst = [[] for _ in range(n)]
set_list = [[] for _ in range(n)]
sum_set = []
for num in range(n):
    xywh_lst[num] = list(map(int, sys.stdin.readline().split()))

for num in range(n-1, -1, -1):
    x, y, wid, hei = xywh_lst[num]
    for i in range(x, x + wid):
        for j in range(y, y + hei):
            if num == (n - 1):
                set_list[num].append((i, j))
                sum_set += [(i, j)]
            else:
                if (i, j) not in sum_set:
                    set_list[num].append((i, j))
                    sum_set += [(i, j)]
print(sum_set)
for k in range(n):
    print(len(set_list[k]))