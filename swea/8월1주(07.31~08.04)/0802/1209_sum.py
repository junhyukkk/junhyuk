import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []

    max_r = 0
    for i in range(100):
        row_total = 0
        for j in range(100):
            row_total += arr[i][j]
        if max_r < row_total:
            max_r = row_total
    sum_list.append(max_r)

    max_c = 0
    for j in range(100):
        col_total = 0
        for i in range(100):
            col_total += arr[i][j]
            if max_c < col_total:
                max_c = col_total
    sum_list.append(max_c)

    dia_total = 0
    for i in range(100):
        dia_total += arr[i][i]
    sum_list.append(dia_total)

    xai_total = 0
    for i in range(100):
        xai_total += arr[i][100-1-i]
    sum_list.append(xai_total)

    max_num = sum_list[0]
    for i in sum_list:
        if max_num < i:
            max_num = i

    print(f'#{tc} {max_num}')





