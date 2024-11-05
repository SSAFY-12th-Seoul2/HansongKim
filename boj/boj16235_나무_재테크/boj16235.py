import sys


def spring():  # 봄, 여름, 가을 일부, 겨울의 모든 작업을 진행하는 함수 (이름만 spring)
    for p in range(n):
        for q in range(n):
            if not trees[p][q]:  # 해당 칸에 나무가 없으면
                grd[p][q] += food[p][q]  # 겨울 비료만 채우고 넘어감
                continue

            will_food = 0  # 죽은 나무로 생성되는 양분
            new_info = {}  # 가을 이후 새로운 나무 정보
            for age, val in sorted(trees[p][q].items()):  # 나이 적은 나무부터 탐색
                # 봄의 작업
                new_info[age + 1] = 0  # new_info에 내년 나이를 key로 생성
                # 나무가 먹을 양분이 있고, 해당 age의 나무가 남아있을 동안
                # 매 나무마다 그 칸의 양분을 age만큼 줄이고
                # 한 살 먹은 상태로 기록되며
                # 현재 나무량은 1 감소
                while grd[p][q] - age >= 0 and val > 0:  
                    grd[p][q] -= age
                    new_info[age + 1] += 1
                    val -= 1

                if new_info[age + 1] == 0:  # 성장한 나무가 없으면
                    new_info.pop(age + 1)  # key에서 삭제

                will_food += (age // 2) * val  # 죽은 나무들을 양분화

            grd[p][q] += (will_food + food[p][q])  # 현재 칸에 여름과 겨울 양분을 더함

            # 가을 작업
            for age, val in new_info.items(): # 봄에서 갱신된 나무 정보로 진행
                if age % 5 == 0:  # 나이가 5의 배수면
                    for w in range(8):
                        if 0 <= (np := p + di[w]) < n and 0 <= (nq := q + dj[w]) < n:
                            spread_tree[np][nq] += val  # 주변 8방향에 나이 1의 나무를 현재 칸 나무수 만큼 퍼뜨림

            trees[p][q] = new_info


di = (-1, -1, -1, 0, 0, 1, 1, 1)
dj = (-1, 0, 1, -1, 1, -1, 0, 1)

n, m, k = map(int, sys.stdin.readline().split())
food = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
grd = [[5 for _ in range(n)] for _ in range(n)]  # 땅의 양분
trees = [[{} for _ in range(n)] for _ in range(n)]  # 각 칸의 나무 정보 (key : 나이, value : 개수)
for _ in range(m):  # 초기 나무값
    x, y, z = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    trees[x][y][z] = 1

year = 0  # 지난 해 수
while year < k:
    spread_tree = [[0 for _ in range(n)] for _ in range(n)]  # 가을에 각 칸에 퍼뜨려지는 나무 수
    spring()  # spring 함수 진행

    for i in range(n):
        for j in range(n):
            if spread_tree[i][j]:
                trees[i][j][1] = spread_tree[i][j]

    year += 1  # 1년이 지남

total = 0  # k년 후 남은 나무 수
for i in range(n):
    for j in range(n):
        if trees[i][j]:  # 나무가 심어져 있으면
            total += sum(val for val in trees[i][j].values())  # 모두 더함(딕셔너리의 value가 나무 수)

print(total)
