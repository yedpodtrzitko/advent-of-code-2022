def p1(data):
    elf_max = 0
    elf_sum = 0
    for line in data:
        if not line:
            elf_max = max(elf_sum, elf_max)
            elf_sum = 0
        else:
            elf_sum += int(line)
    return elf_max


def p2(data):
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


def run(data):
    print(p1(data))
    print(p2(data))
