import sys
sys.stdin = open('sample_input(11902).txt')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int,input().split())
        # 유향
        graph[u].append((v, w))

    # 초기값 설정 중요, 무엇으로 놓을 것인지(큰값)
    # distance[v] => 출발점에 v정점까지의 최단 거리
    distance = [0xffffff] * (N+1)
    distance[0] = 0     # 0번 지점 시작 => 거리 0 이기 때문에
    Q = [0]     # deque로 가능, 해볼 것
    while Q:
        u = Q.pop(0)
        for v, w in graph[u]:   # 튜플이니 u와 w 둘다 받아야함
        # (u,v) 간선완화 : u에서 v로 가는 경로를 그전에 계산된 것 보다 작은것인가 확인하는것
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                Q.append(v)
    print(f'#{tc} {distance[N]}')


# T = int(input())
# for tc in range(1, T+1):
#     N, E = map(int, input().split())
#     graph = [[] for _ in range(N+1)]
#     for _ in range(E):
#         u, v, w = map(int,input().split())
#         # 유향
#         graph[u].append((v, w))
#
#     # 초기값 설정 중요, 무엇으로 놓을 것인지(큰값)
#     # distance[v] => 출발점에 v정점까지의 최단 거리
#     distance = [0xffffff] * (N+1)
#     distance[0] = 0     # 0번 지점 시작 => 거리 0 이기 때문에
#
#     Q = [0]     # deque로 가능, 해볼 것
#     def dfs(u):
#         for v, w in graph[u]:   # 튜플이니 u와 w 둘다 받아야함
#         # (u,v) 간선완화 : u에서 v로 가는 경로를 그전에 계산된 것 보다 작은것인가 확인하는것
#             if distance[v] > distance[u] + w:
#                 distance[v] = distance[u] + w
#                 dfs(v)
#     dfs(0)
#     print(f'#{tc} {distance[N]}')

# 다익스트라로 풀기
# from heapq import heappop, heappush
#
# T = int(input())
# for tc in range(1, T + 1):
#
#     N, E = map(int, input().split())
#     G = [[] for _ in range(N + 1)]
#     for _ in range(E):
#         u, v, weight = map(int, input().split())
#         # 유향
#         G[u].append((v, weight))
#
#     # 초기값 설정 중요!!!!!!!
#     # D[v] => 출발점에 v 정점까지 최단 거리
#     D = [0xfffff] * (N + 1)
#     D[0] = 0
#     Q = []
#     # 큐에 삽입 할 때 (D[v], v)
#     heappush(Q, (0, 0))
#
#     while Q:
#         dist, u = heappop(Q)
#         # 정점 u는 최단경로가 확정된다.
#         if dist > D[u]: continue
#
#         for v, weight in G[u]:
#             if D[v] > D[u] + weight:
#                 D[v] = D[u] + weight
#                 heappush(Q, (D[v], v))
#
#     print(f'#{tc} {D[N]}')