from adventofcode import AoC


def draw(grid, antennas, antinodes):
    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)
    print(antennas)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            char = "."
            if (x, y) in antinodes:
                char = "#"
            for k, v in antennas.items():
                if (x, y) in v:
                    char = k
                    if (x, y) in antinodes:
                        char = "_"
                    continue

            print(char, end="")
        print()
    print()


def part1(lines: list[str]):
    antennas = {}
    grid = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid.add((x, y))
            if c == ".":
                continue
            l = antennas.get(c, [])
            l.append((x, y))
            antennas[c] = l
    antinodes = set()
    for positions in antennas.values():
        position_pairs = []
        for position in positions:
            for other_position in positions:
                if position == other_position:
                    continue
                position_pairs.append((position, other_position))
        for pair1, pair2 in position_pairs:
            dist = (pair1[0] - pair2[0]), (pair1[1] - pair2[1])
            next_point_in_line = pair1[0] + dist[0], pair1[1] + dist[1]
            if next_point_in_line in grid:
                antinodes.add(next_point_in_line)
    # draw(grid, antennas, antinodes)
    return len(antinodes)


def part2(lines: list[str]):
    antennas = {}
    grid = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid.add((x, y))
            if c == ".":
                continue
            if c == "#":
                continue
            l = antennas.get(c, [])
            l.append((x, y))
            antennas[c] = l
    antinodes = set()
    for positions in antennas.values():
        position_pairs = []
        for position in positions:
            for other_position in positions:
                if position == other_position:
                    continue
                position_pairs.append((position, other_position))
        for pair1, pair2 in position_pairs:
            antinodes.add(pair1)
            antinodes.add(pair2)
            while True:
                dist = (pair1[0] - pair2[0]), (pair1[1] - pair2[1])
                next_point_in_line = pair1[0] + dist[0], pair1[1] + dist[1]
                pair2 = pair1
                pair1 = next_point_in_line

                if next_point_in_line in grid:
                    antinodes.add(next_point_in_line)
                else:
                    break
    # draw(grid, antennas, antinodes)
    return len(antinodes)


aoc = AoC(part_1=part1, part_2=part2)

inp = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
aoc.assert_p1(
    inp,
    expected=14,
)
aoc.submit_p1()
aoc.assert_p2(
    """T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........""",
    expected=9,
)
aoc.assert_p2(
    inp,
    expected=34,
)
aoc.submit_p2()
