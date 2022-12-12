from aocd import submit
from aocd.models import Puzzle
import json

YEAR = 2022
DAY = 7


def parse(puzzle_input):
    structure = {}
    pth = []
    for cmd in puzzle_input.split("\n"):
        c = cmd.split()
        if c[0] == '$':
            if c[1] == 'cd':
                if c[2] == '..':
                    pth.pop()
                    pth.pop()
                    # print(f"{cmd:<40}\t|\t new path = {''.join(pth)}")
                    # _ = input()
                    continue
                else:
                    pth.append(c[2])
                    pth.append("/")
                    if ''.join(pth) not in structure:
                        structure[''.join(pth)] = 0
                    # print(f"{cmd:<40}\t|\t new path = {''.join(pth)}")
                    # _ = input()
                    continue
        elif c[0] == 'dir':
            continue
        else:
            key = ''.join(pth)
            old = structure.get(key, 0) 
            structure[key] = old + int(c[0])
            # print(f"{cmd:<40}\t|\t {old} -> {structure[key]}")
            # _ = input()
    return structure


def part1(structure):
    total_sizes = {}
    for path, size in structure.items():
        total_size = 0
        for path2, size2 in structure.items():
            if path2.startswith(path):
                total_size += size2
        total_sizes[path] = total_size

    selected_sizes = 0
    for path, size in total_sizes.items():
        if size <= 100_000:
            print(path)
            selected_sizes += size
    return selected_sizes


def part2(structure):
    total_sizes = {}
    structure['//'] = 0
    for path, size in structure.items():
        total_size = 0
        for path2, size2 in structure.items():
            if path2.startswith(path):
                total_size += size2
        total_sizes[path] = total_size
    
    unused = 70_000_000 - total_sizes['//']
    req = 30_000_000 - unused
    sorted_sizes = dict(sorted(total_sizes.items(), key=lambda item: item[1]))
    print(sorted_sizes)
    for dir, size in sorted_sizes.items():
        if size >= req:
            return size

    return size


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    # print(f"Sample data:\n{data[:50]}")
    # print(data)

    parsed_data = parse(data)
    # pretty = json.dumps(parsed_data, indent=4)
    # print(pretty)
    # print(f"Sample parsed data:\n{parsed_data[:10]}")

    answer1 = part1(parsed_data)
    print(answer1)
    submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(parsed_data)
    print(answer2)
    submit(answer2, part="b", year=YEAR, day=DAY)

