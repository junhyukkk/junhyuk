def dfs(month, acc_cost):
    global ans
    # 기저조건
    if month > 11:
        ans = min(ans, acc_cost)
        return
    # 각 이용권 함수
    dfs(month + 1, acc_cost + (months[month]*cost_day))
    dfs(month + 1, acc_cost + cost_month)
    dfs(month + 3, acc_cost + cost_month3)
    dfs(month + 12, acc_cost + cost_year)

T = int(input())
for tc in range(1, T+1):
    # 주어진 이용권 가격들
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12개월 이용 계획
    months = list(map(int, input().split()))
    ans = 99999999999999    # 큰값

    dfs(0, 0)   # 0말고 1에서 시작
    print(f'#{tc} {ans}')