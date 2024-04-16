T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1): # i 구간의 마지막 인덱스
        for j in range(i):
            if arr[j] > arr[j+1]:       # 인접한 두 숫자가 뒤에 값보다 앞에 값이 크다면
                arr[j], arr[j+1] = arr[j+1], arr[j]      # 앞에있는 숫자와 뒤에있는 숫자의 위치를 바꾸는것
# 처음 값 # [7, 55, 12, 42, 78] 로 결과가 나옴
# 반복하면서 큰 숫자가 뒤로가도록 이 결과를 계속해서 반복해서 해야함
# 언제까지 ? 2개 숫자가 남을떄까지  >> 그래서 N-1 번 반복 하는 것
    print(f'#{tc}', *arr)   # for 문으로 쓰는것도 가능해야함
# 결과물 외우지 말고 문제로 코드를 수집하지 말것,