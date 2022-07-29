import math

input = 20


def find_prime_list_under_number(number):
    prime_list = []
    # 소수를 판별여부를 담을 배열을 선언
    check_prime_list = [0] * (number+1)

    # number+1까지 소수판별배열에 담기
    for i in range(2, number+1):
        check_prime_list[i] = i

    # number+1까지 모든 수를 판별하기보다는 에라토네스의 채를 이용해서 시간복잡도를 줄이는 방법을 선택
    for i in range(2, int(math.sqrt(number))+1):
        if check_prime_list[i] == 0:
            continue
        # number 의 제곱근이하 수의 배수를 활용하여 소수여부를 판별
        for j in range(i*i, number+1, i):
            check_prime_list[j] = 0

    # 소수가 아닌 수들만 뽑아서 prime_list 에 입력
    for i in range(2, number+1):
        if check_prime_list[i] != 0:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
