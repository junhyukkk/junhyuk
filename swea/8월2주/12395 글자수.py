# 글자수 세기
T = int(input())

for tc in range(1, T + 1):
    S1 = input()
    S2 = input()

    # 알파벳의 개수만큼의 길이를 가진 배열 준비
    alpha_count = [0] * 26

    # alpha_count = { "A" : 0 ,..... }

    # S1 안에 들어있는 알파벳의 종류를 확인, (중복 확인)
    S1_set = set(list(S1))  # 중복 제거

    # S2 안에 S1에 포함되어 있는 알파벳이 있나, 있다면 몇개 있고, 그중에 최대값은 얼마인지 구하기

    # S2에서 한글자씩 떼어내서 S1_set에 포함되어 있는지 확인 하고 포함되어 있다면 개수 1씩 증가
    for c in S2:
        # S2에서 떼어온 글자 c가 S1안에 있다면
        if c in S1_set:
            # 개수 증가
            alpha_count[ord(c) - 65] += 1

    # S2안에 있는 모든 알파벳에 대해 검사가 끝나면 그중에 최댓값 구하기
    max_count = 0
    for i in range(26):
        if alpha_count[i] > max_count:
            max_count = alpha_count[i]

    print(f"#{tc} {max_count}")
'''
    str1_list = list(input())
    str2_list = list(input())
    num_dict = {}
    for ch in str2_list:
        num_dict[ch] = num_dict.get(ch, 0) + 1
        
    # max_value = max(num_dict.values())
    max_value = 0
    for ch in str1_list:
        if max_value < num_dict.get(ch,0):
            max_value = num_dict.get(ch, 0)
'''
"""
T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    max_V = 0

    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1

        if max_V < cnt:
            max_V = cnt

    print(f'#{tc} {max_V}')
# 여기서 줄여서 같은 방법
for ch1 in str1:
        cnt = 0
        for ch2 in str2:
            if ch1 == ch2:
                cnt += 1

        if max_V < cnt:
            max_V = cnt

"""
