import sys

paper = set()
for _ in range(4):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for i in range(a, c):
        for j in range(b, d):
            paper.add((i, j))

print(len(paper))