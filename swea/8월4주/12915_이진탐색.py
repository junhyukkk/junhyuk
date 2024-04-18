import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    num = 1

    def inorder(v):
        global num
        if v > N:
            return
        inorder(v * 2)      # 왼쪽자식
        tree[v] = num       # 중위순회
        num += 1
        inorder(v * 2 + 1)  # 오른쪽 자식


    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N // 2]}')

