#!/usr/bin/env python

from pathlib import Path


def get_data(day: int):
    path_input = Path(__file__).parent.parent.parent / "input" / f"day{day}"

    with open(str(path_input), "r") as f:
        data = f.read().split("\n")

    return data


def run(data):
    inventories = []
    elf_inv = []
    for line in data:
        if not line:
            inventories.append(elf_inv)
            elf_inv = []
        else:
            elf_inv.append(int(line))

    res = sorted(inventories, key=lambda x: sum(x), reverse=True)
    return sum([sum(x) for x in res[:3]])


if __name__ == '__main__':

    data = get_data(1)
    print(run(data))
