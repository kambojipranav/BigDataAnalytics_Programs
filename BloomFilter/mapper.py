#!/usr/bin/env python
import sys

# Hash functions
def h1(x):
    return (2 * x) % 13

def h2(x):
    return (x + 15) % 13

def h3(x):
    return (x * 3 + 17) % 13

# Read numbers from input and emit hashed positions
for line in sys.stdin:
    x = int(line.strip())
    positions = [h1(x), h2(x), h3(x)]

    for p in positions:
        print "%s\t%s" % (p, 1)
