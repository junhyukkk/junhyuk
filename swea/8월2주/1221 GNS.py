numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for tc in range(1, T + 1):
    _, N = input().split()
    N = int(N)  # N 은 숫자로 바꾼다.

    # 정렬해야할 문자열
    text = input().split()

    # 카운트 배열
    count = [0] * 10

    # 정렬해야할 문자열이 등장할 때마다 개수 세어주기
    # print(text)

    # count['ZRO']
    # 딕셔너리사용
    # count = {"ZRO" : 0 , "ONE" : 0, .... }

    # 배열

    for number in text:
        # text 안의 문자열 하나 가져왔는데 numbers 안에 있는 문자열이 맞다면 개수 증가
        for i in range(10):
            if number == numbers[i]:
                count[i] += 1

    # 정답 출력
    answer = ""  # 빈 문자열을 만들어 놓고 반복문을 돌면서 결과로 출력해야하는 문자열 조립
    # 우리가 출력해야하는 문자열의 종류는 10개
    for i in range(10):
        answer = answer + (numbers[i]+ " ") * count[i]

    # 출력은 마지막에 한번만..
    print(f"#{tc} {answer}")
