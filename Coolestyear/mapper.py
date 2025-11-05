#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    date, temp = line.split()
    year = date.split("-")[0]   # extract year
    print "%s\t%s" % (year, temp)
