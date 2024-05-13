import sys
sys.stdin = open('input (2).txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        stack = []  # 스택을 빈 리스트로 초기화
        top = -1  # top 변수 초기화
        i = 0
        while i < N:
            if arr[i][j] == 1:
                top += 1
                stack.append(1)  # 1을 스택에 추가
            elif arr[i][j] == 2:
                if top >= 0 and stack[top] == 1:
                    cnt += 1
                    stack.pop()  # 1을 스택에서 제거
                else:
                    stack.append(2)  # 2를 스택에 추가
            i += 1
    print(f'#{tc} {cnt}')
