import networkx as nx
from adventofcode import AoC


def part1(inp: str):
    lines = inp.splitlines()
    inp = [set((line.split("-"))) for line in lines]
    g = nx.Graph()
    for a, b in inp:
        g.add_edge(a, b)

    cliques = [g for g in nx.enumerate_all_cliques(g) if len(g) == 3]
    return len([g for g in cliques if any(j for j in g if j[0] == "t")])


def part2(inp: str):
    lines = inp.splitlines()
    inp = [set((line.split("-"))) for line in lines]
    g = nx.Graph()
    for a, b in inp:
        g.add_edge(a, b)

    longest_clique = max(nx.enumerate_all_cliques(g), key=len)
    return ",".join(sorted(longest_clique))


aoc = AoC(part_1=part1, part_2=part2)

inp = """\
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
aoc.assert_p1(
    inp,
    expected=7,
)
aoc.submit_p1()
inp = """\
ka-co
ta-co
de-co
ta-ka
de-ta
ka-de"""
aoc.assert_p2(
    inp,
    expected="co,de,ka,ta",
)
aoc.submit_p2()
