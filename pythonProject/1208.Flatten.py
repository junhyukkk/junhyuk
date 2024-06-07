T = int(input())
for tc in range(1, T+1):
    dump = int(input())
    height = list(map(int,input().split()))

N = len(height)
max_idx = 0
min_idx = 0
for i in range(1, N+1):
    if height[max_idx] < height[i]:
        max_idx = i

for i in range(1, N+1):
    if height[min_idx] > height[i]:
        min_idx = i


print(f'#{tc} {max_idx}-{min_idx}')



# 1. i = 0, idx[i]에서 부터 [i+1]로 갈때 i보다 i+1이 높다면 다음 상자로 넘어가고
# 2. 낮다면 [i]와 [i+1]의 높이가 같아지게 만든다
# 3. 같아지면 다음 상자로 넘어가서 1.번과 2번을 N번 반복한다.
# 단, 가로길이는 100으로 i가 range(101)까지 갔을때 N의 횟수가 남아있다면, 반대로 [i-1]과 비교하여 평탄화 한다.
# 4. N번의 반복이 끝났을 떄 높이를 비교해서 가장높은박스와 낮은 박스의 차이를 반환한다.

# 1. 가로 인덱스 상자 높이 최대값과 최소값을 구한 후 dump 한 번, 이걸 계속해서 반복?
# 2. dump 횟수를 다
