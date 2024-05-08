# ex)
"""
tree = [0, 'a', 'b'. 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 0, 0]

def inorder(v):     # 노드번호 = 인덱스
    # 공백노드일경우
    if v > N:
        return
    inorder(v*2)
    tree[v]
    inorder(v*2+1)

"""
# 힙의 구현 삽입, 삭제


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


