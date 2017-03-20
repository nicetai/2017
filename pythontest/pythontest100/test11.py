# -*- coding: utf-8 -*-
# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
import json

def checkWords(keywords):
    filtered_words = open("../text/filtered_words.txt","r")
    filtered_words_list = []

    #输入中文可以的
    testlist = ["beijing","天津",u"天津"]
    print json.dumps(testlist, encoding="UTF-8", ensure_ascii=False)
    for words in filtered_words.readline():
        filtered_words_list.append(words.strip('\n'))
    filtered_words.close()

    #还是输入中文的编码
    print filtered_words_list

    filterType = False

    #判断敏感词是否在我们的列表中
    for words in filtered_words_list:
        if words in keywords:
            filterType = True
            break
    if filterType == True:
        print ("Freedom")
    else:
        print ("Human Rights")

if __name__ == "__main__":
    #while True:
    name = raw_input("请输入内容：")
    checkWords(name)
