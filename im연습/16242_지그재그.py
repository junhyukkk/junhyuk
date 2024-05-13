T = int(input())
for tc in range(1, T+1):
    r, c, w, h = map(int, input().split())
    arr = [[0] * 10 for _ in range(10)]

    num = 0
    for i in range(r, r+h):
        if (i-r) % 2 == 0:      # 짝수행인경우
            for j in range(c, c + w):
                num += 1
                arr[i][j] = num
        else:                   # 홀수행인 경우 역으로 더하기
            for j in range(c+w-1, c-1, -1):
                num += 1
                arr[i][j] = num

    print(f'#{tc}')
    for i in arr:
        print(' '.join(map(str, i)))