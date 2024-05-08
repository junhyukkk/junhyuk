"""
num = [3,2,8,8,8]
N = len(num)

for i in range(N-1):
    for j in range(1,N):

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
        print(arr[i], arr[j], arr[k])


arr = 'ABCDE'
N = len(arr)
pick = []
def comb(k, s):
    if k == 3:
        print(pick)
    else:
        for i in range(s, N):
            pick.append(arr[i])
            comb(k+1, i+1)
            pick.pop()
comb(0, 0)
"""
num = [3, 1, 2, 4, 5, 2]
N = len(num)
ans = 0

def find_max(k):
    global ans
    val = int(''.join(map(str, num)))
    if k == N:
        if val in visit[k]:
            return
        visit[k].add[val]
        ans = max(ans, val)
    else:
        for i in range(N - 1):
            for j in range(i + 1, N):
                num[i], num[j] = num[j], num[i]
                find_max(k + 1)
                num[i], num[j] = num[j], num[i]

visit = [set() for _ in range(N + 1)]
find_max(0)
print(ans)


T = int(input())
for tc in range(1, T + 1):
    nums, swap_cnt = input().split()
    nums = list(map(int, nums))
    swap_cnt = int(swap_cnt)
    N = len(nums)
    visit = [set() for _ in range(swap_cnt + 1)]
    ans = 0
    def find_max(k):
        global ans
        val = int(''.join(map(str, nums)))

        if val in visit[k]: return
        visit[k].add(val)

        if k == swap_cnt:
            ans = max(ans, val)
        else:
            for i in range(N -  1):
                for j in range(i + 1, N):
                    nums[i], nums[j] = nums[j], nums[i]
                    # ==========================================
                    find_max(k + 1)
                    # ==========================================
                    nums[i], nums[j] = nums[j], nums[i]

    find_max(0)
    print(f'#{tc} {ans}')
