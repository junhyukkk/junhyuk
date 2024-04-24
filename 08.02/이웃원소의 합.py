T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    max_sum = 0
    max_i = 0
    max_j = 0
    for i in range(N):
        for j in range(N):
            s = 0
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]

            if max_sum < s:
                max_sum = s
                max_i, max_j = i, j
    print(f'#{tc} {max_i} {max_j} {max_sum}')