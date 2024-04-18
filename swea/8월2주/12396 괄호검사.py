# 교재 연습문제2
"""
# stack 직접 구현해서 사용
arr = input()
S = [0] * 100 # 충분히 크게
top = -1    # 초기값, 인덱스 저장
ans = 1
for ch in arr:
    if ch == '({':
        top += 1; S[top] = ch
    elif ch in ')}':
    else:
        if top == -1 or S[top] != '(':
            ans = 0
            break
        top -= 1
if top != -1:
    ans = 0
print(ans)
# =================================
# List의 append()/pop() 사용
arr = input()
S = []
ans = True
for ch in arr:
    if ch == '(':
        S.append(ch)
    else:
        if not S or S[-1] != '(':
            ans = False
            break
        S.pop()
if S:
    ans = False
print(ans)
"""
"""
T = int(input())
for tc in range(1, T+1):
    arr = input()
    S = [0] * 100
    top = -1

    ans = True
    for i in arr:
        if i == '(':
            top += 1
            S[top] = '('
        elif i == '{':
            top += 1
            S[top] = '{'
        elif i == ')':
            if S[top] == '(':
                S[top] = 0
                top -= 1
            else :
                ans = False
                break
        elif i == '}':
            if S[top] == '{':
                S[top] = 0
                top -= 1
            else:
                ans = False
                break
    if S == 0:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')
"""

def check_paren(arr):
    S = [0] * len(arr)
    top = -1

    for ch in arr:
        # 여는괄호
        if ch in '({':
            top += 1; S[top] = ch
        elif ch in ')}':
            if top == -1 or S[top] != '({':
                return 0
            top -= 1
        # 닫는괄호 , 그외
    if top != -1:
        return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    arr = input()
    ans = check_paren(arr)
    print(f'#{tc} {ans}')


def check_paren(arr):
    S = [0] * len(arr)
    top = -1
    for ch in arr:
        # 여는 괄호
        if ch in '({':
            top += 1
            S[top] = ch
        elif ch == ')':
            if top == -1 or S[top] != '(':
                return 0
            top -= 1
        elif ch == '}':
            if top == -1 or S[top] != '{':
                return 0
            top -= 1
    if top != -1:
        return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    arr = input()
    ans = check_paren(arr)
    print(f'#{tc} {ans}')