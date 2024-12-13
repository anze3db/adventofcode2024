from dataclasses import dataclass
from textwrap import dedent

from adventofcode import AoC


def in_clusters(point, clusters):
    for cluster in clusters:
        if point in cluster:
            return True
    return False


@dataclass
class Cluster:
    name: str
    points: set[tuple[int, int]]

    perimeter: int
    sides: int

    @property
    def area(self):
        return len(self.points)

    def __contains__(self, point):
        return point in self.points

    def explore(self, grid, point: tuple[int, int]):
        new_nodes = set()
        to_explore = {point}
        on_perimeter = set()
        while to_explore:
            x, y = to_explore.pop()
            # print(self.grid.get((x, y)))
            self.points.add((x, y))
            if (x, y) in new_nodes:
                continue
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                new_point = (x + dx, y + dy)
                p = grid.get(new_point)
                if p == self.name:
                    if new_point not in self.points:
                        to_explore.add(new_point)
                elif p is not None:
                    self.perimeter += 1
                    on_perimeter.add((x, y))
                    new_nodes.add(new_point)
                elif p is None:
                    self.perimeter += 1
                    on_perimeter.add((x, y))

        print(self.name, on_perimeter)

        return new_nodes


def part1(lines: list[str]):
    result = 0
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c

    to_visit = {(0, 0)}
    visited = set()
    clusters: list[Cluster] = []
    while to_visit:
        current = to_visit.pop()
        if current in visited:
            # already visited
            continue

        cluster = Cluster(name=grid[current], points=set(), perimeter=0, sides=0)
        clusters.append(cluster)
        new_nodes = cluster.explore(grid, current)
        to_visit.update(new_nodes)
        visited.update(cluster.points)

    for cluster in sorted(clusters, key=lambda c: c.name):
        result += cluster.area * cluster.perimeter
    return result


def part2(lines: list[str]):
    result = 0
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c

    to_visit = {(0, 0)}
    visited = set()
    clusters: list[Cluster] = []
    while to_visit:
        current = to_visit.pop()
        if current in visited:
            # already visited
            continue

        cluster = Cluster(name=grid[current], points=set(), perimeter=0, sides=0)
        clusters.append(cluster)
        new_nodes = cluster.explore(grid, current)
        to_visit.update(new_nodes)
        visited.update(cluster.points)

    for cluster in sorted(clusters, key=lambda c: c.name):
        result += cluster.area * cluster.sides
    return result


aoc = AoC(part_1=part1, part_2=part2)

inp = dedent("""\
        AAAA
        BBCD
        BBCC
        EEEC""")
inp2 = dedent("""\
    OOOOO
    OXOXO
    OOOOO
    OXOXO
    OOOOO""")
inp3 = dedent("""\
    RRRRIICCFF
    RRRRIICCCF
    VVRRRCCFFF
    VVRCCCJFFF
    VVVVCJJCFE
    VVIVCCJJEE
    VVIIICJJEE
    MIIIIIJJEE
    MIIISIJEEE
    MMMISSJEEE""")
inp4 = dedent("""\
    EEEEE
    EXXXX
    EEEEE
    EXXXX
    EEEEE""")
inp5 = dedent("""\
    AAAAAA
    AAABBA
    AAABBA
    ABBAAA
    ABBAAA
    AAAAAA""")
# aoc.assert_p1(
#     inp,
#     expected=140,
# )
# aoc.assert_p1(
#     inp2,
#     expected=772,
# )
# aoc.assert_p1(
#     inp3,
#     expected=1930,
# )
# aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=80,
)
aoc.assert_p2(
    inp2,
    expected=436,
)

aoc.assert_p2(
    inp4,
    expected=368,
)
aoc.assert_p2(
    inp5,
    expected=1206,
)
aoc.submit_p2()
