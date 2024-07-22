import sys

col, row = map(int, sys.stdin.readline().split())
cut = int(input())
coli, rowl = [0, col], [0, row]
for i in range(cut):
    dir, idx = map(int, sys.stdin.readline().split())
    if dir:
        coli.append(idx)
    else:
        rowl.append(idx)
coli.sort()
rowl.sort()
cmax, rmax = 0, 0
for j in range(1, len(coli)):
    col_df = coli[j] - coli[j - 1]
    if col_df > cmax:
        cmax = col_df
for k in range(1, len(rowl)):
    row_df = rowl[k] - rowl[k - 1]
    if row_df > rmax:
        rmax = row_df
print(cmax * rmax)