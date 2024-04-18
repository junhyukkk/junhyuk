import sys
sys.stdin = open('sample_input (11891).txt')

# def merge_sort(lst):
#     global cnt
#     if len(lst) <= 1:
#         return lst
#     mid = len(lst) // 2
#     l = merge_sort(lst[:mid])
#     r = merge_sort(lst[mid:])
#     # l, r은 정렬된 리스트
#     if l[-1] > r[-1]:
#         cnt += 1
#     ret = []
#     while l and r:
#         if l[0] <= r[0]:
#             ret.append(l.pop(0))
#         else:
#             ret.append(r.pop(0))
#     if l: ret.extend(l)
#     if r: ret.extend(r)
#
#     return ret  # 병합
# arr = [7, 5, 4, 1, 2, 10, 3, 6, 9, 8]
# cnt = 0
# print(cnt)
# print(arr)
# print(merge_sort(arr))

def merge_sort(lo, hi): # 구간 정보 (시작, 끝)
    global cnt
    if lo == hi:
        return
    mid = (lo + hi) // 2
    merge_sort(lo, mid)
    merge_sort(mid+1, hi)
    if arr[mid-1] > arr[hi]:
        cnt += 1
    # 병합
    i, j, k = lo, mid + 1, lo

    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; i += 1; k += 1
        else:
            tmp[k] = arr[j]; j += 1; k += 1
    while i <= mid:
        tmp[k] = arr[i]; i += 1; k += 1
    while j <= hi:
        tmp[k] = arr[j]; j += 1; k += 1

    for i in range(lo, hi+1):
        arr[i] = tmp[i]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    merge_sort(0, N-1)
    print(f'#{tc} {arr[N // 2]} {cnt}')

