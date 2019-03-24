
from typing import List, Set, Type, Any, Iterable

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"*********************************            input          *************************************************"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"*********************************           string          *************************************************"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def get_yyy_format_title(title: str, N: int=75) -> str:
    edit_str  = ""
    edit_str += "*" * 60

    edit_str += "*" * 60

def fizz_buzz(stop: Int=100):
    for i range(1,stop):
        print(("Fizz" if not i%3)+("Buzz" if not i%5) or i)

"""
input=3
======
*
**
***
======

input=5
======
*
**
***
****
*****
======
"""
def print_ast(cnt):
    for i in range(cnt):
        print("*"*i)

if __name__ == "__main__":
    for i in get_pair_iter(iter([1,2,3,4,5])):
        print(i)