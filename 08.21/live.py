V, E = map(int, input().split())
arr = list(map(int, input().split()))
# len(arr) == E * 2

# 0 은 없다는 것을 표현
L = [0] * (V+1)
R = [0] * (V+1)
P = [0] * (V+1)
for i in range(0, len(arr), 2):
    p, c = arr[i], arr[i+1]         # p = 부모, c = 자식
# 왼쪽 자식을 확인
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    # c의 부모는 P[c]에 저장
    P[c] = p
# ===========================

def dfs(v):     # v는 현재노드
    if v == 0:      # 공백노드, 더 이상 갈 필요가 없어짐
        return
# 여기 들어가면 처음 진입 = 전위
    dfs(L[v])
    print(v, end=' ')     # 방문한 시점이 왼쪽을 방문하고 온다면 중위호출이 됨
    dfs(R[v])
# 여기 들어가면 오른쪽 귀환 = 후위
# 어느 시점에 호출하냐에 따라 전위중위후위가 나뉘어진다 생각하면 됨

def tree_size(v):
    l = tree_size(L[v])
    r = tree_size(R[v])
    return l + r + 1