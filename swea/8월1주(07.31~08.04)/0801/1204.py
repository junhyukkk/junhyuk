T = int(input())

for tc in range(1, T + 1):
    test_num = int(input())
    scores = list(map(int, input().split()))
    # 최대값 K = 100
    cnt_score = [0] * 101

    for score in scores:
        cnt_score[score] += 1

    max_count = 0
    avr = 0

    for score in range(101):
        if cnt_score[score] >= max_count:
            max_count = cnt_score[score]
            avr = score

    print(f'#{tc} {avr}')