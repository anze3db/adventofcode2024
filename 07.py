from adventofcode import AoC


def concat(a, b):
    return int(str(a) + str(b))


def recursive_eval(
    target_value: int, current_value: int, remaining_numbers: list[int], operators
):
    if target_value < current_value:
        return False
    if not remaining_numbers:
        return current_value == target_value
    for operator in operators:
        if recursive_eval(
            target_value,
            operator(current_value, remaining_numbers[0]),
            remaining_numbers[1:],
            operators,
        ):
            return True
    return False


def part1(lines: list[str]):
    result = 0
    for line in lines:
        value, numbers = line.split(": ")
        value = int(value)
        numbers = list(map(int, numbers.split()))
        if recursive_eval(value, numbers[0], numbers[1:], [int.__add__, int.__mul__]):
            result += value
    return result


def part2(lines: list[str]):
    result = 0
    for line in lines:
        value, numbers = line.split(": ")
        value = int(value)
        numbers = list(map(int, numbers.split()))
        if recursive_eval(
            value, numbers[0], numbers[1:], [int.__add__, int.__mul__, concat]
        ):
            result += value
    return result


aoc = AoC(part_1=part1, part_2=part2)

inp = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
aoc.assert_p1(
    inp,
    expected=3749,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=11387,
)
aoc.submit_p2()
