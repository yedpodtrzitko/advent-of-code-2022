#!/usr/bin/env python

from pathlib import Path


def get_data(day: int):
    path_input = Path(__file__).parent.parent.parent / "input" / f"day{day}"

    with open(str(path_input), "r") as f:
        data = f.read().split("\n")

    return data


def run(data):
    elf_max = 0
    elf_sum = 0
    for line in data:
        if not line:
            elf_max = max(elf_sum, elf_max)
            elf_sum = 0
        else:
            elf_sum += int(line)
    return elf_max

if __name__ == '__main__':
    data = get_data(1)
    print(run(data))