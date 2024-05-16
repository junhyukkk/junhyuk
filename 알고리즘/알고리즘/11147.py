"""
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    list = []

    for i in range(1, M // N + 1):
        list.append(N * i)

    print(f'#{tc} *{list}')
"""

T = int(input())
for tc in range(1,T+1):
    N, M, A = map(int,input().split())

    if A == '+':
        result = N + M
    if A == '-':
        result = N - M
    if A == '*':
        result = N * M
    if A == '/':
        result = N / M
    else:

    print(f'#{tc} {result}')
