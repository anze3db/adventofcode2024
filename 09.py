from dataclasses import dataclass

from adventofcode import AoC


def part1(line: str):
    line = line.strip()
    result = 0
    disk = []
    is_file = True
    file_cnt = 0
    for c in line:
        size = int(c)
        if is_file:
            disk.append((file_cnt, size))
            file_cnt += 1
        else:
            disk.append(("F", size))
        is_file = not is_file

    file_pos = len(disk) - 1
    space_pos = 0
    file_ids = []
    while True:
        if file_pos < space_pos:
            break
        if disk[file_pos][0] == "F":
            file_pos -= 1
            continue
        elif disk[space_pos][0] != "F":
            file_ids.append(disk[space_pos])
            space_pos += 1
            continue
        if disk[file_pos][1] == disk[space_pos][1]:
            file_ids.append(disk[file_pos])
            file_pos -= 1
            space_pos += 1
        elif disk[file_pos][1] < disk[space_pos][1]:
            file_ids.append(disk[file_pos])
            disk[space_pos] = ("F", disk[space_pos][1] - disk[file_pos][1])
            file_pos -= 1
        elif disk[file_pos][1] > disk[space_pos][1]:
            file_ids.append((disk[file_pos][0], disk[space_pos][1]))
            disk[file_pos] = (disk[file_pos][0], disk[file_pos][1] - disk[space_pos][1])
            space_pos += 1

    block_id = 0
    cnt = 0
    for file_id, cnt in file_ids:
        for _ in range(cnt):
            result += block_id * file_id
            block_id += 1
    return result


@dataclass
class File:
    pos: int
    size: int
    file_id: int


@dataclass
class Space:
    pos: int
    size: int


def print_disk(disk: list[File | Space]):
    for f_or_s in sorted(disk, key=lambda s: s.pos):
        print(
            f"{f_or_s.pos=}, {f_or_s.size=}, {'space' if isinstance(f_or_s, Space) else f'{f_or_s.file_id}'}"
        )
    print()


def part2(line: str):
    line = line.strip()
    is_file = True
    file_id = 0

    files: list[File] = []
    spaces: list[Space] = []
    pos = 0
    for c in line:
        size = int(c)
        if is_file:
            files.append(File(pos, size, file_id))
            file_id += 1
        else:
            spaces.append(Space(pos, size))
        pos += size
        is_file = not is_file

    for f in reversed(files):
        for s in spaces:
            if s.size < f.size or f.pos < s.pos:
                continue

            f.pos = s.pos
            s.size -= f.size
            s.pos += f.size
            break

    result = 0
    for f in sorted(files, key=lambda f: f.pos):
        for i in range(f.size):
            result += f.file_id * (f.pos + i)
    return result


aoc = AoC(part_1=part1, part_2=part2)

inp = """2333133121414131402"""
aoc.assert_p1(
    inp,
    expected=1928,
)
aoc.submit_p1()
aoc.assert_p2(
    inp,
    expected=2858,
)
aoc.submit_p2()
