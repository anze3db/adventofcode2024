import itertools
from functools import cache

from adventofcode import AoC


def test(curr, patterns):
    if not curr:
        return True
    for pattern in patterns:
        if curr.startswith(pattern):
            if test(curr[len(pattern) :], patterns):
                return True
    return False


@cache
def test2(curr, patterns):
    res = 0
    for pattern in patterns:
        if curr == pattern:
            res += 1
        if curr.startswith(pattern):
            res += test2(curr[len(pattern) :], patterns)
    return res


def part1(lines: str):
    patterns, designs = lines.split("\n\n")
    patterns = set(patterns.split(", "))
    result = 0
    for design in designs.splitlines():
        if test(design, patterns):
            result += 1

    return result


def part2(lines: str):
    patterns, designs = lines.split("\n\n")
    patterns = tuple(patterns.split(", "))
    result = 0
    for design in designs.splitlines():
        result += test2(design, patterns)

    return result


aoc = AoC(part_1=part1, part_2=part2)

inp = """\
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""
aoc.assert_p1(
    inp,
    expected=6,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=16,
)
aoc.submit_p2()
