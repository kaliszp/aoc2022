from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 13


def parse(puzzle_input):
    pairs = []
    for p in puzzle_input.split("\n\n"):
        l_str, r_str = p.split("\n")
        l = eval(l_str)
        r = eval(r_str)
        pairs.append((l, r))
    return pairs


def compare(l, r):
    # print(f"Comparing {l} to {r}")
    if isinstance(l, list) and isinstance(r, list):
        ll = len(l)
        lr = len(r)
        for idx in range(min(ll, lr)):
            res = compare(l[idx], r[idx])
            if res < 0:
                return -1
            elif res > 0:
                return 1
        if ll > lr:
            # print("Left run out of elements")
            return -1
        elif ll < lr:
            # print("Right run out of elements")
            return 1
        return 0
    elif isinstance(l, int) and isinstance(r, int):
        if l < r:
            return 1
        elif l > r:
            return -1
        else:
            return 0
    elif isinstance(l, int):
        return compare([l], r)
    else:
        return compare(l, [r])


def part1(packets):

    correct = 0
    for idx, p in enumerate(packets, start=1):
        # print(f"\nLEFT={p[0]}\nRIGHT={p[1]}")
        res = compare(p[0], p[1])
        # print(f"Correct order: {res}")
        if res == 1:
            correct += idx

    return correct


def part2(packets):

    from functools import cmp_to_key

    flat = []
    for p in packets:
        flat.append(p[0])
        flat.append(p[1])

    flat.append([[2]])
    flat.append([[6]])

    flat = sorted(flat, key=cmp_to_key(compare), reverse=True)
    # print(*flat, sep="\n")

    return (flat.index([[2]]) + 1) * (flat.index([[6]]) + 1)


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    # test data
    # with open("test_data", "r") as f:
    #     data = f.read()

    # print(f"Sample data:\n{data[:50]}")
    parsed_data = parse(data)
    # print(f"Size of map: {parsed_data['size']}")
    # print(f"Start: {parsed_data['start']}")
    # print(f"End: {parsed_data['end']}")

    # answer1 = part1(parsed_data)
    # print(answer1)
    # submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(parsed_data)
    print(answer2)
    submit(answer2, part="b", year=YEAR, day=DAY)
