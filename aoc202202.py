from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 2


def parse(puzzle_input):
    rounds = []
    for line in puzzle_input.split("\n"):
        rounds.append(line.split())
    return rounds


def part1(data):
    points_for_shape = {"X": 1, "Y": 2, "Z": 3}
    points_for_winning = {"w": 6, "d": 3, "l": 0}
    pts = 0
    for m1, m2 in data:
        if m1 == "A":
            if m2 == "Y":
                pts += 3 + points_for_winning["w"]
            elif m2 == "Z":
                pts += points_for_shape[m2]
            else:
                pts += points_for_shape[m2] + points_for_winning["d"]
        elif m1 == "B":
            if m2 == "Z":
                pts += points_for_shape[m2] + points_for_winning["w"]
            elif m2 == "X":
                pts += points_for_shape[m2]
            else:
                pts += points_for_shape[m2] + points_for_winning["d"]
        else:
            if m2 == "X":
                pts += points_for_shape[m2] + points_for_winning["w"]
            elif m2 == "Y":
                pts += points_for_shape[m2]
            else:
                pts += points_for_shape[m2] + points_for_winning["d"]
    return pts


def part2(data):
    points_for_shape = {"r": 1, "p": 2, "s": 3}
    m1_to_shape = {"A": "r", "B": "p", "C": "s"}
    pts = 0
    for m1, m2 in data:
        if m1_to_shape[m1] == 'r':
            if m2 == "Y":
                pts += 3 + points_for_shape[m1_to_shape[m1]]
            elif m2 == "Z":
                pts += 6 + points_for_shape["p"]
            else:
                pts += points_for_shape["s"]
        elif m1_to_shape[m1] == 'p':
            if m2 == "Y":
                pts += 3 + points_for_shape[m1_to_shape[m1]]
            elif m2 == "Z":
                pts += 6 + points_for_shape["s"]
            else:
                pts += points_for_shape["r"]
        else:
            if m2 == "Y":
                pts += 3 + points_for_shape[m1_to_shape[m1]]
            elif m2 == "Z":
                pts += 6 + points_for_shape["r"]
            else:
                pts += points_for_shape["p"]
    return pts


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
