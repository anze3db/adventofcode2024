from dataclasses import dataclass

from adventofcode import AoC

A = 4
B = 5
C = 6


class Computer:
    def __init__(self, program: list[int], reg_a: int, reg_b: int, reg_c: int):
        self.program = program
        self.instructions = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        self.registers: dict[int, int] = {
            A: reg_a,
            B: reg_b,
            C: reg_c,
        }
        self.instr_pointer = 0
        self.output = []

    def run(self):
        while self.instr_pointer < len(self.program):
            instr = self.program[self.instr_pointer]
            operand = self.program[self.instr_pointer + 1]
            self.instructions[instr](operand)
            self.instr_pointer += 2

    def combo_op(self, operand):
        if operand == 7:
            raise ValueError("Invalid program")
        if operand <= 3:
            return operand
        return self.registers[operand]

    def adv(self, operand):
        self.registers[A] = self.registers[A] // (2 ** self.combo_op(operand))

    def bxl(self, operand):
        self.registers[B] = self.registers[B] ^ operand

    def bst(self, operand):
        self.registers[B] = self.combo_op(operand) % 8

    def jnz(self, operand):
        if self.registers[A] == 0:
            return
        self.instr_pointer = operand - 2  # TODO: Possibly -2

    def bxc(self, operand):
        self.registers[B] = self.registers[B] ^ self.registers[C]

    def out(self, operand):
        self.output.append(self.combo_op(operand) % 8)

    def bdv(self, operand):
        self.registers[B] = self.registers[A] // (2 ** self.combo_op(operand))

    def cdv(self, operand):
        self.registers[C] = self.registers[A] // (2 ** self.combo_op(operand))


def part1(lines: str):
    registers, program = lines.split("\n\n")

    reg_a, reg_b, reg_c = [int(r[12:]) for r in registers.splitlines()]
    program = list(map(int, program.strip()[9:].split(",")))
    computer = Computer(program, reg_a, reg_b, reg_c)
    computer.run()
    return ",".join((map(str, computer.output)))


def part2(lines: str):
    _, program = lines.split("\n\n")
    program = list(map(int, program.strip()[9:].split(",")))
    result = []
    for i in range(1, 8):
        c = Computer(program, i, 0, 0)
        c.run()
        if c.output == c.program[-len(c.output) :]:
            result.append(i)

    cnt = 1
    while cnt < 16:
        new_result = []
        for a in result:
            a = a << 3
            for i in range(8):
                p = Computer(program, a + i, 0, 0)
                p.run()
                if p.output == p.program[-len(p.output) :]:
                    new_result.append(a + i)
        result = new_result
        cnt += 1
    return min(result)


aoc = AoC(part_1=part1, part_2=part2)

inp = """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
aoc.assert_p1(
    inp,
    expected="4,6,3,5,6,3,5,2,1,0",
)
aoc.submit_p1()
# inp2 = """\
# Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0"""
# aoc.assert_p2(
#     inp2,
#     expected=117440,
# )
aoc.submit_p2()
