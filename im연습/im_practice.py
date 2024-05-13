T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    cnt = 0
    cnt_h = 0
    A, B, C = 1, 2, 3

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'A':
                for k in range(4):
                    nr, nc = r + di[k], c + dj[k]
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'H':
                        cnt_h += 1
                        arr[nr][nc] = 'X'  # 중복 방문 방지를 위해 H를 X로 변경

            if arr[r][c] == 'B':
                for k in range(4):
                    for l in range(1, B + 1):
                        nr, nc = r + di[k] * l, c + dj[k] * l
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'H':
                            cnt_h += 1
                            arr[nr][nc] = 'X'

            if arr[r][c] == 'C':
                for k in range(4):
                    for l in range(1, C + 1):
                        nr, nc = r + di[k] * l, c + dj[k] * l
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'H':
                            cnt_h += 1
                            arr[nr][nc] = 'X'

    print(f'#{tc} {cnt - cnt_h}')

