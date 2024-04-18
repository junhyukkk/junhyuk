T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_sum = 0
    min_sum = 1000000
    for i in range(0, N - M + 1):
        sum_num = 0
        for j in range(i, i + M):
            sum_num += numbers[j]

        if sum_num > max_sum:
            max_sum = sum_num
        if sum_num < min_sum:
            min_sum = sum_num
        result = max_sum - min_sum
    print(f'#{tc} {result}')