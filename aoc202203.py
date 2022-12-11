from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 3


def parse(puzzle_input):
    rucksacks = []
    for line in puzzle_input.split("\n"):
        rucksacks.append(list(line))
    return rucksacks


def part1(data):
    import string
    prios = 0
    for r in data:
        half = len(r) // 2
        first = set(r[:half])
        second = set(r[half:])
        common = first.intersection(second)
        prios += (string.ascii_letters.index(list(common)[0]) + 1)

    return prios


def part2(data):
    import string
    prios = 0
    groups = len(data) // 3
    for g in range(groups):
        s1, s2, s3 = set(data[3 * g]), set(data[3 * g + 1]
                                           ), set(data[3 * g + 2])
        common = s1.intersection(s2).intersection(s3)
        prios += (string.ascii_letters.index(list(common)[0]) + 1)

    return prios


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
