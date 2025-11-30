import re
from dataclasses import dataclass

from adventofcode import AoC


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int


called = 0


def draw(robots):
    max_x = 101
    max_y = 103
    for y in range(max_y):
        for x in range(max_x):
            count = len([r for r in robots if r.px == x and r.py == y])
            if not count:
                print(".", end="")
            else:
                print(count, end="")
        print()
    print()


def part1(inp: str):
    lines = inp.splitlines()
    robots = []
    for line in lines:
        m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        if not m:
            raise ValueError(f"Invalid line: {line}")
        robots.append(Robot(*list(map(int, m.groups()))))
    global called
    if called == 0:
        called += 1
        max_x = 11
        max_y = 7
    else:
        max_x = 101
        max_y = 103

    for _ in range(100):
        for r in robots:
            r.px += r.vx
            r.px %= max_x
            r.py += r.vy
            r.py %= max_y

    four_quadrants = (
        (0, max_x // 2 - 1, 0, max_y // 2 - 1),
        (max_x // 2 + 1, max_x, 0, max_y // 2 - 1),
        (0, max_x // 2 - 1, max_y // 2 + 1, max_y),
        (max_x // 2 + 1, max_x, max_y // 2 + 1, max_y),
    )
    count_robots_per_quadrant = []
    for startx, endx, starty, endy in four_quadrants:
        count = 0
        for r in robots:
            if startx <= r.px <= endx and starty <= r.py <= endy:
                count += 1
        count_robots_per_quadrant.append(count)

    multi = 1
    for count in count_robots_per_quadrant:
        multi *= count
    return multi


def part2(inp: str):
    lines = inp.splitlines()
    robots = []
    for line in lines:
        m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        if not m:
            raise ValueError(f"Invalid line: {line}")
        robots.append(Robot(*list(map(int, m.groups()))))

    max_x = 101
    max_y = 103

    for i in range(1, 1000000):
        for r in robots:
            r.px += r.vx
            r.px %= max_x
            r.py += r.vy
            r.py %= max_y
        robot_positions = set((r.px, r.py) for r in robots)
        if len(robot_positions) == len(robots):
            draw(robots)
            return i


aoc = AoC(part_1=part1, part_2=part2)

inp = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
aoc.assert_p1(
    inp,
    expected=12,
)
aoc.submit_p1()
aoc.submit_p2()
