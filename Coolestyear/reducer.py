#!/usr/bin/env python
import sys

year_min = {}

for line in sys.stdin:
    year, temp = line.strip().split("\t")
    temp = int(temp)

    # track the minimum temperature for each year
    if year not in year_min or temp < year_min[year]:
        year_min[year] = temp

# print coolest year & its minimum temperature
coolest_year = None
coolest_temp = None

for y in year_min:
    if coolest_temp is None or year_min[y] < coolest_temp:
        coolest_temp = year_min[y]
        coolest_year = y

print "%s\t%d" % (coolest_year, coolest_temp)
