#encoding=utf-8
import jieba
import jieba.analyse as janal
import numpy as np

jieba.set_dictionary('./dict.txt.big')

fp = open('news.txt','r')
list = fp.readline() 
wfp = open('tags.txt', 'w')
wfp.close()

while list:
    list = list.strip('\n') 
    content = open(list, 'rb').read()
    tags = janal.extract_tags(content, 50)

    fpn = open(list, 'r')
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
