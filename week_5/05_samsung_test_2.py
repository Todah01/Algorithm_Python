from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def move_until_to_wall_or_hole(row, col, diff_r, diff_c, temp_map):
    move_cnt = 0

    while temp_map[row][col] != 'O' and temp_map[row + diff_r][col + diff_c] != '#':
        row += diff_r
        col += diff_c
        move_cnt += 1

    return row, col, move_cnt


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1

    for i in range(n):
        for j in range(m):
            if game_map[i][j] == 'R':
                red_row, red_col = i, j
            elif game_map[i][j] == 'B':
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 0))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, lean_cnt = queue.popleft()
        if lean_cnt > 10:
            break

        for i in range(4):
            new_red_row, new_red_col, r_cnt = move_until_to_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            new_blue_row, new_blue_col, b_cnt = move_until_to_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[new_blue_row][new_blue_col] == 'O':
                continue
            if game_map[new_red_row][new_red_col] == 'O':
                return True
            if new_red_row == new_blue_row and new_red_col == new_blue_col:
                if r_cnt > b_cnt:
                    new_red_row -= dr[i]
                    new_red_col -= dc[i]
                elif b_cnt > r_cnt:
                    new_blue_row -= dr[i]
                    new_blue_col -= dc[i]

            if not visited[new_red_row][new_red_col][new_blue_row][new_blue_col]:
                visited[new_red_row][new_red_col][new_blue_row][new_blue_col] = True
                queue.append((new_red_row, new_red_col, new_blue_row, new_blue_col, lean_cnt+1))

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