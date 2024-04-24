di = [0,1,0,-1]
dj = [1,0,-1,0]
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

max_v = 0       # 모든 원소가 0이상이라면
for i in range(N):      # 모든 원소 arr[i][j]에 대해
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for k in range(4):
            ni, nj = i+di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:     # 배열을 벗어나지 않으면
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s


'''
di 와 dj 가 line11 의 range 범위에 행열을 적어주는 것도 가능
실시간 강의 참고'''
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

total1 = 0
total2 = 0
for i in range(N):
    total1 += arr[i][j]
    total2 += arr[i][N-1+j]

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1, 0]
    dj = [1, 0, -1, 0, 0]
    sum_max = -1

    for i in range(N):
        for j in range(M):
            sum = 0
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < M:
                    sum += A[ni][nj]
            if sum_max < sum:
                sum_max = sum

    print(f'#{tc} {sum_max}')