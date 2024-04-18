T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    s += arr[k][l]
            if max_sum < s:
                max_sum = s
    print(f'#{tc} {max_sum}')







