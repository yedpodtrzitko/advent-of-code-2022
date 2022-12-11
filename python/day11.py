from copy import copy
from math import floor, lcm


class Monkey:
    condition = None
    target_true = None
    target_false = None

    def __init__(self, op, div_test, cond_true, cond_false, items) -> None:
        self.items = items
        self.op = op
        self.div_test = div_test
        self.cond_true = cond_true
        self.cond_false = cond_false
        self.inspect_count = 0

    def catch(self, item):
        self.items.append(item)

    def throw(self, item):
        self.inspect_count += 1
        self.items.remove(item)
        return item

    def get_worry_level(self, old):
        res = eval(self.op)
        return res

    def get_throw_target(self, worry):
        if worry % self.div_test:
            return self.cond_false
        return self.cond_true


def p1(data):

    monkeys = {}
    for monkey_block in range(0, 100, 7):
        lines = data[monkey_block : monkey_block + 7]
        if not lines:
            break

        monkey_idx = int(lines[0].rstrip(":")[len("Monkey ") :])
        items_str = lines[1].strip()[len("Starting items: ") :]
        items = [int(x.strip()) for x in items_str.split(",")]
        op = lines[2].strip()[len("Operation: new = ") :]
        div_test = int(lines[3].strip()[len("Test: divisible by ") :])
        cond_true = int(lines[4].strip()[len("If true: throw to monkey ") :])
        cond_false = int(lines[5].strip()[len("If true: throw to monkey ") :])
        monkey = Monkey(
            op=op,
            div_test=div_test,
            cond_true=cond_true,
            cond_false=cond_false,
            items=items,
        )
        monkeys[monkey_idx] = monkey

    for rnd in range(20):
        for monkey_idx in range(len(monkeys)):
            monkey = monkeys[monkey_idx]
            items = copy(monkey.items)
            for item in items:
                throw_item = monkey.throw(item)
                throw_item = floor(monkey.get_worry_level(throw_item) / 3)

                target_idx = monkey.get_throw_target(throw_item)
                target_monkey = monkeys[target_idx]

                target_monkey.catch(throw_item)

    ins_count = [x.inspect_count for x in monkeys.values()]
    ins_count.sort(reverse=True)
    return ins_count[0] * ins_count[1]


def p2(data):
    monkeys = {}
    for monkey_block in range(0, 100, 7):
        lines = data[monkey_block : monkey_block + 7]
        if not lines:
            break

        monkey_idx = int(lines[0].rstrip(":")[len("Monkey ") :])
        items_str = lines[1].strip()[len("Starting items: ") :]
        items = [int(x.strip()) for x in items_str.split(",")]
        op = lines[2].strip()[len("Operation: new = ") :]
        div_test = int(lines[3].strip()[len("Test: divisible by ") :])
        cond_true = int(lines[4].strip()[len("If true: throw to monkey ") :])
        cond_false = int(lines[5].strip()[len("If true: throw to monkey ") :])
        monkey = Monkey(
            op=op,
            div_test=div_test,
            cond_true=cond_true,
            cond_false=cond_false,
            items=items,
        )
        monkeys[monkey_idx] = monkey

    modulus = lcm(*[x.div_test for x in monkeys.values()])

    for rnd in range(10000):

        for monkey_idx in range(len(monkeys)):
            monkey = monkeys[monkey_idx]
            items = copy(monkey.items)
            for item in items:
                throw_item = monkey.throw(item)
                throw_item = floor(monkey.get_worry_level(throw_item)) % modulus

                target_idx = monkey.get_throw_target(throw_item)
                target_monkey = monkeys[target_idx]
                target_monkey.catch(throw_item)

    ins_count = [x.inspect_count for x in monkeys.values()]
    ins_count.sort(reverse=True)
    return ins_count[0] * ins_count[1]


def run(data):
    print(p1(data))
    print(p2(data))


def test_p1():
    data_expected = 10605

    data_raw = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines)
    assert res == data_expected


def test_p2():
    data_expected = 2713310158

    data_raw = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p2(data_lines)
    assert res == data_expected
