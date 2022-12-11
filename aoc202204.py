from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 4


def parse(puzzle_input):
    pairs = []
    for line in puzzle_input.split("\n"):
        e1, e2 = line.split(",")
        pairs.append([e1.split("-"), e2.split("-")])
    return pairs


def part1(pairs):
    f_deps = 0
    for p in pairs:
        s1 = set(range(int(p[0][0]), int(p[0][1]) + 1))
        s2 = set(range(int(p[1][0]), int(p[1][1]) + 1))
        if s1.issubset(s2):
            f_deps += 1
            continue
        if s2.issubset(s1):
            f_deps += 1
            continue
    return f_deps


def part2(pairs):
    p_deps = 0
    for p in pairs:
        s1 = set(range(int(p[0][0]), int(p[0][1]) + 1))
        s2 = set(range(int(p[1][0]), int(p[1][1]) + 1))
        if len(s1.intersection(s2)) > 0:
            p_deps += 1
            continue
        if len(s2.intersection(s1)) > 0:
            p_deps += 1
            continue
    return p_deps


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    print(f"Sample data:\n{data[:10]}")

    parsed_data = parse(data)
    print(f"Sample parsed data:\n{parsed_data[:10]}")

    answer1 = part1(parsed_data)
    print(answer1)
    submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(parsed_data)
    print(answer2)
    submit(answer2, part="b", year=YEAR, day=DAY)
