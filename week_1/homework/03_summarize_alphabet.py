# # 문제의 번호별 조건에 대한 입력 예시와 출력
# Ex 1)
# abc 	# a1/b1/c1
#
# Ex 2-1)
# aaabbbc	# a3/b3/c1
#
# Ex 2-2)
# abbbc	# a1/b3/c1
#
# Ex 3-1)
# ahhhhz	# a1/h4/z1
#
# Ex 3-2)
# acccdeee	# a1/c3/d1/e3

input_list = ["abc", "aaabbbc", "abbbc", "ahhhhz", "acccdeee"]


# 나의 풀이
def summarize_string(input_str):
    result = []
    alphabet_occurrence_array = [0] * 26

    for char in input_str:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    for idx in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[idx] != 0:
            result.append(chr(idx + ord('a')) + str(alphabet_occurrence_array[idx]))
    return "/".join(result)


for input_str in input_list:
    print(summarize_string(input_str))


# 강사님 풀이
def summarize_string(target_string):
    # 이 부분을 채워보세요!
    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1):
        if target_string[i] == target_string[i + 1]:
            count += 1
        else:
            result_str += target_string[i] + str(count + 1) + '/'
            count = 0

    result_str += target_string[n - 1] + str(count + 1)

    return result_str


input_str = "acccdeee"

print(summarize_string(input_str))