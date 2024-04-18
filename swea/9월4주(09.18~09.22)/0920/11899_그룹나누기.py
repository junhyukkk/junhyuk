T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # 정점수, 간선수
    arr = list(map(int, input().split()))
    # disjoint_set
    p = [i for i in range(N + 1)]
    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]

    ans = N # 최초집합의 개수
    for i in range(0, M*2, 2):
        u, v = arr[i], arr[i + 1]

        a = find_set(u)
        b = find_set(v)
        if a == b: continue
        p[b] = a
        ans -= 1
    print(f'#{tc} {ans}')