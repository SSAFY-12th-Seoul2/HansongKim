import sys

N = int(sys.stdin.readline())

pillars = [(tuple(map(int, sys.stdin.readline().split()))) for _ in range(N)]
pillars.sort(key=lambda x:x[0]) # [(2, 4), (4, 6), (5, 3), (8, 10), (11, 4), (13, 6), (15, 8)]

ground = [0] * (max(pillars, key=lambda x:x[0])[0] + 1)

for x, h in pillars: # 카운트 정렬과 비슷하게 위치는 인덱스로, 높이는 값으로 설정
    ground[x] = h # [0, 0, 4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8]

roof_area = 0 # 지붕 면적을 담을 변수

left, right = 0, len(ground) - 1 # 포인터 지정
left_max, right_max = ground[left], ground[right] # 맥스 변수 일단 할당

while left <= right: # 둘이 만날 때까지
    left_max, right_max = max(ground[left], left_max), max(ground[right], right_max) # 현재 위치의 값과 기존 max값 중 큰 값을 max로 재할당
    if left_max <= right_max: # 만약 왼쪽 max가 더 낮으면 오른쪽으로 이동. 
        roof_area += left_max # 이동하면서 해당 높이만큼 지붕 넓이에 추가
        left += 1
    else: # 오른쪽 max가 더 낮으면 오른쪽 포인터가 왼쪽으로 이동
        roof_area += right_max # 이동하면서 해당 높이만큼 지붕 넓이에 추가
        right -= 1

print(roof_area)