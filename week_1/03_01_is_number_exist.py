input = [3, 5, 6, 1, 2, 4]


def is_number_exist_1(number, array):
    for element in array:  # array 의 길이 만큼 아래 연산이 실행
        if number == element:  # 비교 연산 1번 실행
            return True


def is_number_exist_2(number, array):
    if number in array:
        return True
    else:
        return False


result = is_number_exist_1(3, input)
result = is_number_exist_2(3, input)
print(result)
