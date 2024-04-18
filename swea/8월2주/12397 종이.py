# 영준 풀이
def form(n):
    if n < 2:
        return 1
    else:
        return form(n - 2) + 2 ** (n - 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n = N // 10
    print(f'#{tc} {form(n)}')

# 교수님 풀이
def case(n):
    if n < 2:
        return 1
    else:
        return case(n - 1) + case(n - 2) * 2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    n = (N // 10)
    print(f'#{tc} {case(n)}')