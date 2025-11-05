#!/usr/bin/env python2
import sys

def hash_func(val):
    asci_sum = 0
    for c in val:
        asci_sum += ord(c)
    # small hash for demo lab
    return (asci_sum * 6) % 21

def count_trailing_zeros(num):
    if num == 0:
        return 0
    count = 0
    while num % 2 == 0:
        count += 1
        num = num // 2
    return count

max_trail = 0

for ele in sys.stdin:
    ele = ele.strip()
    if not ele:
        continue
    hashed = hash_func(ele)
    trail = count_trailing_zeros(hashed)
    if trail > max_trail:
        max_trail = trail

# FM Estimate = 2^(max_trailing_zeros)
estimate = 2 ** max_trail
print "%d" % (estimate)
