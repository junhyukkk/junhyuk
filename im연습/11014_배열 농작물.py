T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_t = 99999
    for i in range(1, N):
        for j in range(1, N):

            arr1 = 0
            for k in range(0, i):
                for m in range(0, j):
                    arr1 += arr[k][m]

            arr2 = 0
            for n in range(i, N):
                for b in range(0, j):
                    arr2 += arr[n][b]

            arr3 = 0
            for l in range(0, N):
                for a in range(j, N):
                    arr3 += arr[l][a]
            total = [arr1, arr2, arr3]

            max_v = max(total)
            min_v = min(total)
            t = max_v - min_v

            if t < min_t:
                min_t = t

    print(f'#{tc} {min_t}')