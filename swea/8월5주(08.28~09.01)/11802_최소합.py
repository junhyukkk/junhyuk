import sys
sys.stdin = open('sample_input (11082).txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = [[0] * N for _ in range(N)]

    # 시작 지점 (0, 0) 초기화
    min_sum[0][0] = arr[0][0]

    # 위에서 아래로, 왼쪽에서 오른쪽으로 최소 합계 계산
    for i in range(N):
        for j in range(N):
            if i + 1 < N:  # 아래로 이동 가능
                if arr[i + 1][j] <= arr[i][j]:
                    min_sum[i + 1][j] += 1

                else:
                    min_sum[i + 1][j] = min_sum[i + 1][j] - min_sum[i][j] + 1

            if j + 1 < N:  # 오른쪽으로 이동 가능
                if arr[i][j + 1] <= arr[i][j]:
                    min_sum[i][j + 1] += 1
                else:
                    min_sum[i][j + 1] = min_sum[i][j + 1] - min_sum[i][j] + 1

    print(f"#{tc} {min_sum[N - 1][N - 1]}")
