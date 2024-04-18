T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 해당 숫자가 나왔는지 체크하는 리스트
    check_lst = [0] * (N*N+1)
    # 주변에 더 큰 숫자가 있는지 검사하여 check_lst에 표시
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
                    check_lst[arr[i][j]] = 1
    result = 0
    cnt = 0
    start = 0
    for i in range(N*N,0,-1):
        if check_lst[i]:
            cnt += 1  # 연속된 숫자 개수 증가
            if result < cnt:
                result = cnt
                start = i
            elif result == cnt:
                start = i
        else:
            cnt = 0

    print(f'#{t} {start} {result + 1}')

"""

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# T: 테스트 케이스
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 해당 숫자가 나왔는지 체크하는 리스트 초기화
    check_lst = [0] * (N ** 2 + 1)

    # 주변에 더 큰 숫자가 있는지 검사하여 check_lst에 표시
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
                    check_lst[arr[i][j]] = 1

    result = 0
    cnt = 0
    num = 0
    temp = 0
    for i in range(len(check_lst)):
        if check_lst[i]:
            # 이전에 숫자가 나오지 않았거나, 이어진 숫자가 끊어졌을 때
            if i - 1 < 0 or check_lst[i - 1] == 0:
                temp = i  # 시작 숫자 업데이트
            cnt += 1  # 연속된 숫자 개수 증가
        else:
            if result < cnt:
                result = cnt  # 최대 연속 개수 업데이트
                num = temp  # 최대 연속 숫자 업데이트
            cnt = 0  # 연속된 숫자 개수 초기화

    print(f'#{t} {num} {result + 1}')  # 결과 출력

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 해당 숫자가 나왔는지 체크하는 리스트
    check_lst = [0] * (N*N+1)
    # 주변에 더 큰 숫자가 있는지 검사하여 check_lst에 표시
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
                    check_lst[arr[i][j]] = 1
    max_cnt = 0
    cnt = 0
    max_start = 0
    for k in range(N*N,0,-1):
        if check_lst[k]:
            cnt += 1  # 연속된 숫자 개수 증가
            if max_cnt < cnt:
                max_cnt = cnt
                max_start = k
            elif max_cnt == cnt:
                max_start = k
        else:
            cnt = 0

    print(f'#{t} {max_start} {max_cnt+1}')
"""

