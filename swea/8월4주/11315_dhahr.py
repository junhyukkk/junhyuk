import sys
sys.stdin = open('sample_input.txt')

def check_win(arr, N):
    # 가로 방향
    for i in range(N):
        row = ''.join(arr[i]) # arr 을 문자열로
        if 'ooooo' in row:
            return True

    # 세로 방향
    for j in range(N):
        col = ''.join(arr[i][j] for i in range(N))
        if 'ooooo' in col:
            return True

    # 대각선
    for i in range(N - 4):
        for j in range(N - 4):
            diag = ''.join(arr[i + k][j + k] for k in range(5))
            if 'ooooo' in diag:
                return True

    # 반대 대각선
    for i in range(N - 4):
        for j in range(4, N):
            diag_r = ''.join(arr[i + k][j - k] for k in range(5))
            if 'ooooo' in diag_r:
                return True

    return False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    if check_win(arr, N):
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

"""
def check_win(arr, N):
    # 가로 방향 검사
    for i in range(N):
        row = ''.join(arr[i])  # 각 행을 문자열로 변환
        if 'ooooo' in row:  # 'ooooo'가 문자열에 있는지 확인
            return True  # 승리 조건을 만족하면 True

    # 세로 방향 검사
    for j in range(N):
        col = ''.join(arr[i][j] for i in range(N))  # 각 열을 문자열로 변환
        if 'ooooo' in col:
            return True

    # 대각선 검사
    for i in range(N - 4):
        for j in range(N - 4):
            diag = ''.join(arr[i + k][j + k] for k in range(5))  # 대각선 방향의 문자열을 생성
            if 'ooooo' in diag:
                return True

    # 반대 대각선 검사
    for i in range(N - 4):
        for j in range(4, N):
            diag_r = ''.join(arr[i + k][j - k] for k in range(5))  # 반대 대각선 방향의 문자열을 생성
            if 'ooooo' in diag_r:
                return True

    return False  # 어떤 방향에서도 승리하지 않으면 False를 반환



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    # 승리한 경우 'YES', 그렇지 않으면 'NO'를 출력
    if check_win(arr, N):
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
"""