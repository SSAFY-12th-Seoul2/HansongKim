import sys

col, row = map(int, sys.stdin.readline().split())
col_list = [True] * col + [False]
row_list = [True] * row + [False]
cut = int(sys.stdin.readline())
for _ in range(cut):    
    dir, idx = map(int, sys.stdin.readline().split())
    if dir == 0:
        row_list[idx] = False
    else:
        col_list[idx] = False

col_L = []
col_r, row_r = 0, 0
for i in range(len(col_list)):
    if col_list[i]:
        col_r += 1
    else:
        col_L.append(col_r)
        col_r = 1

wide_list = []
for j in range(len(row_list)):
    if row_list[j]:
        row_r += 1
    else:
        for k in range(len(col_L)):
            wide_list.append(row_r * col_L[k])
        row_r = 1

print(max(wide_list))