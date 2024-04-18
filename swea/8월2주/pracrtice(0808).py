# 고지식한 패턴 알고리즘
# 패턴 매칭 : text 에서 pattern이 존재하는 모든 위치를 찾는 문제
p = "CA"
t = "ATATTEWSDTSTCASAAEACADZCASZ"
n, m = len(t), len(p)
i = j = 0
"""
while i < n and j < m:      # j 가 m 이 되면 반복이 종료

    if t[i] == p[j]:
        i, j = i + 1, j + 1
    else:
        i = i - j + 1
        j = 0
if j == m:
    print('찾았다.', t[i-j: ])
    j = 0
"""
   # 같지 않은 경우
while i < n:
    if t[i] != p[j]:
        i = i - j
        j = -1
   # 다음 매칭의 시작위치로 i,j 값을 설정     
    i, j = i + 1, j + 1
    if j == m:
        print(i-m, t[i-j: ])
        j = 0
