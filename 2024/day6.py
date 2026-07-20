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
    visited_positions = {(x, y, dir[0], dir[1])}
    total_rows = len(lines)
    total_cols = len(lines[0])

    count = 0
    while 0 <= x + dir[0] < total_cols and 0 <= y - dir[1] < total_rows:
        next_x, next_y = x + dir[0], y - dir[1]
        dir_aux = change_dir(dir)
        if lines[next_y][next_x] == "#":
            dir = dir_aux
        else:
            next_x_aux, next_y_aux = x + dir_aux[0], y - dir_aux[1]
            if (next_x_aux, next_y_aux, dir_aux[0], dir_aux[1]) in visited_positions:
                count += 1
            x, y = next_x, next_y
            visited_positions.add((x, y, dir[0], dir[1]))

    return count


def run(func, arg, n):
    print(f"-> Part {n}")
    T = time.time()
    print("Result =", func(arg))
    print("Runtime =", round(time.time() - T, 4), "seconds\n")


if __name__ == "__main__":
    with open("./input/day6.txt", "r") as f:
        lines = f.readlines()
    run(part_1, lines, 1)
    run(part_2, lines, 2)
