def check_run_triplet(player):
    for i in range(10):
        if player[i] >= 3:
            return True
        if i <= 7 and player[i] and player[i+1] and player[i+2]:
            return True
    return False

T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    player1 = [0] * 10  # 플레이어들의 카드 숫자를 저장
    player2 = [0] * 10
    result = 0          # 0은 무승부

    for i in range(0, 12, 2):  # 주어진 12장 카드 플레이어 나눠 가지도록
        player1[cards[i]] += 1
        if check_run_triplet(player1):
            result = 1
            break

        player2[cards[i + 1]] += 1
        if check_run_triplet(player2):
            result = 2
            break

    print(f"#{tc} {result}")

'''
T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    player1 = [0] * 10  # 플레이어들의 카드 숫자를 저장
    player2 = [0] * 10
    result = 0          # 0은 무승부
    for i in range(0, 12, 2):         # 주어진 12장 카드 플레이어 나눠 가지도록
        if result != 0:
            break
        player1[cards[i]] += 1
        for j in range(10):
            if player1[j] >= 3:  # 동일한 숫자가 3개 이상인 경우
                result = 1
                                # 숫자 3개가 연속인경우
            if j <= 7 and player1[j] and player1[j+1] and player1[j+2]:
                result = 1                
        if result != 0:
            break
        player2[cards[i + 1]] += 1
        for j in range(10):
            if player2[j] >= 3:
                result = 2            
            if j <= 7 and player2[j] and player2[j+1] and player2[j+2]:
                result = 2
            
    print(f"#{tc} {result}")
'''