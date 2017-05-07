
import sys
from ML.word_prefix_suffix import WordParser

OUTPUT_DIR = "final_output"

def dump_file(sentences, fn):
    output = ""
    for sentence in sentences:
        for word in sentence["words"]:
            output += '|'.join(word["word"])
            if word["class"] != "none":
                output += "({})".format(word["class"])
            output += "|"
        output += "\n"
    output = output[:-1]
    with open("{dir}/{fn}".format(dir=OUTPUT_DIR, fn=fn), "w") as f:
        f.write(output)

def do_merge(pattern_file, ml_file, output_file=None):
    wp = WordParser("Data")
    ptn = wp._parse_file(pattern_file)
    ml = wp._parse_file(ml_file)
    sentences = [] 

    for i in range(len(ptn["sentences"])):
        words = []
        for j in range(len(ptn["sentences"][i]["words"])):
            wptn = ptn["sentences"][i]["words"][j]
            wml = ml["sentences"][i]["words"][j]
            # assert(wptn["word"] == wml["word"])
            if wptn["class"] != "none":
		wclass = wptn["class"].lower()
            elif wml["class"] != "none":
                wclass = wml["class"].lower()
            word = { "word": wptn["word"], "class": wclass } 
            words.append(word)
        sentences.append( { "words": words } )

    dump_file(sentences, output_file)
            
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "Usage ./file pattern_file ml_file out_file"
        sys.exit(-1)


    pattern_file = sys.argv[1]
    ml_file = sys.argv[2]
    out_file = sys.argv[3]

    do_merge(pattern_file, ml_file, out_file)
