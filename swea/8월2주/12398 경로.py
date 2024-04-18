T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for i in range(E):                      # E개의 줄 이후 결로의 존재 확인할
        u, v = map(int,input().split())     # 출발노드, 간선정보
        arr[u].append(v)
# 양방향인경우
#       arr[v].append(u)
    S, G = map(int, input().split())        # 주어진 출발 노드와 간선정보
    Stack = []  # 스택의 빈 리스트
    visited = [0] * (V + 1)  # 정점번호는 1~V까지
    # 1) 시작 정점 v를 결정하여 방문한다. 문제에서 주어진 출발 노드 S
    v = S
    visited[v] = 1
    # while S: # 라고 한다면 S가 빈 리스트가 아니어야 함
    while True:
        # 2) 정점 v에 인접한 정점 리스트 중에서 하나씩 가져오는 데 그것을 w라 하자
        for w in arr[v]:
            # 1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push, 정점 w 를 방문
            if not visited[w]:
                Stack.append(v)
                visited[w] = 1
                # 그리고 w를 v로 하여 다시 2)를 반복한다.
                v = w
                # 중요한 부분, break가 걸리는 부분 break 가 없다면 인접 정점 전부를 방문함,
                break
        else:               # else 로 왔다는 것은 v의 인접 정점에 전부 방문했다는 것
            if Stack:
                v = Stack.pop()  # 스택의 꼭대기에있는 기준으로 pop 해서 다시 반복
            else:                # S 가 비어있지 않다면 break
                break
    print(f'#{tc} {visited[G]}')

