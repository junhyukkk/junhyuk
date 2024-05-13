T = int(input())
for tc in range(1, T+1):
    r, c, N = map(int, input().split())
    arr = [[0]*10 for _ in range(10)]

    for i in range(N):
        arr[r + i][c + i] = arr[r + i][c + i] + 1
        arr[r + i][c + N - 1 - i] = 1

    print(f'#{tc}')
    for i in arr:
        print(' '.join(map(str, i)))
