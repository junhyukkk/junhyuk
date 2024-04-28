V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] =1
    adj_m[v2][v1] =1         # 방향이 없는 경우

def bfs(s,V):   # 시작정점 s, 마지막정점 V
    visited = [0] * (V+1)    # visited 생성
    queue = []    # 큐 생성
    queue.append(s)    # 시작점 인큐
    visited[s] = 1    # 시작점 방문표시
    while queue:        # 큐에 정점이 남아있으면 front != rear
        t = queue.pop(0)    # 디큐
        for w in (1, V+1):
            if adj_m[t][w] == 1 and visited[w] == 0:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
                queue.append(w)
                visited[w] = visited[t] + 1

