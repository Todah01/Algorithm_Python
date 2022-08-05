import itertools, sys

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
    consumer, chicken = [], []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                consumer.append([i, j])
            elif city_map[i][j] == 2:
                chicken.append([i, j])

    chicken_combination = list(itertools.combinations(chicken, m))

    road_length = sys.maxsize
    for number in chicken_combination:
        min_length_to_all = 0
        for home_r, home_c in consumer:
            min_length_to_chicken = sys.maxsize
            for chicken_r, chicken_c in number:
                min_length_to_chicken = min(min_length_to_chicken, abs(home_r - chicken_r) + abs(home_c - chicken_c))
            min_length_to_all += min_length_to_chicken
        road_length = min(road_length, min_length_to_all)

    return road_length


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