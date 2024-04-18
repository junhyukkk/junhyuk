
#선택 정렬 알고리즘
def selectionsort(a, N):
    for i in range(N-1):
        minidx = i
        for j in range(i+1, N):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]
'''
셀렉션 알고리즘
선택 과정 : 1. 정렬 알고리즘을 이용하여 자료 정렬하기
            2. 원하는 순서에 있는 원소 가져오기
## ex)

arr = [64, 25, 10, 22, 11]
- 주어진리스트 중에서 최소값을 찾는다 >> 인덱스(위치)찾기
- 값을 리스트의 맨 앞에 위치한 값과 교환한다
-
>> for문 내부에 들어갈 내용들

N = len(arr)
min_idx = 0
for i in range(1, N):
    if arr[min_idx] > arr[i]:
        min_idx = i
arr[0], arr[min_idx] = arr[min_idx], arr[0]
print(arr)      # [10, 25, 64, 22, 11]

# 1번 부터 N-1번에서 최소값을  찾기
min_idx = 1
for i in range(2, N):
    if arr[min_idx] > arr[i]:
        min_idx = i
arr[1], arr[min_idx] = arr[min_idx], arr[1]
print(arr)      # [10, 11, 64, 22, 25]

min_idx = 2
for i in range(3, N):
    if arr[min_idx] > arr[i]:
        min_idx = i
arr[2], arr[min_idx] = arr[min_idx], arr[2]
print(arr)

# 마지막은 가장 큰 값이 남을 것이기 때문에 N-1 하고 pass 가능

# 0부터 N-1 범위에서 최소값을 찾음
for s in range(0, N-1):
    min_idx = s
    for i in range(s+1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
    arr[s], arr[min_idx] = arr[min_idx], arr[s]
print(arr)

    # 총 10번 (최대 찾기 1번 + 최소 찾기 1번) * 5번
    for j in range(0, 10, 2):
        # 최대 찾기
        max_idx = j
        for i in range(j+1, N):
            if arr[max_idx] < arr[i]:
                max_idx = i
        arr[j], arr[max_idx] = arr[max_idx], arr[j]
 
        # 최소 찾기
        min_idx = j+1
        for i in range(j+2, N):
            if arr[min_idx] > arr[i]:
                min_idx = i
        arr[j+1], arr[min_idx] = arr[min_idx], arr[j+1]
 
    print(f'#{tc}', *arr[:10])

'''
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, 10):
        max_num = i

        for j in range(i+1, N):

            if arr[max_num] < arr[j]:
                max_num = j
        arr[i], arr[max_num] = arr[max_num], arr[i]

        min_num = i+1
        for j in range(i+2, N):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[i+1], arr[min_num] = arr[min_num], arr[i+1]

    print(f'#{tc}', arr[:10])





