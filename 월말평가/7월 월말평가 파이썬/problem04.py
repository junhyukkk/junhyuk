############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
"""
def make_answer(security_str, security_code):
    answer = ''.join(security_str[idx] for idx in security_code)
    return answer

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    answer = make_answer('kXeFSOo1spkSMsuuoAiklFeqYz', [4, 11, 17, 21, 24])
    print(answer)   # => SSAFY
"""
def make_answer(security_str, security_code):
    answer = ""
    for index in security_code:
        answer += security_str[index]
    return answer

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    answer = make_answer('kXeFSOo1spkSMsuuoAiklFeqYz', [4, 11, 17, 21, 24])
    print(answer)  # => SSAFY

