import sys


def apply(sp):  # 프로그램에 따라 행동
    global pointer, pro_p, brain_p, min_loop
    if sp == '-':
        # 포인트가 가리키는 수 1 감소
        memory[pointer] = (memory[pointer] - 1) % 256

    elif sp == '+':
        # 포인터가 가리키는 수 1 증가
        memory[pointer] = (memory[pointer] + 1) % 256

    elif sp == '<':
        # 포인터를 왼쪽으로 한 칸 이동
        pointer = (pointer - 1) % sm

    elif sp == '>':
        # 포인터를 오른쪽으로 한 칸 이동
        pointer = (pointer + 1) % sm

    elif sp == '[':
        # 만약 포인터가 가리키는 수가 0이면, 짝을 이루는 ']'로 점프
        if memory[pointer] == 0:
            brain_p = pack[brain_p]

    elif sp == ']':
        # 만약 포인터가 가리키는 수가 0이 아니면, 짝을 이루는 '['로 점프
        if memory[pointer] != 0:
            brain_p = pack[brain_p]
            # 그 때, 무한루프 상태라면(5천만 번 이상) 최소 '[' 지점을 기록
            if times >= 50000000:
                min_loop = min(brain_p, min_loop)

    elif sp == ',':
        # 문자를 다 읽었으면 255 기록
        # 그렇지 않으면 해당 문자를 아스키코드로 변환하여 기록
        if pro_p == si:
            memory[pointer] = 255
        else:
            memory[pointer] = ord(program[pro_p])
            pro_p += 1

    # 프로그램의 다음 코드로 넘어간다.
    brain_p += 1


def check_loop():
    # '[', ']' 쌍의 위치를 기록
    # 양방향 모두 기록
    stack = []
    in_pack = {}
    for p in range(sc):
        if brainfuck[p] == '[':
            stack.append(p)
        elif brainfuck[p] == ']':
            q = stack.pop()
            in_pack[q] = p
            in_pack[p] = q
    return in_pack


T = int(input())
for _ in range(T):
    sm, sc, si = map(int, sys.stdin.readline().split())
    brainfuck = sys.stdin.readline().strip()
    program = sys.stdin.readline().strip()

    memory = [0] * sm     # 배열
    pointer = 0           # 배열의 포인터
    pro_p = 0             # 입력의 포인터
    min_loop = 5000       # 무한 루프 '[' 위치 초기값
    pack = check_loop()   # loop 위치 딕셔너리

    brain_p = 0           # 프로그램 코드의 포인터
    times = 0             # 수행 횟수
    result = 'Terminates' # 결과
    while brain_p < sc:
        times += 1                 # 수행 횟수 증가
        apply(brainfuck[brain_p])  # 명령 수행 및 프로그램 포인터 변화

        if times >= 100000000:     # 무한 루프 후, 그 루프가 한 번 실행 완료되었을 때
            result = f'Loops {min_loop} {pack[min_loop]}'  # 무한 루프 결과 출력
            break

    print(result)
