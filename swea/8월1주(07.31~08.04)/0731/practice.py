T = int(input())
N = int(input())
for tc in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [0,1,0,-1]
    dj = [-1,0,1,0]
    max_sum = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for k in range(N-1):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]


    print(f'#{tc} {max_sum}')
