def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y, length, used, k):
    global max_length

    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우로 이동하는 데 사용할 x 좌표 변화
    dy = [0, 0, -1, 1]  # 상, 하, 좌, 우로 이동하는 데 사용할 y 좌표 변화

    max_length = max(max_length, length)  # 가장 긴 등산로의 길이를 갱신합니다.

    for d in range(4):  # 상, 하, 좌, 우 4방향에 대해서 반복합니다.
        nx, ny = x + dx[d], y + dy[d]  # 다음 위치 좌표를 계산합니다.

        if is_valid(nx, ny, n) and not used[nx][ny]:  # 다음 위치가 유효하고, 사용되지 않았다면:
            if map_data[nx][ny] < map_data[x][y]:  # 다음 위치의 높이가 현재 위치보다 낮다면:
                used[nx][ny] = True  # 다음 위치를 사용 중으로 표시합니다.
                dfs(nx, ny, length + 1, used, k)  # 다음 위치로 이동하며 길이를 1 증가시킵니다.
                used[nx][ny] = False  # DFS를 빠져나온 후 다음 위치를 다시 사용 중이지 않도록 표시를 해제합니다.
            elif k > 0 and map_data[nx][ny] - k < map_data[x][y]:  # 공사 가능 깊이(k)가 남아있고, 다음 위치를 깎아서 이동할 수 있다면:
                original_height = map_data[nx][ny]  # 원래 높이를 기억해둡니다.
                map_data[nx][ny] = map_data[x][y] - 1  # 다음 위치를 현재 위치보다 1만큼 낮춥니다.
                used[nx][ny] = True  # 다음 위치를 사용 중으로 표시합니다.
                dfs(nx, ny, length + 1, used, 0)  # 다음 위치로 이동하며 길이를 1 증가시키고 공사 가능 깊이를 소모합니다.
                map_data[nx][ny] = original_height  # DFS를 빠져나온 후 다음 위치의 높이를 원래대로 복원합니다.
                used[nx][ny] = False  # 다음 위치를 다시 사용 중이지 않도록 표시를 해제합니다.


T = int(input())  # 테스트 케이스 개수

for t in range(1, T + 1):
    n, k = map(int, input().split())  # 지도 크기와 공사 가능 깊이
    map_data = [list(map(int, input().split())) for _ in range(n)]  # 지도 데이터

    max_height = max(max(row) for row in map_data)  # 지도에서 가장 높은 봉우리의 높이를 찾습니다.
    max_length = 0  # 가장 긴 등산로의 길이를 초기화합니다.

    for i in range(n):
        for j in range(n):
            if map_data[i][j] == max_height:  # 가장 높은 봉우리에서 시작합니다.
                used = [[False] * n for _ in range(n)]  # 사용 여부를 표시하는 2D 배열을 초기화합니다.
                used[i][j] = True  # 현재 위치를 사용 중으로 표시합니다.
                dfs(i, j, 1, used, k)  # DFS를 시작하여 등산로를 탐색합니다.

    print(f"#{t} {max_length}")  # 결과를 출력합니다.
