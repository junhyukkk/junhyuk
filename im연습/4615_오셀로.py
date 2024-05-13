N = 7
arr = [[0] * N for _ in range(N)]
# ===============================
dr = [-1, 0, 1, 0] # 상우하좌
dc = [0, 1, 0, -1]
r = c = 2
arr[r][c] = '*'

for i in range(4):
    nr = r
    nc = c
    while 0 <= nr + dr[i] < N and 0 <= nc + dc[i] < N:
        nr = nr + dr[i]
        nc = nc + dc[i]
        arr[nr][nc] = 1
# ===============================
for line in arr:
    print(*line)