"""
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
"""
# 비트연산
# bit > 0/1을 저장하는 단위(컴퓨터 단위)
# 1byte > 8bit
# 32-bit -> 4byte -> 정수(int)

# 비트 연산자 > 비트 단위 연산 (비트끼리)

print(8 & 5)
print(8 | 5)
print(~8)
print(5<<1)
print(5<<2)
print(5>>1)
print(5<<3)
print(5>>3)
print(5<<4)

def print_bit(n):
arr = [1, 2, 3]
N = len(arr) # N= 4

for subset in range(1 << N): # 0~15
    print_bit(subset)
    for i in range(N):
        if subset & (1 <<i):
            print(arr[i], end ='')
    print()
