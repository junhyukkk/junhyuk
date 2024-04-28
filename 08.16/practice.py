# 계산기
'''
icp = {'(': 3, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # stack에 push하기 전
isp = {'(': 0, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 스택에 내부
infix = '(6+5*(2-8)/2)'
S = []          # 스택
postfix = ''    # 후위표기법 저장
for token in infix:
    if token in icp:   # 연산자
        if token == ')':
            while S and S[-1] != '(':
                postfix += S.pop()
            S.pop()
        else:   # (*/+-
            # token 과 스택의 꼭대기 있는 연산자의 우선순위 비교
            while S and icp[token] <= isp[S[-1]]:
                postfix += S.pop()
            S.append(token)
    else:              # 피연산자
        postfix += token

while S:
    postfix += S.pop()

print(postfix)
'''
# 부분집합과 순열
'''
arr = [1,2,3,4]
N = len(arr)
for i in range(N):
    arr[0], arr[i] = arr[i], arr[0]
    print(arr)
    arr[0], arr[i] = arr[i], arr[0]
'''

arr = [1, 3, 3, 3, 1, 1, 3]
print(arr[1])