#!/usr/bin/python
# -- coding: utf-8 --

import os

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
        words = words[1:-1]
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
                    "class": "none"
                    })

        return parsed_sentence


if __name__ == "__main__":
    word_parser = WordParser("tag_per_v2_u8")
    #print word_parser._parse_file(word_parser._get_relative_path(word_parser.files[0]))
    string = word_parser._parse_file(word_parser._get_relative_path(word_parser.files[0]))
    for sentences in string['sentences']:
        for words in sentences['words']:
            print words
            #if (words['class'] is "per"):
            #    print words['word'][0]
