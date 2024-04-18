'''
# 먼저 완전이진탐색 구성을 맞춰놓고 시작하기
data = [69, 10, 30, 2, 16, 8, 31, 22]
# 저장소
M = [0] * 100
last = 0        # 현재 힙에 저장된 자료수, 마지막 노드의 인덱스

def push(item):
    # 1. 완전 이진트리 구조를 유지하기 위해 마지막 노드를 추가
    global last
    last += 1
    M[last] = item
    # 2. 부모 자식간의 대소 관계를 유지하도록 재조정
    c = last
    p = c//2
    while p > 0 and M[p] > M[c]:
        M[p], M[c] = M[c], M[p]
        c = p
        p = c//2
def pop():
    # 1. 루트를 백업해준다
    # 2. 완전이진트리 유지를 위해 마지막 노드를 루트로 복사
    # 3. 마지막 노드의 인덱스를 1 감소
    global last
    ret = M[1]      # 루트 백업
    M[1] = M[last]  # 마지막 노드 루트로 복사
    last -= 1       # 인덱스 감소

    # 부모/ 자식간의 대소 관계를 재조정
    p, c = 1, 2
    while c <= last:
        # 오른쪽 자식에게도 관심
        if c + 1 <= last and M[c] > M[c+1]:
            c += 1
        if M[p] > M[c]:
            M[p], M[c] = M[c], M[p]
        else:
            break
        p = c
        c = p*2
    return ret

for val in data:
    push(val)
while last:
    print(pop(), end=' ')
'''
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    # 1. 주어진 데이터 내용
    H = [0] * 501
    last = 0
    # 2. 저장소만들기, 마지막 인덱스 0 초기화
    def push(item):
        global last
        last += 1
        H[last] = item
    # 3. 완전이진트리 형태 유지를 위해 마지막 노드 추가
        p, c = last // 2, last
        while p > 0 and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2
    # 4. 부모 자식간의 대소관계 유지하도록 재조정
    for val in data:
        push(val)
    # 5. 데이터 내용을 푸시
    sum_nod = 0
    while N >= 1:
        N = N // 2
        sum_nod += H[N]
    # 6. 문제 조건에 맞도록 마지막 노드의 조상노드의 합 구하기
    print(f'#{tc} {sum_nod}')

