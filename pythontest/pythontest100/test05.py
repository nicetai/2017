# -*- coding: utf-8 -*-
#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os
from PIL import Image

def changImage(path):
    for picname in os.listdir(path):
        if not os.path.isfile(picname):
            print picname
            if picname.endswith('.png') or picname.endswith('.jpg')or picname.endswith('.jpeg'):
                picpath = os.path.join(path, picname)
                im = Image.open(picpath)
                width,height  = im.size
                print width
                print height
                if height  > 1136 or width > 640:
                    th = height / 1136
                    td = width / 640
                    ts = max(th,td)
                    nh = int(height/ts)
                    nw = int(width/ts)
                    im = im.resize((nh,nw))
                    #im.save('finish_'+picname.split('.')[0]+'.jpg', 'jpeg')
                    im.save(picname)
                    print "sucess"
                else:
                    print "false"


if __name__ == "__main__":
    changImage('E:\pythontest\image')

