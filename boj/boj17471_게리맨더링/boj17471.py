import sys


def get_diff(lst):  # 최소차를 구하는 함수
    visited = [False] * (n + 1)  # 선거구가 포함한 지역을 나타낼 리스트
    for w in lst:  # A 선거구 내의 지역이면
        visited[w] = True  # 포함상태
    area = set([w for w in range(1, n + 1)])  # 전체 지역구 숫자 set
    other = list(area.difference(set(lst)))  # B 선거구 구하기

    def connect(v):  # 연결 상태를 보는 함수
        visited[v] = False  # 확인한 지역은 False
        for k in con[v]:  # v 지역과 연결되어 있는 곳 중
            if visited[k]:  # 선거구 안의 지역이면
                connect(k)  # 방문하고 확인
        return any(visited)  # 선거구 내 지역이 모두 연결되어 있으면 False
    ja = connect(lst[0])  # A 선거구 연결 상태 확인
    visited = [False] * (n + 1)  # B 선거구 포함 지역 리스트
    for w in other:  # B 선거구 내의 지역이면
        visited[w] = True  # 포함상태
    jb = connect(other[0])  # B 선거구 연결 상태 확인

    diff = 1e9  # 차이 초기값
    if not ja and not jb:  # 두 선거구 모두 연결되어 있으면
        one_p = sum(people[p - 1] for p in lst)  # A 선거구 인구
        oth_p = sum(people[q - 1] for q in other)  # B 선거구 인구
        diff = abs(one_p - oth_p)  # 차이값
    return diff


n = int(sys.stdin.readline())  # 지역 수
people = list(map(int, sys.stdin.readline().split()))  # 지역별 인구
con = {}  # 연결 상태를 담는 리스트
for i in range(1, n + 1):
    con[i] = list(map(int, sys.stdin.readline().split()))[1:]
    # 입력의 0번 인덱스 값은 개수이므로 제외하고 받음

min_diff = 21e9  # 두 선거구 인구 최소차(출력 값)
for i in range(1, (1 << n) - 1):  # 비트마스킹 이용 부분집합 구하기
    arr = []  # 부분집합 리스트(A 선거구)
    for j in range(n):
        if i & (1 << j):
            arr.append(j + 1)  # 부분집합(A 선거구)에 추가
    min_diff = min(min_diff, get_diff(arr))  # 최소차 확인 및 갱신
if min_diff == 1e9:  # 두 지역구로 나눌 수 없다면
    min_diff = -1  # 출력값은 -1

print(min_diff)