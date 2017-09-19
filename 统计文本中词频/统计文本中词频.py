#!/usr/bin/env python3
#coding:utf-8

import string
import os
filedir=os.getcwd()
print('filedir:'+filedir)
filepath = filedir+'/Walden.txt'
print('filepath:'+filepath)
with open(filepath,'r') as text:
	# 去掉标点符号，并把字母大写的全部转化成小写
	words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()] 
	
	# 创建了一个以单词为key，出现频率为value的字典
	words_index = set(words)
	counts_dict = {index:words.count(index) for index in words_index}
	

# 统计词频并保存到文件中，按单词出现频率从大到小打印
fp=open(filedir+'/WordCountResult.txt','a')
for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True): 
	fp.write('{} -- {} times'.format(word,counts_dict[word]))
	fp.write("\n")
fp.close()