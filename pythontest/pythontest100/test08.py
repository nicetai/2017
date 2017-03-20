# -*- coding: utf-8 -*-
#第 0008 题：一个HTML文件，找出里面的正文。

import urllib
import re

def getbody(url):
    html_content = urllib.urlopen(url).read()
    print html_content
    r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
    #result = r.findall(html_content.decode('GBK').encode('utf-8'))
    result = r.findall(html_content)
    return result


if __name__ == "__main__":
    urlpath = r'http://www.baidu.com/'
    data = getbody(urlpath)
    print data
    with open('../a.txt','w') as f:
        f.write(str(data))
        print data
