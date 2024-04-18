import sys
sys.stdin = open('sample_input (3).txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    s = 0
    t = [[0] * N for _ in range(N)]
    for test in range(M):
        bomb_r, bomb_c, width = map(int, input().split())
        r = bomb_r
        c = bomb_c
        s += arr[bomb_r][bomb_c]
        for i in range(4):
            for j in range(1, width+1):
                nr, nc = r+di[i]*j, c+dj[i]*j
                if 0 <= nr < N and 0 <= nc < N:
                    s += arr[nr][nc]
    print(f'#{tc} {s}')
# 폭발이 여러번 일어나는 경우가 다 더해져야함
# 폭발 범위가 겹치는 부분은 한번만 더 해져야함



'''
        for i in range(N):
            for j in range(N):
                s = arr[bomb_r][bomb_c]
                for k in range(4):      # 폭발 범위가 겹치는 부분은 한번만 넣어야함
                    for l in range(1, arr[i][j]+1):
                        ni, nj = i+di[k]*l, j+dj[k]*l
                        if 0 <= ni < N and 0 <= nj < N:
                s += arr[ni][nj]


    print(f'#{tc} {s}')
'''

