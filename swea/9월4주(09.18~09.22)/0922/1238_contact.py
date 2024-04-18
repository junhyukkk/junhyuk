def bfs(s):
    q = [s]
    visited = [0] * 101
    # 시작점 방문 처리
    visited[s] = 1
    # 최대 숫자와 최대 깊이를 저장할 변수
    max_num = s
    max_depth = 1
    while q:
        now = q.pop(0)
        # 갈 수 있는 지점 전부 봄
        for to in graph[now]:
            if visited[to]:
                continue
            # 기존 방문보다 한 번 더 갔다면,
            visited[to] = visited[now] + 1
            # 한 단계 깊은 곳으로 가거나,
            # 깊이는 같은데 숫자가 더 크다면, max 값 초기화
            if max_depth < visited[to] or (max_depth == visited[to] and max_num < to):
                max_depth = visited[to]
                max_num = to
            q.append(to)

    return max_num

for tc in range(1, 11):
    N, S = map(int, input().split())
    # 전체 입력 받기
    input_graph = list(map(int,input().split()))
    # 실제 사용할 인접 리스트
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        f = input_graph[i]
        t = input_graph[i+1]
        graph[f].append(t)
    r = bfs(S)
    print(f'#{tc} {r}')
