import sys

n = int(input())
hexa = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]

if hexa[0][0] <= 2:
    max_widx = 0
    max_hidx = 1
else:
    max_widx = 1
    max_hidx = 0
for i in range(6):
    if hexa[i][0] <= 2:
        if hexa[max_widx][1] < hexa[i][1]:
            max_widx = i
    else:
        if hexa[max_hidx][1] < hexa[i][1]:
            max_hidx = i

in_widx = (max_hidx + 3) % 6
in_hidx = (max_widx + 3) % 6

big_wide = hexa[max_widx][1] * hexa[max_hidx][1]
small_wide = hexa[in_widx][1] * hexa[in_hidx][1]

melon = n * (big_wide - small_wide)
print(melon)