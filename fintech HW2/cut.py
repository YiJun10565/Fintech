# encoding=utf-8
import jieba
import jieba.analyse as janal
import numpy as np

jieba.set_dictionary('./dict.txt.big')

fp = open('news.txt','r', encoding='utf-8')
list = fp.readline() 
wfp = open('tags.txt', 'w')
wfp.close()

while list:
    list = list.strip('\n') 
    list = "./data/"+list
    content = open(list, 'r', encoding='utf-8').read()
    tags = janal.extract_tags(content, 50)

    fpn = open(list, 'r', encoding='utf-8')
    for(line, value) in enumerate(fpn):
        if line == 1: 
            name = fpn.readline()
    print(name[6:9])
    fpn.close()

    result = open('tags.txt', 'a')
    result.write(name[6:9]+",")
    result.write(",".join(tags))
    result.write("\n")
    result.close()
    
    list = fp.readline()

fp.close()

fp = open('nnews.txt','r', encoding='utf-8')
list = fp.readline() 

while list:
    list = list.strip('\n') 
    list = "./data/"+list
    print(list)
    contents = open(list, 'r', encoding='utf-8').read()
    tags = janal.extract_tags(contents, 50)

    result = open('tags.txt', 'a')
    result.write(",".join(tags))
    result.write("\n")
    result.close()
    
    list = fp.readline()

fp.close()
