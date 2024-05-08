# 16진수를 표현하는 방법 >> 0x 를 붙이면 됨

# 16진수를 2진수로 변환하는 함수
def hex_to_binary(hex_digit):
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    return hex_to_bin[hex_digit]


# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스 처리
for t in range(1, T + 1):
    N, hex_num = input().split()

    # 16진수를 2진수로 변환
    binary_num = ''.join([hex_to_binary(hex_digit) for hex_digit in hex_num])

    # 결과 출력
    print(f'#{t} {binary_num}')
