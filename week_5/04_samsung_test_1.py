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


def get_new_d(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_cnt = 1
    visited = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        visited[r][c].append(i)

    while turn_cnt <= 1000:
        for horse_idx in range(horse_count):
            r, c, d = horse_location_and_directions[horse_idx]
            new_r = r + dr[d]
            new_c = c + dc[d]

            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_new_d(d)

                horse_location_and_directions[horse_idx][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            moving_arr = []
            for i in range(len(visited[r][c])):
                visit_idx = visited[r][c][i]
                if horse_idx == visit_idx:
                    moving_arr = visited[r][c][i:]
                    visited[r][c] = visited[r][c][:i]
                    break

            if game_map[new_r][new_c] == 1:
                moving_arr = reversed(moving_arr)

            for idx in moving_arr:
                visited[new_r][new_c].append(idx)
                horse_location_and_directions[idx][0], horse_location_and_directions[idx][1] = new_r, new_c

            if len(visited[new_r][new_c]) >= 4:
                return turn_cnt

        turn_cnt += 1

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