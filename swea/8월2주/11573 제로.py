"""
# 스택의 구현
def push(item, size):   # 연산
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = item

size = 10
stack = [0] * size      #저장소
top = -1

push(10,size)
top += 1
stack[top] = 20

# pop 알고리즘
def pop():
    if len(s) == 0:
    # underflow
    return
    else:
        return s.pop()
"""
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    stack = [0] * N
    top = -1

    zero_list=[]
    for i in num_list:
        if i != 0:
            zero_list.append(i)
        else:
            zero_list.pop()

    sum_num = 0
    for j in zero_list:
        sum_num += j

    print(f'#{tc} {sum_num}')
'''

T = int(input())
for tc in range(1, T + 1):
    top = -1
    N = int(input())
    stack = [0] * N
    num_list = list(map(int, input().split()))

    def push(item):
        global top
        top += 1
        stack[top] = item

    def pop():
        global top
        top -= 1
        return stack[top+1]

    for i in num_list:
        if i != 0:
            push(i)
        else:
            pop()

    sum_num = 0
    for i in range(top+1):
        sum_num += stack[i]
    print(f'#{tc} {sum_num}')
'''
T = int(input())
for tc in range(1, T + 1):
    top = -1
    N = int(input())
    stack = [0] * N
    num_list = list(map(int, input().split()))

    def push(item):
        global top
        top += 1
        stack[top] = item

    def pop():
        global top
        ret = stack[top]
        top -= 1
        return ret

    for i in num_list:
        if i != 0:
            push(i)
        else:
            pop()

    total = 0
    for i in range(top+1):
        total += stack[i]
    print(f'#{tc} {total}')
'''
