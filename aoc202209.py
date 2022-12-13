import numpy as np
from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 9


def parse(puzzle_input):
    motions = [line.split() for line in puzzle_input.split("\n")]
    return motions


def part1(motions):
    visited = [(0, 0)]
    h_pos = [0, 0]
    t_pos = [0, 0]
    for d, n in motions:

        for _ in range(int(n)):
            old_h = h_pos.copy()
            if d == "U":
                h_pos[0] += 1
            elif d == "D":
                h_pos[0] -= 1
            elif d == "R":
                h_pos[1] += 1
            else:
                h_pos[1] -= 1

            old_t = t_pos.copy()

            # two steps directly
            if (abs(h_pos[0] - t_pos[0]) > 1) and (h_pos[1] == t_pos[1]):
                t_pos[0] = t_pos[0] + 1 if d == "U" else t_pos[0] - 1
            elif (abs(h_pos[0] - t_pos[0]) > 1):
                t_pos[0] = t_pos[0] + 1 if d == "U" else t_pos[0] - 1
                t_pos[1] = h_pos[1]
            elif (abs(h_pos[1] - t_pos[1]) > 1) and (h_pos[0] == t_pos[0]):
                t_pos[1] = t_pos[1] + 1 if d == "R" else t_pos[1] - 1
            elif (abs(h_pos[1] - t_pos[1]) > 1):
                t_pos[1] = t_pos[1] + 1 if d == "R" else t_pos[1] - 1
                t_pos[0] = h_pos[0]
            visited.append((t_pos[0], t_pos[1]))

            # print("=" * 30)
            # print(f"Motion = {d}, {n}")
            # print(f"HEAD: {old_h} -> {h_pos}")
            # print(f"TAIL: {old_t} -> {t_pos}")
            # print(f"(visited = {len(set(visited))})")
            # print("-" * 30)
            # input()

    return len(set(visited))


def print_visited(visited, size=26):
    for r in range(size):
        for c in range(size):
            if (r - size // 2, c - size // 2) in visited:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def print_board(knots, size=26):
    for r in range(size // 2, -size // 2, -1):
        for c in range(-size // 2, size // 2):
            if [r, c] in knots:
                print(knots.index([r, c]), end="")
            else:
                print(".", end="")
        print("")


def part2(motions):

    knots = [[0, 0] for _ in range(10)]
    visited = [(0, 0)]

    for d, n in motions:

        for _ in range(int(n)):

            if d == "U":
                knots[0][0] += 1
            elif d == "D":
                knots[0][0] -= 1
            elif d == "R":
                knots[0][1] += 1
            else:
                knots[0][1] -= 1

            for k in range(1, 10):

                # two steps directly
                h_pos = knots[k - 1].copy()
                t_pos = knots[k].copy()
                if (abs(h_pos[0] - t_pos[0]) > 1) and (h_pos[1] == t_pos[1]):
                    t_pos[0] = t_pos[0] + \
                        1 if h_pos[0] > t_pos[0] else t_pos[0] - 1
                elif (abs(h_pos[0] - t_pos[0]) > 1):
                    t_pos[0] = t_pos[0] + \
                        1 if h_pos[0] > t_pos[0] else t_pos[0] - 1
                    t_pos[1] = t_pos[1] + \
                        1 if h_pos[1] > t_pos[1] else t_pos[1] - 1
                elif (abs(h_pos[1] - t_pos[1]) > 1) and (h_pos[0] == t_pos[0]):
                    t_pos[1] = t_pos[1] + \
                        1 if h_pos[1] > t_pos[1] else t_pos[1] - 1
                elif (abs(h_pos[1] - t_pos[1]) > 1):
                    t_pos[1] = t_pos[1] + \
                        1 if h_pos[1] > t_pos[1] else t_pos[1] - 1
                    t_pos[0] = t_pos[0] + \
                        1 if h_pos[0] > t_pos[0] else t_pos[0] - 1

                knots[k] = t_pos

                if k == 9:
                    visited.append((t_pos[0], t_pos[1]))

        # print("=" * 30)
        # print(f"Motion = {d}, {n}")
        # print(f"HEAD: {old_h} -> {h_pos}")
        # print(f"TAIL: {old_t} -> {t_pos}")
        # print(f"(visited = {len(set(visited))})")
        # print("-" * 30)
        # input()

    return len(set(visited))


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    print(f"Sample data:\n{data[:50]}")

    parsed_data = parse(data)
    print(f"Sample parsed data:\n{parsed_data[:10]}")

    answer1 = part1(parsed_data)
    print(answer1)
    submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(parsed_data)
    # dummy_data = [
    #     ("R", 5),
    #     ("U", 8),
    #     ("L", 8),
    #     ("D", 3),
    #     ("R", 17),
    #     ("D", 10),
    #     ("L", 25),
    #     ("U", 20)
    # ]
    # print_visited(part2(dummy_data))
    print(answer2)
    submit(answer2, part="b", year=YEAR, day=DAY)
