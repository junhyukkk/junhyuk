import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for l in range(L-1, R):
            arr[l] = i

    print(f'#{tc}', *arr)
