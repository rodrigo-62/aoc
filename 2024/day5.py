import time
from collections import defaultdict
from functools import cmp_to_key


def check_update(update, y_to_x):
    page_map = {}
    for idx, page in enumerate(update):
        page_map[page] = idx

    for i in range(0, len(update)):
        if update[i] in y_to_x:
            before_vals = y_to_x[update[i]]
            for x in before_vals:
                if x in page_map and page_map[x] > i:
                    return False
    return True


def parse(lines):
    idx = lines.index("\n")
    rules, updates = lines[:idx], lines[idx + 1 :]

    y_to_x = defaultdict(list)
    for rule in rules:
        x, y = rule.strip().split("|")
        y_to_x[y].append(x)

    return updates, y_to_x


def part_1(lines):
    updates, y_to_x = parse(lines)
    result = 0

    for update in updates:
        update = update.strip().split(",")
        if check_update(update, y_to_x):
            mid_val = update[len(update) // 2]
            result += int(mid_val)

    return result


def fix_update(update, y_to_x):
    for i in range(0, len(update) - 1):
        for j in range(0, len(update) - 1 - i):
            x = update[j]
            y = update[j + 1]
            if y in y_to_x and x in y_to_x[y]:
                update[j], update[j + 1] = update[j + 1], update[j]

    return int(update[len(update) // 2])


def part_2(lines):
    updates, y_to_x = parse(lines)
    result = 0
    for update in updates:
        update = update.strip().split(",")
        if not check_update(update, y_to_x):
            result += fix_update(update, y_to_x)
    return result


def part_2_v2(lines):
    updates, y_to_x = parse(lines)
    result = 0
    for update in updates:
        update = update.strip().split(",")
        if not check_update(update, y_to_x):

            def rules(x, y):
                if y in y_to_x and x in y_to_x[y]:
                    return 1
                return -1

            sorted_update = sorted(update, key=cmp_to_key(rules))
            result += int(sorted_update[len(sorted_update) // 2])
    return result


def run(func, arg, n):
    print(f"-> Part {n}")
    T = time.time()
    print("Result =", func(arg))
    print("Runtime =", round(time.time() - T, 4), "seconds\n")


if __name__ == "__main__":
    with open("./input/day5.txt", "r") as f:
        lines = f.readlines()
    run(part_1, lines, 1)
    run(part_2_v2, lines, 2)
