def print_subset(bit, arr, n):
    total = 0 # 부분집합의 합 (변수의 초기화)
    for i in range(n):
        if bit[i]:
            print(arr[i], end = ' ')
            total += arr[i]
    print(bit, total)


arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit, arr, 4)


# subset2
arr = [1,2,3]

n = len(arr)        # n: 원소의 개수

for i in range(1 << n):       # 1<<n : 부분 집합의 개수
    for j in range(n):      # 원소의 수 만큼 비트를 비교함
        if i & (1 << j):      # i의 j 번 비트가 1인경우
            print(arr[j], end = ", ")   # j번 원소 출력력
    print()
print()


*이진
*특별
래더 좋은문제~~
부분
달팽이
숫자정렬