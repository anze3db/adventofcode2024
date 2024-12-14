import re
from dataclasses import dataclass

from adventofcode import AoC
from z3 import Int, Solver, sat


@dataclass
class Button:
    x: int
    y: int
    cost: int


@dataclass
class Prize:
    x: int
    y: int


@dataclass
class Machine:
    a: Button
    b: Button
    prize: Prize


def part1(inp: str):
    machines = []
    for machine_lines in inp.split("\n\n"):
        a_str, b_str, prize_str = machine_lines.strip().split("\n")
        a_x, a_y = map(int, re.findall(r"X\+(\d+), Y\+(\d+)", a_str)[0])
        a = Button(x=a_x, y=a_y, cost=3)

        b_x, b_y = map(int, re.findall(r"X\+(\d+), Y\+(\d+)", b_str)[0])
        b = Button(x=b_x, y=b_y, cost=1)

        p_x, p_y = map(int, re.findall(r"X=(\d+), Y=(\d+)", prize_str)[0])
        p = Prize(x=p_x, y=p_y)
        machines.append(
            Machine(
                a=a,
                b=b,
                prize=p,
            )
        )

    result = 0
    for machine in machines:
        for i in range(0, 100):
            for j in range(0, 100):
                if (
                    i * machine.a.x + j * machine.b.x == machine.prize.x
                    and i * machine.a.y + j * machine.b.y == machine.prize.y
                ):
                    result += i * machine.a.cost + j * machine.b.cost

    return result


def part2(inp: str):
    machines = []
    for machine_lines in inp.split("\n\n"):
        a_str, b_str, prize_str = machine_lines.strip().split("\n")
        a_x, a_y = map(int, re.findall(r"X\+(\d+), Y\+(\d+)", a_str)[0])
        a = Button(x=a_x, y=a_y, cost=3)

        b_x, b_y = map(int, re.findall(r"X\+(\d+), Y\+(\d+)", b_str)[0])
        b = Button(x=b_x, y=b_y, cost=1)

        p_x, p_y = map(int, re.findall(r"X=(\d+), Y=(\d+)", prize_str)[0])
        p = Prize(x=p_x + 10000000000000, y=p_y + 10000000000000)
        machines.append(
            Machine(
                a=a,
                b=b,
                prize=p,
            )
        )

    result = 0
    for machine in machines:
        s = Solver()
        a = Int("a")
        b = Int("b")
        s.add(machine.prize.x == a * machine.a.x + b * machine.b.x)
        s.add(machine.prize.y == a * machine.a.y + b * machine.b.y)
        if sat == s.check():
            result += (
                s.model()[a].as_long() * machine.a.cost
                + s.model()[b].as_long() * machine.b.cost
            )
    return result


aoc = AoC(part_1_no_splitlines=part1, part_2_no_splitlines=part2)

inp = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
aoc.assert_p1(
    inp,
    expected=480,
)
aoc.submit_p1()
# aoc.assert_p2(
#     inp,
#     expected=None,
# )
aoc.submit_p2()
