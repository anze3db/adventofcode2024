from adventofcode import AoC
import heapq


def draw(grid, max_c):
    for y in range(max_c + 1):
        for x in range(max_c + 1):
            if (x, y) in grid:
                print(".", end="")
            else:
                print("#", end="")
        print()


def part1(lines: list[str], additional=0):
    result = 0
    corrupted = []
    for line in lines:
        x, y = map(int, line.split(","))
        corrupted.append(x)
        corrupted.append(y)
    max_c = max(corrupted)
    if max_c == 6:
        num_points = 12 + additional
    else:
        num_points = 1024 + additional

    corrupted = set()
    for line in lines[:num_points]:
        x, y = map(int, line.split(","))
        corrupted.add((x, y))

    grid = set()
    for x in range(max_c + 1):
        for y in range(max_c + 1):
            if (x, y) in corrupted:
                continue
            grid.add((x, y))

    pos = (0, 0)
    end = (max_c, max_c)

    to_visit = []
    visited = set()
    heapq.heappush(to_visit, (0, pos))
    while to_visit:
        score, current = heapq.heappop(to_visit)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            return score
        grid.add(current)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (current[0] + dx, current[1] + dy)
            if new_pos in grid:
                heapq.heappush(to_visit, (score + 1, new_pos))
    return True


def part2(lines: list[str]):
    if len(lines) > 1000:
        skip = 1024
    else:
        skip = 12
    for i in range(skip, len(lines)):
        if part1(lines[:i] + lines[i + 1 :], additional=i - skip) is True:
            return lines[i - 1]


aoc = AoC(part_1=part1, part_2=part2)

inp = """\
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
aoc.assert_p1(
    inp,
    expected=22,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected="6,1",
)
aoc.submit_p2()
