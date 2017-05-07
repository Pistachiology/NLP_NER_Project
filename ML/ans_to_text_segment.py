#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print "usage ./file answer.txt text_segment.txt"
    sys.exit(-1)


ans_filen = sys.argv[1]
text_segment_filen = sys.argv[2]

with open(ans_filen, "r") as f:
    answers = f.read().split("\n")

print answers
