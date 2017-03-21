# -*- coding: utf-8 -*-
# 第 0013 题： 用 Python 写一个爬图片的程序，爬这个链接里的日本妹子图片 :-)

import os
import re
import urllib

def selectPic(url):
    html_content = urllib.urlopen(url).read()
    r = re.compile('<img pic_type="0" class="BDE_Image" src="(.*?)"')
    pic_url_list = r.findall(html_content.decode('utf-8'))

    os.mkdir("pictures_12")
    os.chdir(os.path.join(os.getcwd(),'pictures_12'))
    for i in range(len(pic_url_list)):
        picture_name = str(i) + '.jpg'
        try:
            urllib.urlretrieve(pic_url_list[i], picture_name)
            print("Success to download " + pic_url_list[i])
        except:
            print("Fail to download " + pic_url_list[i])


if __name__ == "__main__":
    url = "http://tieba.baidu.com/p/2166231880"
    selectPic(url)