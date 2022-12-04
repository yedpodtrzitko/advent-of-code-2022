from string import ascii_letters


def p1(data):
    priorities = 0
    for line in data:
        diameter = len(line) // 2
        c1, c2 = set(line[:diameter]), set(line[diameter:])

        overlap = c1.intersection(c2)
        prio = ascii_letters.index(overlap.pop()) + 1
        assert not overlap
        priorities += prio

    return priorities


def p2(data):
    priorities = 0
    group_size = 3
    offset = 0

    while group := data[offset : offset + group_size]:
        a, b, c = group
        overlap = set(a).intersection(set(b)).intersection(set(c))
        badge = overlap.pop()
        assert not overlap
        priorities += ascii_letters.index(badge) + 1
        offset += group_size

    return priorities


def run(data):
    print(p1(data))
    print(p2(data))


def test_d3_p1():
    data_raw = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    data_lines = [x.strip() for x in data_raw.split()]

    res = p1(data_lines)
    assert res == 157


def test_d3_p2():
    data_raw = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    data_lines = [x.strip() for x in data_raw.split()]

    res = p2(data_lines)
    assert res == 70
