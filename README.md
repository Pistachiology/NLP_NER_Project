# NLP\_NER\_Project

# How to get NER
1.Adding text file (following format) in NLP_NER_Project/Data/untag_per_v2_u8/  
```
นิกจัง|เจ้าคณะจังหวัด|
นาย|นิกจังซ่า|เจ้าคณะจังหวัด|
นาย|นิกจังซ่า|ซ่า|เจ้าคณะจังหวัด|
บริษัท|นิกจัง|
```
2.Go to Script Folder and run find_per_and_org.py
```
python ./find_per_and_org.py
```
3.Get a result in /Result/person_and_org folder
```
cat ./Mytest.txt
```

```
นิกจัง(per)|เจ้าคณะจังหวัด|
นาย|นิกจังซ่า(per)|เจ้าคณะจังหวัด|
นาย|นิกจังซ่า(per)|ซ่า(per)|เจ้าคณะจังหวัด|
บริษัท|นิกจัง(org)|
```


# Machine Learning NER


- Dummy 

```
word_prefix_suffix.py > train_data.txt
crf_learn template.txt train_data.txt model.txt
python gen_test.py > test_data.txt
ก่อน gen_test.py เอาไฟล์ที่จะทำเทสใส่ในโฟลเดอร์ data ก่อนอพ
สุดท้ายก็ crf_test -m model.txt test_data.txt
crf_test -m model.txt test_data.txt > answer.txt`
python ans_to_text_segment.py answer.txt data/POL1101_notag.CUT
python merge_result.py Result/person_and_org/POL1101_notag.CUT ML/output/POL1101_notag.CUT  merged_result.txt
```




# Merge ML and Pattern base
