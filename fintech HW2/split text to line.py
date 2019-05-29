# -*- coding: utf-8 -*-
import os
import sys
import re

# cut String into 
def muti_split(Line, chars):
	if(type(Line) != type([])):

		Line = [Line]
	for char in chars:
		c = char
		newLine = []
		for l in Line:
#			print('Line:', Line)
#			print('c:', c, 'l:' , l)
			tmp = l.split(c)
			for i in tmp:
				if i:
					newLine.append(i)
		Line = newLine
#	print("WellDone", Line)
	return Line 

#def GetLine 

base_url = os.getcwd()
ReadDirPath = base_url + '\\data\\ltn_news_without_title'
WriteDirPath = base_url + '\\data\\ltn_news_without_title\\splitted_into_lines'

print('base', base_url)
print('read', ReadDirPath)
split_char = ['〔', '〕', '。', '\n']
store_char = ['洗錢']
count = 0
Content = []
for root, subFolder, files in os.walk(ReadDirPath):
	for fileName in files :
#		print(fileName)
		file_url = os.path.join(ReadDirPath, fileName)
#		print(file_url)
		readfile = open(file_url, 'r', encoding='utf-8')
		line = readfile.readline()
		while line:
			#print('line', line)
			Line = muti_split(line, split_char)
			#print('split', Line)
			for i in Line:
				for j in store_char:
					if j in i:
						Content.append(i)
			line = readfile.readline()
		readfile.close()

print(Content)
print(len(Content))