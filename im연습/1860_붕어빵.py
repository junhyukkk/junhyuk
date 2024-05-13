T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # 사람 수(N), 붕어빵 제작 시간(M 초당 K개)
    arrival_times = list(map(int, input().split()))  # 손님 도착 시간 리스트
    # 손님 도착 시간을 오름차순 정렬
    arrival_times.sort()
    # 붕어빵 제작 시간을 고려하여 각 손님에게 붕어빵을 제공할 수 있는지 확인
    possible = True
    for i in range(N):
        # 현재 손님이 도착한 시간을 고려하여 몇 개의 붕어빵을 만들 수 있는지 계산
        available_buns = (arrival_times[i] // M) * K
        # 현재 손님에게 붕어빵을 주지 못하는 경우 Impossible 출력하고 종료
        if available_buns < i + 1:
            possible = False
            break
    if possible:
        print(f"#{tc} Possible")
    else:
        print(f"#{tc} Impossible")