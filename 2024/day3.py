import time
import re


def part_1(lines):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum(
        int(match.group(1)) * int(match.group(2))
        for line in lines
        for match in re.finditer(pattern, line)
    )


def part_2(lines):
    pattern = r"(?:mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    enabled = True
    sum = 0

    for line in lines:
        for match in re.finditer(pattern, line):
            if match.group() == "do()":
                enabled = True
            elif match.group() == "don't()":
                enabled = False
            elif enabled:
                sum += int(match.group(1)) * int(match.group(2))

    return sum


def run(func, arg, n):
    print(f"-> Part {n}")
    T = time.time()
    print("Result =", func(arg))
    print("Runtime =", round(time.time() - T, 4), "seconds\n")


if __name__ == "__main__":
    with open("./input/day3.txt", "r") as f:
        lines = f.readlines()
    run(part_1, lines, 1)
    run(part_2, lines, 2)
