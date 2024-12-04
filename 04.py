from adventofcode import AoC


def part1(lines: list[str]):
    result = 0
    grid = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}
    search = "XMAS"
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            for dx, dy in (
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),
                (1, 1),
                (-1, 1),
                (1, -1),
                (-1, -1),
            ):
                for i, c in enumerate(search):
                    if grid.get((x + dx * i, y + dy * i)) != c:
                        break
                else:
                    result += 1
    return result


def part2(lines: list[str]):
    result = 0
    grid = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if grid.get((x, y)) != "A":
                continue
            if grid.get((x + 1, y + 1)) not in ("M", "S"):
                continue
            if grid.get((x - 1, y - 1)) not in ("M", "S"):
                continue
            if grid.get((x + 1, y - 1)) not in ("M", "S"):
                continue
            if grid.get((x - 1, y + 1)) not in ("M", "S"):
                continue
            if grid.get((x + 1, y + 1)) == grid.get((x - 1, y - 1)):
                continue
            if grid.get((x + 1, y - 1)) == grid.get((x - 1, y + 1)):
                continue
            result += 1
    return result


aoc = AoC(part_1=part1, part_2=part2)

inp = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
aoc.assert_p1(
    inp,
    expected=18,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=9,
)
aoc.submit_p2()
