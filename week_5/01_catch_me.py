from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]

    while cony_loc <= 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            cur_pos, cur_time = queue.popleft()

            new_time = cur_time + 1
            new_brown_pos = cur_pos - 1
            # 조건 추가하지 않을 시 visited 의 일정 부분에서 무한루프가 발생
            if 0 <= new_brown_pos <= 200000 and new_time not in visited[new_brown_pos]:
                visited[new_brown_pos][new_time] = True
                queue.append((new_brown_pos, new_time))

            new_brown_pos = cur_pos + 1
            if 0 <= new_brown_pos <= 200000 and new_time not in visited[new_brown_pos]:
                visited[new_brown_pos][new_time] = True
                queue.append((new_brown_pos, new_time))

            new_brown_pos = cur_pos * 2
            if 0 <= new_brown_pos <= 200000 and new_time not in visited[new_brown_pos]:
                visited[new_brown_pos][new_time] = True
                queue.append((new_brown_pos, new_time))

        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10, 3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51, 50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550, 500))