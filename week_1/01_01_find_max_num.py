input = [3, 5, 6, 1, 2, 4]


def find_max_num_1(array):
    max_num = array[0]
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
    return max_num


def find_max_num_2(array):
    for num in array:
        for comp_num in array:
            if num < comp_num:
                break
        else:
            return num


result_1 = find_max_num_1(input)
result_2 = find_max_num_2(input)
print("첫번째 방법 :", result_1)
print("두번째 방법 :", result_2)
