from dataclasses import dataclass

import matplotlib.pyplot as plt
import networkx as nx
from adventofcode import AoC


@dataclass
class Wire:
    inp1_name: str
    inp2_name: str
    res_name: str
    op: str

    def run(self, results):
        if self.inp1_name not in results or self.inp2_name not in results:
            return
        inp1 = results[self.inp1_name]
        inp2 = results[self.inp2_name]
        if self.op == "AND":
            results[self.res_name] = inp1 & inp2
        elif self.op == "OR":
            results[self.res_name] = inp1 | inp2
        elif self.op == "XOR":
            results[self.res_name] = inp1 ^ inp2


def part1(lines: str):
    initial, operations = lines.strip().split("\n\n")
    results = {}
    zoutputs = set()
    for val in initial.split("\n"):
        name, value = val.split(": ")
        results[name] = int(value)
    wires = []
    for operation in operations.split("\n"):
        op, res_name = operation.split(" -> ")
        inp1, op, inp2 = op.split(" ")
        if res_name.startswith("z"):
            zoutputs.add(res_name)
        wires.append(Wire(inp1, inp2, res_name, op))
    zoutputs = sorted(zoutputs, reverse=True)
    while any(name not in results for name in zoutputs):
        for wire in wires:
            wire.run(results)
    return int("".join([str(results[name]) for name in zoutputs]), base=2)


def part2(lines: str):
    # ¯\_(ツ)_/¯

    


aoc = AoC(part_1_no_splitlines=part1, part_2_no_splitlines=part2)

inp = """\
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""
inp2 = """\
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
aoc.assert_p1(
    inp,
    expected=4,
)
aoc.assert_p1(
    inp2,
    expected=2024,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=None,
)
aoc.submit_p2()
