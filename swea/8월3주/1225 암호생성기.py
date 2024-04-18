# 8개의 숫자를 입력받음
# 첫 번째 숫자부터 1씩 감소시키면서 맨 뒤로 이동시킴
# 5 감소시켰을 경우 1사이클 종료
# 만약 숫자가 감소할 때 0보다 작아지는경우 그 숫자는 0으로 만들고
# 맨 뒤로 보낸 후 코드 종료
# 그때의 8가지 숫자 출력

for T in range(1,11):
    tc = int(input())
    arr = list(map(int, input().split()))
    Q = [0] * 100
    while True:
        rear = front = -1
        for i in range(8):      # i가 arr의 길이만큼 순회하면서
            rear += 1           # rear +1을 하고
            Q[rear] = arr[i]    # Q[rear] 자리에 arr[i]를 할당
# Q = [9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551]
# 할당된 Q의 첫 인덱스 부터 1씩 감소시키면서 맨 뒤로 이동
        for j in range(1, 6):    # j의 1사이클 5까지 돌면서 뺄 것이고
            rear += 1            # Q의 rear는 인덱스 8, front는 0 기준으로
            front += 1           # Q[rear]는 Q[front]에서 j를 뺀값을 할당
            Q[rear] = Q[front] - j
            if Q[rear] <= 0:       # Q[rear] 값이 0보다 작거나 같을때
                Q[rear] = 0         # 0을 할당하고 중지
                break
        arr = Q[front+1:rear+1]     # arr의 범위는 Q의 front ~ rear 인데
        if arr[-1] == 0:            # +1을 해준 이유는 인덱스 이기 때문에
            break                   # arr[-1] == 0 일때 브레이크를 넣어준 이유는
                                    # 넣지않으면 Q[rear] 가 전부 0이 될때까지 진행돼서
    print(f'#{tc}', *arr)



