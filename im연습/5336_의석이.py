import sys
sys.stdin = open('sample_input(의석).txt')

T = int(input())
for t in range(1, T + 1):
    words = [input() for _ in range(5)]
    # 각 열을 읽어서 결과 문자열에 추가
    result = ''
    for c in range(15):  # 최대길이 15로 주어짐
        for r in range(5):
            if c < len(words[r]):  # c(열)이 r(행)의 길이보다 작을 때, 만약 r값보다 긴 c일때에는 ''에넣을 수가 없으니까
                result += words[r][c]

    print(f"#{t} {result}")