from collections import deque
from dataclasses import dataclass

from adventofcode import AoC


def prune(secret_num: int) -> int:
    return secret_num % 16777216


def mix(secret_num: int, num: int) -> int:
    return secret_num ^ num


def evolve(secret_num: int) -> int:
    secret_num = prune(mix(secret_num, secret_num * 64))
    secret_num = prune(mix(secret_num, secret_num // 32))
    secret_num = prune(mix(secret_num, secret_num * 2048))
    return secret_num


def part1(lines: list[str]):
    result = 0
    for line in lines:
        secret_num = int(line)
        for _ in range(2000):
            secret_num = evolve(secret_num)
        result += secret_num
    return result


@dataclass
class Buyer:
    seq_price: dict[tuple[int, int, int, int], int]


def part2(lines: list[str]):
    buyers: list[Buyer] = []
    for line in lines:
        secret_num = evolve(int(line))
        last_price = secret_num % 10
        seq = deque(maxlen=4)
        seq_price = {}
        for _ in range(2000):
            secret_num = evolve(secret_num)
            price = secret_num % 10
            seq.append(price - last_price)
            last_price = price
            if len(seq) == 4 and tuple(seq) not in seq_price:
                seq_price[tuple(seq)] = last_price
        buyers.append(
            Buyer(
                seq_price=seq_price,
            )
        )

    max_price_for_sequence = 0
    for k in buyers[0].seq_price.keys():
        max_price_for_sequence = max(
            max_price_for_sequence,
            sum(buyer.seq_price.get(k, 0) for buyer in buyers),
        )
    return max_price_for_sequence


aoc = AoC(part_1=part1, part_2=part2)

inp = """\
1
10
100
2024"""
aoc.assert_p1(
    inp,
    expected=37327623,
)
aoc.submit_p1()
inp = """\
1
2
3
2024"""
aoc.assert_p2(
    inp,
    expected=23,
)
aoc.submit_p2()
