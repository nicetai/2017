# -*- coding: utf-8 -*-
'''
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}

'''

import json
import xlwt

def write_txt_to_xls(txt_file):
    with open(txt_file) as txt_object:
        txt_content = json.load(txt_object)
    print txt_content
    print len(txt_content)
    xlwt_object = xlwt.Workbook()
    sheet = xlwt_object.add_sheet('city')
    for i in range(len(txt_content)):
        sheet.write(i,0,i+1)
        data = txt_content[str(i+1)]
        sheet.write(i, 1, data)
    xlwt_object.save('../text/student_15.xls')

if __name__ == "__main__":
    txt_file = '../text/student_15.txt'
    write_txt_to_xls(txt_file)