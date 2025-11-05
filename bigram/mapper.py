#!/usr/bin/env python
import sys

for line in sys.stdin:
    words = line.strip().split()
    for i in range(len(words)-1):
        bigram = words[i] + "_" + words[i+1]
        print "%s\t1" % bigram
