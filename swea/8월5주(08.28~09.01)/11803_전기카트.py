import sys
sys.stdin = open('sample_input(1953).txt')

def perm(k):
    if k == N:          # k == N 일때 순열생성, 계산
        global used_e   # 글로벌 변수 used_e 를 만들고 초기화
        used_e = 0
        for e in range(N):
            used_e += arr[order[e]][order[e+1]]
        E.append(used_e)

    else:
        for i in range(1, N):
            if used[i]:
                continue
            used[i] = 1
            order[k] = i
            perm(k + 1)
            used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    E = []
    used = [0] * (N+1)
    order = [0] * (N+1)
    perm(1)

    print(f'#{tc} {min(E)}')
