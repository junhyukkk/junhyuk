T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    S = [0] * (len(arr)+1)
    top = -1
    for i in arr:
        if i == '.':
            print(f'#{tc} {S[top]}')
            break
        if i not in '+-/*':
            top += 1
            S[top] = int(i)
        else:
            if top < 1:
                print(f'#{tc} error')
                break
            else:
                a = S[top]
                top -= 1
                b = S[top]
                top -= 1
                if i == '+':
                    top += 1
                    S[top] = b + a
                elif i == '-':
                    top += 1
                    S[top] = b - a 
                elif i == '*':
                    top += 1
                    S[top] = b * a
                elif i == '/':
                    if a == 0:  
                        print(f'#{tc} error')
                        break
                    top += 1
                    S[top] = b // a