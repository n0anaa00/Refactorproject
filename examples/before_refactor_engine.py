import os
import sys

def calc(a, b):
    if a > b:
        if b != 0:
            return a / b
    else:
        return a * b

print(calc(5, 0))