# -*- coding: utf-8 -*-
#第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os,re,sys

def calfile(path):
    totalfilelist = os.listdir(path)
    totalpythonlist = (item for item in totalfilelist if item.endswith('.py'))
    ret = [0,0,0]
    for file in totalpythonlist:
        res = cal(path ,file)
        for i in (0,1,2):
            ret[i] += res[i]
    return tuple(ret)



def cal(path,filename):
    totline = 0
    blackline = 0
    commentline = 0
    file = open(path+filename,"r")
    linelist = file.readline()
    totline = len(linelist)
    for line in linelist:
        pattern = re.compile(r'(\s*)#')
        pattern1 = re.compile(r'(\s*)$')
        if pattern.match(line):
            commentline += 1
        if pattern1.match(line):
            blackline += 1
    file.close()
    return totline,blackline,commentline



if __name__ == "__main__":
    path = r"E:/pythontest/pythontest100/"
    #path = sys.argv[1]
    data = calfile(path)
    dic = dict(zip(('totline','blackline','commentline'),list(data)))
    print dic