#!/usr/bin/env python2
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        print "%s" % (line)
