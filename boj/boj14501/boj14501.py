import sys

n = int(input())
n_list = [[] for _ in range(n+1)]
for i in range(1, n+1):
    work, wage = map(int, sys.stdin.readline().split())
    n_list[i] = [i, work - 1, wage]

while True:
    if n_list[0] + n_list[1] >
    pass