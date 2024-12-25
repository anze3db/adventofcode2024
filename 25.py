from dataclasses import dataclass

from adventofcode import AoC


@dataclass
class Lock:
    heights: list[int]


@dataclass
class Key:
    heights: list[int]


def part1(lines: str):
    locks_or_keys = lines.split("\n\n")
    keys = []
    locks = []
    for lock_or_key in locks_or_keys:
        rows = lock_or_key.split("\n")
        if rows[0][0] == "#":
            lock = Lock([0, 0, 0, 0, 0])
            for row in rows[1:]:
                for i, char in enumerate(row):
                    if char == "#":
                        lock.heights[i] += 1
            locks.append(lock)
        else:
            key = Key([0, 0, 0, 0, 0])
            for row in rows[:-1]:
                for i, char in enumerate(row):
                    if char == "#":
                        key.heights[i] += 1

            keys.append(key)
    result = 0
    for lock in locks:
        for key in keys:
            for i in range(5):
                if lock.heights[i] + key.heights[i] > 5:
                    break
            else:
                result += 1

    return result


def part2(lines: list[str]):
    pass


aoc = AoC(part_1_no_splitlines=part1, part_2=part2)

inp = """\
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""
aoc.assert_p1(
    inp,
    expected=3,
)
aoc.submit_p1()
