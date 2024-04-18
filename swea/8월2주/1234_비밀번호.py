T = 10
for tc in range(1, T+1):
    str_N, str_num = input().split()

    N = int(str_N)
    stack = [0] * N
    top = -1

    for t in str_num:
        if top == -1 or stack[top] != t:
            top += 1
            stack[top] = t
        else:
            top -= 1
    ans = ''
    for i in range(top+1):
        ans += stack[i]

    print(f'#{tc} {ans}')