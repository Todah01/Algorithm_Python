numbers = [1, 1, 1, 1, 1]
target_number = 3
target_cnt = 0


# 나의 풀이
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, array_sum, index):
    if index == len(array):
        if array_sum == target:
            global target_cnt
            target_cnt += 1
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, array_sum + array[index], index + 1)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, array_sum - array[index], index + 1)


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)  # 5를 반환해야 합니다!
print(target_cnt)


numbers = [2, 3, 1]
target_number = 0
result = []  # 모든 경우의 수를 담기 위한 배열


# 튜터님 풀이
def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(array):  # 탈출조건!
        all_ways.append(current_sum)  # 마지막 인덱스에 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index], all_ways)
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index], all_ways)


get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result)
print(len([value for value in result if value == target_number]))
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
# 모든 경우의 수가 출력됩니다!
# [6, 4, 0, -2, 2, 0, -4, -6]
