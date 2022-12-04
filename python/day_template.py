def p1(data):
    pass


def p2(data):
    pass


def run(data):
    print(p1(data))
    print(p2(data))


def test_p1():
    data_raw = """
    """

    data_lines = [x.strip() for x in data_raw.split()]

    res = p1(data_lines)
    assert res == None


def test_p2():
    data_raw = """
    """

    data_lines = [x.strip() for x in data_raw.split()]

    res = p2(data_lines)
    assert res == None
