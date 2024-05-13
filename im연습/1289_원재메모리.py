import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    memory = input()
    base = '0'
    cnt = 0
    for i in memory:
        if base != i:
            cnt += 1
            base = i
    print(memory)
    print(f'#{tc} {cnt}')


