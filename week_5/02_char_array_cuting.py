input = "abcabcdede"


# 파이썬다운 풀이
# def compress(text, tok_len):
#     words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
#     res = []
#     cur_word = words[0]
#     cur_cnt = 1
#     for a, b in zip(words, words[1:] + ['']):
#         if a == b:
#             cur_cnt += 1
#         else:
#             res.append([cur_word, cur_cnt])
#             cur_word = b
#             cur_cnt = 1
#     return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
#
#
# def solution(text):
#     return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
#
#
# a = [
#     "aabbaccc",
#     "ababcdcdababcdcd",
#     "abcabcdede",
#     "abcabcabcabcdededededede",
#     "xababcdcdababcdcd",
#
#     'aaaaaa',
# ]
#
# for x in a:
#     print(solution(x))

input = "abcabcdede"


def string_compression(string):
    str_cut_num = 1
    result = []

    while str_cut_num <= len(string):
        str_temp = ""
        cnt = 1
        str_to_list = [string[i:i + str_cut_num] for i in range(0, len(string), str_cut_num)]
        # print(str_to_list)
        for idx in range(len(str_to_list) - 1):
            # if str_cut_num == 2:
            #     print(str_temp)
            if str_to_list[idx] == str_to_list[idx+1]:
                cnt += 1
            else:
                if cnt > 1:
                    str_temp += str(cnt)
                str_temp += str_to_list[idx]
                cnt = 1

        if cnt > 1:
            str_temp += str(cnt)
        str_temp += str_to_list[-1]

        result.append(len(str_temp))
        str_cut_num += 1

    return min(result)


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))