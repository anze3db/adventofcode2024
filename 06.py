from adventofcode import AoC


def part1(lines: list[str]):
    obstacles = set()
    guard = (0, 0)
    grid = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                guard = (x, y)
            if c == "#":
                obstacles.add((x, y))
            grid.add((x, y))
    visited = set()
    direction = (0, -1)
    while guard in grid:
        visited.add(guard)
        next_position = move(guard, direction)
        if next_position in obstacles:
            direction = rotate(direction)
            next_position = move(guard, direction)
        guard = next_position

    return len(visited)


def move(guard, direction):
    return (guard[0] + direction[0], guard[1] + direction[1])


def move_back(guard, direction):
    return (guard[0] - direction[0], guard[1] - direction[1])


def rotate(direction):
    if direction == (0, -1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (-1, 0)
    elif direction == (-1, 0):
        return (0, -1)


def draw(grid, guard, obstacles, new_obstacle):
    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) == guard:
                print("^", end="")
            elif (x, y) == new_obstacle:
                print("O", end="")
            elif (x, y) in obstacles:
                print("#", end="")
            elif (x, y) in grid:
                print(".", end="")
            else:
                print(" ", end="")
        print()
    print()


def part2(lines: list[str]):
    obstacles = set()
    guard = (0, 0)
    grid = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                original_guard = guard = (x, y)
            if c == "#":
                obstacles.add((x, y))
            grid.add((x, y))
    visited = set()
    direction = (0, -1)

    while guard in grid:
        next_position = move(guard, direction)
        while next_position in obstacles:
            direction = rotate(direction)
            next_position = move(guard, direction)

        guard = next_position
        visited.add(guard)

    obstructions = set()
    for new_obstacle in visited:
        new_obstacles = obstacles | {new_obstacle}

        direction = (0, -1)
        guard = original_guard

        states = set()
        while guard in grid:
            states.add((guard, direction))
            next_position = move(guard, direction)
            while next_position in new_obstacles:
                direction = rotate(direction)
                next_position = move(guard, direction)
            if (next_position, direction) in states:
                obstructions.add(new_obstacle)
                break
            guard = next_position
    return len(obstructions)


aoc = AoC(part_1=part1, part_2=part2)

inp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
aoc.assert_p1(
    inp,
    expected=41,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=6,
)
aoc.submit_p2()
