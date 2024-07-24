import sys

small_lst = [0] * 9
for i in range(9):
    small_lst[i] = int(sys.stdin.readline())
diff = sum(small_lst) - 100

end = 0
for i in range(9):
    for j in range(i+1, 9):
        if (small_lst[i] + small_lst[j]) == diff:
            small_lst.pop(j)
            small_lst.pop(i)
            end = 1
            break
    if end == 1:
        break

small_lst.sort()
for i in small_lst:
    print(i)