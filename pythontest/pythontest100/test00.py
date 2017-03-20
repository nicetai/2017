# -*- coding: utf-8 -*-
#第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果


from PIL import Image,ImageDraw,ImageFont

text = u"7"
im = Image.open('../image/test0.jpg')

dr = ImageDraw.Draw(im)

font = ImageFont.truetype('msyh.ttf', 34)

dr.text((im.size[0]*0.85,im.size[1]*0.05),text,font=font,fill="#ff0000")

im.show()
im.save('result.jpg')

