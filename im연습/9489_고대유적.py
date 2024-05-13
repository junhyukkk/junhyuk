T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_data = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0  # 0을 만나면 연속된 1의 개수를 리셋
            if max_data < cnt:
                max_data = cnt

    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0
            if max_data < cnt:
                max_data = cnt

    print(f'#{tc} {max_data}')
