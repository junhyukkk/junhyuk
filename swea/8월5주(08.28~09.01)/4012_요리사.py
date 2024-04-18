import sys
sys.stdin = open('sample_input(4012).txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_difference = 1000000
    for i in range(1, (1 << N) // 2):
        A = []
        B = []
        for j in range(N):
            if i & (1 << j):
                A.append(j)
            else:
                B.append(j)
        if len(A) == N // 2:
            list_A = 0
            for r in A:
                for c in A:
                    list_A += arr[r][c]
            list_B = 0
            for r in B:
                for c in B:
                    list_B += arr[r][c]

            difference = abs(list_A - list_B)
            min_difference = min(min_difference, difference)

    print(f"#{tc} {min_difference}")



"""
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 식재료 수 입력
    synergy = [list(map(int, input().split())) for _ in range(N)]  # 시너지 정보 입력
    
    min_difference = float('inf')
    
    for i in range(1, 1 << N):
        A_ingredients = []
        B_ingredients = []
        
        for j in range(N):
            if (i & (1 << j)) > 0:
                A_ingredients.append(j)
            else:
                B_ingredients.append(j)
        
        taste_A = 0
        taste_B = 0
        
        for a in A_ingredients:
            for b in A_ingredients:
                taste_A += synergy[a][b]
        
        for a in B_ingredients:
            for b in B_ingredients:
                taste_B += synergy[a][b]
        
        difference = abs(taste_A - taste_B)
        min_difference = min(min_difference, difference)
    
    print(f"#{test_case} {min_difference}")

"""