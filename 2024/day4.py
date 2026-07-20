from os import linesep
import time


def part_1(lines):
    total_rows = len(lines)
    total_cols = len(lines[0])
    target = "XMAS"
    len_target = len(target)
    total = 0

    for n_row in range(total_rows):
        for n_col in range(total_cols):
            if n_col + len_target - 1 < total_cols:
                section = lines[n_row][n_col : n_col + len_target]
                if target == section or target == section[::-1]:
                    total += 1

            if n_row + len_target - 1 < total_rows:
                section = "".join(
                    [lines[n_row + n][n_col] for n in range(0, len_target)]
                )
                if target == section or target == section[::-1]:
                    total += 1

            if (
                n_row + len_target - 1 < total_rows
                and n_col + len_target - 1 < total_cols
            ):
                section = "".join(
                    [lines[n_row + n][n_col + n] for n in range(0, len_target)]
                )
                if target == section or target == section[::-1]:
                    total += 1

            if n_row + len_target - 1 < total_rows and n_col - len_target + 1 >= 0:
                section = "".join(
                    [lines[n_row + n][n_col - n] for n in range(0, len_target)]
                )
                if target == section or target == section[::-1]:
                    total += 1

    return total


def part_1_v2(lines):
    total_rows = len(lines)
    total_cols = len(lines[0])
    target = "XMAS"
    len_target = len(target)
    total_matches = 0

    # right, down, diag right, diag left
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for r in range(total_rows):
        for c in range(total_cols):
            for dr, dc in directions:
                end_r = r + dr * (len_target - 1)
                end_c = c + dc * (len_target - 1)

                if 0 <= end_r < total_rows and 0 <= end_c < total_cols:
                    word = "".join(
                        lines[r + (i * dr)][c + (i * dc)] for i in range(len_target)
                    )

                    if word == target or word == target[::-1]:
                        total_matches += 1

    return total_matches


def part_2(lines):
    total_rows = len(lines)
    total_cols = len(lines[0])
    total = 0

    for n_row in range(1, total_rows - 1):
        for n_col in range(1, total_cols - 1):
            if lines[n_row][n_col] == "A":
                a = lines[n_row - 1][n_col - 1] + lines[n_row + 1][n_col + 1]
                b = lines[n_row + 1][n_col - 1] + lines[n_row - 1][n_col + 1]
                if a in {"MS", "SM"} and b in {"MS", "SM"}:
                    total += 1

    return total


def run(func, arg, n):
    print(f"-> Part {n}")
    T = time.time()
    print("Result =", func(arg))
    print("Runtime =", round(time.time() - T, 4), "seconds\n")


if __name__ == "__main__":
    with open("./input/day4.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    run(part_1_v2, lines, 1)
    run(part_2, lines, 2)
