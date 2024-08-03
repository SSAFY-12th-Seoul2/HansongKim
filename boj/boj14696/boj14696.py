t = int(input())
for _ in range(t):
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    a_cnt = [0 for _ in range(5)]
    b_cnt = [0 for _ in range(5)]

    for aval in a_lst[1:]:
        a_cnt[aval] += 1
    for bval in b_lst[1:]:
        b_cnt[bval] += 1
    
    for i in range(4, 0, -1):
        if a_cnt[i] > b_cnt[i]:
            print('A')
            break
        elif a_cnt[i] < b_cnt[i]:
            print('B')
            break
        else:
            same = True
            if i == 1 and same == True:
                print('D')