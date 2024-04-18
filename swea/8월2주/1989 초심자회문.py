'''
T = int(input())
for tc in range(1, T + 1):
    word = input()
    reverse_word = word[::-1]

    if word == reverse_word:
        result = "1"
    else:
        result = "0"

    print(f'#{tc} {result}')
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    word = input()

    re_word = ' '
    result = 0
    for i in range(len(word)- 1, -1, -1):
        re_word += word[i]
    if word == re_word:
        result += 1
    else:
        pass
    print(f'#{tc} {result}')

T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()

    count = {}

    for ans in N:
        if ans not in count:
            count[ans] = 0
        count[ans] += 1

    max_count = 0

    for ans in M:
        if ans in count:
            max_count = max(max_count, count[ans])

    print(f'#{tc} {max_count}')
