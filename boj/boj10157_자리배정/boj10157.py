import sys


def find_start(row, col, k):
    start = 1
    end = 0
    idx = 1
    max_seat = row * col
    if k > max_seat:
        return 0, 0
    while end < max_seat:
        end += 2 * (row + col) - 4
        if start <= k <= end:
            return idx, start
        row -= 2
        col -= 2
        start = end + 1
        idx += 1


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

col, row = map(int, sys.stdin.readline().split())
k = int(input())
i, s = find_start(row, col, k)
new_r = row - 2 * (i - 1)
new_c = col - 2 * (i - 1)
btn = i
j = i
x = 0
while s < k:
    if btn == 0:
        break
    ni = i + di[x]
    nj = j + dj[x]
    if btn <= ni <= btn + new_r - 1 and btn <= nj <= btn + new_c - 1:
        i = ni
        j = nj
        s += 1
    else:
        x += 1

if btn == 0:
    print(0)
else:
    print(j, i)
