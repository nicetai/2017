# -*- coding: utf-8 -*-
'''
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]

'''

import json
import xlwt

def write_txt_to_xls(txt_file):

    with open(txt_file) as txt_object:
        txt_content = json.load(txt_object)
    print txt_content
    print len(txt_content)
    xlwt_object = xlwt.Workbook()
    sheet = xlwt_object.add_sheet('number')

    for i in range(len(txt_content)):
        data = txt_content[i]
        print data
        print "----"
        #sheet.write(0, i, data[i])
        for j in range(len(data)):
            print data[j]
            print "======"
            #sheet.write(i, 0, data[i])
            #sheet.write(i,i,3)
            sheet.write(i, j, data[j])
        #sheet.write()

    xlwt_object.save('../text/student_16.xls')

if __name__ == "__main__":
    txt_file = '../text/student_16.txt'
    write_txt_to_xls(txt_file)