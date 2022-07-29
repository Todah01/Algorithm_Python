input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if alphabet.isalpha():
            alphabet_occurrence_array[ord(alphabet) - ord('a')] += 1

    not_repeat_char_array = []

    for idx in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[idx] == 1:
            not_repeat_char_array.append(chr(idx + ord('a')))

    for i in string:
        if i in not_repeat_char_array: return i

    return '_'


result = find_not_repeating_character(input)
print(result)
