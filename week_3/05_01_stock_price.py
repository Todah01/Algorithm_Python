from collections import deque


# 나의 풀이
def solution(prices):
    answer = []

    for i in range(len(prices)):
        value_cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                value_cnt += 1
            else :
                value_cnt += 1
                break
        answer.append(value_cnt)

    return answer


# prices = list(map(int, input().split()))
# print(solution(prices))

print("정답 = [2, 1, 2, 1, 0] / 현재 풀이 값 = ", solution([6, 9, 5, 7, 4]))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", solution([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", solution([1, 5, 3, 6, 7, 6, 5]))


# 튜터님 풀이
def solution(prices):
    answer = []
    prices_deque = deque(prices)

    while prices_deque:
        non_drop_cnt = 0
        cur_price = prices_deque.popleft()

        for price in prices_deque:
            if cur_price > price:
                non_drop_cnt += 1
                break
            non_drop_cnt += 1

        answer.append(non_drop_cnt)

    return answer


# prices = list(map(int, input().split()))
# print(solution(prices))

print("정답 = [2, 1, 2, 1, 0] / 현재 풀이 값 = ", solution([6, 9, 5, 7, 4]))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", solution([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", solution([1, 5, 3, 6, 7, 6, 5]))
