############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def get_row_col_maxsum(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.

def get_row_col_maxsum(matrix):
    max_sum = 0
    max_sum_type = ""

    # 각 행(row)의 합 계산
    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum += element
        if row_sum > max_sum:
            max_sum = row_sum
            max_sum_type = "row"

    # 각 열(column)의 합 계산
    num_rows = 0
    num_cols = 0
    for row in matrix:
        num_rows += 1
        for element in row:
            if num_rows == 1:
                num_cols += 1

    for j in range(num_cols):
        col_sum = 0
        for i in range(num_rows):
            col_sum += matrix[i][j]
        if col_sum > max_sum:
            max_sum = col_sum
            max_sum_type = "col"

    return (max_sum_type, max_sum)

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)
