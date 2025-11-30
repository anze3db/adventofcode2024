from adventofcode import AoC


def bfs(grid, starts):
    visited = set()
    while starts:
        new_starts = set()
        for start in starts:
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x, y = start
                curr_slope = grid[(x, y)]
                new_x = x + dx
                new_y = y + dy

                if (new_x, new_y) in visited:
                    continue
                if curr_slope + 1 != grid.get((new_x, new_y)):
                    continue

                visited.add((new_x, new_y))
                new_starts.add((new_x, new_y))
        starts = new_starts
    return visited


def bfs2(grid, starts):
    score = 0
    while starts:
        new_starts = []
        for start in starts:
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x, y = start
                curr_slope = grid[(x, y)]
                new_x = x + dx
                new_y = y + dy

                if curr_slope + 1 != grid.get((new_x, new_y)):
                    continue
                if grid.get((new_x, new_y)) == 9:
                    score += 1
                new_starts.append((new_x, new_y))
        starts = new_starts
    return score


def part1(inp: str):
    lines = inp.splitlines()
    grid = {}
    starts = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ".":
                continue
            grid[(x, y)] = int(c)

            if c == "0":
                starts.add((x, y))

    result = 0
    for start in starts:
        visited = bfs(grid, {start})
        result += len([v for v in visited if grid[v] == 9])
    return result


def part2(inp: str):
    lines = inp.splitlines()
    grid = {}
    starts = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ".":
                continue
            grid[(x, y)] = int(c)
            if c == "0":
                starts.add((x, y))

    result = 0
    for start in starts:
        result += bfs2(grid, {start})
    return result


aoc = AoC(part_1=part1, part_2=part2)

inp = """0123
1234
8765
9876"""
inp2 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
inp3 = """012345
123456
234567
345678
416789
567891"""
aoc.assert_p1(
    inp,
    expected=1,
)
aoc.assert_p1(
    inp2,
    expected=36,
)
aoc.submit_p1()
inp4 = """.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""
aoc.assert_p2(inp4, expected=3)
aoc.assert_p2(
    inp3,
    expected=227,
)
aoc.assert_p2(
    inp2,
    expected=81,
)
aoc.submit_p2()
