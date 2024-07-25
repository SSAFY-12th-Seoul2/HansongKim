c, r = map(int, input().split())
num = int(input())
if num > c * r:
    print(0)
else:
    start = 0
    end = 0
    n = 1
    line = 1
    while True:
        start = end + 1
        end += 2 * (r + c) - 4 * n
        if num >= start and num <= end:
            break

        line += 1
        n += 2

    sub = 2 * (line - 1) + 1
    at_point = [line, line]
    if num == start:
        print(*at_point)
    elif (num - start) <= (r - sub):
        at_point[1] += (num - start)
        print(*at_point)
    elif (num - start) <= (r + c - 2*sub):        
        at_point[0] += (num - (start + r - sub))
        at_point[1] += (r - sub)
        print(*at_point)
    elif (num - start) <= (2*r + c - 3*sub):
        at_point[0] += (c - sub)
        at_point[1] += (start - num + 2*r + c - 3*sub)
        print(*at_point)
    elif num <= end:
        at_point[0] += (start - num + 2*r + 2*c - 4*sub)
        print(*at_point)