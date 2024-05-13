for tc in range(1, 11):
    dump = int(input())
    box_h = list(map(int, input().split()))

    while dump > 0:     # dump 값이 0이 될때까지
        max_box = 0     # 최대 높이, 최저 높이, 그 값들의 인덱스 구하기
        max_idx = 0
        min_box = 1000
        min_idx = 0
        for i in range(100):        # 가로의 박스들을 순회
            if max_box < box_h[i]:  # 박스높이의 최대값, 최소값 구하기
                max_box = box_h[i]
                max_idx = i
            if min_box > box_h[i]:
                min_box = box_h[i]
                min_idx = i

        box_h[max_idx] -= 1         # 최고높이 인덱스 박스높이 -1
        box_h[min_idx] += 1         # 최저높이 인덱스 박스높이 +1
        dump -= 1                   # dump -1

    max_h = 0                       # 덤프가 끝나고 나서의 최고, 최저 높이
    min_h = 1000

    for i in range(100):            # 가로 박스들 순회
        if box_h[i] > max_h:        # 최고높이, 최저높이 구하고
            max_h = box_h[i]
        if box_h[i] < min_h:
            min_h = box_h[i]

    print(f"#{tc} {max_h - min_h}") # 문제에서 요구하는 최고, 최저 높이의 차를 구함