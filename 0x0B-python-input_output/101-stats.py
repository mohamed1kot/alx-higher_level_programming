#!/usr/bin/python3


import sys

file_size = 0
status_tally = {}
count = 0
for line in sys.stdin:
    words = line.split()
    if (words[-2] in status_tally):
        status_tally[words[-2]] += 1
        count += 1
        file_size += int(words[-1])
    else:
        status_tally[words[-2]] = 1
        count += 1
    if (count % 10 == 0):
        print(f"File size: {file_size}")
        for key, value in sorted(status_tally.items()):
            print(f"{key}: {value}")
