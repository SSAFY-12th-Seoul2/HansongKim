import sys


def lets_tetro(si, sj, visit, cnt):
    if cnt == 4:  # 4칸이 선택되면
        return paper[si][sj]  # 마지막칸에 값 반환
    max_as = 0  # 다음 재귀들 중 최대 합 변수
    visit[si][sj] = 1
    for ni, nj in ((si, sj + 1), (si + 1, sj), (si, sj - 1), (si - 1, sj)):
        if ni < 0 or ni >= n or nj < 0 or nj >= m:
            continue
        if visit[ni][nj]:
            continue
        if cnt == 3 and step[ni][nj]:  # 마지막 지점이 이미 시작점으로 사용했던 지점이면 통과
            continue
        max_as = max(lets_tetro(ni, nj, visit, cnt + 1), max_as)  # 최대 합 갱신
    visit[si][sj] = 0
    return paper[si][sj] + max_as  # 현재 칸과 max_as의 합 반환
        

def wu(si, sj):  # 'ㅗ'자 모양일 경우를 판단하는 함수
    total = paper[si][sj]  # 시작위치의 값
    s = 0  # 나머지 3칸의 합 중 최대
    for k in wu_d:
        case_s = 0  # 'ㅗ' 방향별 합
        for di, dj in k:
            ni = si + di
            nj = sj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                break
            case_s += paper[ni][nj]
        s = max(s, case_s)                
    return total + s
    

wu_d = (((0, 1), (0, 2), (1, 1)),
        ((0, 1), (0, 2), (-1, 1)),
        ((1, 0), (2, 0), (1, 1)),
        ((1, 0), (2, 0), (1, -1)))


n, m = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]  # dfs의 visit 배열
step = [[0] * m for _ in range(n)]  # 시작점으로 사용한 지점을 기록하는 배열
max_tetro = 0  # 최대 합 (출력값)

for i in range(n):
    for j in range(m):
        step[i][j] = 1
        max_tetro = max(lets_tetro(i, j, visited, 1), max_tetro, wu(i, j))
        
print(max_tetro)