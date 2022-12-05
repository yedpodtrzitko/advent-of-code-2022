from collections import defaultdict
import re


def p1(data):

    re_match = re.compile(r"move (\d+) from (\d+) to (\d+)")

    stacks = defaultdict(list)
    for line_idx, line in enumerate(data):
        if "[" not in line:
            break

        for idx in range(0, (len(line) // 3)):
            line_offset = idx * 4
            content = line[line_offset + 1 : line_offset + 2].strip()
            if content:
                stacks[idx + 1].insert(0, content)

            if line_offset > len(line):
                break

    for instruction in data[line_idx + 2 :]:
        if not instruction:
            break
        m_amount, m_from, m_to = re_match.match(instruction).groups()
        for _ in range(int(m_amount)):
            stacks[int(m_to)].append(stacks[int(m_from)].pop())

    stack_sorted = sorted(stacks.items())
    res = [v.pop() for (_, v) in stack_sorted]
    return "".join(res)


def p2(data):
    re_match = re.compile(r"move (\d+) from (\d+) to (\d+)")

    stacks = defaultdict(list)
    for line_idx, line in enumerate(data):
        if "[" not in line:
            break

        for idx in range(0, (len(line) // 3)):
            line_offset = idx * 4
            content = line[line_offset + 1 : line_offset + 2].strip()
            if content:
                stacks[idx + 1].insert(0, content)

            if line_offset > len(line):
                break

    for instruction in data[line_idx + 2 :]:
        if not instruction:
            break
        m_amount, m_from, m_to = re_match.match(instruction).groups()
        move = []
        for _ in range(int(m_amount)):
            move.append(stacks[int(m_from)].pop())

        stacks[int(m_to)].extend(move[::-1])

    stack_sorted = sorted(stacks.items())
    res = [v.pop() for (_, v) in stack_sorted]
    return "".join(res)


def run(data):
    print(p1(data))
    print(p2(data))


def test_p1():
    data_expected = "CMZ"

    data_raw = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines)
    assert res == data_expected


def test_p2():
    data_expected = "MCD"
    data_raw = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    data_lines = [x for x in data_raw.split("\n")][1:]

    res = p2(data_lines)
    assert res == data_expected
