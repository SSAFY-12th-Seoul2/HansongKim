c, r = map(int, input().split())
num = int(input())
if num > c * r:
    print(0)
else:
    ft = 2
    n = 1
    bt = 4
    line = 0
    while True:
        line += 1
        dir = ft * (r + c) - bt
        if dir > num:
            break

        ft += 2
        n += 2
        bt += (4 * n)
        print(line, ft, bt, dir)

    ft -= 2
    bt -= (4 * n)