#!/usr/bin/env python
import sys

d = {}

for line in sys.stdin:
    bigram, count = line.strip().split("\t")
    count = int(count)
    d[bigram] = d.get(bigram, 0) + count   # accumulate

for k in d:
    print "%s\t%d" % (k, d[k])
