T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for test in range(N):
        r_s, c_s, r_e, c_e, color = map(int, input().split())

        for i in range(r_s, r_e+1):
            for j in range(c_s, c_e+1):
                arr[i][j] += 1
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2:
                cnt += 1
    print(f'#{tc} {cnt}')

