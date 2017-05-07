#!/usr/bin/python
# -- coding: utf-8 --
import os
import json
import re

def print_words(words):
    print "[ %s ] " % ','.join(words)

class WordParser:

    SEPARATE_TYPE = ["loc", "per", "org"]
    SINGLE_TYPE = ["per", "org", "loc"]

    @staticmethod
    def is_in_separate_type(word):
        for _type in WordParser.SEPARATE_TYPE:
            if "({_type}_start)".format(_type=_type) in word:
                return _type
        return False

    @staticmethod
    def is_in_single_type(word):
        for _type in WordParser.SINGLE_TYPE:
            if "({_type})".format(_type=_type) in word:
                return _type
        return False
    
    def __init__(self, inp, tokenNormalizer=None):
        self.foldername = inp
        if not os.path.isdir(inp):
            raise("Directory {} not founded :(".format(inp))
        self.files = [f for f in os.listdir(inp) if os.path.isfile(os.path.join(inp, f))]

    def _get_relative_path(self, filename):
        return "{}/{}".format(self.foldername, filename)

    def _get_absolute_path(self, filename):
        return os.path.abspath(self._get_relative_path(filename))

    def _parse_file(self, filename):
        with open(filename, "r") as f:
            content = f.read()
        sentences = content.split("\n")
        i = 0
        parsed_sentences = []
        for idx, sentence in enumerate(sentences):
            parsed_sentences.append({
                "idx": idx,
                "words": self._parse_sentence(sentence)
                })
        return {
                "sentences": parsed_sentences
               }

    def _parse_sentence(self, sentence):
        parsed_sentence = []
        words = sentence.split("|")
        if len(words) and words[0] == "":
            words = words[1:]
        if len(words) and words[-1] == "":
            words = words[:-1]

        skip_ = 0
        for idx, word in enumerate(words):
            if skip_ > 0: 
                skip_ -= 1
                continue
            if WordParser.is_in_separate_type(word):
                _type = WordParser.is_in_separate_type(word)
                for rev_idx in range(idx, len(words)):
                    if "({}_end)".format(_type) in words[rev_idx]:
                        break
                    
                new_word = []
                for word in words[idx:rev_idx + 1]:
                    new_word.append(word.rstrip("({}_end)".format(_type)).rstrip("({}_start)".format(_type))
                            .rstrip("({}_con)".format(_type)).rstrip("({})".format(_type)))
                parsed_sentence.append({
                    "word": new_word,
                    "class": _type
                    })
                skip_ = rev_idx - idx
            elif WordParser.is_in_single_type(word):
                _type = WordParser.is_in_single_type(word)
                parsed_sentence.append({
                    "word": [word.rstrip("({})".format(_type))],
                    "class": _type
                    })
            else:
                parsed_sentence.append({
                    "word": [word],
                    "class": "NONE"
                    })

        return parsed_sentence

if __name__ == "__main__":
    word_parser = WordParser("data")

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
                        print 'SPACE ' + 'none '*8
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
                        out += "none"
                    print out
