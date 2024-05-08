import sys
sys.stdin = open('input.txt')

def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N

def find_deadlocks(N, arr):
    deadlocks = 0

    for j in range(N):
        is_blue_in_column = False  # 푸른 자성체가 현재 열에 있는지 여부
        for i in range(N):
            if arr[i][j] == 1:  # 현재 위치에 푸른 자성체가 있는 경우
                if is_blue_in_column:  # 이미 이 열에 푸른 자성체가 있으면 교착 상태
                    deadlocks += 1
                else:
                    is_blue_in_column = True
            elif arr[i][j] == 2:  # 현재 위치에 빨간 자성체가 있는 경우
                is_blue_in_column = False  # 푸른 자성체가 아래로 이동하면 빨간 자성체는 영향을 받지 않음

    return deadlocks

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    deadlocks = find_deadlocks(N, arr)
    print(f"#{tc} {deadlocks}")
