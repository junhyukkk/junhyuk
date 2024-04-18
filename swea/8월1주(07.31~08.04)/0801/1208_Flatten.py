T = 10

for tc in range(1, T + 1):

    N = int(input())

    box = list(map(int, input().split()))

    while N > 0:

        max_idx = 0
        max_height = 0
        min_idx = 0
        min_height = 100
        for i in range(100):

            if box[i] > max_height:
                max_height = box[i]
                max_idx = i
            if box[i] < min_height:
                min_height = box[i]
                min_idx = i

        box[max_idx] -= 1
        box[min_idx] += 1
        N -= 1

    max_height = 0
    min_height = 100

    for i in range(100):
        if box[i] > max_height:
            max_height = box[i]
        if box[i] < min_height:
            min_height = box[i]

    print(f"#{tc} {max_height - min_height}")