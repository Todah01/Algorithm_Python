input = "011110"


# 나의 풀이
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    cnt_0 = 0
    cnt_1 = 0
    idx = 0

    while True:
        if idx < len(string) and string[idx] == '0':
            # print("idx_0 : ", idx)
            while idx < len(string) and string[idx] == '0':
                idx += 1
            cnt_0 += 1
        elif idx < len(string) and string[idx] == '1':
            # print("idx_1 : ", idx)
            while idx < len(string) and string[idx] == '1':
                idx += 1
            cnt_1 += 1

        if idx > (len(string) - 1):
            break

    return min(cnt_0, cnt_1)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)


# 강사님 풀이
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
