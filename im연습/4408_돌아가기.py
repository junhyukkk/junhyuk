import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [0] * 401        # 최대 400개의 방 cnt가 올라갈 수 있도록

    for _ in range(N):      # N명의 학생을 순회하면서
        start, end = map(int, input().split())
        if start <= end:    # 현재방의 번호가 들어가야할 방의 번호보다 작을때
            for i in range(start, end + 1):     # 방마다 +1
                room[i] += 1
        else:
            for i in range(end, start + 1):
                room[i] += 1

    max_count = max(room)

    print(f'#{tc} {max_count}')

"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    roomnum = [0] * 401
    maxnum = 0
    for n in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        if not a % 2:
            a -= 1
        if b % 2:
            b += 1
        for i in range(a, b+1):
            roomnum[i] += 1
            if maxnum < roomnum[i]:
                maxnum = roomnum[i]
    print(f'#{tc} {maxnum}')
"""
