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