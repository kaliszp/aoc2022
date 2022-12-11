from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 7


def parse(puzzle_input):
    structure = {}
    pth = []
    for cmd in puzzle_input[:50].split("\n"):
        c = cmd.split()
        if c[0] == '$':
            if c[1] == 'cd':
                if c[2] == '..':
                    pth.pop()
                    pth.pop()
                    continue
                else:
                    pth.append(c[2])
                    pth.append("/")
                    continue
        elif c[0] == 'dir':
            continue
        else:
            key = ''.join(pth)
            structure[key] = structure.get(key, 0) + int(c[0])
    return structure


def part1(structure):
    total_sizes = {}
    for path, size in structure.items():
        total_size = size
        for path2, size2 in structure.items():
            if path2.startswith(path):
                total_size += size2
        total_sizes[path] = total_size

    selected_sizes = 0
    for path, size in total_sizes.items():
        if size <= 100000:
            selected_sizes += size
    return selected_sizes


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

    print(f"Sample data:\n{data[:50]}")

    parsed_data = parse(data)
    # print(f"Sample parsed data:\n{parsed_data[:10]}")

    answer1 = part1(parsed_data)
    print(answer1)
    submit(answer1, part="a", year=YEAR, day=DAY)

    # answer2 = part2(parsed_data)
    # print(answer2)
    # submit(answer2, part="b", year=YEAR, day=DAY)
