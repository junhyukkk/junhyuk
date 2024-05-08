# in -order  = 중위?
# 예시 문제(swea)
'''
import sys
sys.stdin = open('input.txt')

def inorder(p, N):          # N >> 완전이진트리의 마지막 정점
    if p <= N:
        inorder(p*2, N)                # 왼쪽자식으로 이동
        print(tree[p], end='')      # 중위순회에서 할일 > 위치를 위 아래로 바꾸면 전위 후위 순회
        inorder(p*2+1, N)              # 오른쪽자식으로 이동

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)  # N번 노드까지 있는 완전이진트리 표현
    for _ in range(N):
        arr = list(input().split())      # arr 의 저장형태 확인 중요 print(arr) 로 확인해보자!
        tree[int(arr[0])] = arr[1]
    # 저장을 했으니 순회를한다 (중위순회문제)
    print(f'#{tc} ', end='')
    inorder(1, N)      # root = 1 (문제에서 정해준것도 있지만, 완전이진트리 이기 때문에)
    print()
'''

# 이진탐색트리 연산
# 힙 최대힙과 최소힙 >> 힙은 우선 완전이진트리
# 최대힙 : 부모>자식, 최소힙 : 자식<부모


# 문제풀기 1. (N+1)개 배열생성
#        2. last = 0 초기화

# 힙에서의 삭제
# 기본조건 : 1. 완전이진트리 유지
"""
def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heal[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1           # 루트에 옮긴 값을 자식과 비교 
    c = p * 2       # 왼쪽 자식 (비교할 자식노드 번호)
    while c <= last:    # 자식이 하나라도 있으면~
        if c+1 <= last and heap[c] < heal[c+1]  
            c += 1      # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면 비교 대상이 오른쪽 자식노드
        if heap[p] < heap[c]:    # 자식이 더 크면 최대합 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c       # 자식을 새로운 부모로
            c = p * 2   # 왼쪽 자식 번호를 계산
        else:           # 부모가 더 크면
            break       # 중단
    return tmp

"""
