import sys

n = int(input())
pillar_d = {}
for _ in range(n):
    l, h = map(int, input().split())
    pillar_d[l] = h # {인덱스: 높이} 형태로 딕셔너리에 저장

max_key = 0
for nk in pillar_d.keys():
    if max_key < nk:
        max_key = nk
        # 인덱스의 최대 번호 탐색

stack = []
hei = 0 # 스택에 입력되는 지붕의 높이
for i in range(max_key + 1): # 인덱스 범위 동안
    if pillar_d.get(i) is not None and hei < pillar_d.get(i): 
        # 그 위치에 건물이 있고 기존 최대 건물보다 높이가 높다면
        hei = pillar_d.get(i) # 스택 입력 높이를 갱신
    stack.append(hei) # 높이 추가

m_hei = stack[-1] # 지역 내 높이 중 최고

re_stack = [] # 역으로 출발하는 스택
re_hei = 0 # 스택에 입력되는 지붕의 높이(역순)
for j in range(max_key, -1, -1):
    if pillar_d.get(j) is not None and re_hei < pillar_d.get(j):
        re_hei = pillar_d.get(j)

    if re_hei < m_hei:
        re_stack.append(m_hei - re_hei) # 최고 높이 - 역순 건물 높이를 push
    else:
        break

print(sum(stack) - sum(re_stack)) # 두 스택합의 차를 계산
