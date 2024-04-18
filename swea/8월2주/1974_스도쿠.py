T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

# append, list, count 등 풀이방법 다양

    ans = 1
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:
                break
# 함수식
def sudoku(arr):
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:
                return 0

ans = sudoku(arr)

# 풀이순서체크
# 행 우선
def check_sudoku(arr):
    for r in range(9):
        row = set()
        for c in range(9):
            row.add(arr[r][c])
        if len(row) != 9:
            return 0
# 열 우선
# 사각형

# 배열

