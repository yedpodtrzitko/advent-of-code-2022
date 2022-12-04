#!/usr/bin/env python

from pathlib import Path
import sys


def get_data(day):
    path_input = Path(__file__).parent.parent / "input" / f"day{day}"

    with open(str(path_input), "r") as f:
        data = f.read().split("\n")

    return data


if __name__ == "__main__":
    day = sys.argv[1]

    module = __import__(f"day{day}")
    module.run(get_data(day))
