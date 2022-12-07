from collections import defaultdict
import re


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.subdirs = {}

    def add_file(self, node_name, size):
        self.files[node_name] = int(size)

    def take_subdir(self, node_name):
        if node_name in self.subdirs:
            return self.subdirs[node_name]

        self.subdirs[node_name] = Node(node_name, parent=self)
        return self.subdirs[node_name]

    def get_size(self) -> int:
        size = sum(self.files.values())
        for child_node in self.subdirs.values():
            size += child_node.get_size()
        return size

    def get_tree(self):
        for node in self.subdirs.values():
            yield node
            for subnode in node.get_tree():
                yield subnode


def p1(data):
    current_node = root_node = Node("/", None)
    for line in data[1:]:
        if line.startswith("$ cd"):
            dir_name = line[5:]
            if dir_name == "..":
                current_node = current_node.parent
                if not current_node:
                    raise Exception(f"no parent for {current_node.name}")
            else:
                current_node = current_node.take_subdir(dir_name)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            pass
        else:
            # file size
            size, file_name = line.split()
            current_node.add_file(file_name, size)

    small_dirs_sum = 0
    size_limit = 100_000
    for subdir in root_node.get_tree():
        if subdir.get_size() <= size_limit:
            small_dirs_sum += subdir.get_size()

    return small_dirs_sum


def p2(data):
    current_node = root_node = Node("/", None)
    for line in data[1:]:
        if line.startswith("$ cd"):
            dir_name = line[5:]
            if dir_name == "..":
                current_node = current_node.parent
                if not current_node:
                    raise Exception(f"no parent for {current_node.name}")
            else:
                current_node = current_node.take_subdir(dir_name)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            pass
        else:
            # file size
            size, file_name = line.split()
            current_node.add_file(file_name, size)

    space_total = 70_000_000
    space_taken = root_node.get_size()
    space_free = space_total - space_taken
    space_needed = 30_000_000
    space_to_delete = space_needed - space_free

    delete_candidate = root_node
    for subdir in root_node.get_tree():
        subdir_size = subdir.get_size()
        if subdir_size >= space_to_delete:
            if subdir_size <= delete_candidate.get_size():
                delete_candidate = subdir

    return delete_candidate.get_size()


def run(data):
    print(p1(data))
    print(p2(data))


def test_p1():
    data_expected = 95437

    data_raw = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines)
    assert res == data_expected


def test_p2():
    data_expected = 24933642

    data_raw = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p2(data_lines)
    assert res == data_expected
