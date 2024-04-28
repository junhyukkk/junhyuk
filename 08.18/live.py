# 너비우선탐색

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)        # 방향이 없는 경우


def bfs(s,V):   # 시작정점 s, 마지막정점 V
    visited = [0] * (V+1)    # visited 생성
    queue = []    # 큐 생성
    queue.append(s)    # 시작점 인큐
    visited[s] = 1    # 시작점 방문표시
    while queue:        # 큐에 정점이 남아있으면 front != rear
        t = queue.pop(0)    # 디큐
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:     # w를 인큐하고 인큐되었음을 표시.
                queue.append(w)
                visited[w] = visited[t] + 1

