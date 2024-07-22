import sys
t = int(sys.stdin.readline())
ch_list = list(map(int, sys.stdin.readline().split()))
num_list = [i + 1 for i in range(t)]

for i in range(1, t):
    num_list.pop(i)
    bck = i - ch_list[i]

    num_list.insert(bck, i + 1)

for i in range(t):
    print(num_list[i], end = ' ')