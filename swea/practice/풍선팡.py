T = int(input())
di = [0, 1, 0, -1]          # 하우상좌 의 4방향 설정
dj = [1, 0, -1, 0]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0             # max_sum으로 최댓값의 기본값 설정
    for i in range(N):
        for j in range(M):  # i와j가 NxM을 순회하며
            s = arr[i][j]       # 기준점을 제외하고 구한다면 arr[i][j]를 0으로
            for k in range(4):  # 4방향을 순회하기위한 for문
                for l in range(1, arr[i][j]+1):     # 각 방향에서 꽃가루 개수만큼 추가로 더해지도록 하는 l
                    ni, nj = i + di[k]*l, j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < M:   # 범위 벗어나지 않도록 설정
                        s += arr[ni][nj]
            if max_sum < s:     # 이전의 최댓값이 더해진 S보다 작다면 더해진 S가 최댓값
                max_sum = s
    print(f'#{tc} {max_sum}')
