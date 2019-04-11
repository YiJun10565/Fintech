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
    tags = janal.extract_tags(content, 10)
    result = open('tags.txt', 'a')
    result.write(",".join(tags))
    result.write("\n")
    result.close()
    list = fp.readline()
