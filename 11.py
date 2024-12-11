from functools import cache

from adventofcode import AoC


def part1(line: str):
    arrangement = []

    for l in line.split(" "):
        arrangement.append(int(l))
    return sum(expand_single(a, 25) for a in arrangement)


@cache
def expand_single(a, n):
    if n == 0:
        return 1
    sa = str(a)

    if a == 0:
        return expand_single(1, n - 1)
    elif len(sa) % 2 == 0:
        left = expand_single(int(sa[: len(sa) // 2]), n - 1)
        right = expand_single(int(sa[len(sa) // 2 :]), n - 1)
        return left + right
    else:
        return expand_single(a * 2024, n - 1)


def part2(line: str):
    arrangement = []

    for l in line.split(" "):
        arrangement.append(int(l))
    return sum(expand_single(a, 75) for a in arrangement)


aoc = AoC(part_1_no_splitlines=part1, part_2_no_splitlines=part2)

inp = """125 17"""
aoc.assert_p1(
    inp,
    expected=55312,
)
aoc.submit_p1()
aoc.submit_p2()
