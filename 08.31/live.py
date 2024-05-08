"""
def ncr(n, r):
    if r == 0:
        print(tr)
    elif n < r:     # 남은 원소보다 만은 원소를 선택해야하는 경우
        return      # 불가
    else:
        tr[r-1] = a[n-1]
        ncr(n-1, r-1)
        ncr(n-1, r)     # a[n-1] 조합에 포함시키지 않는경우


N = 5
R = 3
a = [1,2,3,4,5]
tr = [0] * R
ncr(N, R)
"""
#

def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

A = [1,2,3,4,5,6]
N = len(A)
R = 2
comb = [0] * R
nCr(N, R, 0)