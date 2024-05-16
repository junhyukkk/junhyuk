T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

# 튕기는 거리 1,2,..,N까지
# 0번 인덱스 부터 거리를 증가시키면서 arr 에서 값을 읽어와서 누적
    ans = 0
    for step in range(1,N+1):
        for i in range(0, N, step):
            ans += arr[i]
    if ans < 0:
        ans = 0
    print(f'#{tc} {ans}')