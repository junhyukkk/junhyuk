T = 10
for tc in range(1, T+1):
    N = int(input())
    building_h = list(map(int, input().split()))

    cnt = 0
    # 조망권 세대의 수
    for i in range(2, N - 2):
    # 가로 양끝 2개는 건물이 없음 >> 안구해도 됨
        for j in range(building_h[i], -1, -1):
    # i번째 건물의 높이에서 1씩 빼가면서
            if j > building_h[i - 1] and j > building_h[i - 2] and j > building_h[i + 1] and j > building_h[i + 2]:
                cnt += 1
    # 양 옆 두 건물의 높이보다 j번째 건물의 높이가 높다면 +1
            else:
                break
    # j가 1씩 줄어들며 순회하므로 조망권이 없어진 세대나올때까지 +1, and break
    print(f'#{tc} {cnt}')