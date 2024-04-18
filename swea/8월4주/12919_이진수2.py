T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    binary = []  # 이진수를 저장할 리스트

    # N이 0보다 크고 1미만인 동안 반복
    while N > 0:
        # 이진수의 다음 자릿수를 구하기 위해 N에 2를 곱해줌
        N *= 2
        # N이 1보다 크거나 같으면 현재 자릿수는 1, 그렇지 않으면 0
        if N >= 1:
            binary.append("1")
            N -= 1
        else:
            binary.append("0")
    result = "".join(binary)  # binary 리스트에 저장한 이진수 표현

    # 13자리 이상인 경우 "overflow" 출력
    if len(result) >= 13:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc} {result}")