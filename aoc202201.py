from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 1


def parse(puzzle_input):
    elves = []
    elf = []
    for line in puzzle_input.split("\n"):
        if line == "":
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line))
    return elves


def part1(data):
    mx = 0
    for e in data:
        print(e)
        mx = max(mx, sum(e))

    return mx


def part2(data):
    totals = [sum(e) for e in data]
    totals.sort()

    return sum(totals[-3:])


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
