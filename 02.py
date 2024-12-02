from adventofcode import AoC


def part1(line: list[str]):
    safe = 0
    for l in line:
        levels = list(map(int, l.split()))
        incr = levels[0] > levels[1]
        for i in range(len(levels) - 1):
            if (
                abs(levels[i] - levels[i + 1]) > 3
                or abs(levels[i] - levels[i + 1]) == 0
            ):
                break
            if incr and levels[i] < levels[i + 1]:
                break
            if not incr and levels[i] > levels[i + 1]:
                break
        else:
            safe += 1

    return safe


def check(levels: list[int], dempner: bool):
    incr = levels[0] > levels[1]
    for i in range(len(levels) - 1):
        if abs(levels[i] - levels[i + 1]) > 3 or abs(levels[i] - levels[i + 1]) == 0:
            if dempner:
                return False
            return (
                check(levels[:i] + levels[i + 1 :], True)
                or check(levels[: i + 1] + levels[i + 2 :], True)
                or check(levels[: i - 1] + levels[i:], True)
            )
        if incr and levels[i] < levels[i + 1]:
            if dempner:
                return False
            return (
                check(levels[:i] + levels[i + 1 :], True)
                or check(levels[: i + 1] + levels[i + 2 :], True)
                or check(levels[: i - 1] + levels[i:], True)
            )
        if not incr and levels[i] > levels[i + 1]:
            if dempner:
                return False
            return (
                check(levels[:i] + levels[i + 1 :], True)
                or check(levels[: i + 1] + levels[i + 2 :], True)
                or check(levels[: i - 1] + levels[i:], True)
            )
    else:
        return True


def part2(line: list[str]):
    safe = 0
    for l in line:
        levels = list(map(int, l.split()))
        if check(levels, False):
            safe += 1

    return safe


aoc = AoC(part_1=part1, part_2=part2)

inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
aoc.assert_p1(
    inp,
    expected=2,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=4,
)
aoc.submit_p2()
