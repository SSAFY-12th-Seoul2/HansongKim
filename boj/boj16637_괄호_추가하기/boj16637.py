import sys


def calculate(a, b, op):  # 사칙연산 함수
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


n = int(sys.stdin.readline())
ex = list(sys.stdin.readline())

ex_n = n // 2  # 연산자의 수

result = -(2 ** 31)  # 계산 최댓값 (출력값)

# 비트 마스킹 (연산자 위치들의 부분집합)
for i in range(1 << ex_n):
    # 첫 연산자 부분을 괄호로 둘러싸는 것은 의미가 없다.
    # 괄호가 있던 없던 처음이다.
    if i & 1:
        continue

    # 한 부분의 연산자를 선택하면, 양 옆은 선택할 수 없다.
    # 그것을 판단하기 위한 check 배열
    check = [False] * ex_n
    lo = []  # 괄호 계산이 시작되는 숫자의 인덱스 번호 저장 배열
    for j in range(1, ex_n): 
        if i & (1 << j):
            if check[j]:  # 둘 수 없는 자리면 continue
                continue

            lo.append(2 * j)

            # 양 옆 막아놓기
            check[j - 1] = True
            if j + 1 < ex_n:
                check[j + 1] = True

    k = 0
    number = []  # 수를 담을 리스트
    ops = []  # 연산자를 담을 리스트
    while k < n:  # 괄호만 먼저 계산
        if k in lo:  # 괄호 안의 계산
            number.append(calculate(int(ex[k]), int(ex[k + 2]), ex[k + 1]))
            k += 3
        else:  # 그 외
            if ex[k].isdigit():
                number.append(int(ex[k]))
            else:
                ops.append(ex[k])
            k += 1

    # 나머지 계산 진행
    front = number[0]  
    k = 1
    for k in range(len(ops)):
        front = calculate(front, number[k + 1], ops[k])

    result = max(result, front)  # 최대 결과 갱신 및 확인

print(result)
