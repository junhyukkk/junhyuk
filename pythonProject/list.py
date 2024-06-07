# def Counting_Sort(A, B, k)
# A[] : 입력배열(0 to k)    data
# B[] : 졍렬된 배열.      Temp
# C[] : 카운트 배열      counts

# baby-gin game (숫자 카드?)

# 11092
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    min_idx = 0     # 최솟값의 인덱스
    max_idx = 0
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i
    ans = max_idx - min_idx
    if ans < 0:
        ans *= -1
    print(ans)
'''
T = int(input())
for tc in range(1, T +1):
    N = int(input())
    arr = list(map(int,input().split()))

    print(arr)
'''