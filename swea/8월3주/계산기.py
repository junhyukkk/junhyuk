'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    infix = input()     # 중위표기식
    S = [0] * (len(infix)+1)
    postfix = ''        # 후위표기식 들어갈 자리
    top = -1

    for i in infix:
        if i != '+':    # 비연산자라면
            S[top] = int(i)
            top += 1
        else:           # 연산자라면



print()
'''
# 스택 밖에 있을때 우선순위
icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}

# 스택 안에 있을때 우선순위
isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}


# 중위표기식을 후위표기식으로 바꾸기
# infix // postfix

# infix : 후위표기식으로 바꿀 중위표기식
# n : 후위표기식의 길이 (문자열의 길이)
def get_postfix(infix, n):
    # 결과로 만들 후위표기식
    postfix = ""

    stack = []

    # 문자열(중위표기식)에서 글자(토큰) 하나씩 떼오기
    for i in range(n):
        # infix[i] : i번째 글자

        # i번째 토큰이 피연산자이면 문자열에 출력
        if infix[i] not in ["(", "+", "*", "/", "-", ")"]:
            postfix += infix[i]
        # i번째 토큰이 연산자이면
        else:
            # i번째 토큰이 닫는 괄호이면
            if infix[i] == ")":
                # 여는 괄호가 나올때까지 스택안의 연산자 pop 해서 출력
                while stack:
                    opr = stack.pop()
                    # 여는 괄호가 나오면 연산자 꺼내기 중단
                    if opr == "(":
                        break
                    postfix += opr
            # i번째 토큰이 다른 연산자면
            else:
                # 현재 i번째 토큰(연산자)의 우선순위 보다
                # stack의 꼭대기(top) 에 있는 연산자의 우선선순위가 같거나 높으면
                # pop 해서 출력
                # 언제까지? 스택의 꼭대기에 있는 연산자의 우선순위가 i번째 토큰(연산자)의
                # 우선순위보다 낮을 때까지
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                # 반복문이 끝나고 나면 스택안에는 i번째 토큰보다 우선순위가 낮은 애들밖에 없다.
                stack.append(infix[i])

    # 모든 i번째 글자에 대해서 순회가 끝나고
    # 남아 있는 연산자를 출력 , 남아있는 연산자는 상대적으로 우선위가 낮은애들이 남아있음.
    while stack:
        postfix += stack.pop()

    return postfix

infix = "(6+5*(2-8)/2)"

print(get_postfix(infix, len(infix)))


# 2. 후위표기식을 계산하는 함수

def get_result(postfix):
    stack = []

    # 후위표기식에서 토큰 하나씩 떼어오기
    for c in postfix:
        # 피연산자를 만나면 일단 스택에 넣기
        if c not in ["(", "+", "*", "/", "-", ")"]:
            stack.append(int(c)) # 타입 조심

        # 연산자를 만나면 해당 연산에 필요한 만큼 stack에서 pop한다음 계산
        # 계산한 결과를 다음 연산에서 쓰기 위해 push
        else:
            # 오른쪽을 먼저
            right = stack.pop()
            # 왼쪽을 나중에
            left = stack.pop()

            # 연산자의 종류에 따라 계산
            if c == "+":
                result = left + right
            elif c == "-":
                result = left - right
            elif c == "*":
                result = left * right
            elif c == "/":
                result = left // right # 나누기에서 타입 조심!! (나누어 떨어진다던가, 정수)

            # 계산한 결과를 다음 연산자에서 쓰기 위해
            # 여기의 계산결과를 push
            stack.append(result)

    # 마지막에는 남은 결과가 단 하나!!!! 이거 꺼내서 확인하면 된다.
    return stack.pop()

string = "2+3*4/5"
n = len(string)

postfix = get_postfix(string, n)
print(postfix)

print(f'# {get_result(postfix)}')




