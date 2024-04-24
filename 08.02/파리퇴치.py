T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N-M+1):      # N-M+1의 범위값을 설정한 이유는
        for j in range(N-M+1):  # NXN 배열에서 파리채의 범위 MxM이 가질수 있는 최대 범위이기 때문에
            s = 0
            for k in range(i, i+M):         # 파리채의 범위만큼 i값에 추가
                for l in range(j, j+M):     # 파리채의 범위만큼 j값에 추가
                    s += arr[k][l]          # 파리채의 인덱스 k,l 만큼 s값 더하기
            if max_sum < s:
                max_sum = s
    print(f'#{tc} {max_sum}')