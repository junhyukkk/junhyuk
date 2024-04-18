T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    Q = [0] * (M+1)     # Q 의 크기를 만들어주고
    front = rear = -1   # front와 rear -1로 위치 설정

    for i in range(M+1):    # i 가 M을 순회하면서
        if i < N:           # i 가 주어진 N보다 작다면
            rear += 1       # rear를 +1 해주고
            Q[rear] = arr[i]    # Q[rear] 의 인덱스에 arr[i] 를 할당
        else:               # i가 N보다 큰 경우에
            rear += 1       # rear 와 front가 같이 늘어나고
            front += 1      # Q[front]값을 Q[rear] 할당
            Q[rear] = Q[front]
    print(f'#{tc} {Q[front]}')  # front 를 프린트하면 인덱스가 나오고 Q[front] 해야 해당 인덱스 값이 나옴
