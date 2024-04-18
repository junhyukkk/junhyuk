"""
T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # 노드수, 간선수
    arr = list(map(int, input().split()))
    # 노드번호 1 ~ (E + 1)
    L = [0] * (E + 2)  # 왼쪽자식
    R = [0] * (E + 2)  # 오른쪽 자식

    for i in range(0, len(arr), 2):
        p, c = arr[i], arr[i + 1]  # p=부모, c=자식
        # 왼쪽 자식을 확인
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        # c의 부모는 P[c]에 저장

    cnt = 0


    def dfs(v):  # v: 현재 노드
        global cnt
        if v == 0:
            return
        cnt += 1
        dfs(L[v])
        dfs(R[v])


    dfs(N)

    print(f'#{tc} {cnt}')
"""

