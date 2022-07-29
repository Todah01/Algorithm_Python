# 나의 풀이
in_ = [4, 3, 6, 8, 7, 5, 2, 1]


def numeric():
    cnt, stack, answer = 0, [], []
    for i in in_:
        while cnt < i:
            cnt += 1
            stack.append(cnt)
            answer.append("+")
        if stack.pop() != i:
            return "NO"
        else:
            answer.append("-")
    return '\n'.join(answer)


print(numeric())


# 튜터님 풀이
def stack_sequence(n, sequence):

    stack = []
    num = 1
    sequence_idx = 0
    result = []

    while True:
        if len(stack) == 0:
            stack.append(num)
            result.append("+")
            num += 1

        elif sequence[sequence_idx] == stack[-1]:
            stack.pop()
            result.append("-")
            sequence_idx += 1
            if sequence_idx == n:
                break

        else:
            if n < num:
                print("NO")
                break
            stack.append(num)
            result.append("+")
            num += 1

    if len(stack) == 0:
        for char in result:
            print(char)



sequence = list()

n = int(input())
for _ in range(n):
    sequence.append(int(input()))

stack_sequence(n, sequence)