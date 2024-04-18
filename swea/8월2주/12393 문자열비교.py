T = int(input())

for tc in range(1, T + 1):
    S1 = input()		# 주어진 S1 과 S2 문자열 넣기
    S2 = input()

    if S1 in S2:		# S1 이 S2 문자열 안에 있는지 확인
        result = 1		# 문자열을 쪼개지 않았기 때문에 문자열 그대로 S2에 적용해 찾기
    else:
        result = 0		# S1 문자열이 있으면 1 없으면 0

    print(f"#{tc} {result}")
