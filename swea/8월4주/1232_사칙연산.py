def evaluate(node):
    # 만약 현재 노드가 정수라면 그 값을 반환
    if node[0] == 'N':
        return int(node[1])

    # 현재 노드가 연산자라면 왼쪽과 오른쪽 서브트리를 계산한 후 연산을 수행
    left = evaluate(tree[node[2]])
    right = evaluate(tree[node[3]])

    if node[1] == '+':
        return left + right
    elif node[1] == '-':
        return left - right
    elif node[1] == '*':
        return left * right
    elif node[1] == '/':
        return left / right

for t in range(1, 11):
    N = int(input())
    tree = {}  # 이진 트리를 딕셔너리로 표현 (노드 번호를 키로, 정보를 값으로 저장)

    for _ in range(N):
        node_info = input().split()
        node_num = int(node_info[0])

        if len(node_info) == 2:
            tree[node_num] = ('N', int(node_info[1]))  # 정수인 노드 저장
        else:
            operator = node_info[1]
            left_child = int(node_info[2])
            right_child = int(node_info[3])
            tree[node_num] = ('O', operator, left_child, right_child)  # 연산자인 노드 저장

    result = int(evaluate(tree[1]))
    print(f'#{t} {result}')
