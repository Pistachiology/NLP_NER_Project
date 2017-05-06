STEP1.) Convert dictionary from TIS-620 encoding to UTF-8 encoding (convert_tis620_to_utf8.py)
STEP2.) Remove tag every file in tag_per_v2_u8 folder (delete_tag.sh)
STEP3.) Find whole Front_word and whole Back_word from Dictionary (Person_Clue_utf8) (find_front_and_back_person.py)
STEP4.) Find Person Entity word from Rule(front_word_person.txt ans back_word_person.txt)  (find_per.py)
STEP5.) Find whole Front_word and whole Back_word and abbr from Dictionary (OrgAll_utf8) (find_front_back_name_abbr_org.py)
STEP6.) Find Organize Entity word from Rule(front_word_org.txt , back_word_org.txt and name_and_abbr_org.txt)  (find_org.py)
STEP7.) Get person_tag_doing folder and org_tag_doing folder.   -- GG NER --
