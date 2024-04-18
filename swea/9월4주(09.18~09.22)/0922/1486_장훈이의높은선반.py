
def recur(level, acc_height):
    global ans
    # 가지치기 >> 현재까지 탑이 선반 높이를 넘어간다면
    # 앞으로는 더 볼 필요없음
    if acc_height >= B:
        ans = min(ans, acc_height)
        return
    # 기저조건
    if level == N:
        return
    # 해당 점원을 탑에 쓸 경우
    recur(level + 1, acc_height + arr[level])
    # 안쓸경우
    recur(level + 1, acc_height)

    # 다음 재귀 함수 호출

    # 돌아왔을 때

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    arr = list(map(int, input().split()))
    # 1.백트래킹 사용 2.차이의 최소를 구할 예정
    ans = int(1e9) # 큰 숫자를 저장
    recur(0, 0)
    print(f'#{tc} {ans-B}')
