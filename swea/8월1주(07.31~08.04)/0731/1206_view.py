T = 10 # 테스트 케이스 10개
 
for tc in range(1, T + 1):
    #첫번째 줄에는 건물의 개수 N이 입력된다.
    # 파이썬의 input() 함수는 입력으로 들어온 모두를 문자열로 취급한다.
    # 그러므로 숫자로 세기 위해 int 로 변환이 필요
    N = int(input())
    # 각 건물들의 높이가 담긴 리스트(배열)
    # input() 함수는 한줄씩 읽는다
    # split() 함수는 문자열을 기본적으로 "" 기준으로 자른다
    # "3 5 7" >> ["3", "5", "7"]
    # 각 문자열을 숫자로 바꾸는 과정
    # map() 함수는 리스트 같은 컨테이너의 각 원소에 우리가 원하는 함수를 적용시켜준다
    # ex) map(int(["3","5","7"]))의 경우 int 가 3,5,7 전부에 적용
    # 하지만 그 결과가 리스트가 아니기 때문에 우리는 리스트로 변경하는과정
    #  >> list(map(int,input().split()))
    buildings = list(map(int,input().split()))
 
    # 조망권을 가지는 총 세대의 개수
    count = 0
    # 반복문을 통해서 각 빌딩에서 조망권이 확보된 세대의 개수를 센다
    # 중첩 반복문을 통해서 확인한다.
    # for 문이 두 번 들어가는 경우 반복의 순서를 잘 정해야한다
    # 어떤것을 먼저 반복을 할 것인지!
    # 중첩 반복문 >> 밖의 반복문 / 안의 반복문 (안의 반복문이 한바퀴 돌고 난후 밖의 반복문이 움직임)
    # 이 문제의 경우 빌딩의 개수를 밖의 반복문
    # 빌딩의 높이를 안의 반복문 >>> 빌딩의 높이를 받은후 다음 빌딩으로 넘어가기 때문
    for i in range(2, N-2):  # i번째 빌딩에서 가로 길이 양쪽 두칸에는 빌딩을 지을수 없기 때문
    # 빌딩의 높이를 구하는 방법 : buildings 리스트를 변환했기 때문에 
    # 현재 i번째 빌딩의 높이 height
        height = buildings[i]
        for j in range(height, -1, -1):
            # 높이를 바닥에서부터 말고 위에서 부터 재는 방법으로 풀어주심 , -1씩 감소
            # 현재 i번째 빌딩의 높이 j
            # j층에서 양쪽 2칸 확인한 다음 조망권이 있으면 count 를 1씩 증가
 
            # 왼쪽, 오른쪽 검사
            # 왼쪽 -1칸 빌딩의 높이, 왼쪽 -2 칸 빌딩의 높이, 오른쪽 + 1칸 빌딩의 높이, 오른쪽 +2칸 빌딩의 높이
            # 현재 층수 j 가 왼쪽 , 오른쪽의 빌딩보다 높으면 ok
            # 둘다 ok면 조망권 ok
            # 현재 빌딩의 번호는 i 왼쪽은 i-1, i-2
            # 오른쪽의 경우 i+1, i+2
            if j > buildings[i-1] and j > buildings[i-2] and j > buildings[i+1] and j > buildings[i+2]:
                count += 1
            # 조망권이 없는 경우
            else:
                # 위에서부터 조망권을 세다가 조망권이 확보되지 않는 순간부터는 안세도 된다.
                # 다음 건물로 넘어감
                break
    print(f'#{tc} {count}')
'''
for tc in range(1, 11):
    # 하나의 테스트 케이스
    N = int(input())   # 자료수
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(2, N - 3 + 1):
        # i가 기준
        # max_val = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        # --------------------------------------------------------------
        max_val = arr[i - 2]
        if max_val < arr[i - 1]:
            max_val = arr[i - 1]
        if max_val < arr[i + 1]:
            max_val = arr[i + 1]
        if max_val < arr[i + 2]:
            max_val = arr[i + 2]

        if arr[i] > max_val:
            ans += arr[i] - max_val
    print(ans)


#========================================================
for tc in range(1, 11):
    # 하나의 테스트 케이스
    N = int(input())   # 자료수
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(2, N - 3 + 1):
        max_val = arr[i - 2]
        for val in [arr[i - 1], arr[i + 1], arr[i + 2]]:
            if max_val < val:
                max_val = val

        # --------------------------------------------------------------
        if arr[i] > max_val:
            ans += arr[i] - max_val
    print(ans)
'''