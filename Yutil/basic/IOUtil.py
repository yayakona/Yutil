# coding: UTF-8

def input_line(type_= str):
    return list(map(type_, input().split()))


def print_2d_list(lst2):
    "¥n".join(["".join(str(v) for v in lst) for lst in lst2])

def get_list_from_file(path, encoding=“UTF-8”):
    with open(path, “r”, encoding=encoding) as f:
        return readlines.split()
