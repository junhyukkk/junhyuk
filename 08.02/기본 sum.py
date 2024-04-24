'''
행 우선순회
열 우선순회
양 대각선 의 합
순서로 구해서
빈 리스트에 최댓값들의 모임을 넣어놓고
리스트 내에서 최댓값만 출력
'''

T = int(input())
for tc in range(1,T+1):
    N = 100
    arr = [list(map(int,input().split())) for _ in range(100)]