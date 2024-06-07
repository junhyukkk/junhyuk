A = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(A)
B = [0] * (len(A))
# 1 카운팅을 할 떄, 딕셔너리를 이용하고 key 에 값을 넣고, value 에 빈도수를 넣기
cnt_dict = {}
for key in A:
    if key in cnt_dict:
        cnt_dict[key] = cnt_dict[key] + 1
    else:
        cnt_dict[key] = 1
print(cnt_dict)
# 2 카운팅하기
K = 4   # 최댓값
# 카운팅을 하기 위해 자료값을 배열의 인덱스로 사용
# >> 배열의 공간이 미리 생성돼야 한다
# >> 최댓값을 알아야 함, 최대값으로 크기를 결정
# C = [0] * 5 # >> # [0]+[0]+[0]+[0]+[0]
C = [0] * (K + 1)   # > 인덱스는 0부터 시작하기에 +1 붙여야함(마지막 인덱스가 K)
for val in A:
    C[val] += 1     # = C[val] + 1
print(*range(K+1))
print(*C)
# 3 누적 빈도수 계산
for i in range(1, K+1):     # K까지 값이 가야함
    C[i] += C[i - 1]    # = C[i] = C[i-1] + C[i]  이전값에 원래 값을 덮어서 더해줌
print(*C)
# 4 A에서 하나씩 B로 옮기기
for i in range(N-1, -1, -1):
    # A[i] >> B[] 에 넣어주는 것
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]
print(B)

'''
B = [0] * (len(A))
K = 4             # 자료의 최대값
C = [0] * (K + 1) # 마지막 index=K
# 1. 자료의 빈도수를 계산
for val in A:
    C[val] += 1
print(C)

# 2. 누적 빈도수를 계산
for i in range(1, K + 1):
    C[i] = C[i - 1] + C[i]
print(C)

# 3. 원자료들을 하나씩 정렬 될 위치로 복사
for val in A:
    # A ---> B로
    C[val] -= 1
    B[C[val]] = val
print(B)
'''