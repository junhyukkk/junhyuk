# 원형큐로 풀기

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    cheese = list(map(int,input().split()))
    Q = [0] * 100       # Q를 화덕으로 사용 Q를 넣고

    while M < 1:        # 남은 피자의 개수가 0이 될때까지
        rear = front = 0
        for i in range(1, N+1):        # N만큼 피자를 화덕에 넣은 후
            rear += 1
            Q[rear] = cheese[i]























'''
T = int(input())  # 테스트 케이스 개수를 입력받음

for t in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕의 크기 N과 피자 개수 M을 입력받음
    cheese = list(map(int, input().split()))  # 피자에 뿌려진 치즈 양을 입력받음

    # 초기에 화덕에 넣을 피자를 큐에 추가
    oven = [(i, cheese[i]) for i in range(N)]
    idx = N

    while len(oven) > 1:  # 피자가 하나만 남을 때까지 반복
        num, cheese_left = oven.pop(0)  # 화덕의 맨 앞에 있는 피자를 꺼냄
        cheese_left //= 2  # 치즈 양을 반으로 줄임

        if cheese_left > 0:  # 치즈가 남아있는 경우 다시 화덕에 넣음
            oven.append((num, cheese_left))
        else:
            if idx < M:  # 새로운 피자가 남아있는 경우 화덕에 넣음
                oven.append((idx, cheese[idx]))
                idx += 1

    result = oven[0][0] + 1  # 남은 피자의 번호를 구함
    print(f"#{t} {result}")  # 결과 출력
'''