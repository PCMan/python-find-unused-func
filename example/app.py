import sys  # deliberate unused import
import json  # deliberate unused import

import demo
import demo2
from demo2 import used_func2, used_func3

def main():
    demo.used_func1()
    for i in range(10):
        used_func2()
        used_func3()

def unused_func0():
    pass

# Limitation: unused recursive functions are not detected
def unuesd_recursive():
    unuesd_recursive()

if __name__ == '__main__':
    main()
