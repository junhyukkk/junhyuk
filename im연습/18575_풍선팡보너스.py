T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_sum = 0
    min_sum = 1000

    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for k in range(4):
                for l in range(1, N):
                    ni, nj = i + di[k] * l, j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_sum < s:
                max_sum = s
            if min_sum > s:
                min_sum = s
    print(f'#{tc} {max_sum - min_sum}')