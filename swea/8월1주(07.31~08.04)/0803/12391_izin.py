T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    l = 1       # l = start
    r = P       # r = N-1
    cnt_A = 0
    while l <= r:       # c = middle
        c = (l + r)//2
        if c == A:
            break
        elif c > A:
            r = c
            cnt_A += 1
        else:
            l = c
            cnt_A += 1
    l = 1
    r = P
    cnt_B = 0
    while l <= r:
        c = (l + r)//2
        if c == B:
            break
        elif c > B:
            r = c
            cnt_B += 1
        else:
            l = c
            cnt_B += 1
    if cnt_A > cnt_B:   # 횟수가 작은 B를 호출
        result = 'B'
    elif cnt_A < cnt_B:     # 횟수가 작은 A 를 호출
        result = 'A'
    else:
        result = 0      # 횟수가 같아서 비기면 0

    print(f'#{tc} {result}')



'''
def binarysearch(P, A, B):
    l = 1
    r = P
    cnt_A = 0
    while l <= r:
        c = (l + r) // 2
        if c == A:
            break
        elif c > A:
            r = c - 1
        else:
            l = c + 1
        cnt_A += 1

    l = 1
    r = P
    cnt_B = 0
    while l <= r:
        c = (l + r) // 2
        if c == B:
            break
        elif c > B:
            r = c - 1
        else:
            l = c + 1
        cnt_B += 1

    return cnt_A, cnt_B
    if cnt_A > cnt_B:
        result = 'cnt_A'
    elif cnt_A < cnt_B:
        result = 'cnt_B'
    else:
        result = 0
'''






