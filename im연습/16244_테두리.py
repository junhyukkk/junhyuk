T = int(input())
for tc in range(1, T + 1):
    r, c, N = map(int, input().split())

    arr = [[0] * 10 for _ in range(10)]

    for i in range(r, r + N):
        for j in range(c, c + N):
            if i == r or i == r + N - 1 or j == c or j == c + N - 1:
                arr[i][j] = 1

    print(f'#{tc}')
    for area in arr:
        print(' '.join(map(str, area)))