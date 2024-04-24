# DFS 예시문제
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split()) # 정점과 간선의 수
# 각 정점마다 인접 정점에 대한 빈 리스트를 미리 만들기
G = [[] for _ in range(V+1)]
arr = list(map(int,input().split()))
for i in range(0, 2*E, 2):
    u, v = arr[i], arr[i+1]
    G[u].append(v)
# 무향인경우
# 1 -> [2, 3]
# 2 -> [1, 4, 5]
# 3 -> [1, 7]
# 4 -> [2, 6]
# 5 -> [2, 6]
# 6 -> [4, 5, 7]
# 7 -> [6, 3]
# 1 2 4 6 5 7 3
# 유향인경우
# 1 -> [2, 3]
# 2 -> [4, 5]
# 3 -> [7]
# 4 -> [6]
# 5 -> [6]
# 6 -> [7]
# 7 -> []
# 1 2 4 6 7 5 3
for i in range(1, V+1):
    print(i, '->', G[i])


#
S = []      # 스택
visited = [0] * (V+1)       # 정점번호는 1~V까지
# 1) 시작 정점 v를 결정하여 방문한다.
v = 1
visited[v] = 1; print(v, end=' ')# 방문
# while S: # 라고 한다면 S가 빈 리스트가 아니어야 함
while True:
    # 2) 정점 v에 인접한 정점 리스트 중에서 하나씩 가져오는 데 그것을 w라 하자
    for w in G[v]:
        # 1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push, 정점 w 를 방문
        if not visited[w]:
            S.append(v)
            visited[w] = 1; print(w, end=' ')
            # 그리고 w를 v로 하여 다시 2)를 반복한다.
            v = w
            # 중요한 부분, break가 걸리는 부분 break 가 없다면 인접 정점 전부를 방문함,
            break
    else:   # else 로 왔다는 것은 v의 인접 정점에 전부 방문했다는 것
        if S:
            v = S.pop()     # 스택의 꼭대기에있는 기준으로 pop 해서 다시 반복
        else:               # S 가 비어있지 않다면 break
            break

# 재귀호출
'''
def DFS_iter(v):
    pass

def DFS(v):     # v: 현재 방문할 정점 번호
    visited[v] = 1; print(v, end=' ')
    for w in G[v]:
        if not visited[w]:
            DFS(w)
            
visited = [0] * (V + 1)
DFS(1)
'''


