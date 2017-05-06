#!/usr/bin/python
# - * - coding:utf-8 - * -

import os
import re
fronts = []
backs = []

def find_all_front():
    directory = "/Users/idealphase/Desktop/3rd_2nd_term/NLP/NER/Person_Clue_utf8/front/"
    nameOfWholeFiles = os.listdir(directory)
    print "[+] List of whole files in Person_Clue_utf8/front/ :" ,nameOfWholeFiles
    for nameOfFile in nameOfWholeFiles: 
        print "[+] Open ",nameOfFile
        with open(directory+nameOfFile) as f:
            text = f.read()
            words = text.split('\n')
            for word in words:
                fronts.append(word)
            f.close()

def find_all_back():
    directory = "/Users/idealphase/Desktop/3rd_2nd_term/NLP/NER/Person_Clue_utf8/back/"
    nameOfWholeFiles = os.listdir(directory)
    print "[+] List of whole files in Person_Clue_utf8/back/ :" ,nameOfWholeFiles
    for nameOfFile in nameOfWholeFiles: 
        print "[+] Open ",nameOfFile
        with open(directory+nameOfFile) as f:
            text = f.read()
            words = text.split('\n')
            for word in words:
                backs.append(word)
            f.close()

if __name__ == '__main__':
    find_all_front()
    f = open("./front_word_person.txt","w")
    t = ""
    for front in fronts:
        front = re.sub(r'\s+', '',front)
        t +=front+"\n"
    f.write(t)
    f.close

    find_all_back()
    f = open("./back_word_person.txt","w")
    t = ""
    for back in backs:
        back = re.sub(r'\s+', '',back)
        t +=back+"\n"
    f.write(t)
    f.close
