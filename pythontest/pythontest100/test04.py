# -*- coding: utf-8 -*-
#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

import re
import json
from collections import Counter

begin = open('../text/example04.txt','r')
fin = open('../text/result04.txt','w')
str = begin.readline()


reObj = re.compile("\b?([a-zA-Z]+)\b?")

words = reObj.findall(str)

def word_count(txt):
    word_pattern = r'[a-zA-Z]+'
    words = re.findall(word_pattern,txt)
    #print words
    for items in words:
        print items
        fin.write(items)
    #返回元组, Counter 计数器,key是参数iterable对象中的所有元素（去除重复的），而相应value是各元素出现的次数
    return Counter(words).items();

if __name__ == '__main__':
    list1 = word_count(str)
    #转字典对象换成json对象，方便json对象写入文件
    jsObj = json.dumps(list1)
    print jsObj
    fin.write(jsObj).close()
    begin.close()



