# 교재 List02 연습문제 1
"""
조건 :
5x5 2ck 배열에 무작위로 25개의 숫자로 초기화 한후
25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
예를 들어 아래 그림에서 7값의 이웃한 값은 2,6,8,12 이며 차의 절대값의 합은 12이다.
- |2-7|+|6-7|+|8-7|+|12-7| = 12

문제 : 25개의 요소에 대해서 모두 조사하여 총합을 구하시오
벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.
"""
T = int(input)
N = int(input())
for tc in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [0,1,0,-1]
    dj = [-1,0,1,0]
    max_sum = 0
    for i in range(N):
        for j in range(N):
            s = 0
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]

            if max_sum < s:
                max_sum = s
    print(f'#{tc} {max_sum}')


# 파리퇴치
"""
   for i in range(r_s, r_e + 1):
            for j in range(c_s, c_e + 1):
                arr[i][j] += 1
여기서 i,j 의 위치가 정해지고 
w, h 를 통해서 같은 부분을 나타낼 수 있음

"""
