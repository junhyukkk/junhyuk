def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((sti,stj))
    visited[sti][stj] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return visited[i][j]-2

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] +1

    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')

"""
def maze(si, sj):
    Q = []
    visited = [[0] * N for _ in range(N)]  # 큐 생성, 방문행렬 생성
    Q.append((si, sj))  # 출발점을 큐에 넣기
    visited[si][sj] = 1  # 출발점 방문표시(1로 시작)

    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]
    while Q:  # Q에 값이 있는 동안
        t = Q.pop(0)
        for d in range(4):  # 4방향 탐색  d = 0,1,2,3
            i = t[0] + di[d]
            j = t[1] + dj[d]
            if (0 <= i <= N - 1 and 0 <= j <= N - 1):
                if arr[i][j] == 0 and visited[i][j] == 0:
                    Q.append((i, j))
                    visited[i][j] = visited[t[0]][t[1]] + 1

                elif arr[i][j] == 3:
                    return 1
    return 0


for tc in range(1, 11):
    N = 100
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):  # 스타트 값 찾기
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j  # 2가 있는 start 값

    print(f'#{tc} {maze(si, sj)}')
"""