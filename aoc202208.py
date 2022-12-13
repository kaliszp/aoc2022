import numpy as np
from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 8


def parse(puzzle_input):
    forest = np.asarray([list(l) for l in puzzle_input.split("\n")])

    return forest


def part1(forest):
    rows = forest.shape[0]
    cols = forest.shape[1]
    visible = 0
    it = np.nditer(forest, flags=['multi_index'])
    for t in it:
        r = it.multi_index[0]
        c = it.multi_index[1]
        if ((r == rows - 1 or r == 0) or
                (c == cols - 1 or c == 0)):
            visible += 1
        else:
            upper = forest[:r, c]
            lower = forest[(r + 1):, c]
            left = forest[r, :c]
            right = forest[r, (c + 1):]
            if (max(upper) < t):
                visible += 1
            elif (max(lower) < t):
                visible += 1
            elif (max(right) < t):
                visible += 1
            elif (max(left) < t):
                visible += 1

    return visible


def part2(forest):
    forest = forest.astype(int)
    # forest = forest[:10, :10]
    # print(forest)
    rows = forest.shape[0]
    cols = forest.shape[1]
    max_score = 0

    it = np.nditer(forest, flags=['multi_index'])
    for t in it:
        r = it.multi_index[0]
        c = it.multi_index[1]
        score = 0
        if ((r == rows - 1 or r == 0) or
                (c == cols - 1 or c == 0)):
            pass
        else:
            upper = np.flip(forest[:r, c])
            msk = upper >= t
            upper_score = (np.argmax(msk) + 1
                           if (np.max(msk) > 0)
                           else len(msk.reshape(-1, 1)))

            lower = forest[(r + 1):, c]
            msk = lower >= t
            lower_score = (np.argmax(msk) + 1
                           if (np.max(msk) > 0)
                           else len(msk.reshape(-1, 1)))

            left = np.flip(forest[r, :c])
            msk = left >= t
            left_score = (np.argmax(msk) + 1
                          if (np.max(msk) > 0)
                          else len(msk.reshape(-1, 1)))

            right = forest[r, (c + 1):]
            msk = right >= t
            right_score = (np.argmax(msk) + 1
                           if (np.max(msk) > 0)
                           else len(msk.reshape(-1, 1)))

            score = (upper_score * lower_score * left_score * right_score)
            max_score = max(max_score, score)
            # print(f"HEIGHT = {t}")
            # print(it.multi_index)
            # print(f"upper = {upper}")
            # print(f"upper score = {upper_score}")
            # print(f"lower = {lower}")
            # print(f"lower score = {lower_score}")
            # print(f"left = {left}")
            # print(f"left score = {left_score}")
            # print(f"right = {right}")
            # print(f"right score = {right_score}")
            # print(f"total score = {score}")
            # print(f"max score = {max_score}")
            # input()
    return max_score


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    print(f"Sample data:\n{data[:50]}")

    parsed_data = parse(data)
    # print(f"Sample parsed data:\n{parsed_data[:10]}")

    answer1 = part1(parsed_data)
    print(answer1)
    submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(parsed_data)
    print(answer2)
    submit(answer2, part="b", year=YEAR, day=DAY)
