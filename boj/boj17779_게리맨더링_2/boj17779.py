# 좌표의 기울기를 이용한 방식

import sys


def area_five(si, sj):  # 구역을 나누어 최대 최소 인구수 차를 구하는 함수
    min_diff = int(1e9)  # 최소 인구차 초기값 (1억)
    d1 = 1  # 왼쪽 방향
    d2 = 1  # 오른쪽 방향
    while True:
        left = [si + d1 * di[0], sj + d1 * dj[0]]  # 왼쪽 꼭지점 좌표
        right = [si + d2 * di[1], sj + d2 * dj[1]]  # 오른쪽 꼭지점 좌표
        
        # 오른쪽을 먼저 한칸씩 증가시키고,
        # 오른쪽으로 더 이상 갈 수 없으면,
        # 왼쪽을 증가시킨다.
        # 왼쪽마저 끝나면 while문을 종료한다.
        if left[0] >= n or left[1] < 0:
            break
        if right[0] >= n or right[1] >= n:
            d2 = 1
            d1 += 1
            continue
        
        ei, ej = si + d1 + d2, sj - d1 + d2  # 아래 꼭지점 좌표
        population = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  # 구역 별 인구 딕셔너리

        # 열이 x축, 행이 y축이다.
        ## 일반적인 좌표와 리스트 상의 좌표를 비교하면
        ## x축을 기준으로 뒤집어져 있으므로
        ## 그 점을 고려
        for p in range(n):
            for q in range(n):
                # 구역 5 인구수 구하기
                if p >= -(q - sj) + si and p <= -(q - ej) + ei and p >= (q - sj) + si and p <= (q - ej) + ei:
                    population[5] += area[p][q]
                    continue
                
                # 나머지 구역별 인구수 구하기
                if p < left[0] and q <= sj and p < -(q - sj) + si:
                    population[1] += area[p][q]
                elif p <= right[0] and q > sj and p < (q - sj) + si:
                    population[2] += area[p][q]
                elif p >= left[0] and q < ej and p > (q - ej) + ei:
                    population[3] += area[p][q]
                elif p > right[0] and q >= ej and p > -(q - ej) + ei:
                    population[4] += area[p][q]

        # 최대 인구와 최소 인구의 차를 구해서 기존 최소와 갱신     
        case_min_diff = max(population.values()) - min(population.values())
        min_diff = min(min_diff, case_min_diff)
        
        # 오른쪽 방향 한 칸 증가
        d2 += 1
                
    return min_diff


di = (1, 1)
dj = (-1, 1)

n = int(input())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = int(1e9)  # 출력값 (기본 : 1억)

# 최소 십자형이 만들어질수 있는 위쪽 꼭지점 좌표만 순회
for i in range(n - 2):
    for j in range(1, n - 1):
        # 좌표별 최소값을 구한다.
        result = min(result, area_five(i, j))
        
print(result)
