import sys
sys.stdin = open('sample_input(컨테이너).txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 각 리스트 역오름차순 정렬
    container.sort(reverse=True)
    truck.sort(reverse=True)
    max_sum = 0
    used = [0] * N      # 옮겨진 컨테이너 다시 더하지 않기위한 리스트생성
    for i in range(M):
        for j in range(N):
            if used[j] == 0 and truck[i] >= container[j]:
                max_sum += container[j]
                used[j] = 1     # 옮긴 컨테이너의 인덱스 j = 1 로 바꿔줌
                break

    print(f'#{tc} {max_sum}')



