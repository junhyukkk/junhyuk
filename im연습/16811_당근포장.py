import sys
sys.stdin = open('sample_16811.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    min_v = 1000
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if arr[i] != arr[i + 1] and arr[j] != arr[j + 1]:
                small = i + 1
                mid = j - i
                large = N - 1 - j
                if small <= N // 2 and mid <= N // 2 and large <= N // 2:
                    if min_v > (max(small, mid, large) - min(small, mid, large)):
                        min_v = max(small, mid, large) - min(small, mid, large)
    if min_v == 1000:
        min_v = -1
    print(f'#{tc} {min_v}')

