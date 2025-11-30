from dataclasses import dataclass

from adventofcode import AoC

pos_dict = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}


def part1(lines: str):
    result = 0
    grid, moves = lines.split("\n\n")
    grid = grid.splitlines()
    pos = (0, 0)
    walls = set()
    boxes = set()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                pos = (x, y)
            elif cell == "#":
                walls.add((x, y))
            elif cell == "O":
                boxes.add((x, y))

    for move in moves:
        if move == "\n":
            continue
        next_pos = (pos[0] + pos_dict[move][0], pos[1] + pos_dict[move][1])
        if next_pos in walls:
            continue
        elif next_pos in boxes:
            next_next_pos = next_pos
            while True:
                next_next_pos = (
                    next_next_pos[0] + pos_dict[move][0],
                    next_next_pos[1] + pos_dict[move][1],
                )
                if next_next_pos in walls:
                    break
                elif next_next_pos in boxes:
                    continue
                else:
                    boxes.remove(next_pos)
                    boxes.add(next_next_pos)
                    pos = next_pos
                    break

        else:
            pos = next_pos

    for x, y in boxes:
        result += 100 * y + x
    return result


@dataclass
class Box:
    point1: tuple[int, int]
    point2: tuple[int, int]

    def __hash__(self) -> int:
        return id(self)


def boxes_to_move(box, move, walls, box_points) -> set[Box] | None:
    next_pos1 = (box.point1[0] + pos_dict[move][0], box.point1[1] + pos_dict[move][1])
    next_pos2 = (box.point2[0] + pos_dict[move][0], box.point2[1] + pos_dict[move][1])

    if next_pos1 in walls or next_pos2 in walls:
        return None

    to_move: set[Box] = {box}
    if next_pos1 in box_points:
        if box_points[next_pos1] is not box:
            boxes = boxes_to_move(box_points[next_pos1], move, walls, box_points)
            if boxes is None:
                return None
            to_move |= boxes

    if next_pos2 in box_points and box_points[next_pos2] is not box_points.get(
        next_pos1
    ):
        if box_points[next_pos2] is not box:
            boxes = boxes_to_move(box_points[next_pos2], move, walls, box_points)
            if boxes is None:
                return None
            to_move |= boxes
    return to_move


def draw(walls, box_points, pos):
    min_x = min(w[0] for w in walls)
    max_x = max(w[0] for w in walls)
    min_y = min(w[1] for w in walls)
    max_y = max(w[1] for w in walls)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) in box_points:
                box = box_points[(x, y)]
                if (x, y) == box.point1:
                    print("[", end="")
                elif (x, y) == box.point2:
                    print("]", end="")
            elif (x, y) == pos:
                print("@", end="")
            else:
                print(".", end="")
        print()


def part2(lines: str):
    result = 0
    grid, moves = lines.split("\n\n")
    grid = grid.splitlines()
    pos = (0, 0)
    walls = set()
    boxes = set()
    box_points = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pos1 = (x * 2, y)
            pos2 = (x * 2 + 1, y)
            if cell == "@":
                pos = pos1
            elif cell == "#":
                walls.add(pos1)
                walls.add(pos2)
            elif cell == "O":
                box = Box(pos1, pos2)
                boxes.add(box)
                box_points[pos1] = box
                box_points[pos2] = box

    for move in moves:
        if move == "\n":
            continue
        next_pos = (pos[0] + pos_dict[move][0], pos[1] + pos_dict[move][1])
        if next_pos in walls:
            continue
        elif next_pos in box_points:
            to_move = boxes_to_move(box_points[next_pos], move, walls, box_points)
            if to_move is None:
                continue
            for box_to_move in to_move:
                del box_points[box_to_move.point1]
                del box_points[box_to_move.point2]
            for box_to_move in to_move:
                next_pos1 = (
                    box_to_move.point1[0] + pos_dict[move][0],
                    box_to_move.point1[1] + pos_dict[move][1],
                )
                next_pos2 = (
                    box_to_move.point2[0] + pos_dict[move][0],
                    box_to_move.point2[1] + pos_dict[move][1],
                )
                box_points[next_pos1] = box_to_move
                box_points[next_pos2] = box_to_move
                box_to_move.point1 = next_pos1
                box_to_move.point2 = next_pos2
        pos = next_pos

    result = 0
    for box in boxes:
        result += 100 * box.point1[1] + box.point1[0]
    return result


aoc = AoC(part_1=part1, part_2=part2)

inp = """\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
inp0 = """\
#######
#...O..
#......

"""
inp2 = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

aoc.assert_p1(
    inp0,
    expected=104,
)
aoc.assert_p1(
    inp,
    expected=2028,
)
aoc.assert_p1(
    inp2,
    expected=10092,
)
aoc.submit_p1()
aoc.assert_p2(
    inp2,
    expected=9021,
)
aoc.submit_p2()
