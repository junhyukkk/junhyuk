import sys
sys.stdin = open('input(최대상금).txt')

T = int(input())
for tc in range(1, T+1):
    card, M = input().split()       # 문자열 리스트로 받아야할 card 와 정수(숫자)로 받아야할 M
    numbers = list(map(int, card))  # card 를 정수형 리스트로 만들어줌
    M = int(M)                      # M을 정수로 받아줌
    N = len(numbers)                # range에 넣기 위해 리스트의 길이를 구함
    ans = 0
    # 숫자 조합을 저장, 만들어진 숫자 조합 저장(set 중복제거)
    visit = [set() for _ in range(M+1)]

    def find_max(k):
        global ans
        val = int(''.join(map(str, numbers)))   # 문자열로 저장된 numbers 를 정수로 변환해 val로 저장
        if val in visit[k]:     # val 이 visit 리스트에서 k번째 인덱스에 방문했다면 함수를 종료(중복 제거용)
            return
        visit[k].add(val)       # visit[k]에 val 을 추가(방문기록)
        if k == M:              # M번까지 숫자 조합 후 현재 조합인 val과 이전 최대값인 ans 중 최대값 비교
            ans = max(ans, val)

        else:
            for i in range(N - 1):          # numbers 리스트에서 k번째에서 가능한 모든 순열을 생성(리스트의 인덱스 범위)
                for j in range(i + 1, N):   # i번째 숫자 다음위치부터 반복하며 i번째 숫자와 나머지 숫자를 바궈가며 가능한 순열 생성
                    numbers[i], numbers[j] = numbers[j], numbers[i]     # i와 j를 바꾸며 숫자 조합을 변경
                    find_max(k + 1)                                     # 재귀 호출을 통해 모든 가능한 순열을 생성 검사
                    numbers[i], numbers[j] = numbers[j], numbers[i]     # 숫자의 위치를 복구하여 이전상태로 복구
                                                                        # 현재순열이 다음 순열에 영향을 주지 않기위함
    find_max(0)
    print(f'#{tc} {ans}')

