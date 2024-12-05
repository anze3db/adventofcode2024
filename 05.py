from adventofcode import AoC


def part1(lines: str):
    result = 0
    ordering, pages = lines.split("\n\n")
    ordering = set(tuple(map(int, line.split("|"))) for line in ordering.splitlines())
    pages = [list(map(int, line.split(","))) for line in pages.splitlines()]
    for page in pages:
        for i, update in enumerate(page):
            for j, update2 in enumerate(page):
                if i == j:
                    continue
                if i < j and (update2, update) in ordering:
                    break
                if i > j and (update, update2) in ordering:
                    break
            else:
                continue
            break
        else:
            result += page[len(page) // 2]
    return result


def part2(lines: str):
    result = 0
    ordering, pages = lines.split("\n\n")
    ordering = set(tuple(map(int, line.split("|"))) for line in ordering.splitlines())
    pages = [list(map(int, line.split(","))) for line in pages.splitlines()]
    for page in pages:
        incorrect = False
        for i in range(len(page)):
            for j in range(len(page)):
                if i == j:
                    continue
                if i < j and (page[j], page[i]) in ordering:
                    incorrect = True
                    page[i], page[j] = page[j], page[i]
                if i > j and (page[i], page[j]) in ordering:
                    incorrect = True
                    page[i], page[j] = page[j], page[i]
        if incorrect:
            result += page[len(page) // 2]
    return result


aoc = AoC(part_1_no_splitlines=part1, part_2_no_splitlines=part2)

inp = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
aoc.assert_p1(
    inp,
    expected=143,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=123,
)
aoc.submit_p2()
