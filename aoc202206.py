from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 6


def parse(puzzle_input):
    puzzle_input
    return puzzle_input


def part1(characters):
    for i, _ in enumerate(characters, start=1):
        if i > 3:
            if len(set(characters[(i - 4):i])) == 4:
                return i
    return None


def part2(characters):
    for i, _ in enumerate(characters, start=1):
        if i > 13:
            if len(set(characters[(i - 14):i])) == 14:
                return i
    return None


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
