from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def move_until_wall_or_hole(x, y, bump_x, bump_y, game_map):
    move_cnt = 0
    while game_map[x + bump_x][y + bump_y] != "#" and game_map[x][y] != "O":
        x += bump_x
        y += bump_y
        move_cnt += 1

    return x, y, move_cnt


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1

    for x in range(n):
        for y in range(m):
            if game_map[x][y] == "R":
                red_row, red_col = x, y
            elif game_map[x][y] == "B":
                blue_row, blue_col = x, y

    visited[red_row][red_col][blue_row][blue_col] = True
    queue.append((red_row, red_col, blue_row, blue_col, 0))

    while queue:
        red_row, red_col, blue_row, blue_col, try_cnt = queue.popleft()

        if try_cnt > 10:
            break

        for i in range(4):
            next_red_row, next_red_col, red_cnt = move_until_wall_or_hole(red_row, red_col, dx[i], dy[i], game_map)
            next_blue_row, next_blue_col, blue_cnt = move_until_wall_or_hole(blue_row, blue_col, dx[i], dy[i], game_map)

            if game_map[next_blue_row][next_blue_col] == "O":
                continue
            if game_map[next_red_row][next_red_col] == "O":
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if red_cnt > blue_cnt:
                    next_red_row -= dx[i]
                    next_red_col -= dy[i]
                else:
                    next_blue_row -= dx[i]
                    next_blue_col -= dy[i]

            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_cnt + 1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))