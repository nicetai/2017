# -*- coding: utf-8 -*-
"""
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
下所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
</root>
"""
import xlrd
from xml.dom import minidom, Node


def open_xls(xls_file,xls_sheet):
    excel = xlrd.open_workbook(xls_file)
    student_sheet = excel.sheet_by_name(xls_sheet)
    sheet_content = {}
    for i in range(student_sheet.nrows):
        row_value = student_sheet.row_values(i)
        for j in range(len(row_value)):
            if type(row_value[j]) == float:
                row_value[j] = int(row_value[j])
        #str(i + 1)是将其变成字符串
        #sheet_content[i+1] = row_value[1:]
        sheet_content[str(i + 1)] = row_value[1:]
    print sheet_content
    return sheet_content

def build_xml(sheet_content):
    # Create Dom Object
    doc = minidom.Document()
    # Create root tag
    root = doc.createElement('root')
    doc.appendChild(root)
    # Create 'students' tag
    students = doc.createElement('students')
    root.appendChild(students)
    # Create comment element
    students.appendChild(doc.createComment("学生信息表\"id\" : [名字, 数学, 语文, 英文]"))
    # Create text element
    students.appendChild(doc.createTextNode(str(sheet_content)))

    # save in xml
    students_xml = open('../text/student_17.xml','w')
    students_xml.write(doc.toprettyxml())
    students_xml.close()

    print "hello world"



if __name__ == "__main__":
    xls_file = '../text/student_14.xls'
    xls_sheet = 'student'
    sheet_content = open_xls(xls_file,xls_sheet)
    build_xml(sheet_content)