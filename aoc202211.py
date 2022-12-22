from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 11


def parse(puzzle_input):
    import re
    items = dict()
    operations = dict()
    tests = dict()
    outcomes = dict()
    monkeys = puzzle_input.split("Monkey")
    for idx, m in enumerate(monkeys[1:]):
        _, starting, op, test, true, false, *_ = m.split("\n")
        items[idx] = list(re.findall(r"\d+", starting))
        operations[idx] = re.sub("  Operation: new = ", "", op)
        tests[idx] = int(re.sub("  Test: divisible by ", "", test))
        outcomes[idx] = re.findall(r"\d", true), re.findall(r"\d", false)
    return items, operations, tests, outcomes


def part1(items, operations, tests, outcomes):
    inspections = dict()
    for _ in range(20):
        for monkey in items.keys():
            m_items = items[monkey]
            # print(f"Monkey:  #{monkey}")
            # print(f"  Operation:  {operations[monkey]}")
            # print(f"  Operation:  {outcomes[monkey]}")
            # print(f"  Items:  {m_items}")
            for _ in m_items.copy():
                inspections[monkey] = inspections.get(monkey, 0) + 1
                old = int(m_items.pop(0))
                worry = float(eval(operations[monkey])) // 3
                print(f"   Item {worry} | {tests[monkey]}:")
                if worry % tests[monkey] == 0:
                    idx = int(outcomes[monkey][0][0])
                    # print(
                    # f"     divisible moving to monkey #{int(outcomes[monkey][0][0])}")
                else:
                    idx = int(outcomes[monkey][1][0])
                    # print(
                    # f"     not divisible moving to monkey #{int(outcomes[monkey][1][0])}")
                items[idx].append(worry)
    inspections = dict(
        sorted(inspections.items(), key=lambda item: item[1], reverse=True))
    [print(f"{v}:{k}") for v, k in inspections.items()]
    vals = list(inspections.values())

    return vals[0] * vals[1]


def part2(items, operations, tests, outcomes):
    import math

    inspections = dict()
    print(tests)
    print()

    for _ in range(10000):
        lim = math.prod(tests.values())
        for monkey in items.keys():
            m_items = items[monkey]
            # print(f"Monkey:  #{monkey}")
            # print(f"  Operation:  {operations[monkey]}")
            # print(f"  Operation:  {outcomes[monkey]}")
            # print(f"  Items:  {m_items}")
            for _ in m_items.copy():
                inspections[monkey] = inspections.get(monkey, 0) + 1
                old = int(m_items.pop(0))
                worry = int(eval(operations[monkey]))
                worry = worry if worry < lim else worry % lim
                # print(f"   Item {worry} | {tests[monkey]}:")
                if worry % tests[monkey] == 0:
                    idx = int(outcomes[monkey][0][0])
                    # print(
                    # f"     divisible moving to monkey #{int(outcomes[monkey][0][0])}")
                else:
                    idx = int(outcomes[monkey][1][0])
                    # print(
                    # f"     not divisible moving to monkey #{int(outcomes[monkey][1][0])}")
                items[idx].append(worry)
    inspections = dict(
        sorted(inspections.items(), key=lambda item: item[1], reverse=True))
    [print(f"{v}:{k}") for v, k in inspections.items()]
    vals = list(inspections.values())

    return vals[0] * vals[1]


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    # test data
    # with open("test_data", "r") as f:
    #     data = f.read()

    print(f"Sample data:\n{data[:50]}")

    # print(f"Sample parsed data:\n{parsed_data[:10]}")

    # answer1 = part1(*parse(data))
    # print(answer1)
    # submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(*parse(data))
    print(answer2)
    submit(answer2, part="b", year=YEAR, day=DAY)
