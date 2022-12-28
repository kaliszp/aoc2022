from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 14


def parse(puzzle_input):
    filled = set()
    lines = []
    for rl in puzzle_input.split("\n"):
        # print(f"LINE: {rl}")
        lines = []
        for l in rl.split(" -> "):
            x, y = l.split(",")
            lines.append((int(x), int(y)))
        for idx, l in enumerate(lines[1:], start=1):
            start = lines[idx - 1]
            stop = l
            # print(f"{start} -> {stop}")
            if start[0] == stop[0]:
                range_y = (range(start[1], stop[1] + 1)
                           if start[1] < stop[1]
                           else range(stop[1], start[1] + 1)
                           )
                for y in range_y:
                    # print(f"  adding {(l[0], y)}")
                    filled.add((l[0], y))
            else:
                range_x = (range(start[0], stop[0] + 1)
                           if start[0] < stop[0]
                           else range(stop[0], start[0] + 1)
                           )
                for x in range_x:
                    # print(f"  adding {(x, l[1])}")
                    filled.add((x, l[1]))
    return filled


def add_sand(rocks, sand, lim_y):
    pos = (500, 0)
    blocked = rocks.union(sand)
    while (True):
        x = pos[0]
        y = pos[1]
        if y + 1 == lim_y:
            return (x, y)
        elif (x, y + 1) not in blocked:
            pos = (x, y + 1)
            continue
        elif (x - 1, y + 1) not in blocked:
            pos = (x - 1, y + 1)
            continue
        elif (x + 1, y + 1) not in blocked:
            pos = (x + 1, y + 1)
            continue
        else:
            return pos


def part1(rocks):

    max_y = max(rocks, key=lambda x: x[1])[1]
    sand = set()
    while (True):
        new_pos = add_sand(rocks, sand, max_y)
        if new_pos:
            sand.add(new_pos)
            # display(rocks, sand)
        else:
            break

    return len(sand)


def part2(rocks):
    max_y = max(rocks, key=lambda x: x[1])[1]
    sand = set()
    while (True):
        # input()
        new_pos = add_sand(rocks, sand, max_y + 2)
        if new_pos == (500, 0):
            sand.add(new_pos)
            # display(rocks, sand)
            break
        elif new_pos:
            sand.add(new_pos)
            # display(rocks, sand)
        else:
            break

    return len(sand)


def display(rocks, sand):
    max_x = max(rocks, key=lambda x: x[0])[0]
    max_y = max(rocks, key=lambda x: x[1])[1]
    min_x = min(rocks, key=lambda x: x[0])[0]
    min_y = min(rocks, key=lambda x: x[1])[1]

    display = ''
    for y in range(0, max_y + 3):
        for x in range(min_x - 5, max_x + 5):
            if (x, y) in rocks:
                display += "#"
            elif (x, y) in sand:
                display += "o"
            else:
                display += "."
        display += '\n'
    print(display)


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    # test data
    # with open("test_data", "r") as f:
    #     data = f.read()

    # print(f"Sample data:\n{data[:50]}")
    parsed_data = parse(data)
    display(parsed_data, set())

    # answer1 = part1(parsed_data)
    # print(answer1)
    # submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(parsed_data)
    print(answer2)
    submit(answer2, part="b", year=YEAR, day=DAY)
