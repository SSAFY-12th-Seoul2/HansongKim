import sys

def find_route(n_dict, n_wadct, day = 0):
    if day not in n_dict.keys():
        return 0
    m_wage = 0
    wage_lst = [0]
    for next_day in n_dict[day]:
        wage_lst += [n_wadct[day] + find_route(n_dict, n_wadct, next_day)]
    if n_dict[day] == []:
        wage_lst += [n_wadct[day]]
    m_wage = max(wage_lst)
    return m_wage

n = int(input())
n_wadct = {}
n_dict = {}
for i in range(1, n+1):
    work, wage = map(int, sys.stdin.readline().split())
    n_wadct[i] = wage
    if i + work - 1 <= n:
        n_dict[i] = list(range(i+work, n+1))

final_wage = 0
for s_day in n_dict.keys():
    m_wage = find_route(n_dict, n_wadct, s_day)
    if final_wage < m_wage:
        final_wage = m_wage

print(final_wage)