T = int(input())

for tc in range(1, T + 1):
    N, num = input().split()

    binary = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    result = ""

    for i in num:
        result += binary[i]

    print(f"#{tc} {result}")

"""
T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
 
    ans = ''
    for a in M:
        val = int(a, 16)
        if '0' <= a <= '9':
            B = ord(a) - ord('0')
        else:
            B = 10 + ord(a) - ord('A')
 
        ans += '1' if B & 8 else '0'
        ans += '1' if B & 4 else '0'
        ans += '1' if B & 2 else '0'
        ans += '1' if B & 1 else '0'
 
    print(f'#{tc} {ans}')

"""