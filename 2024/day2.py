import time


def is_safe(report):
    dir = report[1] - report[0] > 0
    for n in range(0, len(report) - 1):
        diff = report[n + 1] - report[n]
        if diff == 0 or (diff > 0) != dir or abs(diff) >= 4:
            return 0
    return 1


def part_1(lines):
    safe_count = 0
    for line in lines:
        report = [int(a) for a in line.split()]
        safe_count += is_safe(report)
    return safe_count


def is_safe_2(report, cnt):
    if len(report) <= 1:
        return 0

    dir = report[1] - report[0] > 0

    for n in range(0, len(report) - 1):
        diff = report[n + 1] - report[n]
        if diff == 0 or (diff > 0) != dir or abs(diff) >= 4:
            if cnt == 0:
                return 0
            a = report[:n] + report[n + 1 :]
            b = report[: n + 1] + report[n + 2 :]
            return 1 if is_safe_2(a, cnt - 1) or is_safe_2(b, cnt - 1) else 0

    return 1


def part_2(lines):
    return sum(
        is_safe_2([int(a) for a in line.split()], 1)
        or is_safe_2([int(a) for a in line.split()][1:], 0)
        for line in lines
    )


def run(func, arg, n):
    print(f"-> Part {n}")
    T = time.time()
    print("Result =", func(arg))
    print("Runtime =", round(time.time() - T, 4), "seconds")


if __name__ == "__main__":
    with open("./input/day2.txt", "r") as f:
        lines = f.readlines()
    run(part_1, lines, 1)
    run(part_2, lines, 2)
