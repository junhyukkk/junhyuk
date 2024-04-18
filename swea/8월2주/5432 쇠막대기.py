T = int(input())
S = [0] * 100000
for tc in range(1, T+1):
    arr = input()
    top = -1
    ans = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            top += 1; S[top] = arr[i]
        else:
            top -= 1
            if arr[i - 1] == '(':   # 레이저
                ans += top+1
            else:                   # 막대의 끝
                ans += 1
    print(f'#{tc} {ans}')