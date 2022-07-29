from collections import deque
s = "(())()"


# 나의 풀이 (오답! 테스트 케이스 추가)
def is_correct_parenthesis(string):
    answer = True
    left_bracket_cnt = 0
    right_bracket_cnt = 0

    for i in string:
        if i == "(":
            left_bracket_cnt += 1
        else:
            right_bracket_cnt += 1

    if left_bracket_cnt != right_bracket_cnt:
        answer = False

    return answer


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!


# 나의 풀이 (큐)
def is_correct_parenthesis(string):
    answer = True
    bracket_deque = deque()

    for char in string:
        if char == "(":
            bracket_deque.append(char)
        elif char == ")":
            if not bracket_deque:
                answer = False
                return answer
            bracket_deque.popleft()

    if bracket_deque:
        answer = False
    else:
        answer = True

    return answer


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))


# 튜터님 풀이 (스택)
def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)  # 여기 아무런 값이 들어가도 상관없습니다! ( 가 들어가있는지 여부만 저장해둔 거니까요
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))