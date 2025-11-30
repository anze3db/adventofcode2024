import heapq
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Generator

from adventofcode import AoC

E = (1, 0)
W = (-1, 0)
N = (0, 1)
S = (0, -1)


def draw(grid, path):
    max_x = max(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in path:
                print("O", end="")
            else:
                print(grid.get((x, y), "#"), end="")

        print()


def rotate(current) -> Generator[tuple[int, int], None, None]:
    if current == E:
        yield N
        yield S
    elif current == W:
        yield S
        yield N
    elif current == N:
        yield W
        yield E
    elif current == S:
        yield E
        yield W


@dataclass(order=True)
class State:
    pos: tuple[int, int]
    direction: tuple[int, int]
    path: tuple[tuple[int, int]] = field(default_factory=tuple)

    def rotate(self) -> Generator[tuple[int, int], None, None]:
        if self.direction == E:
            yield N
            yield S
        elif self.direction == W:
            yield S
            yield N
        elif self.direction == N:
            yield W
            yield E
        elif self.direction == S:
            yield E
            yield W

    def __hash__(self) -> int:
        return hash(
            (
                self.pos,
                self.direction,
                # self.path,
            )
        )


def part1(inp: str):
    lines = inp.splitlines()
    start = (0, 0)
    end = (0, 0)
    walls = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
            elif c == "#":
                walls.add((x, y))

    to_visit = [(0, State(start, E))]
    visited = set()
    while to_visit:
        score, current = heapq.heappop(to_visit)
        if current.pos == end:
            return score
        if (current.pos, current.direction) in visited:
            continue
        visited.add((current.pos, current.direction))
        next_pos = (
            current.pos[0] + current.direction[0],
            current.pos[1] + current.direction[1],
        )
        if next_pos not in walls:
            new_state = (score + 1, State(next_pos, current.direction))
            heapq.heappush(to_visit, new_state)
        for next_direction in current.rotate():
            new_state = (score + 1000, State(current.pos, next_direction))
            heapq.heappush(to_visit, new_state)


def count_parents(current: State, parents) -> set[tuple[int, int]]:
    visited = set([current.pos])
    visited_p = set([current])
    to_visit = parents[current].copy()
    while to_visit:
        current = to_visit.pop()
        visited.add(current.pos)
        visited_p.add(current)
        to_visit |= parents[current] - visited_p
    return visited


def part2(inp: str):
    lines = inp.splitlines()
    start = (0, 0)
    end = (0, 0)
    walls = set()
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
            elif c == "#":
                walls.add((x, y))

    to_visit = []
    heapq.heappush(to_visit, (0, State(start, E)))
    pathless_score = {State(start, E): 0}
    prev_states = {}
    while to_visit:
        score, current = heapq.heappop(to_visit)
        pos, direction = current.pos, current.direction
        if pos == end:

            def walk(state):
                pos = state.pos
                if pos == start:
                    yield [state]
                    return
                for prev_state in prev_states[state]:
                    for path in walk(prev_state):
                        yield path + [state]

            draw(grid, {pos.pos for path in walk(current) for pos in path})
            return len({pos.pos for path in walk(current) for pos in path})

        for neighbor in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_pos = (pos[0] + neighbor[0], pos[1] + neighbor[1])
            if next_pos in walls:
                continue

            if direction == neighbor:
                new_score = score + 1
            elif direction[0] == neighbor[0] and direction[1] != neighbor[1]:
                new_score = score + 1001
            elif direction[1] == neighbor[1] and direction[0] != neighbor[0]:
                new_score = score + 1001
            else:
                new_score = score + 2001

            prev_score = pathless_score.get(State(next_pos, neighbor), float("inf"))
            if new_score <= prev_score:
                pathless_score[State(next_pos, neighbor)] = new_score
                next_state = State(next_pos, neighbor)
                heapq.heappush(to_visit, (new_score, next_state))
                if next_state in prev_states:
                    prev_states[next_state].add(current)
                else:
                    prev_states[next_state] = set([current])


aoc = AoC(part_1=part1, part_2=part2)

inp = """\
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
inp2 = """\
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
aoc.assert_p1(
    inp,
    expected=7036,
)
aoc.assert_p1(
    inp2,
    expected=11048,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=45,
)
aoc.assert_p2(
    inp2,
    expected=64,
)
aoc.submit_p2()
