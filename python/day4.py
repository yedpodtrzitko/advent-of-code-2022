import re


def p1(data):
    overlaps = 0
    re_match = re.compile(r"(\d+)\-(\d+),(\d+)\-(\d+)")

    for line in data:
        if not line:
            continue
        d1_from, d1_to, d2_from, d2_to = [int(x) for x in re_match.match(line).groups()]
        if d1_from <= d2_from and d1_to >= d2_to:
            overlaps += 1

        elif d1_from >= d2_from and d1_to <= d2_to:  # d1 is subset
            overlaps += 1

    return overlaps


def p2(data):
    overlaps = 0
    re_match = re.compile(r"(\d+)\-(\d+),(\d+)\-(\d+)")

    for line in data:
        if not line:
            continue
        d1_from, d1_to, d2_from, d2_to = [int(x) for x in re_match.match(line).groups()]

        if d1_from <= d2_from and d1_to >= d2_from:
            overlaps += 1

        elif d1_from >= d2_from and d1_from <= d2_to:
            overlaps += 1

    return overlaps


def run(data):
    print(p1(data))
    print(p2(data))


def test_p1():
    data_raw = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    data_lines = [x.strip() for x in data_raw.split()]

    res = p1(data_lines)
    assert res == 2


def test_p2():
    data_raw = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    data_lines = [x.strip() for x in data_raw.split()]

    res = p2(data_lines)
    assert res == 4
