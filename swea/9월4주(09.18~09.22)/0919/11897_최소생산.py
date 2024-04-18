import sys
sys.stdin = open('sample_input (11897).txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 1000000

    def dfs(i,ans):
        global visited, min_sum
        if i == N:
            min_sum = min(min_sum, ans)
        if ans >= min_sum:
            return
        for j in range(N):
            if visited[j]:
                continue
            visited[j] = 1
            dfs(i+1, ans+arr[i][j])
            visited[j] = 0

    dfs(0,0)
    print(f'#{tc} {min_sum}')

"""
def dfs(i, ans):
    global visited
    if i == N:
        global min_sum
        min_sum = min(min_sum, ans)

    if ans >= min_sum:
        return

    for j in range(N):
        if visited[j]:
            continue
        visited[j] = 1
        dfs(i+1, ans+arr[i][j])
        visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 100000
    visited = [0] * N
    dfs(0, 0)
    print(f'#{tc} {min_sum}')
"""