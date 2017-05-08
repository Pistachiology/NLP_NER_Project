#!/usr/bin/python
# -- coding: utf-8 --
import os
import json
import re
from word_prefix_suffix import WordParser

if __name__ == "__main__":
    word_parser = WordParser("tag_per_v2_u8")

    prefix_per = {}
    f = open("dictionary/front_word_person.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for t in temp:
        prefix_per[re.sub(r'\s+','',t)]=True
    f.close()

    prefix_org = {}
    f = open("dictionary/front_word_org.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for t in temp:
        prefix_org[re.sub(r'\s+','',t)]=True
    f.close()

    suffix_per = {}
    f = open("dictionary/back_word_person.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for t in temp:
        suffix_per[re.sub(r'\s+','',t)]=True
    f.close()

    suffix_org = {}
    f = open("dictionary/back_word_org.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for t in temp:
        suffix_org[re.sub(r'\s+','',t)]=True
    f.close()

    firstname = {}
    f = open("dictionary/firstname.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for t in temp:
        firstname[re.sub(r'\s+','',t)]=True
    f.close()

    lastname = {}
    f = open("dictionary/lastname.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for t in temp:
        lastname[re.sub(r'\s+','',t)]=True
    f.close()

    common = {}
    f = open("dictionary/common_utf8.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for t in temp:
        common[re.sub(r'\s+','',t)]=True
    f.close()

    name_org = {}
    f = open("dictionary/name_and_abbr_org.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for t in temp:
        name_org[re.sub(r'\s+','',t)]=True
    f.close()

    for i in range(len(word_parser.files)):
        data = word_parser._parse_file(word_parser._get_relative_path(word_parser.files[i]))
        for sentence in data["sentences"]:
            for word in sentence["words"]:
                for w in word["word"]:
                    w = re.sub(r'\s+', '',w)
                    if w == '':
                        print 'SPACE ' + 'none '*8 + word["class"].upper()
                        continue
                    out = ""
                    out += w + " "
                    if prefix_per.has_key(w):
                        out += "prefix_per "
                    else :
                        out += "none "
                    if suffix_per.has_key(w):
                        out += "suffix_per "
                    else :
                        out += "none "
                    if prefix_org.has_key(w):
                        out += "prefix_org "
                    else :
                        out += "none "
                    if suffix_org.has_key(w):
                        out += "suffix_org "
                    else :
                        out += "none "
                    if common.has_key(w):
                        out += "common "
                    else :
                        out += "none "
                    if name_org.has_key(w):
                        out += "org "
                    else :
                        out += "none "
                    if firstname.has_key(w):
                        out += "firstname "
                    else :
                        out += "none "
                    if lastname.has_key(w):
                        out += "lastname "
                    else :
                        out += "none "
                    if word["class"] != "loc":
                        out += word["class"].upper()
                    else:
                        out += "NONE"
                    print out
