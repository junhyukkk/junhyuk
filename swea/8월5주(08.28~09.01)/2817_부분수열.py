import sys
sys.stdin = open('sample_input(2817).txt')


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    list_a = list(map(int, input().split()))

    n = len(list_a)
    count = 0

    for i in range(1, 1 << n):      # 부분집합 1 << n 2^n-1 만큼 구하기
        s = 0
        for j in range(n):
            if i & (1 << j):
                s += list_a[j]

        if s == K:
            count += 1

    print(f"#{t} {count}")

"""
def f(k, a, visited):
    global cnt
    if k > K:
        return
 
    if k == K:
        cnt += 1
        return
 
    for i in range(a, N):
        if not visited[i]:
            visited[i] = 1
            f(k+arr[i], i+1, visited)
            visited[i] = 0
 
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * N
    cnt = 0
    f(0, 0, visited)
 
    print(f'#{tc} {cnt}')

"""
