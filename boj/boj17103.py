import sys

v = 1000000
pft_list = [False] * 2 + [True] * (v - 1)

for i in range(2, v + 1):
    if pft_list[i]:
        for j in range(2 * i, v + 1, i):
            if pft_list[j] == True:
                pft_list[j] = False
pft_dict = dict(enumerate(pft_list))

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    goldbach = 0
    if n == 4:
        goldbach = 1
    else:
        half_n = n // 2
        for j in range(3, half_n + 1, 2):
            side_j = n - j
            if pft_dict[j] and pft_dict[side_j]:
                goldbach += 1    
    
    print(goldbach)