T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input()))
    K = 9
    cnt = [0] * (9 + 1)

    for val in card_list:
        cnt[val] += 1

    max_idx = 0
    count = 0

    for val in range(10):
        if cnt[max_idx] <= cnt[val]:
            max_idx = val
            count = cnt[val]
    print(f'#{tc} {max_idx} {count}')