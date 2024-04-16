
import sys
sys.stdin = open('input.txt')   # input.txt 불러오기

T = int(input())    # TC(테스트 케이스)개수

for tc in range(1, T+1):    # 테스트케이스가 1~10까지 반복을 진행하는데
    ans = 0     # 첫 ans 에는 0이 할당
    N = int(input())    #N 에는 정수형 input이 할당
    arr = list(map(int, input().split()))   # 정수형 인풋을 각각 나눠서 리스트화
    max_val = min_val = arr[0]      # 리스트 arr 첫 값을 최대 and 최소 값으로 설정
    for val in arr:     # val 변수를 arr 리스트에서 반복할때
        if max_val < val:   # val 값이 max_val 값보다 크다면
            max_val = val    # val 변수값은 max_val 변수값과 같고
        if min_val > val:   # val 값이 min_val 값보다 작다면
            min_val = val   # val 변수값은 min_val 변수 값과 같다.
# print(arr) >> arr리스트 제대로 들어와 있는지 확인
    print(f'#{tc} {max_val - min_val}')     # #{테스트케이스}에서 {최댓값-최솟값} 출력



# 테스트 케이스가 주어지고
# T = int(input())
# for tc in range(1, T+1):    # 테스트케이스가 1~T까지 반복을 진행하는데
#    ans = 0     # 첫 ans 에는 0이 할당
#    N = int(input())    #N 에는 정수형 input이 할당
#    arr = list(map(int, input().split()))
# >>  복사 붙여넣기 하지말고 타이핑 치기(기본사항)

