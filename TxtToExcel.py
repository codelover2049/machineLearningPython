# coding=utf-8
'''
main function：主要实现把txt中的每行数据写入到excel中
'''
 
#################
#第一次执行的代码
import xlwt #写入文件
import xlrd #打开excel文件
import re

fopen=open("/Users/lzc/Desktop/Localizable.txt",'r')
ptopen=open("/Users/lzc/Desktop/Localizable_pt.txt",'r')
lines=fopen.readlines()
ptlines = ptopen.readlines()

#新建一个excel文件
file=xlwt.Workbook(encoding='utf-8',style_compression=0)
#新建一个sheet
sheet=file.add_sheet('data')

def ptValue(enKey):
    ptValueStr = ''
    for ptline in ptlines:
        if '=' in ptline:
            ptkey = ptline.split('=')[0]
            if enKey in ptkey:
                ptValueStr = ptline.split('=')[1].strip()
                break;
    return ptValueStr;
 

i=0
for line in lines:
    if ('=' in line):
        key = line.split('=')[0]
        value = line.split('=')[1]
        sheet.write(i,0,key.strip())
        sheet.write(i,1,value.strip())
        sheet.write(i,2,ptValue(key))
        i=i+1


file.save('Localizeble.xls')
