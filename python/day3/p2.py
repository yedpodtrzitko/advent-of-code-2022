from pathlib import Path
from string import ascii_letters


def get_data(day: int):
    path_input = Path(__file__).parent.parent.parent / "input" / f"day{day}"

    with open(str(path_input), "r") as f:
        data = f.read().split("\n")

    return data


def run(data):
    priorities = 0
    group_size = 3
    offset = 0

    while group := data[offset:offset+group_size]:
        a,b,c = group
        overlap = set(a).intersection(set(b)).intersection(set(c))
        badge = overlap.pop()
        assert not overlap
        priorities += ascii_letters.index(badge) + 1
        offset += group_size

    return priorities


if __name__ == "__main__":
    file_data = get_data(3)
    print(run(file_data))


def test_d3_p2():
    data_raw = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    data_lines = [x.strip() for x in data_raw.split()]

    res = run(data_lines)
    assert res == 70
