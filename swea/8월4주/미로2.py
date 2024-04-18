def bfs(sti, stj, N):
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q = []  # 큐 생성
    q.append((sti, stj))  # 시작점 인큐
    visited[sti][stj] = 1  # 시작점 인큐 표시
    while q:  # 큐가 비워질 때까지
        i, j = q.pop(0)  # deQ
        if maze[i][j] == 3:  # 처리
            return visited[i][j] - 2  # 지나온 칸 수 리턴

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

"""
# 1. 시작지점의 인덱스 찾기
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 출발지점
                return i, j
 
# 2. BFS로 답 찾기
def bfs(st_i, st_j, N):
    visited = [[0] * N for _ in range(N)]  # visited 생성
    Q = []                                 # 큐 생성
    Q.append((st_i, st_j))                 # 시작점 인큐
    visited[st_i][st_j] = 1                # 시작점 인큐 표시
 
    # 큐가 빌 때 까지 반복!
    while Q:
        i, j = Q.pop(0)  # deQ
        # 도착지점(3)이 되면, 종료
        if maze[i][j] == 3:
            return visited[i][j] - 2  # 순수하게 이동한 거리만 계산
        # 인접 및 인큐 안한 곳, 인큐 및 표시
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # check 할것! : 미로 내부에 있는 값인지 / 갈 수 있는 길인지 / 방문 안한 곳인지
            if ( 0 <= ni < N and 0 <= nj < N ) \
                    and maze[ni][nj] != 1 \
                    and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    # 목표에 도달할 수 없는 경우
    return 0
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 1. 시작 지점의 인덱스 찾기
    st_i, st_j = find_start(N)
    # 2. BFS로 답 찾기
    ans = bfs(st_i, st_j, N)
    # 3. 답 출력
    print(f'#{tc} {ans}')
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')
