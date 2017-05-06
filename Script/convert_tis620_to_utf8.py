#!/usr/bin/python
# - * - coding:utf-8 - * -

import os
docs_name = ['OrgAll','Person_Clue']

for doc_name in docs_name:
    directory = "/Users/idealphase/Desktop/3rd_2nd_term/NLP/NER/"+doc_name+"/"
    nameOfWholeFiles = os.listdir(directory)
    print "[+] List of whole files in working directory :" ,nameOfWholeFiles
    for nameOfFile in nameOfWholeFiles: 
        print "[+] Open ",nameOfFile
        with open(directory+nameOfFile) as f:
            text = f.read()
            words = text.split('\n')
            nameWithoutExtension = nameOfFile.split('.')[0]+"_utf8.txt"
            with open("./"+doc_name+"_utf8/"+nameWithoutExtension,'w') as f2:
                t = ""
                for word in words:
                    t+=str(word.decode('tis-620').encode('utf-8'))+'\n'
                f2.write(t)
                f2.close()
            f.close()



