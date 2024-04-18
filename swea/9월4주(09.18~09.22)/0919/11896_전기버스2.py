import sys
sys.stdin = open('sample_input (11896).txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    cnt = 0
    goal = N-1
    while goal:
        for i in range(N):
            if i+arr[i+1] >= goal:
                goal = i
                break
        cnt += 1
    print(f'#{tc} {cnt-1}')


# 표현방법 1
# T = int(input())
# for tc in range(1, T+1):
#     arr = list(map(int, input().split()))
#     N = arr[0]
#     cnt = 0
#     goal = N
#     while goal > 1:
#         for i in range(1, N+1):
#             if i+arr[i] >= goal:
#                 goal = i
#                 break
#         cnt += 1
#     print(f'#{tc} {cnt-1}')

# 표현방법 2
# T = int(input())
# for tc in range(1, T+1):
#     N, *arr = list(map(int, input().split()))
#     cnt = 0
#     goal = N-1
#     while goal > 0:
#         for i in range(N):
#             if i+arr[i] >= goal:
#                 goal = i
#                 break
#         cnt += 1
#     print(f'#{tc} {cnt-1}')
