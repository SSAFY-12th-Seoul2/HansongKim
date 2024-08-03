import sys

wid, hei = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
hour = int(input())

loca_p = (p + hour) % (2 * wid)
loca_q = (q + hour) % (2 * hei)
if loca_p > wid:
    loca_p = 2 * wid - loca_p
if loca_q > hei:
    loca_q = 2 * hei - loca_q

print(loca_p, loca_q)