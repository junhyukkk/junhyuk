# 사각영역 >> 좌상단 좌표와 우하단 좌표를 알아야함
# or 좌상단 좌표와 사각행열의 크기를 알아야함
# ex)
"""
arr = [[0] * 9 for _ in range(9)]
val = 1
for sr in (0,3,6):
    for cr in (0,3,6):
        for r in range(sr,sr+3):
            for c in range(cr, cr+3):
                arr[r][c] = val
        val += 1

for line in arr:
    print(*line)
"""
'''
# 재귀호출
# 1. DFS(그래프탐색)
# 2. 백트래킹(DFS 방식 >> 알고리즘)
# 3. 분할 정복(이진 검색,...)
# 4. 동적 계획법(점화식 구현)
        -> 최적부분구조(피보나치 수 DP에서)
# 5. 재귀적 구조의 자료구조(트리...)
# ; 재귀 함수 >> 재귀적 문제를 해결
# 반복문으로 하는 일을 동일하게 할 수 있음

# for i in range(3):
#    print(i, '반복할 일')
=> while 문으로 변경
i = 0 
while i < 3:
    print(i, '반복할 일')
    i += 1

def print_hello()
    if 재귀호출 종료를 판단:     # 재귀호출의 종료를 판단할 조건식이 필요함
        pass                 # 본인(재귀호출) 내부에서는 판단할 근거가 없음
    print('반복할 일')         # 재귀함수의 종료를 판단하는 것은 매개변수(외부에서 주어지는 값)
    print+hello()

ex)
i = 0
def print_hello(i, n)
    if i == n:
        pass
#   else 가 빠진다면 무한루프 돌지 않기위해 return을 작성해줘야함 
    else:
        print(i + 1, '반복할 일')

def print_hello(i, n):
    if i == n:
        pass
    else:
        print(i, '호출전')
        print_hello(i+1,n)
        print(i,'호출후')
print_hello(0,3)
'''
cnt = 0
def print_hello(i, n):
    if i == n:
        global cnt
        cnt += 1
    else:
        print_hello(i + 1, n)
        print_hello(i + 1, n)

print_hello(0, 3)
print(cnt)

# 함수 호출한 것 두번을 0~3까지 세번 돌리면  ** 이 되어서 2**3 과 같음

