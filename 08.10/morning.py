# fibo1
'''
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))

def fibo(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range (2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fibo(100))
'''
# DFS 깊이우선탐색

def dfs(n, V, adj_m):
    stack = []
    visited = [0] * (V+1)
    visited[n] = 1
    print(n)
    while True:     # 현재 정점 n 에 인접하고 미방문한 w 찾기
        for w in range(1, V+1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)     # push(n), v = w
                n = w
                print(n)
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
        return

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''