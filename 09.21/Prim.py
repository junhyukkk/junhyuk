'''
정점(V) 7, 간선(E) 11
출발점과 도착점
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# 프림 알고리즘 구현
import heapq
# 자동으로 오름차순 정렬 push

def prim(start):
    heap = []
    # MST 에 포함되었는지 여부
    MST = [0] * V
    # heapq. heappush((heap, (w, start)) = 가중치와 정점 정보
    heapq.heappush(heap, (0, start))
    # 누적합 저장
    sum_weight = 0
    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)
        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue
        # 방문체크
        MST[v] = 1

        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈수없다면 pass and 이미 방문햇다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight
# 여기부터는 기본
V, E = map(int, input().split())
# 인접행렬
graph = [[0] * (V) for _ in range(V)] # 2차원 배열 만들기

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
# 그래프 방향 중요! 무뱡향인지 단방향인지 제대로 확인, 위 코드는 단방향
    graph[t][f] = w
# 반대 방향까지 넣어야 무방향 됨.
prim(0)
result = prim(0)
print(f'최소비용 = {result}')