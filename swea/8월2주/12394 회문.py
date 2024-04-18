# 10 x 10 문자열 배열을 생성하고
# 가로 회문
# 1. 행 우선순회로 행 리스트의 인덱스의 뒤집은 것도 똑같은지 확인
# 2. 행의 절반을 비교해서 앞 뒤가 같게 나오는지 확인
# 세로 회문
# 1. 가로 회문한 것을 열 우선순회로만 바꿔서 세로회문에 그대로 적용?

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = ""

    for i in range(N):
        for j in range(N - M + 1):
            if arr[i][j:j + M] == arr[i][j:j + M][::-1]:
                result = ''.join(arr[i][j:j + M])
                break

        for j in range(N):
            for i in range(N - M + 1):
                result2 = [arr[i][j] for i in range(i, i + M)]
                if result2 == result2[::-1]:
                    result = ''.join(result2)
                    break

    print(f'#{tc} {result}')



