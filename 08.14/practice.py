# 부분 집합, 순열
'''
arr = [1, 2, 3]
N = len(arr)
bits = [0] * N
for i in range(2):
    bits[0] = i
    for j in range(2):
        bits[1] = j
        for j in range(2):
            bits[2] = k
            print(bits)

'''
"""
arr = [1, 2, 3]
N = len(arr)
used = [0] * N
lst = [0] & N
def perm(k, n):
    if k == n:
        print(lst)
    else:
        for i in range(N):
            if used[i]: continue
            used[i] = 1
            lst[k] = arr[i]
            perm(K+1,n)
            used[i] = 0
perm = 
"""