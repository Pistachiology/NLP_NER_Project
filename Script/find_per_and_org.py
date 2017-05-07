#!/usr/bin/python
# - * - coding:utf-8 - * -

import os
import re
fronts_per = dict()
backs_per = dict()
fronts_org = dict()
backs_org = dict()
abbr_names = dict()
commons = dict()

def is_empty(string):
    CountString = len(string)
    for character in string:
        if character != ' ':
            return False
    return True

def find_person_and_org():
    directory = "../Data/untag_per_v2_u8/"
    nameOfWholeFiles = os.listdir(directory)
    print "[+] List of files in directory",nameOfWholeFiles
    for nameOfFile in nameOfWholeFiles:
        print "[+] Open ",nameOfFile
        print "[+] Calculating Person ..."
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
                isOrg = list()
                j=0
                while j<CountWords:
                    isPerson.append(False)
                    isOrg.append(False)
                    j+=1
                # -- End Initial
                # --> Person
                # -- Processing with Suffix
                #print "Before Calculate suffix",isPerson
                i = 1 
                while(i<CountWords):
                    if words[i] != ' ':
                        words[i] = re.sub(r'\s+', '',words[i])
                    else:
                        words[i] = "SPACE"
                    if backs_per.has_key(words[i]) and is_empty(words[i])==False:
                        # -- Check front 5 words before suffix 
                        notAdded = True
                        k = 5
                        while k>1 and notAdded:
                            if i-k>=0 and fronts_per.has_key(words[i-k]):
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
                    if fronts_per.has_key(words[i])  and is_empty(words[i])==False and isPerson[i]==False :
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
                
                # -- Org
                # ---- Suffix
                i = 1
                while(i<CountWords):
                    if words[i] != ' ':
                        words[i] = re.sub(r'\s+','',words[i])
                    else:
                        words[i] = "SPACE"
                    if backs_org.has_key(words[i]) and is_empty(words[i])==False:
                        isOrg[i+1]=True
                    i+=1

                # ---- Prefix
                i = 0
                while(i<CountWords):
                    if words[i] != ' ':
                        words[i] = re.sub(r'\s+','',words[i])
                    else:
                        words[i] = "SPACE"
                    if fronts_org.has_key(words[i]) and is_empty(words[i])==False and isOrg[i]==False:
                        if i+1<CountWords and isOrg[i+1]==False:
                            isOrg[i+1]=True
                    i+=1

                # ---- Name and Abbr
                i = 0
                while(i<CountWords):
                    if words[i] != ' ':
                        words[i] = re.sub(r'\s+','',words[i])
                    else:
                        words[i] = "SPACE"
                    if abbr_names.has_key(words[i]) and is_empty(words[i])==False and isOrg[i]==False:
                        isOrg[i]=True
                    i+=1


                #  -- Print
                i = 0
                while(i<CountWords):
                    if words[i]=="SPACE":
                        words[i]=' '
                    if isPerson[i]==True and isOrg[i]==True:
                        answer+=words[i]+"(per)(org)|"
                    elif isPerson[i]==True:
                        answer+=words[i]+"(per)|"
                    elif isOrg[i]==True:
                        answer+=words[i]+"(org)|"
                    else:
                        if words[i] != '' :
                            answer+=words[i]+"|"
                        else:
                            answer+=words[i]
                    i+=1
                answer+='\n'

            save_directory = "../Result/person_and_org/"
            f2 = open(save_directory+nameOfFile,'wa')
            f2.write(answer)
            f2.close()

if __name__ == '__main__':
    f = open("../Dictionary/front_word_person.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for front in temp:
        fronts_per[re.sub(r'\s+','',front)]=True
    f.close()

    f = open("../Dictionary/back_word_person.txt","r")
    text = f.read()
    temp = text.split('\n')
    for back in temp:
        backs_per[re.sub(r'\s+','',back)]=True
    f.close()

    f = open("../Dictionary/common_utf8.txt","r")
    text = f.read()
    temp = text.split('\n')
    for common in temp:
        commons[re.sub(r'\s+','',common)]=True
    f.close()

    f = open("../Dictionary/front_word_org.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for front in temp:
        fronts_org[re.sub(r'\s+','',front)]=True
    f.close()

    f = open("../Dictionary/back_word_org.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for front in temp:
        backs_org[re.sub(r'\s+','',front)]=True
    f.close()

    f = open("../Dictionary/name_and_abbr_org.txt","r")
    text = f.read() 
    temp = text.split('\n')
    for abbr in temp:
        abbr_names[re.sub(r'\s+','',abbr)]=True
    f.close()

    find_person_and_org()
