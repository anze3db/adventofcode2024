import re

from adventofcode import AoC


def part1(lines: list[str]):
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    result = 0
    for line in lines:
        matches = regex.findall(line)
        result += sum(int(x) * int(y) for x, y in matches)
    return result


def part2(lines: list[str]):
    regex = re.compile(r"(don\'t\(\))|(do\(\))|mul\((\d{1,3}),(\d{1,3})\)")
    result = 0
    enabled = True
    for line in lines:
        matches = regex.findall(line)
        for dont, do, x, y in matches:
            if dont:
                enabled = False
            elif do:
                enabled = True
            elif enabled:
                result += int(x) * int(y)
    return result


aoc = AoC(part_1=part1, part_2=part2)

inp = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
aoc.assert_p1(
    inp,
    expected=161,
)
aoc.submit_p1()
aoc.assert_p2(
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
    expected=48,
)
aoc.submit_p2()
