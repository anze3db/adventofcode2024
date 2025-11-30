from collections import defaultdict, deque
from functools import cache
from itertools import pairwise

from adventofcode import AoC

numerical = """\
789
456
123
 0A"""

directional = """\
 ^A
<v>"""

# FROMTOMOVE
paths = """\
A0<
A3^
0A>
02^
3Av
32<
36^
20v
21<
23>
25^
12>
14^
63v
65<
69^
52v
54<
56>
58^
41v
45>
47^
96v
98<
89>
85v
87<
78>
74v
A^<
A>v
^A>
^vv
<v>
v<<
v^^
v>>
>A^
>v<"""
p = defaultdict(list)
for path in paths.splitlines():
    frm, to, res = path
    p[frm].append((to, res))


def search(frm: str, to: str) -> list[str]:
    q = deque([(frm, [])])
    paths = []
    shortest = None
    while q:
        frm, path = q.popleft()
        if frm == to:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                paths.append("".join(path + ["A"]))
            continue
        if shortest and len(path) >= shortest:
            continue
        for nxt, step in p[frm]:
            q.append((nxt, path + [step]))
    return paths


@cache
def dfs(path: str, level: int):
    result = 0
    seq = "A" + path
    for frm, to in pairwise(seq):
        paths = search(frm, to)
        if level == 0:
            result += min(len(path) for path in paths)
        else:
            result += min(dfs(path, level - 1) for path in paths)
    return result


def part1(inp: str):
    lines = inp.splitlines()
    result = 0

    for code in lines:
        result += dfs(code, 2) * int(code[:-1])

    return result


def part2(inp: str):
    lines = inp.splitlines()
    result = 0

    for code in lines:
        result += dfs(code, 25) * int(code[:-1])

    return result


aoc = AoC(part_1=part1, part_2=part2)

inp = """\
029A
980A
179A
456A
379A"""
aoc.assert_p1(
    inp,
    expected=126384,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=154115708116294,
)
aoc.submit_p2()
