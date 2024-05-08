# 탐욕과 완전탐색비교 이해

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    work_time = []
    for _ in range(N):
        s, e = map(int, input().split())
        work_time.append((s, e))
#   print(work_time) = [(4, 14), (8, 18), (17, 20), (20, 23), (23, 24)]
    work_time.sort(key=lambda x:x[1])

    now_car = work_time[0][1]
#   print(work_car) = 14
    work_cnt = 1
    for i in range(1, N):
        if now_car <= work_time[i][0]:
            work_cnt += 1
            now_car = work_time[1][0]
