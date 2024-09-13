x = 7

def myfun(val):
    print(f"Converting {val} to integer: {int(val)}.")

from .auxil import helper

def myfun10(val):
    print(f"Converting {val} to integer plus 10: {int(helper(val))}.")
