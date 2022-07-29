import sys
from itertools import combinations

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    customer_loc = []
    chicken_loc = []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                customer_loc.append([i+1, j+1])
            elif city_map[i][j] == 2:
                chicken_loc.append([i+1, j+1])

    chicken_number_of_case = list(combinations(chicken_loc, m))

    road_sum_number_of_case = []
    for case in chicken_number_of_case:
        road_sum = 0
        for customer_x, customer_y in customer_loc:
            chicken_road = sys.maxsize
            for loc_x, loc_y in case:
                chicken_road = min(chicken_road, abs(customer_x - loc_x) + abs(customer_y - loc_y))
            road_sum += chicken_road
        road_sum_number_of_case.append(road_sum)

    return min(road_sum_number_of_case)


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))