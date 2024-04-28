# stack 2
"""
- 부분집합, 순열
- 분할정복

# 부분집합 재귀

"""
# 부분집합 재귀 라이브 강의 복습해서 참고할것 !
'''
def f(i, N):
    if i ==N:
        print(bit)
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)
        return
A = [1,2,3]
bit = [0] * 3
f(0, 3)
'''
# 부분집합의 합 _재귀
'''
def f(i, N):
    if i == N:
        print(bit, end = ' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end = ' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        return

A = [1,2,3]
bit = [0] * 3
f(0, 3)
'''
'''
# 부분집합의 합 _재귀 2
def f(i, N, s):     # s: i-1 원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end = ' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1      # 부분집합에 A[i] 포함
        f(i + 1, N, s+A[i])
        bit[i] = 0      # 부분집합에 A[i] 미포함(빠짐)
        f(i + 1, N, s)
        return

A = [1,2,3]
bit = [0] * 3
f(0, 3, 2)
'''
# 부분집합의 합, 연습문제
def f(i, N, s):     # s: i-1 원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        if s == 10:
            print(bit)
        print(bit, end = ' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1      # 부분집합에 A[i] 포함
        f(i + 1, N, s+A[i])
        bit[i] = 0      # 부분집합에 A[i] 미포함(빠짐)
        f(i + 1, N, s)
        return

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 5
A = [i for i in range(1, N+1)]
bit = [0] * N
f(0, 5, 0)

# 순열
'''

'''

# 거듭제곱
"""
def f1(b, e):
    if b == 0:
    return 1
    r = 1
    for i in range(e):
        r *= b
    return r
    
def f2(b, e):
    if b == 0 or e == 0:
        return 1
    if e % 2:   # 홀수인경우
        r = f2(b, (e-1)//2)
        return r*r*b
    else:       # 짝수인경우
        r = f2(b, e//2)
        return r*r

print(f1(2,10))
print(f2(2,10))    
"""

