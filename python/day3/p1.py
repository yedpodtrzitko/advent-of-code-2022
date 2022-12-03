from pathlib import Path
from string import ascii_letters


def get_data(day: int):
    path_input = Path(__file__).parent.parent.parent / "input" / f"day{day}"

    with open(str(path_input), "r") as f:
        data = f.read().split("\n")

    return data


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


if __name__ == "__main__":
    file_data = get_data(3)
    print(p1(file_data))


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
