from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 5


def parse(puzzle_input):
    import re
    stacks = [[] for _ in range(9)]
    instructions = []
    num_idxs = list(range(1, 37, 4))
    for line in puzzle_input.split("\n"):
        if re.match(r'^move', line):
            instructions.append(tuple(re.findall(r'\d+', line)))
        elif re.match(r'^(\[[A-Z ]\])|([ ]{3})', line):
            print(line)
            [stacks[i].append(line[j]) for i, j in enumerate(num_idxs)]

    for i, j in enumerate(stacks):
        j.reverse()
        stacks[i] = list(str.strip(''.join(j)))

    return instructions, stacks


def part1(instructions, stacks):
    [print(f"{i}: {''.join(j)}") for i, j in enumerate(stacks)]
    for n, f, t in instructions:
        # print(f"N: {n}, from: {int(f)-1}, to: {int(t)-1}")
        for i in range(int(n)):
            # print(i)
            # [print(f"{i}: {''.join(j)}") for i, j in enumerate(stacks)]
            # print()
            stacks[int(t) - 1].append(stacks[int(f) - 1].pop())
    # print()
    # [print(f"{i}: {''.join(j)}") for i, j in enumerate(stacks)]
    return ''.join([i[-1:][0] for i in stacks if i])


def part2(instructions, stacks):
    for n, f, t in instructions:
        mv = stacks[int(f) - 1][-int(n):]
        stacks[int(f) - 1] = stacks[int(f) - 1][:-int(n)]
        stacks[int(t) - 1] += mv
    return ''.join([i[-1:][0] for i in stacks if i])


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    print(f"Sample data:\n{data[:10]}")

    instructions, stacks = parse(data)
    # print(f"Sample parsed data:\n{parsed_data[:10]}")

    answer1 = part1(*parse(data))
    print(answer1)
    submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(*parse(data))
    print(answer2)
    submit(answer2, part="b", year=YEAR, day=DAY)
