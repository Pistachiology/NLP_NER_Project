#!/usr/bin/python

import sys
from word_prefix_suffix import WordParser

OUTPUT_DIR = "output/"
if len(sys.argv) != 3:
    print "usage ./file answer.txt text_segment.txt"
    sys.exit(-1)


ans_filen = sys.argv[1]
text_segment_filen = sys.argv[2]

with open(ans_filen, "r") as f:
    answers = f.read().split("\n")


def dump_file(sentences, fn):
    output = ""
    for sentence in sentences:
        for word in sentence["words"]:
            output += '|'.join(word["word"])
            if word["class"] != "none":
                output += "({})".format(word["class"])
            output += "|"
        output += "\n"
    with open("{dir}/{fn}".format(dir=OUTPUT_DIR, fn=fn), "w") as f:
        f.write(output)
            
wp = WordParser("data")
it = 0

for _f in wp.files:
    data = wp._parse_file(wp._get_relative_path(_f))
    for sentence in data["sentences"]:
        for word in sentence["words"]:
            word['class'] = answers[it].split("\t")[-1].lower()
            it += 1
    dump_file(data["sentences"], _f)
    

# print answers[0].split("\t")
