import time


def find_guard(lines, target):
    for n_row in range(len(lines)):
        try:
            n_col = lines[n_row].index(target)
            return n_col, n_row
        except Exception:
            pass
    return 0, 0


def change_dir(dir):
    aux = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
    return aux[dir]


def part_1(lines):
    x, y = find_guard(lines, "^")
    visited_positions = {(x, y)}
    dir = (0, 1)
    total_rows = len(lines)
    total_cols = len(lines[0])

    while 0 <= x + dir[0] < total_cols and 0 <= y - dir[1] < total_rows:
        next_x, next_y = x + dir[0], y - dir[1]
        if lines[next_y][next_x] == "#":
            dir = change_dir(dir)
        else:
            x, y = next_x, next_y
            visited_positions.add((x, y))

    return len(visited_positions)


def part_2(lines):
    x, y = find_guard(lines, "^")
    dir = (0, 1)
    visited_states = {(x, y, dir[0], dir[1])}
    visited_positions = {(x, y)}
    total_rows = len(lines)
    total_cols = len(lines[0])

    def check_for_loop(sx, sy, sdir, visited, obx, oby):
        while True:
            if (sx, sy, sdir[0], sdir[1]) in visited:
                return True
            visited.add((sx, sy, sdir[0], sdir[1]))

            next_x, next_y = sx + sdir[0], sy - sdir[1]
            if not (0 <= next_x < total_cols and 0 <= next_y < total_rows):
                return False

            if lines[next_y][next_x] == "#" or (next_x == obx and next_y == oby):
                sdir = change_dir(sdir)
            else:
                sx, sy = next_x, next_y

    obstacle_positions = set()

    while True:
        next_x, next_y = x + dir[0], y - dir[1]
        if not (0 <= next_x < total_cols and 0 <= next_y < total_rows):
            break

        if lines[next_y][next_x] == "#":
            dir = change_dir(dir)
            visited_states.add((x, y, dir[0], dir[1]))
        else:
            if (next_x, next_y) not in visited_positions:
                dir_aux = change_dir(dir)
                if check_for_loop(x, y, dir_aux, visited_states.copy(), next_x, next_y):
                    obstacle_positions.add((next_x, next_y))

            x, y = next_x, next_y
            visited_states.add((x, y, dir[0], dir[1]))
            visited_positions.add((x, y))

    return len(obstacle_positions)


def run(func, arg, n):
    print(f"-> Part {n}", flush=True)
    T = time.time()
    res = func(arg)
    print("Result =", res)
    print("Runtime =", round(time.time() - T, 4), "seconds\n")


if __name__ == "__main__":
    with open("./input/day6.txt", "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    run(part_1, lines, 1)
    run(part_2, lines, 2)
