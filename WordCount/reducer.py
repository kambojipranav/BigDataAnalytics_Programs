#!/usr/bin/env python
import sys

word_count = {}

for line in sys.stdin:
    word, count = line.strip().split("\t")
    count = int(count)
    word_count[word] = word_count.get(word, 0) + count

for word in word_count:
    print "%s\t%d" % (word, word_count[word])
