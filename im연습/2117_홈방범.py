T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_houses = 0  # 최대 서비스 제공 집 수
    max_profit = 0  # 최대 이익
    # 서비스 영역 크기 K를 1부터 N+1까지 증가시키며 검사
    for K in range(1, N + 2):
        for r in range(N):
            for c in range(N):
                total_houses = 0  # 현재 서비스 영역 내에 포함되는 집의 수
                # 현재 영역 내의 모든 좌표 검사
                for i in range(r - (K - 1), r + K):  # 중심좌표로부터 범위 설정 중요
                    for j in range(c - (K - 1), c + K):
                        if 0 <= i < N and 0 <= j < N:
                            if abs(r - i) + abs(c - j) <= K - 1:  # 마름모 모양 영역
                                total_houses += arr[i][j]  # 영역에서 집있을때 마다 +1
                cost = K * K + (K - 1) * (K - 1)  # 주어진 운영비용 공식
                profit = total_houses * M - cost  # 현재 영역에서 얻는 이익
                if profit >= 0 and total_houses > max_houses:
                    max_houses = total_houses
        max_profit = max(max_profit, max_houses)
    print(f"#{tc} {max_profit}")
