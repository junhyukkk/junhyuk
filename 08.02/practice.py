# 열 우선 순회
# i 행
# j 열
'''
for j in range(m):
    # 이 자리에 열의 합을 구한다면 s=0 이 들어가 열마다 초기화 하는 작업이 필요
    for i in range(n):
        f(array[i][j])
'''

N = 2   # 행의 크기
M = 4   # 열의 크기

arr = [[0,1,2,3],[4,5,6,7]]
# 행 우선순회
for i in range(N):
    for j in range(M):
        print(arr[i][j])
# 열 우선순회
for j in range(M):
    for i in range(N):
        print(arr[i][j])
    # 지그재그 순회
for i in range(N):
    for j in range(M):
        print(arr[i][j + (M=1=2*j)*(i%2)])
    #   if i%2 == 1:      # 홀수 행인 경우

'''
# arr = [0] * M >> 1차원 배열
arr = [[0] * M for _ in range(N)]
arr2 = [[0]*M]*N    # 틀린경우 
arr[0][0] = 1       # (0.0)에만 1이 들어가야하는데
arr2[0][0] = 1      # (1,0)에도 복사가 되어 들어가는 문제가 생김
print(arr)      # [[1, 0, 0, 0], [0, 0, 0, 0]]
print(arr2)     # [[1, 0, 0, 0], [1, 0, 0, 0]]
'''
# 행의 합 최대 구하기
max_v = 0
for i in range(N):
    row_total = 0
    for j in range(M):
        row_total += arr[i][j]
    if max_v < row_total:
        max_v = row_total

