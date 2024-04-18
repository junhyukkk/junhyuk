def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)]     # visited 생성
    q = []                      # 큐 생성
    q.append((sti,stj))         # 시작점 인큐
    visited[sti][stj] = 1       # 시작점 인큐 표시
    while q:                    # 큐가 비워질 때까지
        i, j = q.pop()          # 디큐
        if maze[i][j] == 3:     # 처리
            return visited[i][j]-2     # 지나온 칸 수 리턴
        # 인접하고 인큐된 적이 없다면
        # 인큐, 인큐 표시
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] +1

    return 0    # 3인칸에 도달할 수 없는 경우

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)        # start_i, start_j
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')

'''
def bfs(s, V, g):
    visited = [0] * (V + 1)
    Q = []
    Q.append(s)
    visited[s] = 1
    flag = 1
    result = 0
    while Q and flag:
        t = Q.pop(0)  # 맨 앞
        for w in lines[t]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[t] + 1
                if w == g:
                    result = visited[g] - 1
                    flag = 0
                Q.append(w)
                visited[w] = visited[t] + 1
    return result


T = int(input())
for tc in range(1, T + 1):

    V, E = map(int, input().split())  # V: 노드 수 , E : 간선 정보

    lines = [[] for _ in range(V + 1)]

    for i in range(E):
        v1, v2 = map(int, input().split())
        lines[v1].append(v2)
        lines[v2].append(v1)

    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S, V, G)}')
'''