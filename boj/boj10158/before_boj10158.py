import sys

wid, hei = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
hour = int(input())

dp = dq = t = 1
while t <= hour:
    p += dp
    q += dq
    if p == 0 or p == wid:
        dp *= (-1)
    if q == 0 or q == hei:
        dq *= (-1)
    t += 1

print(p, q)

"""
세로벽 : wid만 바뀌어
가로벽 : hei만 바뀌어
꼭지점은 다바뀌어
"""