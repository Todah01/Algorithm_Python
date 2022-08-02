k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def get_dir(direction):
    if direction % 2 == 0:
        return direction + 1
    else:
        return direction - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    horse_map = [[[] for _ in range(n)] for _ in range(n)]

    for horse_idx in range(horse_count):
        cur_r, cur_c, cur_d = horse_location_and_directions[horse_idx]
        horse_map[cur_r][cur_c].append(horse_idx)

    turn = 1

    while turn <= 1000:
        for i in range(horse_count):
            cur_r, cur_c, cur_d = horse_location_and_directions[i]
            new_r = cur_r + dr[cur_d]
            new_c = cur_c + dc[cur_d]

            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_dir(cur_d)

                horse_location_and_directions[i][2] = new_d
                new_r = cur_r + dr[new_d]
                new_c = cur_c + dc[new_d]

                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            moving_arr = []
            for idx in range(len(horse_map[cur_r][cur_c])):
                if i == horse_map[cur_r][cur_c][idx]:
                    moving_arr = horse_map[cur_r][cur_c][idx:]
                    horse_map[cur_r][cur_c] = horse_map[cur_r][cur_c][:idx]
                    break

            if game_map[new_r][new_c] == 1:
                moving_arr = reversed(moving_arr)

            for value in moving_arr:
                horse_map[new_r][new_c].append(value)
                horse_location_and_directions[value][0], horse_location_and_directions[value][1] = new_r, new_c

            if len(horse_map[new_r][new_c]) >= 4:
                return turn

        turn += 1

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))