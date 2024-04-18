"""
- 격자판
==> 이차원 배열
>> 각 격자찬: 0~9 숫자

현재 지점 + 6번 이동하면서 숫자를 붙임
>> 이동= 네방향, 델타사용
격자칸을 다시 가 됨  = visited 안써도 됨

0시작 : 0102001
> 숫자가 0으로 시작 가능
> 문자열로 해결하면 편할것 같다

요구하는 조건:
    서로 다른 일곱 자리 수들의 개수
    문제를 보면 가지치기가 불가능한 경우임
    일곱자리 다 붙여봐야 결과가 나옴
- 서로 다른 일곱자리 수들의 개수
--> 중복을 제거할 방법?
--> set 자료구조 사용!

정리 : 1. 재귀사용, 2. 숫자를 붙이고, 7자리일 때. 3. set사용
"""
# 트정 위치를 기점으로 상하좌우 문자를 붙여야 하므로
# 파라미터로 좌표값을 받음
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x, y, num):
    if len(num) == 7:
        # 추가적인 작업
        result.add(num)
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
    # 갈 수 없는 위치면 continue
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4: continue
    # 갈 수 있는 위치면 다음 위치로
        dfs(nx, ny, num + maps[nx][ny])

T = int(input())
for tc in range(1, T + 1):
    # 서로 다른 수를 합친다 >> 문자열이 더 좋다(활용해보자)
    maps = [input().split() for _ in range(4)]
    # 7자리 수를 중복 제거하여 저장
    result = set()

    # 시작 지점이 정해져 있지 않음 >> 모두 보아야함
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])
    print(f'#{tc} {len(result)}')