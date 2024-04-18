# 입력으로 문자열들의 리스트
# 문자열들을 리스트로 변환해서 저장
# arr = ['abcde', 'efghi']
# arr = [['a''b''c''d''e''],
#       ['e''f''g''h''i']]
# 리스트를 읽기만 하면 쪼갤 필요 없음
# 쪼갤 필요가 있는 경우만 쪼개면 됨
# arr = [list(input()) for _ in range(N)]

# 한 행에 대해 계산을 잘 수행하면
line = 'gdfgtsdlevelfasdas'
N = len(line)
M = 5 # 찾을 회문의 길이 >> 패턴매칭으로 가능
        # 길이가 5인 문자열의 가능성 전부를 조사해서 회문나오는걸 출력
def find_palindrome(line, N, M):

    for s in range(N-M+1):
        e = s + M -1
        for i in range(M//2):
            if line[s + i] != line[e - i]:  # 시작이 0이기 떄문에
                break
        else:
            return (line[s:])
        # 회문이다
    return None

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ret = None
    for line in arr:
        ret = find_palindrome(line, N, M)
        if ret:
            break
    print(ret)


"""
# 기본 구조
   for i in range(M//2):
        if line[0 + i] != line[0 + M-1-i]:  # 시작이 0이기 떄문에
            break
        else:

        # 회문이다
            break
"""

# 2차원 배열의 길이 N * N
N = 8

T = 10
for tc in range(1, T + 1):
    # 우리가 찾아야 하는 회문의 길이 M
    M = int(input())

    # 주어지는 문자로 이루어진 2차원 배열
    puzzle = [list(input()) for _ in range(N)]

    # 우리가 원하는 답 = 길이가 M인 회문의 개수
    count = 0

    # 행번호 = i, 열번호 = j
    # 모든위치 (i,j) 에서 회문을 만들어 본다.
    # (i,j) ~ (i,j + M) => 문자열 하나
    # (i,j) ~ (i + M,j) => 문자열 하나
    for i in range(N):
        for j in range(N - M + 1):
            # 가로 : 행번호 i, 열번호 j
            # (i,j) ~ (i, j+M) 으로 만든 문자열이
            # 회문인지 아닌지 검사

            # string_row = ""
            # for k in range(M):
            #    string_row += puzzle[i][j+k]

            # string_row 가 회문인지 아닌지 검사
            for k in range(M):
                if puzzle[i][j + k] != puzzle[i][j + M - k - 1]:
                    # 비교해봤는데 같지 않으면 회문이 아니다.
                    break  # 반복 종료
            else:
                # 여기로 들어오면?? 중간에 반복문이 종료되지 않았다..
                # 회문 발견!!!!
                count += 1

            # 세로 : 행번호 j, 열번호 i
            for k in range(M):
                if puzzle[j + k][i] != puzzle[j + M - k - 1][i]:
                    break
            else:
                count += 1

    print(f"#{tc} {count}")

    # # 세로
    # for j in range(N):
    #     for i in range(N - M + 1):
