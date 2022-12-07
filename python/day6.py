from collections import defaultdict
import re
import pytest


def p1(data):
    for idx in range(len(data)):
        if len(set(data[idx : idx + 4])) == 4:
            return idx + 4


def p2(data):
    for idx in range(len(data)):
        if len(set(data[idx : idx + 14])) == 14:
            return idx + 14


def run(data):
    print(p1(data[0]))
    print(p2(data[0]))


@pytest.mark.parametrize(
    ["data_input", "data_expected"],
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_p1(data_input, data_expected):
    res = p1(data_input)
    assert res == data_expected


@pytest.mark.parametrize(
    ["data_input", "data_expected"],
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_p2(data_input, data_expected):
    res = p2(data_input)
    assert res == data_expected
