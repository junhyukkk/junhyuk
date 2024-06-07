############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def find_one(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
            


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    sample_matrix = [
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]
    ]
    print(find_one(sample_matrix))  # => (1, 1)
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.


def find_one(matrix):
    for row_idx, row in enumerate(matrix):
        for col_idx, element in enumerate(row):
            if element == 1:
                return (row_idx, col_idx)

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    sample_matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(find_one(sample_matrix))  # => (1, 1)
"""
주어진 행렬 matrix는 리스트 안에 리스트로 구성되어 있으며, 각 요소는 0 또는 1입니다. 
숫자 1이 처음 발견되는 위치(인덱스)를 찾아서 반환하는 함수 find_one을 작성합니다.

여러 가지 방법이 있지만, 내장 함수를 사용하지 않고 루프를 이용하여 해당 요소를 찾는 방법으로 구현할 수 있습니다.
위 코드에서 find_one 함수는 이중 루프를 사용하여 matrix를 순회하며 각 요소를 검사합니다. 
요소가 1인 경우 해당 위치(인덱스)인 (row_idx, col_idx)를 반환합니다. 
이렇게 하면 주어진 sample_matrix에서 숫자 1의 위치(인덱스)인 (1, 1)을 반환합니다.
"""