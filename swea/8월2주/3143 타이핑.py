# 타이핑을 푸는 방식 : 패턴매칭: bruteforce
p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

n, m = len(t), len(p)

# 교재에 포함된 패턴 매칭, 비교시 텍스트 인덱스 i가 증가함
i = j = 0
while i < n:
    if p[j] != t[i]:
        i = i - j
        j = -1

    i, j = i + 1, j + 1
    if j == m:
        print(i - m, t[i - m: i])
        j = 0
"""
for tc in range(1,int(input())+1):
    A,B = input().split()
    n,m = len(A), len(B)
 
    i_list = []
    count = 0
 
    i = 0
    while i <= n - m:
        for x in range(0,m):
            if A[i+x] != B[x]:
                break
        else:
            count += 1
            i = i + m - 1
        i += 1
    result1 = n - ((m-1) * count)
    print(f'#{tc} {result1}')
"""