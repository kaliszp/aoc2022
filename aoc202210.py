from aocd import submit
from aocd.models import Puzzle
import numpy as np

YEAR = 2022
DAY = 10


def parse(puzzle_input):
    instructions = []
    for i in puzzle_input.split("\n"):
        if i == "noop":
            instructions.append(None)
        else:
            instructions.append(i.split())

    cycles = [1]
    for i in instructions:
        # print(f"INSTRUCTION: {i}")
        if not i:
            cycles.append(cycles[-1:][0])
            # print(f"#{len(cycles)}: {cycles[-1:]}")
        else:
            add = int(i[1])
            limit = 1
            for _ in range(limit):
                cycles.append(cycles[-1:][0])
                # print(f"#{len(cycles)}: {cycles[-1:]}")
            cycles.append(cycles[-1:][0] + add)
            # print(f"#{len(cycles)}: {cycles[-1:]}")
    return cycles


def part1(cycles):
    power = 0
    for idx in range(20, 221, 40):
        print(f"CYCLE {idx}: {cycles[idx-1]} | POWER {idx * cycles[idx-1]}")
        power += idx * cycles[idx-1]

    return power


def part2(cycles):

    screen = []
    for idx, c in enumerate(cycles):
        if c - 1 <= idx % 40 <= c + 1:
            screen.append("#")
        else:
            screen.append(".")

    display =''
    for r in range(6):
        for c in range(40):
            display += screen[r*40+c][0]
        display += '\n'
    print(display)

    return None


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    #test data
    # with open("test_data", "r") as f:
    #     data = f.read()

    print(f"Sample data:\n{data[:50]}")

    parsed_data = parse(data)
    print(f"Sample parsed data:\n{parsed_data[:10]}")

    answer1 = part1(parsed_data)
    print(answer1)
    submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(parsed_data)
    print(answer2)
    # submit(answer2, part="b", year=YEAR, day=DAY)
