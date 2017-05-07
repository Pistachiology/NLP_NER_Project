# NLP_NER_Project

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
