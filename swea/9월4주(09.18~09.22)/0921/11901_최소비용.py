import sys
sys.stdin = open('sample_input (11901).txt')

import heapq

def dijksrta(i,j):
    pq = []
    heapq.heappush(pq,(0,i,j))
    distance[i][j] = 0
    while pq:
        dist, x, y = heapq.heappop(pq)
        if distance[x][y] < dist: continue
        for di,dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni,nj = x+di ,y+dj
            if ni<0 or nj<0 or ni>N-1 or nj> N-1: continue
            if arr[ni][nj] > arr[x][y]:
                sum_fuel = dist + 1 + (arr[ni][nj] - arr[x][y])
            else:
                sum_fuel = dist + 1
            if distance[ni][nj] <= sum_fuel: continue
            distance[ni][nj] = sum_fuel
            heapq.heappush(pq, (sum_fuel, ni,nj))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[int(1e9)]* N for _ in range(N)]
    dijksrta(0,0)
    print(f'#{tc} {distance[N-1][N-1]}')


# di = [1, 0, -1, 0]
# dj = [0, 1, 0, -1]
# def dijksrta(i,j):
#     pq = []
#     heapq.heappush(pq,(0,i,j))
#     distance[i][j] = 0
#
#     while pq:
#         dist, x, y = heapq.heappop(pq)
#         if distance[x][y] < dist:
#             continue
#         for k in range(4):
#             ni,nj = x+di[k],y+dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 if arr[ni][nj] > arr[x][y]:
#                     sum_fuel = dist + 1 + (arr[nj][nj] - arr[x][y])
#                 else:
#                     sum_fuel = dist + 1
#                 if distance[nj][nj] <= sum_fuel:
#                     continue
#                 distance[ni][nj] = sum_fuel
#                 heapq.heappush(pq, (sum_fuel, ni,nj))
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     distance = [[int(1e9)]* N for _ in range(N)]
#
#     dijksrta(0,0)
#     print(f'#{tc} {distance[N-1][N-1]}')
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 최소 = 매우 큰값 설정
#     min_sum = [[999999999] * N for _ in range(N)]
#     # 출발 위치 초기화
#     min_sum[0][0] = arr[0][0]
#     # 4방향
#     di = [1, 0, -1, 0]
#     dj = [0, 1, 0, -1]
#
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):
#                 ni, nj = i + di[k], j + dj[k]
#                 if 0 <= ni < N and 0 <= nj < N:
#                     high = 0        # 높이차이 값
#                     if arr[ni][nj] > arr[i][j]:
#                         high = arr[ni][nj] - arr[i][j]
#                     sum_high = min_sum[i][j] + 1 + high  # 움직일때마다 1 + 높이차이값
#                     min_sum[ni][nj] = min(min_sum[ni][nj], sum_high)
#                     high = 0
#     result = min_sum[N - 1][N - 1]
#     print(f"#{tc} {result}")
# #


