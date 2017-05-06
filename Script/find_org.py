#!/usr/bin/python
# - * - coding:utf-8 - * -

import os
import re
fronts = dict()
backs = dict()
commons = dict()
abbr_names = dict()

def is_empty(string):
    CountString = len(string)
    for character in string:
        if character != ' ':
            return False
    return True

def find_org():
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
                isOrg = list()
                j=0
                while j<CountWords:
                    isOrg.append(False)
                    j+=1
                # -- End Initial

                # -- Processing with Suffix
                i = 1 
                while(i<CountWords):
                    if words[i] != ' ':
                        words[i] = re.sub(r'\s+', '',words[i])
                    else:
                        words[i] = "SPACE"
                    if backs.has_key(words[i]) and is_empty(words[i])==False:
                        isOrg[i-1]=True
                    i+=1  #Step next words
                # -- End process with Suffix

                # -- Processing with Prefix
                i =0
                while(i<CountWords):
                    if words[i] != ' ' :
                        words[i] = re.sub(r'\s+', '',words[i])
                    else :
                        words[i] = "SPACE"
                    if fronts.has_key(words[i])  and is_empty(words[i])==False and isOrg[i]==False :
                        # -- Check common word 
                        if (i+1 < CountWords) and isOrg[i+1]==False:
                            isOrg[i+1]=True
                            '''
                            if (i+2 < CountWords) and commons.has_key(words[i+2])==False:
                                isOrg[i+2]=True
                                if (i+3 < CountWords):
                                    if (i+4 <CountWords) and commons.has_key(words[i+4])==False:
                                        isOrg[i+3]=True
                                        isOrg[i+4]=True
                        if (i+1 < CountWords) and words[i+1]!="SPACE" and isOrg[i+1]==False and commons.has_key(words[i+1])==False:
                            isOrg[i+1]=True
                            if (i+2 <CountWords) and words[i+2] == 'SPACE':
                                if (i+3 <CountWords) and commons.has_key(words[i+3])==False:
                                    isOrg[i+2]=True
                                    isOrg[i+3]=True
                        '''
                    i+=1
                # -- End process with Prefix

                # -- Processing with abbr and name
                i = 0
                while(i<CountWords):
                    if words[i] != ' ' :
                        words[i] = re.sub(r'\s+', '',words[i])
                    else :
                        words[i] = "SPACE"
                    if abbr_names.has_key(words[i]) and is_empty(words[i])==False and isOrg[i]==False:
                        isOrg[i]=True
                    i+=1
                # -- End process with abbr and name
                
                i = 0
                while(i<CountWords):
                    if words[i]=="SPACE":
                        words[i]=' '
                    if isOrg[i]==True:
                        answer+=words[i]+"(org)|"
                    else:
                        if words[i] != '' :
                            answer+=words[i]+"|"
                        else:
                            answer+=words[i]
                    i+=1
                answer+='\n'

            save_directory = "/Users/idealphase/Desktop/3rd_2nd_term/NLP/NER/org_tag_doing/"
            f2 = open(save_directory+nameOfFile,'wa')
            f2.write(answer)
            f2.close()

if __name__ == '__main__':
    f = open("./front_word_org.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for front in temp:
        fronts[re.sub(r'\s+','',front)]=True
    f.close()

    f = open("./back_word_org.txt","r")
    text = f.read()
    temp = text.split('\n')
    for back in temp:
        backs[re.sub(r'\s+','',back)]=True
    f.close()

    f = open("./name_and_abbr_org.txt","r")
    text = f.read()
    temp = text.split('\n')
    for abbr_name in temp:
        abbr_names[re.sub(r'\s+','',abbr_name)]=True
    f.close()

    f = open("./common_utf8.txt","r")
    text = f.read()
    temp = text.split('\n')
    for common in temp:
        commons[re.sub(r'\s+','',common)]=True
    f.close()
    find_org()
