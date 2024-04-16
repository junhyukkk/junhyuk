"""
9
7 4 2 0 0 6 0 7 0


N = int(input())
arr = list(map(int, input().split()))

print(N)
print(arr)
"""
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x)-ord('0')
    return i

s = '123'
a = atoi(s)
print(a+1)