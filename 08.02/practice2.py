"""
N = 5
arr = [[0] * N for _ in range(N)]
num = 1
for r in range(N):
    for c in range(N):
        arr[r][c] = num
        num += 1    # 1 2 3 4 5
                    # 6 7 8 9 10
                    # 11 12 13 14 15
                    # 16 17 18 19 20
                    # 21 22 23 24 25
"""
"""        
for c in range(N):      # 열 우선
    for r in range(N):
        arr[r][c] = num
        num += 1
"""
'''
# 지그재그
for r in range(N):
    if r % 2 == 0:
        for c in range(N):
            arr[r][c] = num
            num += 1
    else:
        for c in range(N-1, -1, -1):
            arr[r][c] = num
            num += 1

for r in range(N):
    arr[r][r] = 1   # 1 0 0 0 0
                    # 0 1 0 0 0
                    # 0 0 1 0 0
                    # 0 0 0 1 0
                    # 0 0 0 0 1
    arr[r][N-1-r] = 2
for line in arr:
     print(*line)
'''
# 전치행렬
'''
for r in range(N):
    for c in range(r+1, N):     # 대각기준 행값 변경
        arr[r][c] = 1
        
for r in range(N):
    for c in range(r):    # 대각기준 열값 변경
        arr[r][c] = 1
'''
# 델타
'''
N = 10
arr = [[0] * N for _ in range(N)]
r, c = 5, 5     # 기준점

arr[r][c] = '*'
arr[r-1][c] = 1
arr[r][c-1] = 2
arr[r+1][c] = 3
arr[r][c+1] = 4

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
# 기준점을 기준으로 nr, nc 를 만들 때 항상 경계 체크를 해야함(음수로 넘어가는 것 방지)
# if 0 <= nr < N and 0 <= nc < N:
    arr[nr][nc] = i+1

arr[r+dr[0]][c+dc[0]] = 1
arr[r+dr[1]][c+dc[1]] = 2
arr[r+dr[2]][c+dc[2]] = 3
arr[r+dr[3]][c+dc[3]] = 4
'''
# ex) 문제
N = 10
arr = [[0] * N for _ in range(N)]
r, c = 5, 5
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for i in range(4):
    for j in range(1, N):
        nr = r + dr[i] * j
        nc = c + dc[i] * j
        if 0 <= nr < N and 0 <= nc < N:     # if nr < 0 or nr >= N or nc < 0 or nc >= N:
            break               # 첫 if 에서는 범위값이 넘어가도 변경하도록 하니 범위를 if 2 로 범위를 정해줌
        arr[nr][nc] = i + 1
for line in arr:
    print(*line)