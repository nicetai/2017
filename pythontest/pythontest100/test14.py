# -*- coding: utf-8 -*-
'''
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}

请将上述内容写到 student.xls 文件中，如下图所示：
'''

import json
import xlwt

def write_txt_to_xls(txt_file):

    # Read form the txt file
    with open(txt_file,'r') as txt_object:
        file_content = json.load(txt_object)
    txt_object1 = open(txt_file, 'r')
    txt_object_content = txt_object1.read()
    print txt_object_content
    print file_content
    # Write to the xls file
    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('student')
    for i in range(len(file_content)):
        print i
        sheet.write(i,0,i+1)
        data = file_content[str(i+1)]
        print data
        for j in range(len(data)):
            sheet.write(i,j+1,data[j])
    xls_object.save('../text/student_14.xls')

if __name__ == "__main__":
    txt_file = '../text/student_14.txt'
    write_txt_to_xls(txt_file)

