# -*- coding: utf-8 -*-
#第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」

import json
def changeWords(badwords):
    totalwords = open("../text/filtered_words.txt",'r')
    totalwordslist = []

    #注意readline()是读一行，readlines()是读两行
    for words in totalwords.readlines():
        totalwordslist.append(words.strip('\n'))
    #print totalwordslist
    print json.dumps(totalwordslist, encoding="UTF-8", ensure_ascii=False)
    wordsFlag = False
    for i in totalwordslist:
        if i in badwords:
            wordsFlag = True
            badwords = badwords.replace(i,'***')
            #注意加break啊，不然搞不赢
    print "*************"
    print badwords

if __name__ == "__main__":
    words = raw_input("您输入的内容是：")
    changeWords(words)