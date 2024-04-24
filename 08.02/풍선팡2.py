T = int(input())
for tc in range(1,T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]      # i,j 기준 상하좌우의 위치 설정
    dj = [1, 0, -1, 0]

    max_sum = 0                 # 합한 꽃가루의 값 0 초기화
    for i in range(N):          # i를 N 줄에 걸쳐 순회할 때
        for j in range(M):      # j를 M 줄에 걸쳐 순회하고
            s = arr[i][j]       # i,j 의 인덱스를 s 로 설정
            for k in range(4):  # 4방향의 k값을 더해주기 위해 k를 4번 순회
                ni, nj = i+di[k], j+dj[k]   # i,j 값에 k 방향으로 간 인덱스를 ni, nj에 할당
                if 0 <= ni < N and 0 <= nj < M:  # 방향 값이 범위를 넘지 않기 위해 범위 설정
                    s += arr[ni][nj]        # 4방향 ni,nj 값 합하고
            if max_sum < s:             # 4방향 순회 후의
                max_sum = s             # s값과 max_sum 비교 최대값도출


    print(f'#{tc} {max_sum}')



