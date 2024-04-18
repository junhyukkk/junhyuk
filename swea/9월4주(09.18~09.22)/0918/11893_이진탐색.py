# !!!! 주의 !!!!
# 반드시 정렬된 상태에서 이진 탐색을 진행한다.

def binary_serach_iter(arr, lo, hi, key):
    # 중간 위치 선택
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

arr = [8, 11, 16, 28, 39, 49, 60, 67, 85, 89]
N = len(arr)
print(binary_serach_iter(arr, 0, N - 1, 67))
print(binary_serach_iter(arr, 0, N - 1, 68))

#=======================================================
# 이진탐색 재귀

def binary_serach(arr, lo, hi, key):
    if lo >= hi:
        return -1

    mid = (lo + hi) >> 1

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_serach(arr, lo, mid - 1, key)
    else:
        return binary_serach(arr, mid + 1, hi, key)


arr = [8, 11, 16, 28, 39, 49, 60, 67, 85, 89]
N = len(arr)
print(binary_serach(arr, 0, N - 1, 67))
print(binary_serach(arr, 0, N - 1, 68))
