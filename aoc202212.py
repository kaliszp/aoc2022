from aocd import submit
from aocd.models import Puzzle

YEAR = 2022
DAY = 12


def parse(puzzle_input):
    import re
    import string
    r = 0
    h_map = dict()
    for line in puzzle_input.split("\n"):
        if "S" in line:
            h_map["start"] = (r, line.index("S"))
            line = re.sub("S", "a", line)
        if "E" in line:
            h_map["end"] = (r, line.index("E"))
            line = re.sub("E", "z", line)
        c = 0
        for l in line:
            h_map[(r, c)] = string.ascii_lowercase.index(l)
            c += 1
        r += 1
    h_map["size"] = (r, c)

    return h_map


def part1(h_map):
    import math
    start = h_map["start"]
    end = h_map["end"]
    visited = set()

    dists = dict()
    for k, h in h_map.items():
        if k in ["start", "end", "size"]:
            continue
        else:
            dists[k] = math.inf
    dists[start] = 0

    while end not in visited:
        unvisited = dict([(k, v)
                         for k, v in dists.items() if k not in visited])
        pos = sorted(unvisited.items(), key=lambda item: item[1])[0][0]
        curr_h = h_map[pos]
        curr_d = dists[pos]

        l, r = (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)
        u, b = (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1])
        to_check = []
        if l in h_map.keys() and curr_h + 1 >= h_map[l] and l not in visited:
            to_check.append(l)
        if r in h_map.keys() and curr_h + 1 >= h_map[r] and r not in visited:
            to_check.append(r)
        if u in h_map.keys() and curr_h + 1 >= h_map[u] and u not in visited:
            to_check.append(u)
        if b in h_map.keys() and curr_h + 1 >= h_map[b] and b not in visited:
            to_check.append(b)

        for c in to_check:
            dists[c] = min(dists[c], curr_d + 1)

        visited.add(pos)
        print(f"\r{len(visited)}", end='')
        print()

    return dists[end]


def part2(h_map):

    import math
    start = h_map["end"]
    end = h_map["end"]
    lengths = []
    starts = [k for k, v in h_map.items() if v == 0]
    print(f"Starting points: {len(starts)}")
    visited = set()

    dists = dict()
    for k, h in h_map.items():
        if k in ["start", "end", "size"]:
            continue
        else:
            dists[k] = math.inf
    dists[start] = 0

    while len(visited) < len(dists):
        unvisited = dict([(k, v)
                          for k, v in dists.items() if k not in visited])
        pos = sorted(unvisited.items(), key=lambda item: item[1])[0][0]
        curr_h = h_map[pos]
        curr_d = dists[pos]

        l, r = (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)
        u, b = (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1])
        to_check = []
        if l in h_map.keys() and curr_h - 1 <= h_map[l] and l not in visited:
            to_check.append(l)
        if r in h_map.keys() and curr_h - 1 <= h_map[r] and r not in visited:
            to_check.append(r)
        if u in h_map.keys() and curr_h - 1 <= h_map[u] and u not in visited:
            to_check.append(u)
        if b in h_map.keys() and curr_h - 1 <= h_map[b] and b not in visited:
            to_check.append(b)

        for c in to_check:
            dists[c] = min(dists[c], curr_d + 1)

        visited.add(pos)

    for s in starts:
        lengths.append(dists[s])

    print(lengths)

    return (min(lengths))


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    data = puzzle.input_data

    # test data
    # with open("test_data", "r") as f:
    #     data = f.read()

    print(f"Sample data:\n{data[:50]}")
    parsed_data = parse(data)
    print(f"Size of map: {parsed_data['size']}")
    print(f"Start: {parsed_data['start']}")
    print(f"End: {parsed_data['end']}")

    # answer1 = part1(parsed_data)
    # print(answer1)
    # submit(answer1, part="a", year=YEAR, day=DAY)

    answer2 = part2(parsed_data)
    print(answer2)
    # submit(answer2, part="b", year=YEAR, day=DAY)
