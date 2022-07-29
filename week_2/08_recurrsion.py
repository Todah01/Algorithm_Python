# def count_down(number):
#     if number == 0: return
#     print(number)          # number를 출력하고
#     count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!
#
#
# count_down(60)


def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)


# print(factorial(5))


input = "abccba"


# 나의 풀이
def is_palindrome(string):
    # print(string)
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

    # elif len(string) == 2:
    #     if string[0] == string[-1]:
    #         return True
    # elif len(string) > 2:
    #     if string[0] == string[-1]:
    #         return is_palindrome(string[1:-1])
    #     else:
    #         return False


print(is_palindrome(input))


# 튜터님 풀이
def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome(input))