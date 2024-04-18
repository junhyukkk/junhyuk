icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}
# 스택에 푸쉬하기전 외부에서의 계산 우선순위
# 스택 푸쉬후 내부에서의 계산 우선순위
def get_postfix(infix, n):
    postfix = ""
    stack = []
# 후위표기식 구하는 함수(중위표기식 = infix이 주어지고, n = 중위표기식의 길이)
# postfix : 후위표기식이 들어갈 곳
# stack : 스택 쌓아올릴 리스트
    for i in range(n):
        if infix[i] not in ["(", "+", "*", "/", "-", ")"]:
            postfix += infix[i]
        else:
            if infix[i] == ")":
# i 가 길이 n 을 순회 하며 비연산자라면 postfix에 추가하고
# 비연산자일때 ')' 라면 스택을 pop 해 나가는데 '('을 만나면 break
                while stack:
                    opr = stack.pop()
                    if opr == "(":
                        break
                    postfix += opr
# i번째 토큰이 다른 연산자면 top에 있는 연산자가 i번쨰 토큰의 우선순위보다 우선순위가 낮을때까지
# pop 해서 출력 > 반복문이 끝나면 i번째 토큰보다 우선순위 낮은거만 남음
            else:
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()
# 이후 전체 stack 에는 남아있는 연산자의 우선순위가 낮은것만 남은상태로 return
    return postfix

# 후위표기식 계산하는 함수
def get_result(postfix):
    stack = []
    for c in postfix:
        if c not in ["(", "+", "*", "/", "-", ")"]:
            stack.append(int(c)) # 타입 조심
# c가 postfix 를 순회하며 c가 비연산자일 때 stack에 추가(정수형)
        else:
            right = stack.pop()
            left = stack.pop()
# c 가 연산자인 경우에 필요한 만큼의 stack 에서 pop
# 계산한 결과는 push 해서 사용
            if c == "+":
                result = left + right
            elif c == "-":
                result = left - right
            elif c == "*":
                result = left * right
            elif c == "/":
                result = left // right
            stack.append(result)

    return stack.pop()
# 마지막에 남은 결과를 pop 해서 결과 확인(postfix 에서 얻는 결과값)
for tc in range(1, 11):
    n = int(input())
    string = input()
    postfix = get_postfix(string, n)

    print(f'#{tc} {get_result(postfix)}')