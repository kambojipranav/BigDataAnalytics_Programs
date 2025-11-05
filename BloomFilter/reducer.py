#!/usr/bin/env python
import sys, math

bit_arr = [0] * 13  
coll = 0            
for line in sys.stdin:
    pos, val = line.strip().split('\t')
    pos = int(pos)
    if bit_arr[pos] == 1:
        coll += 1 

    bit_arr[pos] = 1  # Set bit

x = 4   # number of inserted elements (modify if needed)
z = 3   # number of hash functions
print "Number of Collisions:", coll

# False positive probability formula
fp = (1 - math.exp(-z * x / float(len(bit_arr)))) ** z
print "False Positive Probability:", fp
