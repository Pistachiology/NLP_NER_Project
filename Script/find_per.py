#!/usr/bin/python
# - * - coding:utf-8 - * -

import os
import re
fronts = dict()
backs = dict()
commons = dict()

def is_empty(string):
    CountString = len(string)
    for character in string:
        if character != ' ':
            return False
    return True

def find_person():
    CountFronts = len(fronts)
    CountBacks = len(backs)
    directory = "/Users/idealphase/Desktop/3rd_2nd_term/NLP/NER/untag_per_v2_u8/"
    nameOfWholeFiles = os.listdir(directory)
    print "[+] List of files in directory",nameOfWholeFiles
    for nameOfFile in nameOfWholeFiles:
        print "[+] Open ",nameOfFile
        answer=""
        with open(directory+nameOfFile) as f:
            text = f.read()
            sentences = text.split('\n')
            del sentences[-1]
            for sentence in sentences:
                # -- Initial
                words = sentence.split('|')
                CountWords = len(words)
                isPerson = list()
                j=0
                while j<CountWords:
                    isPerson.append(False)
                    j+=1
                # -- End Initial

                # -- Processing with Suffix
                #print "Before Calculate suffix",isPerson
                i = 1 
                while(i<CountWords):
                    if words[i] != ' ':
                        words[i] = re.sub(r'\s+', '',words[i])
                    else:
                        words[i] = "SPACE"
                    if backs.has_key(words[i]) and is_empty(words[i])==False:
                        # -- Check front 5 words before suffix 
                        notAdded = True
                        k = 5
                        while k>1 and notAdded:
                            if i-k>=0 and fronts.has_key(words[i-k]):
                                j=k-1
                                while j>0:
                                    isPerson[i-j]=True
                                    j-=1
                                notAdded = False
                            k-=1
                        if notAdded:
                            isPerson[i-1]=True
                    i+=1  #Step next words
                #print "After Calculate suffix",isPerson 
                # -- End process with Suffix

                # -- Processing with Prefix
                #print "Before Calculate prefix",isPerson

                i =0
                while(i<CountWords):
                    if words[i] != ' ' :
                        words[i] = re.sub(r'\s+', '',words[i])
                    else :
                        words[i] = "SPACE"
                    #print words[i] , fronts.has_key(words[i])
                    if fronts.has_key(words[i])  and is_empty(words[i])==False and isPerson[i]==False :
                        # -- Check common word 
                        if (i+1 < CountWords) and isPerson[i+1]==False and words[i+1]== "SPACE":
                            if (i+2 < CountWords) and commons.has_key(words[i+2])==False:
                                isPerson[i+2]=True
                                if (i+3 < CountWords):
                                    if (i+4 <CountWords) and commons.has_key(words[i+4])==False:
                                        isPerson[i+3]=True
                                        isPerson[i+4]=True
                        if (i+1 < CountWords) and words[i+1]!="SPACE" and isPerson[i+1]==False and commons.has_key(words[i+1])==False:
                            isPerson[i+1]=True
                            if (i+2 <CountWords) and words[i+2] == 'SPACE':
                                if (i+3 <CountWords) and commons.has_key(words[i+3])==False:
                                    isPerson[i+2]=True
                                    isPerson[i+3]=True
                            

                    i+=1
                #print "After Calculate prefix",isPerson                                
                #End process with Prefix
                i = 0
                while(i<CountWords):
                    if words[i]=="SPACE":
                        words[i]=' '
                    if isPerson[i]==True:
                        answer+=words[i]+"(per)|"
                    else:
                        if words[i] != '' :
                            answer+=words[i]+"|"
                        else:
                            answer+=words[i]
                    i+=1
                answer+='\n'

            save_directory = "/Users/idealphase/Desktop/3rd_2nd_term/NLP/NER/person_tag_doing/"
            f2 = open(save_directory+nameOfFile,'wa')
            f2.write(answer)
            f2.close()

if __name__ == '__main__':
    f = open("./front_word_person.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for front in temp:
        fronts[re.sub(r'\s+','',front)]=True
    f.close()

    f = open("./back_word_person.txt","r")
    text = f.read()
    temp = text.split('\n')
    for back in temp:
        backs[re.sub(r'\s+','',back)]=True
    f.close()

    f = open("./common_utf8.txt","r")
    text = f.read()
    temp = text.split('\n')
    for common in temp:
        commons[re.sub(r'\s+','',common)]=True
    f.close()
    find_person()
