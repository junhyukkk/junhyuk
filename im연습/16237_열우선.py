T = int(input())
for tc in range(1, T+1):
    r, c, w = map(int, input(). split())
    N = 10
    arr = [[0] * N for _ in range(N)]
    s = 0
    for i in range(r, r+w):
        for j in range(c, c+w):
            s += 1
            arr[i][j] = s

    print(f'#{tc}')
    for i in arr:
        print(' '.join(map(str, i)))