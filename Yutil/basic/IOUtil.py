# coding: UTF-8

def input_line(type_= str):
    return list(map(type_, input().split()))


def print_2d_list(lst2):
    "¥n".join(["".join(str(v) for v in lst) for lst in lst2])

