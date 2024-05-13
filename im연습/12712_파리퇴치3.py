T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    xi = [1, -1, -1, 1]
    xj = [1, 1, -1, -1]
    max_s = 0
    max_x = 0

    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni, nj = i+di[k]*l, j+dj[k]*l
                    if 0<=ni<N and 0<=nj<N:
                        s += arr[ni][nj]

            if max_s < s:
                max_s = s

    for i in range(N):
        for j in range(N):
            x = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    mi, mj = i + xi[k] * l, j + xj[k] * l
                    if 0 <= mi < N and 0 <= mj < N:
                        x += arr[mi][mj]

            if max_x < x:
                max_x = x

    max_sum = max(max_s, max_x)

    print(f'#{tc} {max_sum}')