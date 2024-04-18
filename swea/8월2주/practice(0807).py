"""
mystr = 'algorithm'
# # 1. 파이썬의 내장된 기능
print(mystr[::-1])
#
# # 2. 새로운 공간에 저장, 뒤에서 읽어서 붙이기
rev_str = ''
for i in range(len(mystr) - 1, -1, -1):
    rev_str += mystr[i]
print(rev_str)
"""

# 3. 교환을 통해서 뒤집기
arr = input()
N = len(arr)
ans = 1
for i in range(N // 2):
    if arr[i] != arr[N - 1 - i]:
        ans = 0
        break
