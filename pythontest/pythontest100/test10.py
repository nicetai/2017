# -*- coding: utf-8 -*-
#使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image,ImageFont,ImageDraw,ImageFilter
import string
import random
import os

def generate_authenticode():
    print "hello world"
    # print ran.choice(string.ascii_letters)：随机一个英文字母
    # i in range(4)：随机生成四个数字\
    # [random.choice(string.ascii_letters) for i in range(4)] :生成随机的四个数字，并返回一个list
    # ''.join  取出list中的每个元素，拼接生成字符串
    letters = ''.join([random.choice(string.ascii_letters) for i in range(4)])
    print letters

    # Set the size of the image
    width = 100
    height = 40

    # Set the size of the image
    im = Image.new("RGB",(width,height),(255,255,255))

    # Draw letters on the image
    # 创建Draw对象:
    dr = ImageDraw.Draw(im)

    # 创建Font对象:
    font = ImageFont.truetype("arial.ttf", 30)

    for i in range(4):
        dr.text((5 + i * 20, 5), letters[i], (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),font)
    del dr

    # Change the background color
    for x in range(width):
        for y in range (height):
            if im.getpixel((x, y)) == (255, 255, 255):
                im.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # save the image

    #获取当前目录的上一级目录
    currentDir = os.path.dirname(os.getcwd())
    print currentDir
    #拼接目录
    currentPicDir = os.path.join(currentDir,'image\\test10_1.png')
    print currentPicDir

    #对图像进行模糊处理
    im = im.filter(ImageFilter.BLUR)

    # 将im对象保存在文件
    im.save(currentPicDir)



if __name__ == "__main__":
    generate_authenticode()
