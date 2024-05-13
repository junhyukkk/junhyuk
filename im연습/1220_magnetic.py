import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ns = 0      # 교착상태의 값
    for j in range(N):
        red = 0     # 열이 바뀔때 마다 n극 = 0
        for i in range(N):      # 열 우선 순회하며
            if arr[i][j] == 1:  # n극 값인 1을 찾았을때
                red = 1         # n극 1 할당한 후
            elif arr[i][j] == 2 and red == 1:   # 열 우선 순회하며 n극을 가진 상태로 s극 2를 만나면
                ns += 1         # 교착상태 +1
                red = 0         # n극 초기화, 안할 시 열 순회하며 2만날때마다 ns += 1됨
    # s극을 따로 할 필요 없음. 배열 전체를 순회하며 n극과 교착상태일 s극을 다 찾았기 때문에
    print(f'#{tc} {ns}')
'''
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    table = [[0] for _ in range(N)]
    for j in range(N):
        S = [0] * 100
        top = -1
        for i in range(N):
            if arr[i][j] == 1:
                top += 1
                S[top] = 1
            elif arr[i][j] == 2:
                top += 1
                S[top] = 1
'''
