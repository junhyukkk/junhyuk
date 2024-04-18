import sys
sys.stdin = open('sample_input(화물도크).txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = []               # 주어진 작업시간을 넣어서 정리시킬 빈 리스트
    for test in range(N):
        s, e = map(int, input().split())
        time.append([s, e])
#   print(time) = [(4, 14), (8, 18), (17, 20), (20, 23), (23, 24)]
    # 종료 시간 순으로 정렬
    time.sort(key=lambda x: x[1])   # 주어진 시간들을 오름차순으로 정리하는데
                                    # 종료시간을 key값으로 정리
    work = time[0][1]      # 첫번째

    ans = 1                # 한 트럭은 무조건 작업을 함 = 1
    for i in range(1, N):  # 이후 작업할 수 있는 화물차 계산
        if work <= time[i][0]:  # 이전 종료시간 이후에 작업하는 화물차
            ans += 1
            work = time[i][1]   # 이전 화물차의 종료시간을 저장
    print(time)
    print(f'#{tc} {ans}')

