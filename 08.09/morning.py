# 스택
"""
- 선형 구조(자료간의 관계가 1대1)를 갖는다
- 마지막에 삽입한 자료를 가장 먼저 꺼내는 후입선출
- 스택에서 마지막에 삽입된 원소의 위치 인덱스 = top
- pop 과 peek 의 차이는 peek 은 확인하는 정도의 반환의 의미


stack = [0] * 10
top = -1    # 초기값, 인덱스 위치 저장(-1은 가리키는게 없다라는 뜻)
            # top 은 가장 마지막 자료의 인덱스

def push(item):
    global top
    top += 1
    stack[top] = item
    pass
def pop():
    global top
    ret = stack[top]
    top -= 1
    return ret
    pass

- 스택을 이용한 괄호 검사에서 두 가지 경우
1. 수식이 끝낫찌만 괄호가 남은경우
2. 닫는괄호를 한 번 더 적어서 pop이 남는경우



# 재귀호출



i = 0
while i < 3:
    print('Hello') # 반복할 작업
    i += 1

# 재귀 호출(1)
def print_hello(i):
    if i == 3:
        return
    else:
        print('Hello')  # 반복할 작업
        print_hello(i + 1)
print_hello(0)
"""

stack = [0] * 10
top = -1    # 초기값, 인덱스 위치 저장(-1은 가리키는게 없다라는 뜻)
            # top 은 가장 마지막 자료의 인덱스
            # top 만 -1 로 설정하면 지우지 않더라도 초기화하는 것과 같아짐
# ===============
top += 1; stack[top] = 1
top += 1; stack[top] = 2
top += 1; stack[top] = 3


# 예시
def push(item):
    global top
    # if top == 마지막 인덱스:
    # 인덱스 초과해서 저장이 안되기 떄문에
    # stack-full인 상태에서는 더 실행이 되면안됨
    top += 1
    stack[top] = item
    pass
def pop():      # 꺼내올게 없을때 문제가 됨
    global top
#    if top == -1: # stack-empty
#        return full(상태)
    ret = stack[top]
    top -= 1
    return ret
    pass
def isEmpty():
    if top == -1:
        return True

push(1); print(top, stack)
push(2); print(top, stack)
push(3); print(top, stack)
print(pop()); print(top, stack)
push(-1); print(top, stack)

while not isEmpty():
    print(pop())
"""
공백인지 아닌지 확인하는 연산
def isempty():
    top == -1
    return True    
"""

# 빈 리스트를 만들고 리스트 체크
stack = []
stack.append(1)
stack.append(1)
stack.append(1)

while stack:
    print(stack.pop())