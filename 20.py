import heapq

from adventofcode import AoC


def part1(inp: str):
    """Inneficient, but I didn't bother fixing it once I solved p2"""
    lines = inp.splitlines()
    result = 0
    walls = set()
    start = (0, 0)
    end = (0, 0)
    path = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
            elif c == "#":
                walls.add((x, y))
            elif c == ".":
                path.add((x, y))
    path.add(start)
    path.add(end)

    to_visit = [(0, start)]
    visited = set()

    while to_visit:
        cost, (x, y) = heapq.heappop(to_visit)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) == end:
            result = cost
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (x + dx, y + dy) in walls:
                continue
            heapq.heappush(to_visit, (cost + 1, (x + dx, y + dy)))
    inital_result = result
    saved = []
    for wall in walls:
        path.add(wall)
        to_visit = [(0, start)]
        visited = set()

        while to_visit:
            cost, (x, y) = heapq.heappop(to_visit)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if (x, y) == end:
                result = cost
                break
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (x + dx, y + dy) not in path:
                    continue
                heapq.heappush(to_visit, (cost + 1, (x + dx, y + dy)))
        if result < inital_result:
            saved.append(inital_result - result)
        path.remove(wall)
    return len([r for r in saved if r >= 100])


def part2(inp: str):
    lines = inp.splitlines()
    walls = set()
    start = (0, 0)
    end = (0, 0)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
            elif c == "#":
                walls.add((x, y))

    dist = 0
    d_dist = {}
    visited = set()
    while start != end:
        visited.add(end)
        d_dist[end] = dist
        dist += 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_end = end[0] + dx, end[1] + dy
            if new_end in walls or new_end in visited:
                continue
            end = new_end
            break
    d_dist[start] = dist

    result = 0
    for k, v in reversed(d_dist.items()):
        for k2, v2 in d_dist.items():
            d = abs(k[0] - k2[0]) + abs(k[1] - k2[1])
            if d <= 20 and v2 - v - d >= 100:
                result += 1
    return result


aoc = AoC(part_1=part1, part_2=part2)
inp = """\
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
aoc.assert_p1(
    inp,
    expected=0,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=0,
)
aoc.submit_p2()
