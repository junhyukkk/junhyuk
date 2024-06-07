############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calculate_sum_number(word):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calculate_sum_number('ab123cd45ef6')) # => 21
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.



def calculate_sum_number(word):
    total = 0
    for char in word:
        if char.isdigit():  # char가 숫자인지 검사
            total += int(char)
    return total

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    print(calculate_sum_number('ab123cd45ef6'))  # => 21


'''
주어진 문제는 주어진 문자열 word에서 숫자들만 추출하여 이를 모두 더하는 함수 calculate_sum_number를 구현하는 것입니다.

함수를 작성하기 위해서는 다음과 같은 과정을 수행해야 합니다:

word를 순회하며 각 문자가 숫자인지 검사합니다.
숫자인 경우 해당 숫자를 추출하여 더합니다.
isdigit() 함수는 문자열에서 각 문자가 숫자인지 아닌지를 판별하는 메서드입니다. 
문자가 숫자라면 int(char)를 통해 해당 숫자로 변환하여 누적하여 더하게 됩니다. 
이렇게 하면 문자열에서 숫자만 추출하여 이들을 모두 더한 결과로 21이 출력됩니다.

'''