import time


def part_1(lines):
    right, left = [], []
    for line in lines:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    sum = 0
    for i in range(0, len(left)):
        sum += abs(left[i] - right[i])

    return sum


def part_1_v2(lines):
    left = sorted(int(line.split()[0]) for line in lines)
    right = sorted(int(line.split()[1]) for line in lines)
    return sum(abs(a - b) for a, b in zip(left, right))


def part_2(lines):
    left = [int(line.split()[0]) for line in lines]
    right = [int(line.split()[1]) for line in lines]

    freq = {}
    for r in right:
        freq[r] = freq.get(r, 0) + 1

    return sum(n * freq.get(n, 0) for n in left)


def run(func, arg, n):
    print(f"-> Part {n}")
    T = time.time()
    print("Result =", func(arg))
    print("Runtime =", round(time.time() - T, 4), "seconds\n")


if __name__ == "__main__":
    with open("./input/day1.txt", "r") as f:
        lines = f.readlines()
    run(part_1_v2, lines, 1)
    run(part_2, lines, 2)
