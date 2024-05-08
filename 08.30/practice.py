arr = 'abc'
"""
# 부분집합
N = len(arr)
A = []
B = []
def subset(k):
    if k == N:
        print(A)
    else:
        A.append(arr[k])
        subset(k+1)
        A.pop()

        B.append(arr[k])
        subset(k+1)
        B.pop()

A = [arr[0]]
subset(0)
"""
# 순열

N = len(arr)
used = [0] * N
order = [0] * N     # 실제 생성되는 순열 저장

for i in range(N):
    if used[i]: continue
    used[i] = 1
    order[0] = arr[i]
    for j in range(N):
        if used[j]: continue
        used[j] = 1
        order[1] = arr[j]
        for k in range(N):
            if used[k]: continue
            used[k] = 1
            order[2] = arr[k]
            print(order)