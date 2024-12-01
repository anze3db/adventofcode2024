from collections import Counter

from adventofcode import AoC


def part1(line: list[str]):
    list1 = []
    list2 = []
    for i in line:
        num1, num2 = i.split()
        list1.append(int(num1))
        list2.append(int(num2))
    list1 = sorted(list1)
    list2 = sorted(list2)
    distances = 0
    for i in range(len(list1)):
        distances += abs(list1[i] - list2[i])

    return distances


def part2(line: list[str]):
    list1 = []
    cntr = Counter()
    for i in line:
        num1, num2 = i.split()
        list1.append(int(num1))
        cntr.update([int(num2)])

    distances = 0
    for i in list1:
        distances += i * cntr[i]

    return distances


aoc = AoC(part_1=part1, part_2=part2)

inp = """3   4
4   3
2   5
1   3
3   9
3   3"""
aoc.assert_p1(
    inp,
    expected=11,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=31,
)
aoc.submit_p2()
