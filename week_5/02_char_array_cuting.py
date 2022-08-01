input = "abcabcdede"


# 파이썬다운 풀이
# def compress(text, tok_len):
#     words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
#     res = []
#     cur_word = words[0
#     ]
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

input = "abcabcabcabcdededededede"


def string_compression(string):
    # 모든 경우의 수를 탐색해야 한다.
    n = len(string)
    split_size = 1
    compress_arr = []

    while split_size <= n//2:
        split_string = [string[i:i + split_size] for i in range(0, n, split_size)]

        temp = ""
        cnt = 1
        for idx in range(len(split_string)-1):
            if split_string[idx] == split_string[idx+1]:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt)
                temp += split_string[idx]
                cnt = 1

        if cnt > 1:
            temp += str(cnt)
        temp += split_string[-1]

        compress_arr.append(len(temp))

        split_size += 1

    return min(compress_arr)


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))