import sys
sys.stdin = open('sample_input (11892).txt')

def quick_hoare(s, e):
    if s >= e: return

    # partition
    i, j = s, e
    p = arr[s]
    while i <= j:
        while i <= e and p >= arr[i]:
            i += 1
        while p < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[s], arr[j] = arr[j], arr[s]
    # 분할 위치는 pivot이 있는 j
    quick_hoare(s, j - 1)
    quick_hoare(j + 1, e)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick_hoare(0, len(arr) - 1)
    print(arr)
    print(f'#{tc} {arr[N//2]}')

# def quick_lomuto(lo, hi):
#     # 계속 갈지 말지 ...
#     if lo >= hi: return
#
#     i = lo - 1
#     for j in range(lo, hi):
#         if arr[j] <= arr[hi]: # arr[hi] = 피봇
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     i += 1
#     arr[i], arr[hi] = arr[hi], arr[i]
#     # 분할 위치는 pivot이 있는 i
#     quick_lomuto(lo, i - 1)
#     quick_lomuto(i + 1, hi)
#
#
# arr = [69, 30, 10, 2, 16, 8, 32, 21]
# # arr = [1, 1, 1, 1, 0, 0, 0, 0, 0]
# quick_lomuto(0, len(arr) - 1)
# print(arr)
