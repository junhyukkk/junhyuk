def find_min(s, e):
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        lmin = find_min(s, mid)
        rmin = find_min(mid+1, e)
        if arr[lmin] - arr[rmin] == 0 or arr[lmin] - arr[rmin] == -2 or arr[lmin] - arr[rmin] == 1:
            return lmin
        else:
            return rmin
"""
        if arr[lmin] - arr[rmin] == 0:
            return lmin
        if arr[lmin] - arr[rmin] == -2:
            return lmin
        if arr[lmin] - arr[rmin] == 1:
            return lmin
        else:
            return rmin
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {find_min(0, N-1)}+1')