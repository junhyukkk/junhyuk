T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_sum = 0     # 0으로 초기화 하는 이유 : 0보다 작을수는 없기때문(조건별로 생각해서 적기)
    for i in range(N):
        for j in range(M):
            s = arr[i][j]       # 터트린 풍선의 꽃가루 수
            for k in range(4):      #i,j 인접에 대해
                # for k in range(0, 3)
                # for # k방향으로 확인하는 개수 일때 위 아래 순서는 바뀌어도 됨
                # ex) for p in range(1, arr[i][j]+1):
                # 아래 코드에 [k] 뒤에 *p
                ni, nj = i+di[k], j+dj[k]   # k 방향으로 더해준 값
                if 0 <= ni < N and 0 <= nj < M:     # 벗어나면 안된다, 벗어나지 않는 조건
                    s += arr[ni][nj]
            if max_sum < s:     # i, j 인접 풍선까지 더한 개수의 비교
                max_sum = s
    print(f'#{tc} {max_sum}')