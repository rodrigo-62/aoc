import time


def rec(result, elements, idx, acc):
    if idx == len(elements):
        return result == acc

    if acc > result:
        return False

    aux_add = acc + elements[idx]
    if rec(result, elements, idx + 1, aux_add):
        return True

    aux_mult = acc * elements[idx]
    if rec(result, elements, idx + 1, aux_mult):
        return True

    return False


def rec2(result, elements, idx, acc):
    if idx == len(elements):
        return result == acc

    if acc > result:
        return False

    aux_concat = int(f"{acc}{elements[idx]}")
    if rec2(result, elements, idx + 1, aux_concat):
        return True

    aux_add = acc + elements[idx]
    if rec2(result, elements, idx + 1, aux_add):
        return True

    aux_mult = acc * elements[idx]
    if rec2(result, elements, idx + 1, aux_mult):
        return True

    return False


def part_1(lines, func):
    total = 0
    for line in lines:
        result, elements = line.strip().split(":")
        elements = [int(el) for el in elements.strip().split()]
        result = int(result)
        if func(result, elements, 1, elements[0]):
            total += result

    return total


def run(func, arg, arg2, n):
    print(f"-> Part {n}")
    T = time.time()
    print("Result =", func(arg, arg2))
    print("Runtime =", round(time.time() - T, 4), "seconds\n")


if __name__ == "__main__":
    with open("./input/day7.txt", "r") as f:
        lines = f.readlines()
    run(part_1, lines, rec, 1)
    run(part_1, lines, rec2, 2)
